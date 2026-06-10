"""The execution court (QUALITY_GATE.md).

Runs every validator. Exits non-zero on any governance violation.
A red gate blocks merge — fix the change, or change the law explicitly
in the governing document with a DECISION_LOG.md entry. No third path.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_definitional
import validate_engine
import validate_glossary
import validate_links
import validate_reference
import validate_routes
import validate_score_model
import validate_seo

VALIDATORS = [
    ("score model (SCORE_GOVERNANCE.md)", validate_score_model),
    ("lexicon (LEXICON_GOVERNANCE.md)", validate_glossary),
    ("routes (ROUTE_GOVERNANCE.md)", validate_routes),
    ("internal links (ROUTE_GOVERNANCE.md)", validate_links),
    ("seo / ai-readability (AI_READABILITY_POLICY.md)", validate_seo),
    ("reference standard (DEC-013)", validate_reference),
    ("definitional authority (DEC-014)", validate_definitional),
    ("score engine governance (DEC-015)", validate_engine),
]


def main():
    total = 0
    print("OutMerchant Quality Gate")
    print("=" * 60)
    for name, module in VALIDATORS:
        errors = module.run()
        status = "PASS" if not errors else f"FAIL ({len(errors)})"
        print(f"[{status:>9}] {name}")
        for e in errors:
            print(f"            - {e}")
        total += len(errors)
    print("=" * 60)
    if total:
        print(f"GATE RED — {total} violation(s). Fix the change or change the law (DECISION_LOG.md).")
        return 1
    print("GATE GREEN — every layer serves the merchant.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
