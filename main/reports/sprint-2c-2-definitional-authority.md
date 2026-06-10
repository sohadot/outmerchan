# Sprint 2C-2 Report — Canonical Lexicon + Protocol (Definitional Authority)

**Date:** 2026-06-10
**Decision:** DEC-014 — OutMerchant moved from standard surface to definitional authority
**Gate result:** 🟢 GREEN — all 7 validators pass

---

## Goal Achieved

The deeper objective set for this sprint: lexicon pages are canonical definitions (published verbatim from the governed record, enforced mechanically), and `/protocol/` explains why the definitions, the instrument, and the ranks are one system, not separate parts.

## Files Created

| File | Role |
|------|------|
| `lexicon/index.html` | The canonical DefinedTermSet surface — full lexicon, 15 terms in JSON-LD |
| `lexicon/outmerchant/index.html` | The headword: verb + rank as two senses of one entry, with the referential closure |
| `lexicon/<12 term dirs>/index.html` | Canonical term pages: governed definition verbatim, "In the Standard", usage, related terms, DefinedTerm JSON-LD |
| `protocol/index.html` | The binding page: Named / Measured / Explained / Protected — standards register |
| `main/scripts/build_lexicon_pages.py` | Governed lexicon builder — pages regenerated from glossary_terms.json, never hand-edited |
| `main/scripts/validate_definitional.py` | Seventh gate validator — definitional authority integrity |
| `main/reports/sprint-2c-2-definitional-authority.md` | This report |

## Files Modified

| File | Change |
|------|--------|
| `main/data/pages.json` | 15 routes `planned → active` (lexicon index, 13 term pages, protocol); topology extended |
| `main/data/internal_links.json` | +15 required edges (99 → 114) |
| `main/data/glossary_terms.json` | All 15 terms now `in_jsonld: true` (machine-published) |
| `sitemap.xml` | Regenerated: 29 active URLs |
| `main/scripts/build_reference_pages.py` | Dimension pages now link their canonical term + `/protocol/` (bidirectional meaning network) |
| `dimensions/*/index.html` (8) | Regenerated with canonical-term and protocol links |
| `score/index.html` | Canonical definition of "Merchant Sovereignty Score" added verbatim + its DefinedTerm JSON-LD; curated links to 4 key terms + full lexicon + protocol (deliberately not all terms) |
| `index.html` | Lexicon canon box now links to `/lexicon/` (one link added; homepage otherwise unchanged) |
| `main/scripts/validate_seo.py` | DefinedTermSet coverage now validated across home + `/lexicon/` surfaces |
| `main/scripts/quality_gate.py` | Registered seventh validator |
| `DECISION_LOG.md` | DEC-014 |

## Routes Activated (15)

`/lexicon/`, `/lexicon/outmerchant/`, `/lexicon/merchant-sovereignty/`, `/lexicon/route-to-buyer-control/`, `/lexicon/platform-capture/`, `/lexicon/platform-dependency/`, `/lexicon/portable-reputation/`, `/lexicon/ai-merchant-sovereignty/`, `/lexicon/agentic-commerce-readiness/`, `/lexicon/machine-readable-trust/`, `/lexicon/non-aligned-commerce/`, `/lexicon/settlement-exposure/`, `/lexicon/governance-independence/`, `/lexicon/agent-selectable-merchant/`, `/protocol/`

**Active total: 29.** No planned routes remain in the original Phase 4 scope.

## The Meaning Network (now bidirectional)

```
home → score, lexicon (canon box)
score → 8 dimensions, 4 levels, 4 key terms, lexicon, protocol
dimension ⇄ canonical term · dimension → score, tier, protocol
term → its dimension/tier/score, related terms, lexicon, protocol
lexicon index → all 13 term pages, score, protocol
protocol → score, lexicon, dimensions (examples), protected rank
```

Registry: 114 required edges. Rendered graph verified: every active route has inbound and outbound links; zero links to non-active routes.

## SEO / Indexation Checks

All 29 active pages: canonical, unique title/description, robots meta, exactly one H1, OG/Twitter, valid JSON-LD, sitemap entry. Word counts: lexicon terms 248–353, lexicon index 649, protocol 475 (floor is 200). Every term page carries its governed definition **verbatim** — enforced by the gate, so published definitions can never drift from `glossary_terms.json`. All 15 terms machine-published as DefinedTerms with `inDefinedTermSet` references.

## Quality Gate Result

```
[PASS] score model · lexicon · routes · internal links
[PASS] seo / ai-readability · reference standard (DEC-013)
[PASS] definitional authority (DEC-014)   ← new, 7th validator
GATE GREEN
```

During the sprint the new validator caught a real violation before merge: `/score/` (the canonical route of the term "Merchant Sovereignty Score") did not carry the governed definition verbatim. Fixed by adding the canonical definition block and DefinedTerm JSON-LD to the score page.

Constraints honored: no monetization, no buyer/acquisition pages, no marketplace claims, no Web3 expansion, protocol page is normative, not epic.

## Known Limitations

1. **`lastmod` still static** in sitemap (should derive from git history).
2. **Home DefinedTermSet** keeps its original 3-term excerpt; the full set lives on `/lexicon/` (validated as a union — intentional, but the excerpt could later reference the full set explicitly via `subjectOf`).
3. **No external indexation proof yet** — everything above is self-attested until Search Console verification.

## Next Sprint Recommendation

**Phase 6 — Search Console (owner-gated):** the surface is now complete as the user specified — homepage, score, 8 dimensions, 4 levels, lexicon pages, protocol. The owner should: (1) verify outmerchant.com in Google Search Console (DNS TXT via Cloudflare dashboard, or HTML-file method through the repo), (2) submit `sitemap.xml`, (3) request indexing for the five highest-value pages first: `/`, `/score/`, `/levels/outmerchant/`, `/lexicon/merchant-sovereignty/`, `/protocol/`. After first impressions data arrives, Sprint 3 can begin: indexation monitoring report + the AI commerce doctrine layer (Phase 5).

---

*Report maintained under the OutMerchant Governance Operating System.*
