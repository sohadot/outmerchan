# Route Governance

> Every page on Outmerchant.com must be intentional, registered, and owned. This file governs how pages enter, live in, and leave the canonical route registry.
>
> **Every layer serves the merchant. No layer owns the merchant.**

## The Route Registry

The route registry (`main/data/pages.json`) is the single source of truth for every page that exists, is planned, or has been deprecated on the asset. A page that is not in the registry does not officially exist; a page in the registry that has no corresponding file is a quality failure.

## Governed Artifacts

| File | Role |
|------|------|
| `main/data/pages.json` | Single source of truth for all routes |
| Quality gate | Enforces registry completeness on every push |

## The Route Admission Law

A page enters the registry only when it has:

1. A canonical URL (route)
2. A type (`index`, `lexicon`, `level`, `dimension`, `score`, `protocol`, `editorial`)
3. A status (`active`, `planned`, `deprecated`)
4. An owner (the governance document that governs this page's content)
5. A purpose statement (one sentence: what does this page *do* for the asset?)

The quality gate rejects registry entries missing any of these.

## Route Status Rules

- **`active`** — the page exists and is live. Must have a corresponding HTML file. Quality gate validates.
- **`planned`** — the page is committed to but not yet built. No file required. Planning horizon: current sprint only.
- **`deprecated`** — the page existed and has been retired. Must carry a deprecation date and a redirect destination.

## Change Control

- Adding a route: requires a registry entry and, if active, the file. No page without a registry entry.
- Changing a route URL: requires a registry update, a redirect from the old URL, and a decision log entry if the page is externally linked or indexed.
- Deprecating a route: requires status change to `deprecated`, a deprecation date, and a redirect. Never deleted from the registry.

## Dimension-to-Route Mapping

Every scored dimension has a reference page. The mapping is:

| Code | Route |
|------|-------|
| DEP | `/dimensions/platform-dependency/` |
| OWN | `/dimensions/customer-ownership/` |
| REP | `/dimensions/reputation-portability/` |
| PAY | `/dimensions/payment-settlement-exposure/` |
| FEE | `/dimensions/fee-margin-leakage/` |
| XBR | `/dimensions/cross-border-trust/` |
| AGT | `/dimensions/ai-commerce-readiness/` |
| GOV | `/dimensions/governance-independence/` |

These routes are inviolable while the dimensions they map to are inviolable.

---

*Governed under the Outmerchant Governance Operating System. Enforced by `main/scripts/validate_routes.py`.*
