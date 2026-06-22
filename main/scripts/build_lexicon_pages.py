"""Governed builder for lexicon term pages (Sprint 2C-2, DEC-014).

Generates one HTML page per term from glossary_terms.json.
Pages are regenerated, never hand-edited: run
`python3 main/scripts/build_lexicon_pages.py` after any governed
glossary change, then run the quality gate.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"
ORIGIN = "https://outmerchant.com"

glossary = json.loads((DATA / "glossary_terms.json").read_text())["terms"]
TERM_BY_SLUG = {t["slug"]: t for t in glossary}


# ---------------------------------------------------------------- helpers
def nav_html(active: str = "") -> str:
    links = [
        ("/", "Home"),
        ("/score/", "Score"),
        ("/reference/", "Reference"),
        ("/lexicon/", "Lexicon"),
    ]
    items = []
    for href, label in links:
        cls = ' class="active"' if label == active else ""
        items.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    return "<ul>" + "".join(items) + "</ul>"


def footer_html() -> str:
    return (
        '<footer>'
        '<p>© 2025 OutMerchant. Built for merchants who intend to remain independent.</p>'
        '</footer>'
    )


def related_terms_html(slugs: list) -> str:
    if not slugs:
        return ""
    items = []
    for slug in slugs:
        t = TERM_BY_SLUG.get(slug)
        if t:
            items.append(f'<li><a href="/lexicon/{slug}/">{t["term"]}</a></li>')
    if not items:
        return ""
    return "<h2>Related terms</h2><ul class=\"related-terms\">" + "".join(items) + "</ul>"


def term_page(t: dict) -> str:
    slug = t["slug"]
    term = t["term"]
    short_def = t.get("short_definition", "")
    long_def = t.get("long_definition", "")
    usage = t.get("usage_note", "")
    related = t.get("related_terms", [])
    related_html = related_terms_html(related)
    canonical = f"{ORIGIN}/lexicon/{slug}/"
    description = short_def[:155] if short_def else long_def[:155]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{term} — OutMerchant Lexicon</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<header>
<a href="/" class="logo">OutMerchant</a>
<nav>{nav_html('Lexicon')}</nav>
</header>
<main>
<article class="lexicon-entry">
<h1>{term}</h1>
<p class="short-def"><strong>{short_def}</strong></p>
<section>
<h2>Full definition</h2>
<p>{long_def}</p>
</section>
{'<section><h2>Usage note</h2><p>' + usage + '</p></section>' if usage else ''}
{related_html}
</article>
</main>
{footer_html()}
</body>
</html>"""


def lexicon_index(terms: list) -> str:
    items = []
    for t in sorted(terms, key=lambda x: x["term"].lower()):
        slug = t["slug"]
        term = t["term"]
        short_def = t.get("short_definition", "")
        items.append(
            f'<li><a href="/lexicon/{slug}/"><strong>{term}</strong></a>'
            f' — {short_def}</li>'
        )
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        "<title>Lexicon — OutMerchant</title>\n"
        '<meta name="description" content="Definitions of the terms used in the OutMerchant'
        ' sovereignty scoring system.">\n'
        '<link rel="canonical" href="https://outmerchant.com/lexicon/">\n'
        '<link rel="stylesheet" href="/assets/css/style.css">\n'
        "</head>\n"
        "<body>\n"
        "<header>\n"
        '<a href="/" class="logo">OutMerchant</a>\n'
        f"<nav>{nav_html('Lexicon')}</nav>\n"
        "</header>\n"
        "<main>\n"
        '<article class="lexicon-index">\n'
        "<h1>Lexicon</h1>\n"
        "<p>Definitions of the terms used in the OutMerchant sovereignty scoring system.</p>\n"
        "<ul class=\"term-list\">\n"
        + "\n".join(items)
        + "\n</ul>\n"
        "</article>\n"
        "</main>\n"
        + footer_html()
        + "\n</body>\n</html>"
    )


# ---------------------------------------------------------------- write
OUT = ROOT / "lexicon"

for t in glossary:
    slug = t["slug"]
    dest = OUT / slug / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(term_page(t), encoding="utf-8")
    print(f"  wrote {dest.relative_to(ROOT)}")

idx_dest = OUT / "index.html"
idx_dest.write_text(lexicon_index(glossary), encoding="utf-8")
print(f"  wrote {idx_dest.relative_to(ROOT)}")

print("build_lexicon_pages: done")
