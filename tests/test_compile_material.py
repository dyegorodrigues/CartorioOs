"""Regression checks for propagation, references, and the BUILD boundary.

These tests intentionally do not claim to verify the truth of legal prose.
"""

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.compile_material import SOURCE, case_review_fingerprint, compile_documents, render_sections, run, validate


class MaterialCompilerTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_canonical_correction_reaches_each_answer_surface(self):
        unit = self.data["units"][0]
        prop = unit["propositions"][1]
        old_rule = prop["rule"]
        marker = "CORRECAO-DE-TESTE-SEM-CONTEUDO-JURIDICO"
        prop["rule"] = marker
        sections = render_sections(unit, self.data)
        for name in ("MASTER", "REVIEW", "Q→A", "EXAM / OUTPUT"):
            with self.subTest(surface=name):
                self.assertIn(marker, sections[name])
                self.assertNotIn(old_rule, sections[name])
        # Two cases depend on this proposition; both receive the corrected base.
        self.assertEqual(sections["EXAM / OUTPUT"].count(marker), 2)

    def test_case_cannot_silently_cite_missing_or_untaught_rule(self):
        for target in ("UNKNOWN", "LRP-RI-PAGAMENTO-015"):
            with self.subTest(target=target):
                data = copy.deepcopy(self.data)
                data["units"][0]["cases"][0]["proposition_ids"] = [target]
                with self.assertRaisesRegex(ValueError, "taught propositions"):
                    compile_documents(data)

    def test_rule_cannot_lose_its_official_source(self):
        for refs in ([], ["UNVERIFIED"]):
            with self.subTest(refs=refs):
                data = copy.deepcopy(self.data)
                data["units"][0]["propositions"][0]["source_ids"] = refs
                with self.assertRaisesRegex(ValueError, "source"):
                    compile_documents(data)

    def test_graph_links_resolve_across_units_without_duplicating_home(self):
        validate(self.data)
        ri = render_sections(self.data["units"][1], self.data)["MAP"]
        self.assertIn("RG_AFASTAMENTO_INTERVENCAO_V0.1.md#rg-pen-032iii", ri)
        self.data["units"][1]["edges"][-1]["to"] = "MISSING"
        with self.assertRaisesRegex(ValueError, "unknown node"):
            compile_documents(self.data)

    def test_prerequisite_cycle_is_rejected_but_contrast_is_allowed(self):
        validate(self.data)  # Existing confusable_with edges are not prerequisites.
        self.data["units"][0]["edges"].append({
            "from": "RG-BASE-FINALIDADE", "type": "requires", "to": "RG-DISC-PREV-001"
        })
        with self.assertRaisesRegex(ValueError, "cycle"):
            compile_documents(self.data)

    def test_duplicate_id_and_output_collision_are_rejected(self):
        data = copy.deepcopy(self.data)
        data["units"][1]["propositions"][0]["id"] = data["units"][0]["propositions"][0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate id"):
            compile_documents(data)
        self.data["units"][1]["filename"] = self.data["units"][0]["filename"]
        with self.assertRaisesRegex(ValueError, "duplicate output"):
            compile_documents(self.data)

    def test_no_implicit_sufficiency_or_exam_snapshot_promotion(self):
        for state in ("S2", "RELEASED", None):
            data = copy.deepcopy(self.data)
            data["state"] = state
            with self.assertRaisesRegex(ValueError, "no release promotion"):
                compile_documents(data)
        self.data["exam_snapshot"] = "VERIFIED"
        with self.assertRaisesRegex(ValueError, "exam snapshot"):
            compile_documents(self.data)

    def test_case_requires_new_editorial_review_after_rule_or_conclusion_edit(self):
        for field in ("rule", "answer", "explanation", "question"):
            with self.subTest(field=field):
                data = copy.deepcopy(self.data)
                unit = data["units"][0]
                target = unit["propositions"][1] if field in {"rule", "explanation"} else unit["cases"][0]
                target[field] += " ALTERACAO-DE-TESTE"
                with self.assertRaisesRegex(ValueError, "stale editorial review"):
                    compile_documents(data)

    def test_missing_review_cannot_be_treated_as_independent_validation(self):
        case = self.data["units"][0]["cases"][0]
        case["editorial_review"]["kind"] = "BLIND_HELD_OUT"
        with self.assertRaisesRegex(ValueError, "editorial review"):
            compile_documents(self.data)

    def test_review_fingerprint_changes_with_source_snapshot(self):
        unit = self.data["units"][0]
        case = unit["cases"][0]
        original = case_review_fingerprint(case, unit, self.data)
        self.data["sources"][0]["checked_at"] = "2026-09-11"
        self.assertNotEqual(original, case_review_fingerprint(case, unit, self.data))
        with self.assertRaisesRegex(ValueError, "stale editorial review"):
            compile_documents(self.data)

    def test_check_detects_stale_derivative_and_does_not_rewrite_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            with self.assertRaisesRegex(ValueError, "missing or stale"):
                run(output=output, check=True)
            run(output=output)
            run(output=output, check=True)
            file = output / self.data["units"][0]["filename"]
            file.write_text("resposta antiga", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing or stale"):
                run(output=output, check=True)
            self.assertEqual(file.read_text(encoding="utf-8"), "resposta antiga")

    def test_output_path_cannot_escape_working_directory(self):
        self.data["units"][0]["filename"] = "../../STATUS.md"
        with self.assertRaisesRegex(ValueError, "output filename"):
            compile_documents(self.data)

    def test_committed_derivatives_are_current(self):
        run(check=True)


if __name__ == "__main__":
    unittest.main()
