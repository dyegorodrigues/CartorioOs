"""Read-only consistency checks for the 2026-09-12 audit, not legal validation.

Run: python3 -B scripts/audit_checks.py
No network, dependencies, learner writes, or automatic S2 promotion.
"""

import hashlib
import json
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data/audit/validation_review_2026-09-12.json"


def new_precept_eligible(exam_date, days, effective_from=None, not_before=None):
    """Temporal gate only. Does not infer scope or handle repealed provisions."""
    if type(days) is not int or days < 0:
        raise ValueError("days must be a nonnegative integer")
    cutoff = date.fromisoformat(exam_date) - timedelta(days=days)
    exact = date.fromisoformat(effective_from) if effective_from else None
    lower = date.fromisoformat(not_before) if not_before else None
    if exact and lower and exact < lower:
        raise ValueError("effective date conflicts with lower bound")
    if exact:
        return exact <= cutoff
    if lower and lower > cutoff:
        return False
    return None  # Unknown is not approval.


def independent_pass_eligible(item):
    atoms = item.get("required_atoms", [])
    return bool(
        item.get("scope") == "IN_SCOPE"
        and item.get("item_status") == "VALID"
        and item.get("result") == "COVERED"
        and item.get("evaluation") == "BLIND_HELD_OUT"
        and item.get("used_in_build") is False
        and item.get("answer_sealed_before_key") is True
        and item.get("official_source_verified") is True
        and item.get("legal_snapshot_verified") is True
        and atoms
        and all(a.get("covered") is True and a.get("evidence") for a in atoms)
    )


def validate(data, root):
    errors = []
    if data.get("schema_version") != 1:
        errors.append("unsupported schema version")
    if data.get("learner_release") is not False:
        errors.append("audit snapshot must not release learner material")
    for section in ("items", "frozen_documents", "normative_checks"):
        if not isinstance(data.get(section), list) or not data[section]:
            errors.append(f"missing or empty audit section: {section}")
    if errors:
        return errors
    seen = set()
    for item in data.get("items", []):
        key = item.get("id")
        if not key or key in seen:
            errors.append(f"duplicate or missing item id: {key}")
        seen.add(key)
        if item.get("scope") not in {"IN_SCOPE", "OUT_OF_SCOPE"}:
            errors.append(f"{key}: invalid scope")
        if item.get("item_status") not in {"VALID", "ANNULLED", "UNKNOWN"}:
            errors.append(f"{key}: invalid item status")
        if item.get("result") not in {"COVERED", "GAP", "EXCLUDED"}:
            errors.append(f"{key}: invalid result")
        if not item.get("source_urls"):
            errors.append(f"{key}: missing source URLs")
        if item.get("result") == "COVERED":
            atoms = item.get("required_atoms", [])
            if not atoms or not all(a.get("covered") is True and a.get("evidence") for a in atoms):
                errors.append(f"{key}: coverage claim lacks atom evidence")
            if item.get("scope") != "IN_SCOPE" or item.get("item_status") != "VALID":
                errors.append(f"{key}: excluded/annulled item cannot be a scored pass")
        if type(item.get("claim_independent_pass")) is not bool:
            errors.append(f"{key}: explicit independent-pass flag required")
        elif item["claim_independent_pass"] and not independent_pass_eligible(item):
            errors.append(f"{key}: unsupported independent pass")

    for frozen in data.get("frozen_documents", []):
        path = (root / frozen["path"]).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            errors.append(f"invalid frozen path: {frozen['path']}")
            continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != frozen["sha256"]:
            errors.append(f"frozen document changed: {frozen['path']}")

    for norm in data.get("normative_checks", []):
        try:
            expected = new_precept_eligible(
                norm["exam_date"], norm["exclusion_days"],
                norm.get("effective_from"), norm.get("effective_not_before"),
            )
            if norm.get("new_precept_eligible") is not expected:
                errors.append(f"{norm['id']}: incorrect temporal eligibility")
            lower = norm.get("effective_from") or norm.get("effective_not_before")
            if lower and date.fromisoformat(data["checked_at"]) < date.fromisoformat(lower):
                if norm.get("current_status") != "NOT_YET_EFFECTIVE":
                    errors.append(f"{norm['id']}: premature current-law claim")
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f"invalid normative check: {exc}")
    return errors


def main():
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    errors = validate(data, ROOT)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    eligible = sum(independent_pass_eligible(i) for i in data["items"])
    print(f"Consistency OK: {len(data['items'])} audit records; "
          f"{len(data['frozen_documents'])} frozen hashes preserved.")
    print(f"Independent passes added by this audit: {eligible}. "
          "No S2 or learner release. Legal/pedagogical sufficiency is not tested by this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
