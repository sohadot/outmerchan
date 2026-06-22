"""Enforces orthography governance (DEC-016): Outmerchant is the official spelling.
Forbidden forms: OutMerchant, Out Merchant, outMerchant.
DECISION_LOG.md is excluded to preserve historical record verbatim."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN = ["OutMerchant", "Out Merchant", "outMerchant"]


def _files():
    for p in ROOT.rglob("*.html"):
        yield p
    for name in [
        "README.md", "ASSET_THESIS.md", "CATEGORY_GRAVITY.md",
        "SCORE_GOVERNANCE.md", "LEXICON_GOVERNANCE.md", "ROUTE_GOVERNANCE.md",
        "CLAIM_POLICY.md", "AI_READABILITY_POLICY.md", "QUALITY_GATE.md",
    ]:
        p = ROOT / name
        if p.exists():
            yield p
    for p in (ROOT / "main" / "data").glob("*.json"):
        yield p
    for p in (ROOT / "main" / "reports").glob("*.md"):
        yield p


def run():
    errors = []
    for path in _files():
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for form in FORBIDDEN:
            if form in content:
                count = content.count(form)
                errors.append(
                    f"orthography: '{form}' found {count} time(s) in {path.relative_to(ROOT)}"
                )
    return errors


if __name__ == "__main__":
    import sys
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("orthography: OK" if not errs else f"orthography: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
