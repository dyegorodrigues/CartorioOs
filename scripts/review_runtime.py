"""Ensaio do núcleo de revisão/retomada. Apenas dados fictícios, sem I/O remoto.

Não é corretor jurídico, scheduler curricular, banco de produção ou serviço ativo.
O adaptador persiste o retorno completo e confere leitura antes de anunciar salvo.
"""
from copy import deepcopy
from datetime import datetime, timezone, timedelta
from hashlib import sha256
from importlib.metadata import version
import json

from fsrs import Card, Rating, Scheduler

ENGINE = "6.3.2"


def utc(value):
    result = datetime.fromisoformat(value)
    if result.tzinfo is None:
        raise ValueError("Timestamp deve informar fuso; não inferir fuso do candidato.")
    return result.astimezone(timezone.utc)


def digest(value):
    return sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                             separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def content_hash(item):
    return digest({key: item[key] for key in ("prompt", "answer", "version")})


def new_state():
    if version("fsrs") != ENGINE:
        raise ValueError("Instalar a versão fixada em requirements-review.txt.")
    return {"schema": 1, "mode": "SANDBOX", "engine_version": ENGINE,
            "scheduler": Scheduler(enable_fuzzing=False).to_dict(),
            "cards": {}, "events": [], "pending": None}


def check_state(state):
    if (state["schema"] != 1 or state["mode"] != "SANDBOX"
            or state["engine_version"] != ENGINE or version("fsrs") != ENGINE):
        raise ValueError("Ensaio não aceita estado real nem migração silenciosa.")


def eligible(item):
    return item["release"] == "SANDBOX_ONLY" and item["freshness"] == "CURRENT"


def apply_event(state, event, catalog, expected_revision):
    """Transição pura; retry exato é idempotente. Revisão não é lock remoto."""
    check_state(state)
    if not isinstance(event.get("id"), str) or not event["id"]:
        raise ValueError("Evento precisa de ID estável.")
    for saved in state["events"]:
        if saved["id"] == event["id"]:
            if saved != event:
                raise ValueError("Colisão: mesmo ID com conteúdo diferente.")
            return deepcopy(state)
    if expected_revision != len(state["events"]):
        raise ValueError("Estado antigo: reler antes de aplicar.")
    at = utc(event["at"])
    if state["events"] and at < utc(state["events"][-1]["at"]):
        raise ValueError("Evento fora de ordem; não inventar intervalo de revisão.")
    result = deepcopy(state)
    kind, key = event["kind"], event["item_id"]
    if not key.startswith("SYN-"):
        raise ValueError("Este ensaio aceita apenas itens fictícios SYN-.")
    if kind == "cancel":
        if not result["pending"] or result["pending"]["item_id"] != key or not event.get("reason"):
            raise ValueError("Cancelamento precisa da tarefa pendente e motivo.")
        result["pending"] = None
    else:
        item = catalog[key]
        if not eligible(item):
            raise ValueError("Item sem liberação de ensaio ou exigindo revalidação.")
        if kind == "expose":
            if key in result["cards"] or result["pending"]:
                raise ValueError("Exposição duplicada ou tarefa pendente.")
            result["cards"][key] = {
                "content_hash": content_hash(item), "suspended": False,
                "fsrs": Card(card_id=len(result["cards"]) + 1, due=at).to_dict()}
        elif kind in ("present", "answer"):
            stored = result["cards"].get(key)
            if not stored or stored["content_hash"] != content_hash(item) or stored["suspended"]:
                raise ValueError("Exposição ausente, conteúdo alterado ou item suspenso.")
            if kind == "present":
                if result["pending"]:
                    raise ValueError("Retomar tarefa pendente antes de abrir outra.")
                result["pending"] = {"item_id": key, "prompt": item["prompt"],
                                     "content_hash": content_hash(item), "at": event["at"]}
            else:
                pending = result["pending"]
                if not pending or pending["item_id"] != key:
                    raise ValueError("Resposta não corresponde à tarefa pendente.")
                outcome = event["outcome"]
                if outcome not in ("correct", "incorrect", "assisted", "material_gap"):
                    raise ValueError("Resultado não reconhecido.")
                # Sem medir/inferir latência pela distância entre mensagens.
                if outcome in ("correct", "incorrect"):
                    rating = 3 if outcome == "correct" else 1
                    scheduler = Scheduler.from_dict(result["scheduler"])
                    card, _ = scheduler.review_card(Card.from_dict(stored["fsrs"]),
                                                    Rating(rating), review_datetime=at)
                    stored["fsrs"] = card.to_dict()
                elif outcome == "material_gap":
                    stored["suspended"] = True
                result["pending"] = None
        else:
            raise ValueError("Tipo de evento não reconhecido.")
    result["events"].append(deepcopy(event))
    return result


