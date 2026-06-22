"""Quick orthography gate (Sprint 3C, DEC-021).

Checks every HTML file under lexicon/ and score/ for the banned-form list.
Run: python3 main/scripts/validate_orthography.py
Exit 0 = clean. Exit 1 = violations found (list printed to stdout).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Each entry: (banned_pattern, canonical_form)
BANNED = [
    (r"\bmerchant sovereignty\b", "merchant-sovereignty"),
    (r"\bMerchant Sovereignty\b", "Merchant Sovereignty (hyphenated in slug only)"),
    (r"\bplatform capture\b", "platform-capture (noun-phrase slug)"),
    (r"\broute to buyer\b", "route-to-buyer"),
    (r"\bai merchant\b", "AI Merchant (caps) or ai-merchant (slug)"),
]

violations = []
for html in sorted(ROOT.glob("lexicon/**/*.html")) + sorted(ROOT.glob("score/**/*.html")):
    text = html.read_text()
    for pattern, canonical in BANNED:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            violations.append(f"{html.relative_to(ROOT)}:{m.start()} — {m.group()!r} → use {canonical!r}")

if violations:
    print(f"ORTHOGRAPHY VIOLATIONS ({len(violations)}):")
    for v in violations:
        print(" ", v)
    sys.exit(1)
else:
    print("Orthography clean.")
