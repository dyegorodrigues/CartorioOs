"""Validate modular links and review freshness; never certify legal accuracy."""
import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique(records, label):
    result = {}
    for item in records:
        key = item.get("id")
        require(isinstance(key, str) and key.strip(), f"{label}: missing id")
        require(key not in result, f"{label}: duplicate id {key}")
        result[key] = item
    return result


def text_fields(item, names):
    for name in names:
        require(isinstance(item.get(name), str) and item[name].strip(),
                f"{item.get('id')}: missing {name}")


def confined(root, path):
    target = (root / path).resolve()
    require(target.is_relative_to(root.resolve()), f"path outside content: {path}")
    require(target.is_file(), f"missing file: {path}")
    return target


def links(values, known, label, nonempty=False):
    require(isinstance(values, list), f"{label}: expected list")
    require(not nonempty or bool(values), f"{label}: empty links")
    require(len(values) == len(set(values)), f"{label}: duplicate links")
    for value in values:
        require(value in known, f"{label}: unknown reference {value}")


def acyclic(graph, label):
    active, done = set(), set()
    def visit(key):
        require(key not in active, f"{label}: cycle at {key}")
        if key in done:
            return
        active.add(key)
        for child in graph[key]:
            visit(child)
        active.remove(key)
        done.add(key)
    for key in graph:
        visit(key)


