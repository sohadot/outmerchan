# Phase 6A — Indexation Intelligence Log

> External visibility is observed, never invented. Every field below is filled only with data the owner provides or that tooling verifiably reports. `pending` means no data yet.

**Governed by:** `CATEGORY_GRAVITY.md` · **Asset:** outmerchant.com · **Active public routes:** 29
**Last updated:** 2026-06-10 (owner-provided screenshots: GSC, Bing WMT ×2, Cloudflare)

---

## Verification Status

| Item | Status | Date |
|------|--------|------|
| Google Search Console property verification | ✅ verified (evidenced by accepted sitemap submission) | 2026-06-10 |
| Verification method (DNS TXT / HTML file) | pending confirmation from owner (domain is on Cloudflare DNS) | — |
| Bing Webmaster Tools verification | ✅ verified (evidenced by accepted sitemap + URL submission) | 2026-06-10 |
| Sitemap submitted to Google | ✅ submitted | 2026-06-10 |
| Sitemap submitted to Bing | ✅ submitted | 2026-06-10 |
| Sitemap status — Google | ✅ **Success** ("Opération effectuée") · last read 2026-06-10 · **29 pages discovered** | 2026-06-10 |
| Sitemap status — Bing | ⏳ Processing · 0 URLs discovered yet · 0 errors · 0 warnings | 2026-06-10 |
| Bing manual URL submission | ✅ batch submitted at 12:51 (priority URLs) | 2026-06-10 |

### Verified Observation — Sitemap Parity

Google read **29 URLs** from the sitemap — exact parity with the 29 active routes in `pages.json`. The external crawler sees precisely the surface the registry governs: first external confirmation that the governed registry and the public surface do not diverge.

> Note: *discovered* is not *indexed*. Discovery confirms the sitemap pipeline; indexation is the next signal to watch in the Pages report.

## Infrastructure Observation — Cloudflare Edge Layer

As of 2026-06-10 outmerchant.com is proxied through Cloudflare (free plan; CDN/caching, SSL/TLS, DDoS mitigation active). Per the Sovereign Asset System Cloudflare governance: GitHub remains the source of truth; Cloudflare is an edge-governance layer only and must not create hidden redirects, unmanaged edge logic, or undocumented state.

**Edge check items (owner/next session):**
- [ ] SSL/TLS mode is "Full (strict)" (avoid redirect loops / mixed canonical signals)
- [ ] "Always Use HTTPS" on; no Page Rules rewriting or redirecting governed routes
- [ ] No edge caching of stale `sitemap.xml` / `robots.txt` after deploys (purge on release if needed)
- [ ] Rocket Loader / auto-minify off for the score engine page (script integrity)

## Manually Inspected URLs

Priority inspection order (request indexing in this order in GSC URL Inspection):

| URL | Inspected | Indexation status | Canonical status |
|-----|-----------|-------------------|------------------|
| `/` | pending | pending | pending |
| `/score/` | pending | pending | pending |
| `/levels/outmerchant/` | pending | pending | pending |
| `/lexicon/merchant-sovereignty/` | pending | pending | pending |
| `/protocol/` | pending | pending | pending |
| `/lexicon/outmerchant/` | pending | pending | pending |
| `/dimensions/platform-dependency/` | pending | pending | pending |

(Bing: a manual URL batch was submitted 2026-06-10 12:51; per-URL status pending.)

## Indexation Status by URL (full surface)

| Segment | Routes | Discovered (Google) | Indexed | Crawled not indexed | Discovered not indexed |
|---------|--------|--------------------|---------|--------------------|------------------------|
| Home | 1 | ✅ (in 29) | pending | pending | pending |
| Score | 1 | ✅ (in 29) | pending | pending | pending |
| Protocol | 1 | ✅ (in 29) | pending | pending | pending |
| Lexicon (index + 13 terms) | 14 | ✅ (in 29) | pending | pending | pending |
| Dimensions | 8 | ✅ (in 29) | pending | pending | pending |
| Levels | 4 | ✅ (in 29) | pending | pending | pending |

## First Signals

| Signal | Value | Date observed |
|--------|-------|---------------|
| First impressions (Google) | pending | pending |
| First queries (Google) | pending | pending |
| First click | pending | pending |
| First tier-name query (captured/dependent/emerging/outmerchant merchant) | pending | pending |
| First lexicon-term query | pending | pending |

## Issues Observed

| Class | Observation | Status |
|-------|------------|--------|
| Crawled — currently not indexed | none observed yet | — |
| Discovered — currently not indexed | none observed yet | — |
| Robots / noindex conflicts | none observed (sitemap read Success, 0 errors) | — |
| Canonical conflicts (Google chose different canonical) | pending | — |
| Soft 404 / quality signals | pending | — |

## Next Corrective Decision

No corrective action required — the pipeline is healthy (Google: Success, 29/29; Bing: Processing is normal for a first submission). **Next review:** check the GSC Pages (indexing) report and Bing sitemap status in 7–14 days; record indexed counts and any "crawled/discovered — not indexed" entries above; run URL Inspection on the 7 priority URLs and record canonical status. Corrective actions that change routes, canonicals, or robots policy require a `DECISION_LOG.md` entry per `ROUTE_GOVERNANCE.md`.

---

## Update Protocol

1. Owner verifies property / submits sitemap → record dates above. ✅ done 2026-06-10
2. Weekly during Phase 6A: update inspection and signal tables from Search Console data only.
3. Never record estimated or assumed values. `pending` is an honest state; an invented number is a governance violation (`CLAIM_POLICY.md`).

---

*Maintained under the Outmerchant Governance Operating System.*
