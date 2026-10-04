"""Validate Tutor OS V2 claim graph, coverage maps and question-to-claim links."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

CLAIM_KINDS = {"concept","rule","exception","distinction","classification","doctrine","jurisprudence","exam_pattern","example"}
RENDER_ROLES = {"core","attention","exception","trap","comparison","law","jurisprudence","depth","example"}
FRESHNESS_CLASSES = {"stable_doctrine","legislation","jurisprudence","exam_pattern","mixed"}
FRESHNESS_STATUS = {"needs_review","current","possibly_stale","superseded"}
REVIEW_STATUS = {"draft","needs_review","reviewed"}
PIPELINE_STATUS = {"mapped","drafting","review","study_ready"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path):
    rows=[]
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{n}: invalid JSON: {exc}") from exc
    return rows


def require(cond,msg):
    if not cond:
        raise ValueError(msg)


def acyclic(graph,label):
    active=set()
    done=set()
    def visit(node):
        if node in done:
            return
        require(node not in active,f"{label}: cycle at {node}")
        active.add(node)
        for dep in graph.get(node,[]):
            visit(dep)
        active.remove(node)
        done.add(node)
    for node in graph:
        visit(node)


def main(root=ROOT):
    root=Path(root)
    content=root/"content"
    catalog=read_json(content/"catalog.json")
    source_rows=read_json(content/"sources.json")["sources"]
    sources={x["id"]:x for x in source_rows}
    require(len(sources)==len(source_rows),"duplicate source id")

    topics={}
    modules={}
    claims={}
    questions=[]

    for entry in catalog["modules"]:
        mpath=root/entry["path"]
        module=read_json(mpath)
        modules[module["id"]]=(mpath,module)
        for topic in module["topics"]:
            tid=topic["id"]
            require(tid not in topics,f"duplicate topic {tid}")
            topics[tid]=topic

    for mid,(mpath,module) in modules.items():
        pipeline=module.get("pipeline_status")
        if pipeline is not None:
            require(pipeline in PIPELINE_STATUS,f"{mid}: invalid pipeline_status {pipeline}")

        source_map_file=module.get("source_map_file")
        if source_map_file:
            smpath=mpath.parent/source_map_file
            require(smpath.is_file(),f"{mid}: missing source map")
            sm=read_json(smpath)
            require(sm.get("module_id")==mid,f"{mid}: source map module mismatch")
            micro_ids=set()
            covered=set()
            for micro in sm.get("microtopics",[]):
                mic=micro.get("id")
                require(isinstance(mic,str) and mic and mic not in micro_ids,f"{mid}: duplicate/missing microtopic id")
                micro_ids.add(mic)
                tid=micro.get("topic_id")
                require(tid in topics,f"{mic}: unknown topic {tid}")
                covered.add(tid)
                require(micro.get("freshness_class") in FRESHNESS_CLASSES,f"{mic}: invalid freshness class")
                refs=micro.get("sources",[])
                require(refs,f"{mic}: no source mapping")
                for ref in refs:
                    require(ref.get("source_id") in sources,f"{mic}: unknown source {ref.get('source_id')}")
                    require(isinstance(ref.get("locator"),str) and ref["locator"].strip(),f"{mic}: missing locator")
            if pipeline in {"mapped","drafting","review","study_ready"}:
                module_topics={x["id"] for x in module["topics"]}
                require(module_topics <= covered,f"{mid}: mapped module has uncovered topics {sorted(module_topics-covered)}")

        claims_file=module.get("claims_file")
        if claims_file:
            cpath=mpath.parent/claims_file
            require(cpath.is_file(),f"{mid}: missing claims file")
            for claim in read_jsonl(cpath):
                cid=claim.get("id")
                require(isinstance(cid,str) and cid and cid not in claims,f"{cpath}: duplicate/missing claim id")
                require(claim.get("kind") in CLAIM_KINDS,f"{cid}: invalid claim kind")
                require(claim.get("render_role") in RENDER_ROLES,f"{cid}: invalid render role")
                statement=claim.get("statement")
                require(isinstance(statement,str) and statement.strip(),f"{cid}: empty statement")
                tids=claim.get("topic_ids")
                require(isinstance(tids,list) and tids,f"{cid}: missing topic_ids")
                for tid in tids:
                    require(tid in topics,f"{cid}: unknown topic {tid}")
                refs=claim.get("source_refs")
                require(isinstance(refs,list) and refs,f"{cid}: missing source_refs")
                for ref in refs:
                    require(ref.get("source_id") in sources,f"{cid}: unknown source {ref.get('source_id')}")
                    require(isinstance(ref.get("locator"),str) and ref["locator"].strip(),f"{cid}: missing source locator")
                freshness=claim.get("freshness",{})
                require(freshness.get("class") in FRESHNESS_CLASSES,f"{cid}: invalid freshness class")
                require(freshness.get("status") in FRESHNESS_STATUS,f"{cid}: invalid freshness status")
                require(claim.get("review_status") in REVIEW_STATUS,f"{cid}: invalid review status")
                deps=claim.get("depends_on_claim_ids")
                require(isinstance(deps,list),f"{cid}: invalid dependencies")
                claims[cid]=(mid,claim)

        qpath=mpath.parent/module["questions_file"]
        for q in read_jsonl(qpath):
            questions.append((mid,q))

    graph={}
    for cid,(mid,claim) in claims.items():
        deps=claim["depends_on_claim_ids"]
        for dep in deps:
            require(dep in claims,f"{cid}: unknown claim dependency {dep}")
        graph[cid]=deps
    acyclic(graph,"claims")

    for mid,q in questions:
        claim_ids=q.get("claim_ids",[])
        require(isinstance(claim_ids,list),f"{q.get('id')}: claim_ids must be a list")
        for cid in claim_ids:
            require(cid in claims,f"{q.get('id')}: unknown claim {cid}")
            claim_topics=set(claims[cid][1]["topic_ids"])
            require(claim_topics.intersection(q["topic_ids"]),f"{q.get('id')}: claim {cid} does not overlap question topics")
        pipeline=modules[mid][1].get("pipeline_status")
        if pipeline=="study_ready":
            require(claim_ids,f"{q.get('id')}: study-ready question without claim_ids")

    print(f"Claim graph OK: {len(claims)} claims, {len(questions)} questions, {len(topics)} topics.")


if __name__=="__main__":
    try:
        main()
    except (ValueError,KeyError,TypeError,OSError) as exc:
        raise SystemExit(f"Claim validation failed: {exc}")
