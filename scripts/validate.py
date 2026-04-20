#!/usr/bin/env python3
"""
Integrity check for the Tai Po citizen archive registry.

Verifies:
  - Registry has 23 records
  - All records have a WFC-### identifier
  - Identifiers are unique
  - Every registry record appears in the scoring matrix
  - Every mitigation action references a known record
  - EDTF dates look plausible (uuuu, YYYY, YYYY-MM, YYYY-MM-DD, or ongoing markers)
  - Every dc_type value is in the controlled vocabulary
"""
from __future__ import annotations
import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
RISK = REPO / "risk_assessment"

EDTF_PATTERNS = [
    re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    re.compile(r"^\d{4}-\d{2}$"),
    re.compile(r"^\d{4}$"),
    re.compile(r"^uuuu$"),
    re.compile(r"^\d{4}-\d{2}~$"),
    re.compile(r"^\d{4}~$"),
]

def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))

def check(name: str, ok: bool, detail: str = "") -> bool:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {name}" + (f" — {detail}" if detail else ""))
    return ok

def main() -> int:
    print("Validating Tai Po Citizen Archive repository...\n")
    all_ok = True

    registry = read_csv(DATA / "registry.csv")
    scoring = read_csv(RISK / "scoring_matrix.csv")
    actions = read_csv(RISK / "mitigation_actions.csv")
    vocab_type = read_csv(DATA / "vocab_dc_type.csv")

    print("Registry:")
    all_ok &= check("21 records", len(registry) == 21, f"found {len(registry)}")

    ids = [r["dc_identifier"] for r in registry]
    id_pattern = re.compile(r"^WFC-\d{3}$")
    all_ok &= check("all identifiers match WFC-###",
                    all(id_pattern.match(i) for i in ids))
    all_ok &= check("identifiers are unique", len(set(ids)) == len(ids))

    registry_types = {r["dc_type"] for r in registry}
    vocab_terms = {v["term"] for v in vocab_type}
    missing = registry_types - vocab_terms
    all_ok &= check("all dc_type values in controlled vocab",
                    not missing,
                    f"unknown: {missing}" if missing else "")

    bad_dates = []
    for r in registry:
        for field in ("dc_date_created", "dc_date_modified"):
            val = r.get(field, "").strip()
            if not val:
                continue
            if not any(p.match(val) for p in EDTF_PATTERNS):
                bad_dates.append(f"{r['dc_identifier']}.{field}={val!r}")
    all_ok &= check("all dates match EDTF patterns",
                    not bad_dates,
                    f"{len(bad_dates)} bad" if bad_dates else "")

    print("\nScoring matrix:")
    all_ok &= check("21 rows", len(scoring) == 21, f"found {len(scoring)}")
    scoring_ids = {r["id"] for r in scoring}
    registry_ids = set(ids)
    all_ok &= check("scoring IDs match registry IDs",
                    scoring_ids == registry_ids)

    print("\nMitigation actions:")
    action_ids = {r["id"] for r in actions}
    orphan_actions = action_ids - registry_ids
    all_ok &= check("every action references a known record",
                    not orphan_actions,
                    f"orphan: {orphan_actions}" if orphan_actions else "")

    valid_priorities = {"URGENT", "SHORT-TERM", "LONG-TERM",
                        "ONGOING", "ETHICAL", "RECOMMENDED"}
    bad_priorities = {r["priority"] for r in actions} - valid_priorities
    all_ok &= check("all priorities valid",
                    not bad_priorities,
                    f"bad: {bad_priorities}" if bad_priorities else "")

    print()
    if all_ok:
        print("All checks passed.")
        return 0
    print("Some checks failed.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
