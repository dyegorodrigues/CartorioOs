"""Generate BUILD-only material from one editorial source; no legal certification.

Run with --check to detect missing/stale derivatives without writing files.
This deliberately has no learner, Notion, network, or sufficiency integration.
"""

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/material/pilot_recortes_v0.1.json"
OUTPUT = ROOT / "material/working"
SECTIONS = ("MAP", "MASTER", "LEI SECA GUIADA", "REVIEW", "Q→A", "EXAM / OUTPUT")


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def case_review_fingerprint(case, unit, data):
    """Bind an editorial review to case wording and its actual teaching basis.

    This detects edits, not legal truth or changes on a remote source website.
    There is deliberately no command to approve all reviews automatically.
    """
    props = {prop["id"]: prop for prop in unit["propositions"]}
    basis = [props[key] for key in case["proposition_ids"]]
    source_ids = {key for prop in basis for key in prop["source_ids"]}
    return fingerprint({
        "case": {key: case[key] for key in ("id", "question", "answer", "reasoning", "proposition_ids")},
        "basis": basis,
        "sources": [source for source in data["sources"] if source["id"] in source_ids],
        "foundations": unit["foundations"],
        "scope": unit["scope"],
        "exclusions": unit["exclusions"],
        "checked_at": data["checked_at"],
    })


def require_text(record, fields):
    for field in fields:
        if not isinstance(record.get(field), str) or not record[field].strip():
            raise ValueError(f"missing text: {record.get('id', 'record')}.{field}")


def validate(data):
    """Check referential and release integrity, not correctness of legal prose."""
    if data.get("schema_version") != 1 or data.get("state") != "BUILD":
        raise ValueError("only schema 1 / BUILD is supported; no release promotion")
    if (data.get("legal_snapshot"), data.get("exam_snapshot")) != ("CURRENT_LAW", "NOT_ASSESSED"):
        raise ValueError("this batch does not certify an exam snapshot")
    date.fromisoformat(data["checked_at"])
    for key in ("sources", "units"):
        if not isinstance(data.get(key), list) or not data[key]:
            raise ValueError(f"missing or empty {key}")
    ids, sources, nodes, filenames = set(), set(), {}, set()

    def register(record):
        require_text(record, ("id",))
        key = record["id"]
        if not re.fullmatch(r"[A-Z0-9-]+", key) or key in ids:
            raise ValueError(f"invalid or duplicate id: {key}")
        ids.add(key)

    for source in data["sources"]:
        register(source)
        require_text(source, ("title", "url", "scope", "checked_at"))
        if not source["url"].startswith("https://"):
            raise ValueError("source requires an HTTPS URL")
        if date.fromisoformat(source["checked_at"]) > date.fromisoformat(data["checked_at"]):
            raise ValueError("source checked after batch snapshot")
        sources.add(source["id"])
    for unit in data["units"]:
        register(unit)
        require_text(unit, ("title", "filename", "scope", "exclusions", "provenance"))
        name = unit["filename"]
        if not re.fullmatch(r"[A-Z0-9_.-]+\.md", name) or name in filenames:
            raise ValueError(f"invalid or duplicate output filename: {name}")
        filenames.add(name)
        for key in ("foundations", "propositions", "cases", "edges"):
            if not isinstance(unit.get(key), list) or not unit[key]:
                raise ValueError(f"missing or empty {unit['id']}.{key}")
        for foundation in unit["foundations"]:
            register(foundation)
            require_text(foundation, ("title", "text"))
            nodes[foundation["id"]] = foundation
        for prop in unit["propositions"]:
            register(prop)
            require_text(prop, ("title", "locator", "rule", "explanation", "recall_question"))
            if prop.get("depth") not in {"P0", "P1", "P2", "P3", "P4"}:
                raise ValueError(f"invalid depth: {prop['id']}")
            refs = prop.get("source_ids")
            if not isinstance(refs, list) or not refs or any(ref not in sources for ref in refs):
                raise ValueError(f"missing or unknown source: {prop['id']}")
            nodes[prop["id"]] = prop
        for case in unit["cases"]:
            register(case)
            require_text(case, ("question", "answer", "reasoning"))
            refs = case.get("proposition_ids")
            local_props = {prop["id"] for prop in unit["propositions"]}
            if not isinstance(refs, list) or not refs or any(ref not in local_props for ref in refs):
                raise ValueError(f"case must refer to taught propositions in its unit: {case['id']}")

    prerequisites = {key: [] for key in nodes}
    for unit in data["units"]:
        for edge in unit["edges"]:
            if edge.get("from") not in nodes or edge.get("to") not in nodes:
                raise ValueError("edge has unknown node")
            if edge.get("type") not in {"requires", "confusable_with"}:
                raise ValueError("unsupported relation")
            if edge["from"] == edge["to"]:
                raise ValueError("self relation")
            if edge["type"] == "requires":
                prerequisites[edge["from"]].append(edge["to"])
    visiting, done = set(), set()

    def visit(key):
        if key in visiting:
            raise ValueError("cycle in prerequisites")
        if key in done:
            return
        visiting.add(key)
        for dependency in prerequisites[key]:
            visit(dependency)
        visiting.remove(key)
        done.add(key)

    for key in nodes:
        visit(key)

    for unit in data["units"]:
        for case in unit["cases"]:
            review = case.get("editorial_review", {})
            if (review.get("kind") != "SAME_CONTEXT_EDITORIAL"
                    or review.get("checked_at") != data["checked_at"]
                    or review.get("fingerprint") != case_review_fingerprint(case, unit, data)):
                raise ValueError(f"missing or stale editorial review: {case['id']}")


