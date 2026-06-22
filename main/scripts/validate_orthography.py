"""Enforces orthography governance (DEC-016): Outmerchant is the official spelling.
Forbidden forms: OutMerchant, Out Merchant, outMerchant."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN = ["OutMerchant", "Out Merchant", "outMerchant"]

SCAN_PATTERNS = [
    ROOT.glob("**/*.html"),
    [ROOT / f for f in [
        "README.md", "ASSET_THESIS.md", "CATEGORY_GRAVITY.md",
        "SCORE_GOVERNANCE.md", "LEXICON_GOVERNANCE.md", "ROUTE_GOVERNANCE.md",
        "CLAIM_POLICY.md", "AI_READABILITY_POLICY.md", "QUALITY_GATE.md"
    ]],
    (ROOT / "main" / "data").glob("*.json"),
]
# NOTE: DECISION_LOG.md and main/reports/ are intentionally excluded from SCAN_PATTERNS.
# DECISION_LOG.md preserves historical decision body text verbatim (DEC-001 through DEC-015)
# which references the superseded spelling as a historical record.
# main/reports/ audit documents intentionally quote forbidden forms for documentation purposes.


def run():
    errors = []
    files = []
    for pattern in SCAN_PATTERNS:
        files.extend(pattern)
    for path in files:
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for form in FORBIDDEN:
            if form in content:
                count = content.count(form)
                errors.append(f"orthography: '{form}' found {count} time(s) in {path.relative_to(ROOT)}")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("orthography: OK" if not errs else f"orthography: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