def resume(state, catalog, now, review_budget_seconds=300):
    """Fila curta de recall já exposto. Não escolhe matéria nova nem concede mastery."""
    check_state(state)
    now = utc(now)
    if state["events"] and now < utc(state["events"][-1]["at"]):
        raise ValueError("Retomada anterior ao último evento.")
    if type(review_budget_seconds) is not int or review_budget_seconds < 0:
        raise ValueError("Orçamento deve ser inteiro não negativo.")
    pending = state["pending"]
    if pending:
        item = catalog.get(pending["item_id"])
        valid = item and eligible(item) and content_hash(item) == pending["content_hash"]
        return {"action": "RESUME" if valid else "REVALIDATE",
                "pending": deepcopy(pending), "queue": []}
    due, blocked = [], []
    for key, stored in state["cards"].items():
        item = catalog.get(key)
        if (not item or not eligible(item) or stored["suspended"]
                or stored["content_hash"] != content_hash(item)):
            blocked.append(key)
            continue
        if type(item["estimated_seconds"]) is not int or item["estimated_seconds"] <= 0:
            raise ValueError("Estimativa de tarefa inválida.")
        card = Card.from_dict(stored["fsrs"])
        if card.due <= now:
            due.append((card.due, key))
    queue, remaining = [], review_budget_seconds
    for _, key in sorted(due):
        cost = catalog[key]["estimated_seconds"]
        if cost <= remaining:
            queue.append(key)
            remaining -= cost
    return {"action": "REVIEW" if queue else "NO_REVIEW_FITS",
            "queue": queue, "due_count": len(due), "blocked": blocked,
            "estimated_seconds": review_budget_seconds - remaining}


def recall_estimate(state, key, now):
    """Estimativa do modelo genérico, nunca porcentagem pessoal comprovada."""
    check_state(state)
    card = Card.from_dict(state["cards"][key]["fsrs"])
    at = utc(now)
    if card.last_review is None:
        return None
    if at < card.last_review:
        raise ValueError("Estimativa anterior à revisão.")
    return Scheduler.from_dict(state["scheduler"]).get_card_retrievability(card, at)


def pack(state):
    check_state(state)
    return {"state": deepcopy(state), "sha256": digest(state)}


def unpack(envelope):
    if digest(envelope["state"]) != envelope["sha256"]:
        raise ValueError("Checkpoint incompleto ou divergente.")
    check_state(envelope["state"])
    return deepcopy(envelope["state"])


def demo():
    """26 eventos fictícios + uma tarefa pendente; nenhuma resposta do candidato."""
    catalog = {f"SYN-{i}": {"prompt": f"Qual é o código fictício do objeto {i}?",
                           "answer": f"Código {i}.", "version": "1",
                           "release": "SANDBOX_ONLY", "freshness": "CURRENT",
                           "estimated_seconds": 30} for i in (1, 2)}
    state = new_state()
    at = utc("2026-09-01T12:00:00+00:00")

    def append(kind, key, **kwargs):
        nonlocal state
        state = apply_event(state, {"id": f"DEMO-{len(state['events']) + 1:02d}",
                                   "kind": kind, "item_id": key,
                                   "at": at.isoformat(), **kwargs}, catalog, len(state["events"]))

    for key in catalog:
        append("expose", key)
    for i in range(12):
        key = f"SYN-{i % 2 + 1}"
        at += timedelta(hours=12)
        append("present", key)
        append("answer", key, outcome="incorrect" if i in (2, 7) else "correct")
    append("present", "SYN-1")
    return {"catalog": catalog, "checkpoint": pack(state)}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
