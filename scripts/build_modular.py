"""Build separate module payloads and generated study readings for on-demand loading."""
import argparse
import hashlib
import html
import json
from pathlib import Path
from validate_modular import ROOT, validate


ROLE_LABELS = {
    "core": "Núcleo",
    "attention": "Atenção",
    "exception": "Exceção",
    "trap": "Pegadinha",
    "comparison": "Comparação",
    "law": "Lei seca",
    "jurisprudence": "Jurisprudência",
    "depth": "Aprofundamento",
    "example": "Exemplo",
}


def read_jsonl(path):
    rows = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def render_claims_html(descriptor, claims, questions, laws):
    topic_titles = {x["id"]: x["title"] for x in descriptor["topics"]}
    grouped = {tid: [] for tid in topic_titles}
    ungrouped = []
    for claim in claims:
        tid = claim.get("topic_ids", [None])[0]
        if tid in grouped:
            grouped[tid].append(claim)
        else:
            ungrouped.append(claim)

    linked_law_ids = []
    seen_laws = set()
    for claim in claims:
        for lid in claim.get("authority_ids", []):
            if lid not in seen_laws:
                seen_laws.add(lid)
                linked_law_ids.append(lid)
    for question in questions:
        for lid in question.get("law_ids", []):
            if lid not in seen_laws:
                seen_laws.add(lid)
                linked_law_ids.append(lid)

    css = """
:root{font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.5;color:#182033;background:#f5f7fb}
*{box-sizing:border-box} body{margin:0} main{max-width:980px;margin:auto;padding:28px 18px 64px}
.hero{background:white;border:1px solid #dfe5ef;border-radius:18px;padding:24px;margin-bottom:20px;box-shadow:0 8px 28px rgba(22,34,57,.06)}
.hero h1{margin:0 0 8px;font-size:1.7rem}.meta{color:#657187;font-size:.92rem}
.notice{margin-top:14px;background:#fff7dd;border:1px solid #ead28d;border-radius:12px;padding:10px 12px;font-size:.9rem}
.topic{margin-top:28px}.topic h2{font-size:1.25rem;margin:0 0 12px}
.card{background:white;border:1px solid #dfe5ef;border-left:5px solid #5576b9;border-radius:12px;padding:14px 16px;margin:10px 0;box-shadow:0 4px 14px rgba(22,34,57,.04)}
.card[data-role="trap"]{border-left-color:#d39a22}.card[data-role="exception"]{border-left-color:#b64a4a}.card[data-role="comparison"]{border-left-color:#7957b8}.card[data-role="depth"]{border-left-color:#64748b}.card[data-role="attention"]{border-left-color:#b86a2d}.card[data-role="law"]{border-left-color:#2f8a68}
.badge{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.02em;text-transform:uppercase;background:#edf2fb;color:#445c8d;border-radius:999px;padding:3px 8px;margin-bottom:7px}
.statement{font-size:1rem}.source{margin-top:8px;color:#788398;font-size:.76rem}
.lawbox{background:#f4fbf8;border:1px solid #bee0d2;border-radius:12px;padding:14px 16px;margin:10px 0}.lawbox strong{display:block;margin-bottom:6px}
.questions{margin-top:34px}.questions details{background:white;border:1px solid #dfe5ef;border-radius:12px;margin:9px 0;padding:0 14px}.questions summary{cursor:pointer;font-weight:650;padding:13px 0}.answer{border-top:1px solid #e6eaf1;padding:12px 0}.explain{color:#596579}
.small{font-size:.78rem;color:#758095}.empty{color:#7f8897;font-style:italic}
@media print{body{background:white}.hero,.card,.lawbox,.questions details{box-shadow:none;break-inside:avoid}main{max-width:none;padding:0}.questions details[open]{break-inside:avoid}}
"""

    parts = [
        "<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width,initial-scale=1'>",
        f"<title>{html.escape(descriptor['title'])}</title><style>{css}</style></head><body><main>",
        "<section class='hero'>",
        f"<h1>{html.escape(descriptor['title'])}</h1>",
        f"<div class='meta'>{len(claims)} proposições canônicas • {len(questions)} perguntas de revisão</div>",
        "<div class='notice'><strong>Rascunho editorial.</strong> O material abaixo é gerado a partir dos Claims do Tutor OS. Itens normativos e jurisprudenciais só devem ser promovidos após conferência oficial e revisão.</div>",
        "</section>",
    ]

    for tid, title in topic_titles.items():
        parts.append(f"<section class='topic'><h2>{html.escape(title)}</h2>")
        rows = grouped.get(tid, [])
        if not rows:
            parts.append("<div class='empty'>Conteúdo ainda não redigido neste tópico.</div>")
        for claim in rows:
            role = claim.get("render_role", "core")
            label = ROLE_LABELS.get(role, role)
            refs = " • ".join(
                f"{html.escape(r['source_id'])} {html.escape(r.get('locator',''))}"
                for r in claim.get("source_refs", [])
            )
            parts.append(
                f"<article class='card' data-role='{html.escape(role)}'>"
                f"<div class='badge'>{html.escape(label)}</div>"
                f"<div class='statement'>{html.escape(claim['statement'])}</div>"
                f"<div class='source'>{refs}</div></article>"
            )
        parts.append("</section>")

    if ungrouped:
        parts.append("<section class='topic'><h2>Outros pontos</h2>")
        for claim in ungrouped:
            parts.append(f"<article class='card'><div class='statement'>{html.escape(claim['statement'])}</div></article>")
        parts.append("</section>")

    if linked_law_ids:
        parts.append("<section class='topic'><h2>Lei seca vinculada</h2>")
        for lid in linked_law_ids:
            law = laws.get(lid)
            if not law:
                continue
            parts.append(
                "<article class='lawbox'>"
                f"<strong>{html.escape(law['instrument'])} - {html.escape(law['article'])}</strong>"
                f"<div>{html.escape(law['text'])}</div>"
                f"<div class='small'>Conferido em {html.escape(law['checked_at'])} • "
                f"<a href='{html.escape(law['official_url'])}'>fonte oficial</a></div></article>"
            )
        parts.append("</section>")

    if questions:
        ordered = sorted(questions, key=lambda q: (q.get("order", 999999), q["id"]))
        parts.append("<section class='questions'><h2>Revisão ativa</h2>")
        for q in ordered:
            parts.append(
                "<details>"
                f"<summary>{html.escape(q['prompt'])}</summary>"
                f"<div class='answer'><strong>Resposta:</strong> {html.escape(q['answer'])}</div>"
                f"<div class='explain'>{html.escape(q['explanation'])}</div>"
                f"<p class='small'>{html.escape(q['id'])} • {html.escape(q['difficulty'])} • {html.escape(q['review_status'])}</p>"
                "</details>"
            )
        parts.append("</section>")

    parts.append("</main></body></html>")
    return "".join(parts)


