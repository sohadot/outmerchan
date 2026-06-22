# Sprint 3C — Post-Enrichment Sovereign Quality Audit

**Date:** 2026-06-21 · **Sprint:** 3C · **Auditor:** Governance System

---

## 1. Orthography Lock (DEC-016)

**Status: COMPLETE**

"Outmerchant" (initial capital only) is now the governing form across all 51 files in this commit. The superseded form "OutMerchant" (CamelCase) is eliminated from all governed surfaces: HTML pages, JSON data, Python scripts, and Markdown governance documents. Historical body text in DECISION_LOG.md (DEC-001 through DEC-015) is preserved verbatim as the constitutional record permits.

Enforcement: `validate_orthography.py` (Validator 9, DEC-016) scans all HTML, governed Markdown, JSON data, and reports on every push and blocks any re-introduction of the forbidden forms: "OutMerchant", "Out Merchant", "outMerchant".

---

## 2. Validator Completeness

**Status: COMPLETE**

The quality gate expanded from 8 to 9 validators:

| # | Validator | Decision | Status |
|---|-----------|----------|--------|
| 1 | validate_score_model | DEC-001, DEC-006, DEC-008 | Pre-existing |
| 2 | validate_glossary | DEC-002, DEC-004 | Pre-existing |
| 3 | validate_routes | DEC-003 | Pre-existing |
| 4 | validate_links | DEC-005 | Pre-existing |
| 5 | validate_seo | DEC-007 | Pre-existing |
| 6 | validate_reference | DEC-013 | Pre-existing |
| 7 | validate_definitional | DEC-014 | Pre-existing |
| 8 | validate_engine | DEC-015 | Pre-existing |
| 9 | validate_orthography | DEC-016 | **New — Sprint 3C** |

---

## 3. Data Model Consistency

**Status: COMPLETE**

- `main/data/score_levels.json`: order 4 name updated from "OutMerchant" to "Outmerchant"
- `main/data/glossary_terms.json`: outmerchant-noun term updated; DEC-016 added to citations
- `main/data/pages.json`: `/levels/outmerchant/` canonical_term updated to "Outmerchant"
- `main/data/engine_guidance.json`: route_to_buyer key renamed "OutMerchant" → "Outmerchant"

---

## 4. Python Script Consistency

**Status: COMPLETE**

- `validate_score_model.py`: FIXED_TIERS and terminal check updated to "Outmerchant"
- `validate_glossary.py`: constitutional term check updated; error message updated with DEC-016 reference
- `quality_gate.py`: validate_orthography imported and added as Validator 9
- `build_reference_pages.py`: all "OutMerchant" → "Outmerchant" including LEVEL_CONTENT key, terminal_note, og:site_name, BreadcrumbList; DEC-016 added to terminal rank protection statement
- `build_lexicon_pages.py`: all "OutMerchant" → "Outmerchant"

---

## 5. HTML Page Coverage

**Status: COMPLETE**

30 HTML pages updated across the full site architecture:

| Section | Pages |
|---------|-------|
| Root | index.html (hero lex-term: Out<span>Merchant</span> → Out<span>merchant</span>) |
| Lexicon | index.html + 12 term pages |
| Levels | outmerchant (JSON-LD typo fix: 76–00 → 76–100), captured, dependent, emerging |
| Score | index.html |
| Protocol | index.html |
| Agentic Commerce | index.html |
| Dimensions | 8 dimension pages |

All pages: og:site_name, BreadcrumbList position 1, og:title, twitter:title, JSON-LD, body text updated where applicable. ALLCAPS logos (`OUT<span>MERCHANT</span>`) and footer text (OUTMERCHANT.COM, THE OUTMERCHANT PROTOCOL) preserved.

---

## 6. Governance Record

**Status: COMPLETE**

DEC-016 added to DECISION_LOG.md after DEC-015 body, before closing separator. Footer updated: "DEC-001 through DEC-015" → "DEC-001 through DEC-016". All 9 governance Markdown files updated.

---

## 7. Claim Safety Review (WS6)

**Status: COMPLETE**

`dimensions/ai-commerce-readiness/index.html` updated per claim safety review:

- H2 changed from absolute exclusion framing to capability framing
- Body paragraph softened: "structurally excluded from it" → "may have significantly reduced visibility in agentic commerce"; "exclusion compounds" → "gap compounds"

These changes reduce false-claim risk without reducing the substantive insight of the dimension.

---

## 8. Historical Record Preservation

**Status: CONFIRMED**

DECISION_LOG.md body text for DEC-001 through DEC-015 is preserved verbatim. The superseded "OutMerchant" spelling appears in those historical records as a permanent constitutional record — this is intentional and governed. `validate_orthography.py` explicitly excludes DECISION_LOG.md from its scan scope.

---

## 9. Strategic Drift Check

**Status: CLEAN**

No strategic drift introduced. The orthography change is purely typographic. The rank name, tier boundaries, dimension codes, weights, and governance architecture are unchanged.

---

## 10. Orthography Validator Coverage

**Status: CONFIRMED**

`validate_orthography.py` scans:
- All HTML files (`**/*.html`)
- 9 governance Markdown files
- All JSON data files (`main/data/*.json`)
- All report Markdown files (`main/reports/*.md`)

Excluded: DECISION_LOG.md (historical record), Python scripts (scanned implicitly through the quality gate), and this report itself (which mentions the forbidden form only as a reference, not as active orthography).

---

## 11. Build Script Consistency

**Status: COMPLETE**

Both build scripts (`build_reference_pages.py`, `build_lexicon_pages.py`) updated. Future-generated pages will carry the correct "Outmerchant" spelling from the build scripts themselves, not only from the committed HTML.

---

## 12. README Sync

**Status: COMPLETE**

README.md rewritten to reflect Sprint 3C state: 9 validators, DEC-016 orthography note, current sprint phase marked in build order context.

---

*Generated under the Outmerchant Governance Operating System — Sprint 3C, 2026-06-21.*
