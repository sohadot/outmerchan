"""Enforces AI_READABILITY_POLICY.md: canonical/meta discipline, valid JSON-LD,
DefinedTermSet coverage, and sitemap consistency with active routes."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"
ORIGIN = "https://outmerchant.com"


def collect_defined_terms(node, out):
    if isinstance(node, dict):
        if node.get("@type") == "DefinedTerm" and node.get("name"):
            out.add(node["name"])
        for v in node.values():
            collect_defined_terms(v, out)
    elif isinstance(node, list):
        for v in node:
            collect_defined_terms(v, out)


def run():
    errors = []
    pages = json.loads((DATA / "pages.json").read_text())["pages"]
    terms = json.loads((DATA / "glossary_terms.json").read_text())["terms"]
    active = [p for p in pages if p["status"] == "active"]

    for p in active:
        path = ROOT / "index.html" if p["route"] == "/" else ROOT / p["route"].strip("/") / "index.html"
        if not path.exists():
            errors.append(f"seo: active route {p['route']} has no file")
            continue
        html = path.read_text()
        expected_canonical = ORIGIN + p["route"]
        if f'<link rel="canonical" href="{expected_canonical}"' not in html:
            errors.append(f"seo: {p['route']} missing canonical {expected_canonical}")
        if not re.search(r"<title>[^<]+</title>", html):
            errors.append(f"seo: {p['route']} missing title")
        if not re.search(r'<meta name="description" content="[^"]+"', html):
            errors.append(f"seo: {p['route']} missing meta description")
        if not re.search(r'<meta name="robots" content="index', html):
            errors.append(f"seo: {p['route']} missing robots meta")
        h1_count = len(re.findall(r"<h1[\s>]", html))
        if h1_count != 1:
            errors.append(f"seo: {p['route']} must have exactly one H1, found {h1_count}")
        text = re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", html, flags=re.S)
        words = len(text.split())
        if words < 200:
            errors.append(f"seo: {p['route']} is thin content ({words} words of visible text)")

    # JSON-LD must parse on every canonical lexicon surface (home + /lexicon/),
    # and the union of their DefinedTerms must cover every in_jsonld term.
    defined = set()
    for surface, path in (("home", ROOT / "index.html"), ("/lexicon/", ROOT / "lexicon" / "index.html")):
        if not path.exists():
            continue
        html = path.read_text()
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        if not blocks:
            errors.append(f"seo: {surface} surface carries no JSON-LD")
        for block in blocks:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as exc:
                errors.append(f"seo: invalid JSON-LD on {surface} surface ({exc})")
                continue
            collect_defined_terms(data, defined)
    for t in terms:
        if t.get("in_jsonld") and t["term"] not in defined:
            errors.append(f"seo: lexicon term '{t['term']}' marked in_jsonld but absent from DefinedTermSet surfaces")

    # Indexability layer
    robots = ROOT / "robots.txt"
    sitemap = ROOT / "sitemap.xml"
    if not robots.exists():
        errors.append("seo: robots.txt missing")
    elif "sitemap" not in robots.read_text().lower():
        errors.append("seo: robots.txt does not reference the sitemap")
    if not sitemap.exists():
        errors.append("seo: sitemap.xml missing")
    else:
        sm = sitemap.read_text()
        for p in active:
            if f"<loc>{ORIGIN}{p['route']}</loc>" not in sm:
                errors.append(f"seo: active route {p['route']} missing from sitemap.xml")
        # Only active routes may appear in the sitemap — never planned or unregistered ones
        active_routes = {p["route"] for p in active}
        for loc in re.findall(r"<loc>([^<]+)</loc>", sm):
            route = loc.replace(ORIGIN, "") or "/"
            if route not in active_routes:
                errors.append(f"seo: sitemap contains non-active route {route}")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("seo: OK" if not errs else f"seo: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