def build(root=ROOT, output=None):
    root = Path(root)
    output = Path(output) if output else root / "dist/modular"
    data = validate(root)
    output.mkdir(parents=True, exist_ok=True)
    entries = []
    module_paths = {x["id"]: Path(x["path"]) for x in data["catalog"]["modules"]}
    law_rows = json.loads((root / "content/law_registry.json").read_text(encoding="utf-8"))["provisions"]
    laws = {x["id"]: x for x in law_rows}

    for mid, module in data["modules"].items():
        descriptor = module["descriptor"]
        target = output / "modules" / mid
        target.mkdir(parents=True, exist_ok=True)

        base_dir = (root / module_paths[mid]).parent
        claims_file = descriptor.get("claims_file")
        claims = read_jsonl(base_dir / claims_file) if claims_file else []

        payload = {"module": descriptor, "claims": claims, "questions": module["questions"]}
        raw = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode()
        (target / "module.json").write_bytes(raw)

        reading_hash = None
        reading_origin = None
        if module["reading_text"]:
            reading_text = module["reading_text"]
            reading_origin = "authored_file"
        elif claims:
            reading_text = render_claims_html(descriptor, claims, module["questions"], laws)
            reading_origin = "generated_from_claims"
        else:
            reading_text = None

        if reading_text:
            reading = reading_text.encode()
            (target / "reading.html").write_bytes(reading)
            reading_hash = hashlib.sha256(reading).hexdigest()
        elif (target / "reading.html").exists():
            (target / "reading.html").unlink()

        entries.append({
            "id": mid,
            "title": descriptor["title"],
            "status": descriptor["status"],
            "pipeline_status": descriptor.get("pipeline_status"),
            "path": f"modules/{mid}/module.json",
            "reading_path": f"modules/{mid}/reading.html" if reading_hash else None,
            "reading_origin": reading_origin,
            "payload_sha256": hashlib.sha256(raw).hexdigest(),
            "reading_sha256": reading_hash,
            "claim_count": len(claims),
            "question_count": len(module["questions"]),
        })

    manifest = {
        "schema_version": 2,
        "title": data["catalog"]["title"],
        "subjects": data["catalog"]["subjects"],
        "booklets": data["catalog"]["booklets"],
        "modules": entries,
        "legal_certification": False,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for filename in ("sources.json", "law_registry.json"):
        (output / filename).write_bytes((root / "content" / filename).read_bytes())

    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(output=args.output)
    generated = sum(1 for m in result["modules"] if m["reading_path"])
    print(f"Built {len(result['modules'])} separate modules; {generated} study readings available. No site deployment.")
