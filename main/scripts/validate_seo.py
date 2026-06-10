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

    # JSON-LD on the home surface must parse and carry the lexicon
    html = (ROOT / "index.html").read_text()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    if not blocks:
        errors.append("seo: home surface carries no JSON-LD")
    defined = set()
    for block in blocks:
        try:
            data = json.loads(block)
        except json.JSONDecodeError as exc:
            errors.append(f"seo: invalid JSON-LD on home surface ({exc})")
            continue
        collect_defined_terms(data, defined)
    for t in terms:
        if t.get("in_jsonld") and t["term"] not in defined:
            errors.append(f"seo: lexicon term '{t['term']}' marked in_jsonld but absent from DefinedTermSet")

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
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("seo: OK" if not errs else f"seo: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