def render_sections(unit, data):
    sources = {source["id"]: source for source in data["sources"]}
    props = {prop["id"]: prop for prop in unit["propositions"]}
    homes = {node["id"]: (owner["filename"], node["title"])
             for owner in data["units"] for key in ("foundations", "propositions") for node in owner[key]}

    def link(key):
        filename, title = homes[key]
        return f"[{title}]({filename}#{key.lower()})"

    def citations(prop):
        links = "; ".join(f"[{key}]({sources[key]['url']})" for key in prop["source_ids"])
        return f"{links} — {prop['locator']}."

    mapping = [unit["scope"], "P0 = pré-requisito; P1 = cobertura; P2 = discriminativo; P3 = produção avançada; P4 = referência. Os itens deste recorte estão em P1, sem score de frequência inventado."]
    mapping.append("| Conhecimento | Relação | Conexão útil |\n|---|---|---|")
    labels = {"requires": "requer", "confusable_with": "comparar para não confundir"}
    mapping.extend(f"| {link(e['from'])} | {labels[e['type']]} | {link(e['to'])} |" for e in unit["edges"])

    master = ["### Base necessária"]
    for foundation in unit["foundations"]:
        master += [f"<a id=\"{foundation['id'].lower()}\"></a>", f"#### {foundation['title']}", foundation["text"]]
    for prop in props.values():
        master += [f"<a id=\"{prop['id'].lower()}\"></a>", f"### {prop['title']}",
                   f"`{prop['id']}` · {prop['depth']}", prop["rule"], prop["explanation"], citations(prop)]

    guided = ["A síntese é autoral. Abra o texto oficial e localize os elementos pedidos; este roteiro não substitui a redação legal."]
    for prop in props.values():
        guided += [f"**{prop['title']}** — {citations(prop)}", f"Foco da leitura: {prop['recall_question']}"]

    review = ["Versão compacta: somente as regras canônicas, sem as explicações e os exemplos do MASTER."]
    recall = ["Perguntas de recuperação para revisar o material internamente. As respostas abaixo são geradas das mesmas regras do MASTER."]
    for prop in props.values():
        review += [f"**{prop['title']}** (`{prop['id']}`): {prop['rule']} {citations(prop)}"]
        recall += [f"### {prop['recall_question']}", f"{prop['rule']} {citations(prop)}", f"Referência: `{prop['id']}`."]

    cases = ["Casos **GX sintéticos / BUILD**. Não são questões oficiais, itens reservados, notas do candidato ou prova de suficiência. A justificativa aplica regras já ensinadas; a base normativa é inserida automaticamente pelos IDs."]
    for case in unit["cases"]:
        cases += [f"### {case['id']}", case["question"], f"**Resposta comentada: {case['answer']}** {case['reasoning']}", "**Base para conferir a resposta:**"]
        cases += [f"- `{key}`: {props[key]['rule']} {citations(props[key])}" for key in case["proposition_ids"]]
    cases += ["### Critério de revisão da produção", "Em cada caso, conferir: identificação da hipótese; conclusão; presença dos elementos das proposições indicadas; ausência de condição ou efeito inventado. É uma rubrica editorial para este recorte, sem pontuação de mastery e sem validação da capacidade de resolver uma prova completa."]
    return dict(zip(SECTIONS, ("\n\n".join(mapping[:2]) + "\n\n" + "\n".join(mapping[2:]),
                               "\n\n".join(master), "\n\n".join(guided),
                               "\n\n".join(review), "\n\n".join(recall), "\n\n".join(cases))))


def compile_documents(data):
    validate(data)
    digest = fingerprint(data)
    documents = {}
    for unit in data["units"]:
        header = [f"# {unit['title']}", "**BUILD / NÃO VALIDADO / NÃO INICIAR ESTUDO.**",
                  f"Conferência legal delimitada: {data['checked_at']}. CURRENT_LAW; elegibilidade para edital específico não avaliada.",
                  "Gerado por `scripts/compile_material.py` a partir de `data/material/pilot_recortes_v0.1.json`. Edite a fonte editorial e regenere; não edite esta derivação.",
                  f"Fingerprint semântico da fonte: `{digest}`.",
                  f"**Proveniência:** {unit['provenance']}", f"**Limites:** {unit['exclusions']}"]
        sections = render_sections(unit, data)
        body = [f"## {index}. {name}\n\n{sections[name]}" for index, name in enumerate(SECTIONS, 1)]
        documents[unit["filename"]] = "\n\n".join(header + body) + "\n"
    return documents


def run(source=SOURCE, output=OUTPUT, check=False):
    documents = compile_documents(json.loads(Path(source).read_text(encoding="utf-8")))
    output = Path(output)
    if check:
        stale = [name for name, content in documents.items()
                 if not (output / name).is_file() or (output / name).read_text(encoding="utf-8") != content]
        if stale:
            raise ValueError("missing or stale derivatives: " + ", ".join(stale))
    else:
        output.mkdir(parents=True, exist_ok=True)
        for name, content in documents.items():
            (output / name).write_text(content, encoding="utf-8")
    return len(documents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        count = run(check=args.check)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f"Material check failed: {error}\n")
    print(f"{count} BUILD documents {'verified' if args.check else 'generated'}; no learner release or S2 claim.")
