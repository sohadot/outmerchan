# AI Readability Policy

> Outmerchant.com is built to be read by machines, not only by humans. This file governs the minimum AI-readability requirements for every page on the asset.
>
> **Every layer serves the merchant. No layer owns the merchant.**

## Why AI Readability Is a First-Class Concern

The asset's purpose is to be the canonical source for Merchant Sovereignty vocabulary and measurement. Canonical sources must be readable by the systems that route citation and discovery: search engines, AI language models, and AI buying agents. A page that cannot be machine-parsed is invisible to the systems that determine whether the asset is cited, indexed, or trusted.

This is not a technical nicety. It is a core strategic requirement: if Outmerchant.com is to be the source others cite, it must be a source machines can read and evaluate without human intermediation.

## The Minimum Requirements (Every Page)

Every active page on the asset must carry:

1. **Canonical URL** — `<link rel="canonical" href="...">` pointing to the page's own URL, with trailing slash
2. **Title** — `<title>` tag with the page's specific title
3. **Meta description** — `<meta name="description">` with a complete sentence describing the page's content
4. **JSON-LD structured data** — at minimum, an `Article` or `WebPage` type with `@id`, `headline`, `description`, `url`, `isPartOf`, and `publisher`

The quality gate rejects pages missing any of these four elements.

## Lexicon-Specific Requirements

For lexicon term pages:

- `DefinedTerm` type in JSON-LD with `name`, `description`, `url`, and `inDefinedTermSet` pointing to the Outmerchant lexicon
- The DefinedTermSet must be present on `index.html` and enumerated in the sitemap

## Score-Specific Requirements

For the score page and any score result surface:

- `FAQPage` schema for scored questions (when structured as FAQ)
- `BreadcrumbList` with position 1 always pointing to `/` with name "Outmerchant"

## Sitemap Requirements

Every `active` page in the route registry must appear in `sitemap.xml` with:
- `<loc>` matching the canonical URL exactly
- `<changefreq>` and `<priority>` appropriate to the page type

No page that is `planned` or `deprecated` appears in the sitemap.

## robots.txt Requirements

`robots.txt` must:
- Allow all crawlers on all pages (no active page is disallowed)
- Point to the sitemap URL

## Ongoing Enforcement

The quality gate enforces all of the above on every push. A page that passes the gate is AI-readable. A page that fails is blocked until it meets the minimum.

---

*Governed under the Outmerchant Governance Operating System. Enforced by `main/scripts/validate_seo.py`.*
