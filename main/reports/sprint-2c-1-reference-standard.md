# Sprint 2C-1 Report — Reference Standard Pages

**Date:** 2026-06-10
**Decision:** DEC-013 — Outmerchant moved from diagnostic product to reference standard surface
**Gate result:** 🟢 GREEN — all 6 validators pass

---

## Files Created

| File | Role |
|------|------|
| `dimensions/platform-dependency/index.html` | Dimension 01 / DEP reference page |
| `dimensions/customer-ownership/index.html` | Dimension 02 / OWN reference page |
| `dimensions/reputation-portability/index.html` | Dimension 03 / REP reference page |
| `dimensions/payment-settlement-exposure/index.html` | Dimension 04 / PAY reference page |
| `dimensions/fee-margin-leakage/index.html` | Dimension 05 / FEE reference page |
| `dimensions/cross-border-trust/index.html` | Dimension 06 / XBR reference page |
| `dimensions/ai-commerce-readiness/index.html` | Dimension 07 / AGT reference page |
| `dimensions/governance-independence/index.html` | Dimension 08 / GOV reference page |
| `levels/captured/index.html` | Tier 1 definition (0–25) |
| `levels/dependent/index.html` | Tier 2 definition (26–50) |
| `levels/emerging/index.html` | Tier 3 definition (51–75) |
| `levels/outmerchant/index.html` | Tier 4 definition (76–100) — protected rank |
| `main/scripts/build_reference_pages.py` | Governed page builder — pages generated from the model files, never hand-edited |
| `main/scripts/validate_reference.py` | Sixth gate validator — reference-standard integrity |
| `main/reports/sprint-2c-1-reference-standard.md` | This report |

## Files Modified

| File | Change |
|------|--------|
| `main/data/pages.json` | 12 routes `planned → active`; topology extended (score→4 levels, dimension→relevant level) |
| `main/data/internal_links.json` | +11 required edges (88 → 99) |
| `sitemap.xml` | Regenerated from active routes only: 14 URLs |
| `score/index.html` | Reference-standard link grid added (8 dimensions + 4 levels, crawlable static links); robots meta added |
| `index.html` | Robots meta added; homepage still links only to /score/ per sprint requirement |
| `main/scripts/validate_seo.py` | New checks: robots meta, exactly one H1, thin-content floor (200 words), sitemap may contain active routes only |
| `main/scripts/validate_links.py` | New checks: rendered links on active pages must target active routes (no live 404s); inbound/outbound coverage for every active route |
| `main/scripts/quality_gate.py` | Registered `validate_reference.py` |
| `DECISION_LOG.md` | DEC-013 |

## Routes Activated (12)

`/dimensions/platform-dependency/`, `/dimensions/customer-ownership/`, `/dimensions/reputation-portability/`, `/dimensions/payment-settlement-exposure/`, `/dimensions/fee-margin-leakage/`, `/dimensions/cross-border-trust/`, `/dimensions/ai-commerce-readiness/`, `/dimensions/governance-independence/`, `/levels/captured/`, `/levels/dependent/`, `/levels/emerging/`, `/levels/outmerchant/`

Active routes total: **14** (home, /score/, 12 reference pages). Planned (not in sitemap, not linked live): /protocol/, /lexicon/ and 13 lexicon term routes.

## Internal Link Changes

- `/score/` → all 8 dimension pages + all 4 level pages (rendered grid + registry edges)
- Every dimension page → `/score/`, its characteristic tier, `/levels/outmerchant/`, home
- Every level page → `/score/`, `/levels/outmerchant/`, home
- Homepage → `/score/` only (navigation deliberately not expanded)
- Registry graph: 99 required edges; rendered graph verified — every active route has inbound and outbound links; zero links to non-active routes

## SEO / Indexation Checks

Every active page verified to carry: canonical URL, unique title, unique meta description, `robots: index, follow`, exactly one H1, Open Graph + Twitter metadata, valid JSON-LD (Article + BreadcrumbList on reference pages), sitemap entry. Visible-text word counts (thin-content floor is 200): dimensions 390–456 words; levels 271–409 words. Sitemap contains exactly the 14 active routes — no planned route appears.

## Quality Gate Result

```
[PASS] score model (SCORE_GOVERNANCE.md)
[PASS] lexicon (LEXICON_GOVERNANCE.md)
[PASS] routes (ROUTE_GOVERNANCE.md)
[PASS] internal links (ROUTE_GOVERNANCE.md)
[PASS] seo / ai-readability (AI_READABILITY_POLICY.md)
[PASS] reference standard (DEC-013)
GATE GREEN
```

Protected-rank integrity confirmed: tier names/boundaries unchanged; `/levels/outmerchant/` defines Outmerchant as the protected highest sovereignty rank citing DEC-001/DEC-006; the gate rejects any drift.

Sprint constraints honored: no monetization, no email capture, no marketplace claim, no buyer outreach, no crypto-hype register.

## Known Limitations

1. **Lexicon term pages are not yet built** — 13 lexicon routes remain planned; lexicon terms are currently defined only on the homepage section and in structured data.
2. **/protocol/ is not yet built** — dimension pages intentionally do not render protocol links yet (registry edge exists for Phase 4).
3. **`lastmod` dates are static** — sitemap regeneration sets a fixed date; should derive from git history in a future sprint.
4. **No Search Console verification yet** — indexation cannot be confirmed until the owner verifies the property and submits the sitemap (manual step, owner-only).
5. **Reference pages share one characteristic-tier mapping per dimension** — editorial choice, recorded in the builder; revisit if data from real score runs suggests different tier correlations.

## Next Sprint Recommendation

**Sprint 2C-2 — Lexicon Pages:** build the 13 planned `/lexicon/` term pages plus the `/lexicon/` index from `glossary_terms.json` via the same governed-builder pattern (per-term DefinedTerm JSON-LD per `AI_READABILITY_POLICY.md`), then `/protocol/`. After that, Phase 6: owner verifies Google Search Console and submits the sitemap — the first external indexation milestone.

---

*Report maintained under the Outmerchant Governance Operating System.*
