# Quality Gate

> The execution court. The repository itself must prevent drift — not by intention, but by automated enforcement on every push.
>
> **Every layer serves the merchant. No layer owns the merchant.**

## Principle

Governance documents declare the law; the quality gate enforces it. A rule that exists only as prose is a wish. Every law that can be checked mechanically must be checked mechanically.

## How to Run

```
python3 main/scripts/quality_gate.py
```

Runs all validators and exits non-zero on any failure. The same command runs in CI on every push and pull request (`.github/workflows/quality-gate.yml`). A red gate blocks merge.

## Validators

| Script | Enforces | Source law |
|--------|----------|-----------|
| `validate_score_model.py` | 8 dimensions, codes fixed, weights sum to 100, 20 questions all mapped, 4 tiers contiguous 0–100, terminal tier named "OutMerchant" | `SCORE_GOVERNANCE.md` |
| `validate_glossary.py` | Every term has definition, system function, relations (resolvable), route (registered), score relation; canonical casing of the verb/rank pair | `LEXICON_GOVERNANCE.md` |
| `validate_routes.py` | Schema completeness, no duplicate routes, active routes have files, no orphan active routes, required links point to registered routes, owners valid | `ROUTE_GOVERNANCE.md` |
| `validate_links.py` | Internal link graph consistency: every edge connects registered routes, anchor links on the live surface resolve | `ROUTE_GOVERNANCE.md` |
| `validate_seo.py` | Canonical URL, title, meta description present; JSON-LD parses; DefinedTermSet covers all `in_jsonld` lexicon terms; sitemap covers active routes | `AI_READABILITY_POLICY.md` |

## Checks Enforced

- No broken internal links
- No missing canonical
- No missing title / meta description
- No orphan pages
- No duplicate routes
- No missing sitemap entry for an active route
- No invalid score dimension, weight drift, or unmapped question
- No undefined or malformed lexicon term
- No active route without a file
- Terminal tier name integrity ("OutMerchant" at 76–100)

## Checks Enforced by Review (not yet mechanical)

- No empty or thin content pages (mechanical check arrives with Sprint 2B content routes)
- No external JS dependency without approval
- No monetization surface before the allowed phase (DEC-005)
- Claim policy compliance (`CLAIM_POLICY.md`)

Each of these graduates to a mechanical check as soon as the corresponding surface exists.

## Failure Handling

A failing gate is never overridden by urgency. Either the change is fixed to comply, or the law itself is changed — explicitly, in the governing document, with a `DECISION_LOG.md` entry. There is no third path. Silent exceptions are how governed systems decay into ordinary websites.

---

*Governed under the OutMerchant Governance Operating System.*
