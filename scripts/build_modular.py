"""Build separate module payloads and a small manifest for on-demand loading."""
import argparse
import hashlib
import json
from pathlib import Path
from validate_modular import ROOT, validate


def build(root=ROOT, output=None):
    root = Path(root)
    output = Path(output) if output else root / "dist/modular"
    data = validate(root)
    output.mkdir(parents=True, exist_ok=True)
    entries = []
    for mid, module in data["modules"].items():
        descriptor = module["descriptor"]
        target = output / "modules" / mid
        target.mkdir(parents=True, exist_ok=True)
        payload = {"module": descriptor, "questions": module["questions"]}
        raw = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode()
        (target / "module.json").write_bytes(raw)
        reading_hash = None
        if module["reading_text"]:
            reading = module["reading_text"].encode()
            (target / "reading.html").write_bytes(reading)
            reading_hash = hashlib.sha256(reading).hexdigest()
        elif (target / "reading.html").exists():
            (target / "reading.html").unlink()
        entries.append({"id": mid, "title": descriptor["title"], "status": descriptor["status"],
                        "path": f"modules/{mid}/module.json",
                        "reading_path": f"modules/{mid}/reading.html" if reading_hash else None,
                        "payload_sha256": hashlib.sha256(raw).hexdigest(),
                        "reading_sha256": reading_hash,
                        "question_count": len(module["questions"])})
    manifest = {"schema_version": 1, "title": data["catalog"]["title"],
                "subjects": data["catalog"]["subjects"], "booklets": data["catalog"]["booklets"],
                "modules": entries, "legal_certification": False}
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    # Laws and sources are referenced registries, not replicated in each chapter.
    for filename in ("sources.json", "law_registry.json"):
        (output / filename).write_bytes((root / "content" / filename).read_bytes())
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build(output=args.output)
    print(f"Built {len(result['modules'])} separate modules. Content states preserved; no site deployment.")
