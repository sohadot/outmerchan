"""Enforces reference-standard integrity (Sprint 2C-1, DEC-013):
dimension pages match score_dimensions.json, level pages match
score_levels.json, the protected Outmerchant rank statement is present,
and required cross-links exist in the rendered pages."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"


def page_html(route):
    path = ROOT / route.strip("/") / "index.html"
    return path.read_text(encoding="utf-8") if path.exists() else None


def hrefs(html):
    return set(re.findall(r'href="(/[^"#]*)"', html))


def run():
    errors = []
    dims = json.loads((DATA / "score_dimensions.json").read_text(encoding="utf-8"))["dimensions"]
    levels = json.loads((DATA / "score_levels.json").read_text(encoding="utf-8"))["levels"]

    for d in dims:
        html = page_html(d["route"])
        if html is None:
            errors.append(f"reference: dimension page missing for {d['route']}")
            continue
        if d["name"] not in html:
            errors.append(f"reference: {d['route']} does not state dimension name '{d['name']}'")
        if f"{d['order']:02d} / {d['code']}" not in html:
            errors.append(f"reference: {d['route']} does not state governed dimension ID {d['order']:02d}/{d['code']}")
        links = hrefs(html)
        if "/score/" not in links:
            errors.append(f"reference: {d['route']} does not link to /score/")
        if not any(l.startswith("/levels/") for l in links):
            errors.append(f"reference: {d['route']} does not link to any level page")

    for l in levels:
        html = page_html(l["route"])
        if html is None:
            errors.append(f"reference: level page missing for {l['route']}")
            continue
        if l["name"] not in html:
            errors.append(f"reference: {l['route']} does not state tier name '{l['name']}'")
        if f"{l['min']} — {l['max']}" not in html:
            errors.append(f"reference: {l['route']} does not state governed range {l['min']}–{l['max']}")
        links = hrefs(html)
        if "/score/" not in links:
            errors.append(f"reference: {l['route']} does not link to /score/")
        if "/levels/outmerchant/" not in links:
            errors.append(f"reference: {l['route']} does not link to /levels/outmerchant/")

    # The protected rank: /levels/outmerchant/ must define it as the protected highest rank
    om = page_html("/levels/outmerchant/")
    if om:
        if "protected" not in om.lower():
            errors.append("reference: /levels/outmerchant/ does not define Outmerchant as a protected rank")
        if "DEC-006" not in om:
            errors.append("reference: /levels/outmerchant/ does not cite the protecting decision (DEC-006)")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("reference: OK" if not errs else f"reference: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
