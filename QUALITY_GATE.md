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

| # | Validator | Decision | What It Checks |
|---|-----------|----------|-----------------|
| 1 | validate_score_model | DEC-001, DEC-006, DEC-008 | Score model integrity, tier boundaries, terminal tier |
| 2 | validate_glossary | DEC-002, DEC-004 | Glossary term completeness and constitutional term presence |
| 3 | validate_routes | DEC-003 | Route completeness and route-to-dimension mapping |
| 4 | validate_links | DEC-005 | Internal link integrity across all HTML pages |
| 5 | validate_seo | DEC-007 | SEO metadata completeness on all HTML pages |
| 6 | validate_reference | DEC-013 | Reference page generation from governed model |
| 7 | validate_definitional | DEC-014 | Definitional page structure and content governance |
| 8 | validate_engine | DEC-015 | Engine guidance file integrity |
| 9 | validate_orthography | DEC-016 | Orthography governance — "Outmerchant" is the official form |

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
- Terminal tier name integrity ("Outmerchant" at 76–100)

## Checks Enforced by Review (not yet mechanical)

- No empty or thin content pages (mechanical check arrives with Sprint 2B content routes)
- No external JS dependency without approval
- No monetization surface before the allowed phase (DEC-005)
- Claim policy compliance (`CLAIM_POLICY.md`)

Each of these graduates to a mechanical check as soon as the corresponding surface exists.

## Failure Handling

A failing gate is never overridden by urgency. Either the change is fixed to comply, or the law itself is changed — explicitly, in the governing document, with a `DECISION_LOG.md` entry. There is no third path. Silent exceptions are how governed systems decay into ordinary websites.

---

*Governed under the Outmerchant Governance Operating System.*
