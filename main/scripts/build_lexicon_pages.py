"""Governed builder for lexicon term pages (Sprint 3C, DEC-020).

Generates one HTML page per term from the governed glossary_terms.json.
Pages are regenerated, never hand-edited.
Run: python3 main/scripts/build_lexicon_pages.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"
ORIGIN = "https://outmerchant.com"

glossary = json.loads((DATA / "glossary_terms.json").read_text())["terms"]
TERM_BY_SLUG = {t["slug"]: t for t in glossary}


# ---------------------------------------------------------------- helpers
def _canonical(path: str) -> str:
    return f'<link rel="canonical" href="{ORIGIN}{path}">'


def _head(title: str, description: str, path: str, extra: str = "") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{_canonical(path)}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{ORIGIN}{path}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="/assets/css/main.css">
{extra}
</head>"""


def _foot() -> str:
    return """<footer class="site-footer">
<div class="footer-inner">
<p class="footer-copy">&copy; 2025 Outmerchant. Built for independent commerce.</p>
</div>
</footer>
</body></html>"""


def _nav(active: str = "") -> str:
    links = [
        ("/", "Home"),
        ("/score/", "Score"),
        ("/lexicon/", "Lexicon"),
        ("/about/", "About"),
    ]
    items = []
    for href, label in links:
        cls = ' class="active"' if label.lower() == active.lower() else ""
        items.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    return '<nav class="site-nav"><ul>' + "".join(items) + "</ul></nav>"


def _breadcrumb(*crumbs) -> str:
    parts = []
    for label, href in crumbs:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return '<nav class="breadcrumb">' + ' › '.join(parts) + '</nav>'


def _related_links(slugs: list) -> str:
    if not slugs:
        return ""
    items = []
    for s in slugs:
        term = TERM_BY_SLUG.get(s)
        label = term["term"] if term else s
        items.append(f'<li><a href="/lexicon/{s}/">{label}</a></li>')
    return "<ul class=\"related-terms\">" + "".join(items) + "</ul>"


# ---------------------------------------------------------------- builder
def _build_term_page(term: dict) -> None:
    slug = term["slug"]
    label = term["term"]
    definition = term["definition"]
    path = f"/lexicon/{slug}/"
    context_note = term.get("context_note", "")
    related = term.get("related_terms", [])
    see_also = term.get("see_also", [])
    usage_note = term.get("usage_note", "")
    sources = term.get("sources", [])
    category = term.get("category", "")

    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": label,
        "description": definition,
        "inDefinedTermSet": {
            "@type": "DefinedTermSet",
            "name": "Outmerchant Lexicon",
            "url": f"{ORIGIN}/lexicon/"
        }
    }, indent=2)

    related_html = _related_links(related + see_also)

    page = f"""{_head(
        title=f"{label} | Outmerchant Lexicon",
        description=definition[:155],
        path=path,
        extra=f'<script type="application/ld+json">{jsonld}</script>'
    )}
<body>
{_nav('lexicon')}
<main class="page-content">
{_breadcrumb(('Home', '/'), ('Lexicon', '/lexicon/'), (label, None))}
<article class="lexicon-term-page" itemscope itemtype="https://schema.org/DefinedTerm">
  <header class="term-header">
    <h1 itemprop="name">{label}</h1>
    {f'<span class="term-category">{category}</span>' if category else ''}
  </header>

  <section class="term-section" id="definition">
    <h2>Definition</h2>
    <p itemprop="description">{definition}</p>
  </section>

  {f'<section class="term-section" id="context"><h2>Context</h2><p>{context_note}</p></section>' if context_note else ''}

  {f'<section class="term-section" id="usage"><h2>Usage note</h2><p>{usage_note}</p></section>' if usage_note else ''}

  {f'<section class="term-section" id="related"><h2>Related terms</h2>{related_html}</section>' if related_html else ''}

  {f'<section class="term-section" id="sources"><h2>Sources</h2><ul>' + ''.join(f'<li>{s}</li>' for s in sources) + '</ul></section>' if sources else ''}
</article>
</main>
{_foot()}"""

    out = ROOT / path.lstrip("/")
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page)
    print(f"  wrote {path}")


# ---------------------------------------------------------------- main
if __name__ == "__main__":
    print("Building lexicon pages …")
    for term in glossary:
        _build_term_page(term)
    print(f"Done. {len(glossary)} pages written.")
