"""Synthetic fixtures test mechanics only; they are NOT exam evidence."""

import copy
import json
import unittest

from scripts.audit_checks import (
    LEDGER, ROOT, independent_pass_eligible, new_precept_eligible, validate,
)


def clean_fixture():
    return {
        "id": "SYNTHETIC-TEST-ONLY", "scope": "IN_SCOPE", "item_status": "VALID",
        "evaluation": "BLIND_HELD_OUT", "result": "COVERED",
        "used_in_build": False, "answer_sealed_before_key": True,
        "official_source_verified": True, "legal_snapshot_verified": True,
        "claim_independent_pass": True,
        "required_atoms": [{"id": "TEST-ATOM", "covered": True, "evidence": "fixture only"}],
        "source_urls": ["https://example.invalid/test-only"],
    }


class AuditChecksTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(LEDGER.read_text(encoding="utf-8"))

    def test_real_ledger_consistent(self):
        self.assertEqual(validate(self.data, ROOT), [])

    def test_missing_or_empty_sections_rejected(self):
        for section in ("items", "frozen_documents", "normative_checks"):
            with self.subTest(section=section):
                data = copy.deepcopy(self.data)
                data[section] = []
                self.assertTrue(validate(data, ROOT))
                del data[section]
                self.assertTrue(validate(data, ROOT))

    def test_no_new_independent_passes(self):
        self.assertFalse(any(independent_pass_eligible(i) for i in self.data["items"]))

    def test_clean_synthetic_fixture_eligible(self):
        self.assertTrue(independent_pass_eligible(clean_fixture()))

    def test_each_safety_condition_is_required(self):
        bad_values = {
            "scope": "OUT_OF_SCOPE", "item_status": "ANNULLED",
            "evaluation": "COVERAGE_AUDIT", "result": "GAP",
            "used_in_build": True, "answer_sealed_before_key": None,
            "official_source_verified": False, "legal_snapshot_verified": False,
            "required_atoms": [],
        }
        for field, value in bad_values.items():
            with self.subTest(field=field):
                item = clean_fixture()
                item[field] = value
                self.assertFalse(independent_pass_eligible(item))

    def test_missing_atom_evidence_rejects_pass(self):
        item = clean_fixture()
        item["required_atoms"][0]["evidence"] = None
        self.assertFalse(independent_pass_eligible(item))

    def test_promotion_of_real_gap_rejected(self):
        self.data["items"][0]["claim_independent_pass"] = True
        self.assertTrue(validate(self.data, ROOT))

    def test_annulled_or_out_of_scope_cannot_be_covered(self):
        for field, value in [("scope", "OUT_OF_SCOPE"), ("item_status", "ANNULLED")]:
            with self.subTest(field=field):
                item = clean_fixture()
                item[field] = value
                item["claim_independent_pass"] = False
                data = copy.deepcopy(self.data)
                data["items"] = [item]
                self.assertTrue(validate(data, ROOT))

    def test_duplicate_id_rejected(self):
        self.data["items"].append(copy.deepcopy(self.data["items"][0]))
        self.assertTrue(validate(self.data, ROOT))

    def test_frozen_hash_change_detected(self):
        self.data["frozen_documents"][0]["sha256"] = "0" * 64
        self.assertTrue(validate(self.data, ROOT))

    def test_learner_release_blocked(self):
        self.data["learner_release"] = True
        self.assertTrue(validate(self.data, ROOT))

    def test_exact_cutoff_inclusive(self):
        self.assertTrue(new_precept_eligible("2026-11-22", 90, "2026-08-24"))
        self.assertTrue(new_precept_eligible("2026-11-22", 90, "2026-08-23"))
        self.assertFalse(new_precept_eligible("2026-11-22", 90, "2026-08-25"))

    def test_unknown_date_is_not_approval(self):
        self.assertIsNone(new_precept_eligible("2026-11-22", 90))
        self.assertIsNone(new_precept_eligible("2026-11-22", 90, not_before="2026-08-01"))

    def test_prov255_lower_bound_already_excludes_new_precepts(self):
        self.assertFalse(new_precept_eligible("2026-11-22", 90, not_before="2026-09-19"))

    def test_false_current_or_eligible_claim_rejected(self):
        for field, value in [("current_status", "CURRENT"), ("new_precept_eligible", True)]:
            with self.subTest(field=field):
                data = copy.deepcopy(self.data)
                data["normative_checks"][0][field] = value
                self.assertTrue(validate(data, ROOT))

    def test_inconsistent_or_invalid_dates_fail(self):
        with self.assertRaises(ValueError):
            new_precept_eligible("2026-11-22", 90, "2026-08-01", "2026-09-19")
        with self.assertRaises(ValueError):
            new_precept_eligible("2026-11-22", -1)


if __name__ == "__main__":
    unittest.main()
