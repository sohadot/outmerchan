# AI Readability Policy

> OutMerchant must be legible to humans and machines simultaneously. AI agents are becoming buyers, evaluators, and routers of commerce; the asset that defines machine-readable trust must itself be exemplary at it.
>
> **The future merchant must be legible, trustworthy, and selectable by AI without surrendering sovereignty to AI-controlled market access.**

## Position

AI is treated as the future control layer of commerce (DEC-003): a control layer in discovery, comparison, trust, and purchase routing. OutMerchant is therefore built AI-native, not AI-decorated. This is not a feature — it is dimension 07 (AI Commerce Readiness) of the asset's own standard, applied to itself.

## Requirements — Current (Phase 1, enforced now)

1. **JSON-LD on the live surface.** `index.html` must carry valid JSON-LD including `WebSite`, `Organization`, and a `DefinedTermSet` exposing the canonical lexicon to machines.
2. **DefinedTerm coverage.** Every founding lexicon term marked `"in_jsonld": true` in `glossary_terms.json` must appear as a `DefinedTerm` in the structured data. The lexicon a machine reads and the lexicon a human reads must be the same lexicon.
3. **Canonical and metadata discipline.** Every active route: canonical URL, title, meta description. No exceptions.
4. **Indexability.** `robots.txt` and `sitemap.xml` present and consistent with active routes in `pages.json`.
5. **Semantic HTML.** Headings express document structure; definitional content is text, not images; no meaning carried only by visual styling.

## Requirements — Planned (Phase 2+, gated)

1. **Structured score results.** When `/score/` ships, results must be expressible in a structured, machine-readable form (JSON output contract matching `SCORE_GOVERNANCE.md`'s scoring contract).
2. **Per-term DefinedTerm pages.** Each lexicon route carries its own `DefinedTerm` JSON-LD referencing the canonical `DefinedTermSet`.
3. **Agentic commerce standard.** A formal `AGENTIC_COMMERCE_STANDARD.md` defining AI-readable merchant identity and machine-readable trust — what an AI buying agent must be able to verify about a merchant. This document inherits its claims discipline from `CLAIM_POLICY.md`.

## Sovereignty Boundary

Machine legibility must never become machine dependency. The policy's own doctrine sentence draws the line: merchants (and this asset) become *selectable by* AI without becoming *owned by* AI-controlled market access. Concretely:

- No structured data that hands exclusive interpretation rights to any single AI platform
- No participation in closed agentic ecosystems that would contradict the anti-single-point-of-control doctrine
- Open standards (schema.org, open JSON contracts) over proprietary feeds wherever a choice exists

## Prohibited

- Decorative or invalid JSON-LD (structured data that does not parse fails the build)
- Schema markup claiming entities or facts the page does not contain
- Machine-readable claims that violate `CLAIM_POLICY.md`

---

*Governed under the OutMerchant Governance Operating System. Enforced by `main/scripts/validate_seo.py`.*
