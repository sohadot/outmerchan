# Sprint 3A Report — Authority Hardening & Score Engine Reinforcement

**Date:** 2026-06-10
**Branch:** `claude/outmerchant-strategic-asset-8hpaql`
**Commit:** `9f3c0ef` — *Sprint 3A — Harden category gravity and score engine*
**Decision:** DEC-015 — Category Gravity Before Value Extraction
**Gate result:** 🟢 GREEN — all **8** validators pass

---

## System State

| Metric | Value |
|--------|-------|
| Validators in the quality gate | **8** |
| Active public routes | **29** |
| Required internal link edges | **114** |
| Sitemap URLs | 29 (active public pages only) |
| Engine version | 1.1.0 (model version 1.0.0) |

## Files Created

| File | Role |
|------|------|
| `CATEGORY_GRAVITY.md` | Constitutional doctrine: category gravity before value extraction; the six laws; gravity metrics; governing sentence |
| `main/reports/phase-6a-indexation-intelligence.md` | Indexation intelligence log — GSC/Bing verification, sitemap status, per-URL indexation, first signals; all fields honestly `pending` |
| `main/data/engine_guidance.json` | Governed guidance layer: per-dimension weak interpretation + one controlled next action; per-tier Route-to-Buyer interpretation; boundary statement; engine_version |
| `main/scripts/validate_engine.py` | 8th gate validator — engine governance |
| `main/reports/sprint-3a-authority-hardening-engine.md` | This report |

## Files Modified

| File | Change |
|------|--------|
| `DECISION_LOG.md` | DEC-015 recorded with the required title and text |
| `score/index.html` | Engine reinforcement (details below) |
| `main/data/pages.json` | `/score/` topology synced to curated links (12 edges) |
| `main/data/internal_links.json` | Score edges rewritten; total edges 114 |
| `main/scripts/quality_gate.py` | 8th validator registered |

## Validators Added or Updated

- **Added `validate_engine.py`:** guidance file exists/parses; every active dimension has non-empty guidance; no unknown guidance codes; route_to_buyer covers all four tiers; boundary statement and engine_version present; `/score/` carries the Engine Boundary section; no default-0 result; neutral pre-completion state present; no email capture; no payment language; no marketplace claims; no external JS dependency; all 12 export schema fields present; guidance read from governed data.
- **Negative test verified:** injecting a default-0 result and an email input produced exactly 2 failures; gate returned green after restore.

## Engine Improvements

1. **Result explainability:** total score; sovereignty level with range; level explanation pulled from `score_levels.json`; full 8-dimension breakdown; three weakest dimensions, each with governed interpretation and one controlled next action from `engine_guidance.json`; Route-to-Buyer Control interpretation per tier; visible boundary statement under every result.
2. **No false default:** result placeholder is `—`, neutral state line "Result appears after completing the diagnostic." shown until completion.
3. **Governed guidance layer:** all interpretive copy lives in `engine_guidance.json`; the page fetches it alongside the model — zero interpretive prose hardcoded in JavaScript.
4. **Machine-readable export upgraded** to: `engine_version`, `generated_at`, `total_score`, `level_id`, `level_name`, `level_range`, `dimension_scores`, `weakest_dimensions`, `canonical_terms_used`, `protocol_url`, `score_url`, `boundary_statement`.
5. **Engine Boundary section (visible):** measures Merchant Sovereignty posture; does not predict revenue; does not certify; does not create a marketplace listing; does not store answers; does not transmit answers.
6. **Curated internal links only:** 8 dimension pages, `/protocol/`, `/lexicon/merchant-sovereignty/`, `/lexicon/outmerchant/`, `/levels/outmerchant/`. Links to the lexicon index, other terms, and the three lower tier pages were removed from `/score/` (those remain reachable through dimension pages and the lexicon index; inbound/outbound coverage re-verified by the gate).

## Search Console / Webmaster Tools Status (user-provided)

No verification data has been provided by the owner yet. All fields in `phase-6a-indexation-intelligence.md` are `pending`. No data was invented.

## Constraints Respected

No monetization · no buyer outreach · no public sale posture · no marketplace claim · no email capture · no analytics dependency · no external JavaScript · no new network calls (the guidance fetch is the same same-origin governed-data pattern as the model files) · no crypto-hype language · no mass page expansion (zero new public routes) · no live links to inactive routes · no score ontology outside governed model files · `/score/` remains indexable and privacy-preserving.

## Known Next Step

**Owner-gated:** verify outmerchant.com in Google Search Console (and optionally Bing Webmaster Tools), submit `sitemap.xml`, request indexing for `/`, `/score/`, `/levels/outmerchant/`, `/lexicon/merchant-sovereignty/`, `/protocol/` — then record real dates and statuses in `phase-6a-indexation-intelligence.md`. After first impressions data arrives: Sprint 3B (indexation intelligence review + Phase 5 AI commerce doctrine layer).

---

*Report maintained under the OutMerchant Governance Operating System.*
