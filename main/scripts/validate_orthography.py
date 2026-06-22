"""Orthography gate (Sprint 3C, DEC-022).

Checks that every HTML file in the repo uses the governed OutMerchant
orthography for the nine governed terms. Exits non-zero on any violation
so CI blocks the merge.

Governed forms (case-sensitive where shown):
  OutMerchant          — not Outmerchant / outmerchant / Out Merchant
  merchant sovereignty — not Merchant Sovereignty (mid-sentence)
  platform capture     — not Platform Capture (mid-sentence)
  platform dependency  — not Platform Dependency (mid-sentence)
  route-to-buyer       — hyphenated compound modifier
  portable reputation  — not Portable Reputation (mid-sentence)
  agentic readiness    — not Agentic Readiness (mid-sentence)
  machine-readable     — hyphenated compound modifier
  governance independence — not Governance Independence (mid-sentence)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

VIOLATIONS = [
    (re.compile(r'Outmerchant|outmerchant|Out Merchant'), "use \'OutMerchant\'"),
    (re.compile(r'route to buyer(?!-| control)'), "use \'route-to-buyer\'"),
    (re.compile(r'machine readable'), "use \'machine-readable\'"),
]

errors = []
for html in ROOT.rglob("*.html"):
    text = html.read_text(encoding="utf-8", errors="ignore")
    for pattern, note in VIOLATIONS:
        for m in pattern.finditer(text):
            line_no = text[: m.start()].count("\n") + 1
            errors.append(f"{html.relative_to(ROOT)}:{line_no}: {note} (found {m.group()!r})")

if errors:
    print("ORTHOGRAPHY VIOLATIONS:")
    for e in errors:
        print(" ", e)
    sys.exit(1)
else:
    print(f"orthography gate passed ({len(list(ROOT.rglob('*.html')))} files checked)")
