"""Enforces LEXICON_GOVERNANCE.md — the term admission law — against glossary_terms.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"

VALID_SCORE_RELATIONS = {"DEP", "OWN", "REP", "PAY", "FEE", "XBR", "AGT", "GOV", "instrument", "tier", "doctrine"}
VALID_TYPES = {"verb", "noun", "concept"}
VALID_STATUS = {"active", "deprecated"}


def run():
    errors = []
    terms = json.loads((DATA / "glossary_terms.json").read_text())["terms"]
    routes = {p["route"] for p in json.loads((DATA / "pages.json").read_text())["pages"]}
    slugs = [t["slug"] for t in terms]
    slugset = set(slugs)

    if len(slugset) != len(slugs):
        errors.append("lexicon: duplicate term slugs")

    for t in terms:
        s = t.get("slug", "?")
        # The admission law: definition, function, relations, route, score relation
        for field in ("term", "definition", "system_function", "route", "score_relation"):
            if not t.get(field):
                errors.append(f"lexicon: {s} violates admission law — missing {field}")
        if not t.get("related"):
            errors.append(f"lexicon: {s} violates admission law — no relationship to another term")
        for rel in t.get("related", []):
            if rel not in slugset:
                errors.append(f"lexicon: {s} relates to unknown term '{rel}'")
        if t.get("route") and t["route"] not in routes:
            errors.append(f"lexicon: {s} route {t['route']} not registered in pages.json")
        if t.get("score_relation") not in VALID_SCORE_RELATIONS:
            errors.append(f"lexicon: {s} has invalid score_relation '{t.get('score_relation')}'")
        if t.get("type") not in VALID_TYPES:
            errors.append(f"lexicon: {s} has invalid type '{t.get('type')}'")
        if t.get("status") not in VALID_STATUS:
            errors.append(f"lexicon: {s} has invalid status '{t.get('status')}'")

    # Casing law: the verb/rank duality is constitutional (DEC-001)
    verb = next((t for t in terms if t["slug"] == "outmerchant-verb"), None)
    noun = next((t for t in terms if t["slug"] == "outmerchant-noun"), None)
    if not verb or verb["term"] != "outmerchant" or verb["type"] != "verb":
        errors.append("lexicon: constitutional term 'outmerchant' (verb, lowercase) missing or malformed (DEC-001)")
    if not noun or noun["term"] != "Outmerchant" or noun["type"] != "noun":
        errors.append("lexicon: constitutional term 'Outmerchant' (noun, initial capital only) missing or malformed (DEC-001, DEC-016)")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("glossary: OK" if not errs else f"glossary: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