def basis_digest(question, modules, topics, sources, laws):
    """Bind review to item wording and linked teaching, not only its IDs."""
    relevant = sorted({topics[t][0] for t in question["topic_ids"]})
    payload = {
        "question": {k: v for k, v in question.items()
                     if k not in {"review", "review_status"}},
        "topics": [topics[t][1] for t in question["topic_ids"]],
        "teaching": [{"module": mid, "text": modules[mid]["reading_text"]}
                     for mid in relevant],
        "sources": [sources[s] for s in question["source_ids"]],
        "laws": [laws[s] for s in question["law_ids"]],
    }
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def validate(root=ROOT):
    root = Path(root).resolve()
    content = root / "content"
    catalog = read(content / "catalog.json")
    require(catalog.get("schema_version") == 1, "unsupported catalog schema")
    sources = unique(read(content / "sources.json")["sources"], "sources")
    laws = unique(read(content / "law_registry.json")["provisions"], "laws")
    subjects = unique(catalog["subjects"], "subjects")
    booklets = unique(catalog["booklets"], "booklets")
    entries = unique(catalog["modules"], "catalog modules")
    modules, topics, questions = {}, {}, {}
    for mid, entry in entries.items():
        path = confined(content, Path(entry["path"]).relative_to("content"))
        m = read(path)
        require(m.get("schema_version") == 1 and m.get("id") == mid,
                f"{mid}: descriptor mismatch")
        require(m["subject_id"] in subjects and m["booklet_id"] in booklets,
                f"{mid}: unknown curriculum parent")
        require(m["status"] in {"planned", "draft", "reviewed"}, f"{mid}: invalid status")
        links(m["source_ids"], sources, mid + " sources", True)
        require(m["curriculum_source"]["source_id"] in sources, f"{mid}: curriculum source")
        require(m["topics"], f"{mid}: no topics")
        for tid, topic in unique(m["topics"], mid + " topics").items():
            require(tid not in topics, f"duplicate topic {tid}")
            text_fields(topic, ("title",))
            topics[tid] = (mid, topic)
        reading = ""
        if m.get("reading_file"):
            reading = confined(path.parent, m["reading_file"]).read_text(encoding="utf-8")
            require(reading.strip(), f"{mid}: empty reading")
        if m["status"] == "reviewed":
            require(reading.strip(), f"{mid}: reviewed without reading")
            date.fromisoformat(m["legal_checked_at"])
        qpath = confined(path.parent, m["questions_file"])
        local = []
        for lineno, line in enumerate(qpath.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            q = json.loads(line)
            qid = q.get("id")
            require(isinstance(qid, str) and qid and qid not in questions,
                    f"{qpath.name}:{lineno}: duplicate/missing question id")
            questions[qid] = q
            local.append(q)
        modules[mid] = {"descriptor": m, "reading_text": reading,
                        "questions": local, "source_path": path}
    for mid, data in modules.items():
        m = data["descriptor"]
        links(m["prerequisite_ids"], modules, mid + " prerequisites")
        links(m["related_module_ids"], modules, mid + " related modules")
    acyclic({mid: m["descriptor"]["prerequisite_ids"] for mid, m in modules.items()}, "modules")
    listed = []
    for bid, booklet in booklets.items():
        require(booklet["subject_id"] in subjects, f"{bid}: unknown subject")
        links(booklet["module_ids"], modules, bid, True)
        for mid in booklet["module_ids"]:
            m = modules[mid]["descriptor"]
            require(m["booklet_id"] == bid and m["subject_id"] == booklet["subject_id"],
                    f"{mid}: inconsistent booklet membership")
        listed += booklet["module_ids"]
    require(len(listed) == len(set(listed)) and set(listed) == set(modules),
            "each module must belong to exactly one booklet")
    for law in laws.values():
        text_fields(law, ("instrument", "article", "version", "text", "official_url", "checked_at"))
        require(law["official_url"].startswith("https://"), "law requires official HTTPS URL")
        date.fromisoformat(law["checked_at"])
        links(law["topic_ids"], topics, law["id"] + " topics", True)
    for q in questions.values():
        text_fields(q, ("prompt", "answer", "explanation"))
        require(q["kind"] in {"learning", "recall", "comparison", "application", "official", "oral", "discursive"},
                f"{q['id']}: invalid kind")
        require(q["origin"] in {"authored", "adapted", "official"}, f"{q['id']}: invalid origin")
        require(q["difficulty"] in {"very_easy", "easy", "medium", "hard", "very_hard"}, "invalid difficulty")
        require(type(q["order"]) is int and q["order"] >= 0, "invalid question order")
        links(q["topic_ids"], topics, q["id"] + " topics", True)
        links(q["source_ids"], sources, q["id"] + " sources", True)
        links(q["law_ids"], laws, q["id"] + " laws")
        links(q["requires_question_ids"], questions, q["id"] + " prerequisites")
        require((q["kind"] == "official") == (q["origin"] == "official"), "official label mismatch")
        if q["origin"] in {"official", "adapted"}:
            exam = q.get("exam", {})
            text_fields(exam, ("board", "contest", "phase", "question_number", "original_url", "answer_key_url", "final_answer"))
            require(type(exam.get("year")) is int, "exam year missing")
            require(exam.get("status") in {"valid", "annulled", "unknown"}, "exam status missing")
        if q["origin"] == "adapted":
            text_fields(q, ("adaptation_note",))
        if q["kind"] in {"oral", "discursive"}:
            require(bool(q.get("rubric")), f"{q['id']}: missing rubric")
        require(q["review_status"] in {"draft", "needs_review", "reviewed"}, "invalid review status")
        if q["review_status"] == "reviewed":
            review = q.get("review", {})
            date.fromisoformat(review["checked_at"])
            require(review.get("basis_digest") == basis_digest(q, modules, topics, sources, laws),
                    f"{q['id']}: stale review")
            require(all(modules[topics[t][0]]["reading_text"].strip() for t in q["topic_ids"]),
                    f"{q['id']}: reviewed question without teaching")
    acyclic({qid: q["requires_question_ids"] for qid, q in questions.items()}, "questions")
    candidates = read(content / "research_candidates.json")["candidates"]
    for candidate in candidates:
        require(candidate["source_id"] in sources, "candidate source missing")
        links(candidate["module_ids"], modules, "candidate modules", True)
    return {"catalog": catalog, "modules": modules, "topics": topics,
            "sources": sources, "laws": laws, "questions": questions}


if __name__ == "__main__":
    try:
        data = validate()
        print(f"Structure OK: {len(data['modules'])} modules, {len(data['topics'])} topics, "
              f"{len(data['questions'])} questions. Legal/pedagogical review remains separate.")
    except (ValueError, KeyError, TypeError, OSError) as exc:
        raise SystemExit(f"Validation failed: {exc}")
