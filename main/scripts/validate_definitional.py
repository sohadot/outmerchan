"""Enforces definitional authority (Sprint 2C-2, DEC-014):
every active lexicon term has a live canonical page carrying its governed
definition verbatim and its DefinedTerm JSON-LD; the /lexicon/ index lists
every term; /protocol/ binds the four system functions together."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"
ORIGIN = "https://outmerchant.com"


def page_html(route):
    path = ROOT / route.strip("/") / "index.html"
    return path.read_text(encoding="utf-8") if path.exists() else None


def jsonld_terms(html):
    names = set()
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            return None
        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                if node.get("@type") == "DefinedTerm" and node.get("name"):
                    names.add(node["name"])
                stack.extend(node.values())
            elif isinstance(node, list):
                stack.extend(node)
    return names


def run():
    errors = []
    terms = json.loads((DATA / "glossary_terms.json").read_text(encoding="utf-8"))["terms"]
    pages = json.loads((DATA / "pages.json").read_text(encoding="utf-8"))["pages"]
    status = {p["route"]: p["status"] for p in pages}
    active_terms = [t for t in terms if t["status"] == "active"]

    # Status parity: every active term has a registered, ACTIVE route with a live page
    for t in active_terms:
        r = t["route"]
        if r not in status:
            errors.append(f"definitional: term '{t['term']}' route {r} not registered")
            continue
        if status[r] != "active":
            errors.append(f"definitional: term '{t['term']}' is active but its route {r} is {status[r]}")
            continue
        html = page_html(r)
        if html is None:
            errors.append(f"definitional: term '{t['term']}' has no live page at {r}")
            continue
        if t["term"] not in html:
            errors.append(f"definitional: {r} does not state the canonical term '{t['term']}'")
        if t["definition"] not in html:
            errors.append(f"definitional: {r} does not carry the governed definition of '{t['term']}' verbatim")
        found = jsonld_terms(html)
        if found is None:
            errors.append(f"definitional: invalid JSON-LD on {r}")
        elif t.get("in_jsonld") and t["term"] not in found:
            errors.append(f"definitional: {r} missing DefinedTerm JSON-LD for '{t['term']}'")

    # The /lexicon/ index must list every active term and carry the full DefinedTermSet
    idx = page_html("/lexicon/")
    if idx is None:
        errors.append("definitional: /lexicon/ index page missing")
    else:
        idx_terms = jsonld_terms(idx) or set()
        for t in active_terms:
            if f'href="{t["route"]}"' not in idx:
                errors.append(f"definitional: /lexicon/ does not link to {t['route']}")
            if t.get("in_jsonld") and t["term"] not in idx_terms:
                errors.append(f"definitional: /lexicon/ DefinedTermSet missing '{t['term']}'")

    # /protocol/ binds the system: named, measured, explained, protected
    proto = page_html("/protocol/")
    if proto is None:
        errors.append("definitional: /protocol/ page missing")
    else:
        if "named, measured, explained, and protected" not in proto:
            errors.append("definitional: /protocol/ does not state the binding sentence (named, measured, explained, protected)")
        for target in ("/score/", "/lexicon/", "/levels/outmerchant/"):
            if f'href="{target}"' not in proto:
                errors.append(f"definitional: /protocol/ does not link to {target}")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("definitional: OK" if not errs else f"definitional: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
