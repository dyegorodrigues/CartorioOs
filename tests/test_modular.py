import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_modular import validate, basis_digest
from build_modular import build


class ModularIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / "content", self.root / "content")
        self.module = self.root / "content/modules/penal/dp01/c01/module.json"
        self.qpath = self.module.parent / "questions.jsonl"

    def change(self, path, update):
        value = json.loads(path.read_text())
        update(value)
        path.write_text(json.dumps(value))

    def question(self):
        return {"id": "TEST-Q-1", "kind": "learning", "origin": "authored",
                "prompt": "Fixture question", "answer": "Fixture answer",
                "explanation": "Fixture explanation", "topic_ids": ["PEN-DP01-C01-T01"],
                "source_ids": ["DD-2026-PEN-DP01"], "law_ids": [],
                "requires_question_ids": [], "difficulty": "easy", "order": 1,
                "review_status": "draft"}

    def test_build_keeps_modules_separate(self):
        manifest = build(self.root)
        self.assertEqual(len(manifest["modules"]), 7)
        self.assertTrue(all(m["status"] == "planned" for m in manifest["modules"]))
        for m in manifest["modules"]:
            self.assertTrue((self.root / "dist/modular" / m["path"]).is_file())
        self.assertNotIn("reading_text", json.dumps(manifest))

    def test_unknown_question_topic_fails(self):
        q = self.question()
        q["topic_ids"] = ["MISSING"]
        self.qpath.write_text(json.dumps(q))
        with self.assertRaisesRegex(ValueError, "unknown reference"):
            validate(self.root)

    def test_module_cycle_fails(self):
        self.change(self.module, lambda x: x.update(prerequisite_ids=["PEN-DP01-C02"]))
        with self.assertRaisesRegex(ValueError, "cycle"):
            validate(self.root)

    def test_reviewed_empty_module_fails(self):
        self.change(self.module, lambda x: x.update(status="reviewed", legal_checked_at="2026-10-03"))
        with self.assertRaisesRegex(ValueError, "without reading"):
            validate(self.root)

    def test_review_invalidated_by_teaching_edit(self):
        reading = self.module.parent / "reading.html"
        reading.write_text("<p>Fixture teaching.</p>")
        self.change(self.module, lambda x: x.update(reading_file="reading.html", status="draft"))
        q = self.question()
        self.qpath.write_text(json.dumps(q))
        data = validate(self.root)
        q["review_status"] = "reviewed"
        q["review"] = {"checked_at": "2026-10-03", "basis_digest": basis_digest(
            q, data["modules"], data["topics"], data["sources"], data["laws"])}
        self.qpath.write_text(json.dumps(q))
        validate(self.root)
        reading.write_text("<p>Changed fixture teaching.</p>")
        with self.assertRaisesRegex(ValueError, "stale review"):
            validate(self.root)

    def test_official_label_requires_exam_metadata(self):
        q = self.question()
        q.update(kind="official", origin="official")
        self.qpath.write_text(json.dumps(q))
        with self.assertRaisesRegex(ValueError, "missing board"):
            validate(self.root)

    def test_cannot_reference_outside_module(self):
        outside = self.root / "outside.html"
        outside.write_text("private")
        self.change(self.module, lambda x: x.update(reading_file=str(outside)))
        with self.assertRaisesRegex(ValueError, "outside content"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
