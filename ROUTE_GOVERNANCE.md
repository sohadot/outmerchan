# Route Governance

> Every page is part of the system or it does not exist. This file governs routes, their lifecycle, and the laws that prevent the site from degrading into a content pile.
>
> **Every layer serves the merchant. No layer owns the merchant.**

## The Route Laws

1. **No page without a function.** Every route must declare a `purpose` that serves the score, the lexicon, the protocol, or buyer logic.
2. **No orphan pages.** Every active route must be reachable from `/` through navigation or required internal links.
3. **No SEO-only pages.** A page whose only justification is search volume is rejected.
4. **No duplicate routes.** One concept, one canonical route.
5. **One governance owner per route.** Every route belongs to exactly one owner: `lexicon`, `score`, `protocol`, `doctrine`, `governance`, or `home`.

## Governed Artifacts

| File | Role |
|------|------|
| `main/data/pages.json` | The route registry — single source of truth for all routes |
| `main/data/navigation.json` | The governed navigation structure |
| `main/data/internal_links.json` | The required internal link graph |

A page that exists on the site but not in `pages.json` is a governance violation. A route in `pages.json` marked `active` whose file does not exist is a build failure.

## Route Record Schema

Every route in `pages.json` must carry:

```json
{
  "route": "/lexicon/platform-dependency/",
  "type": "lexicon | score | dimension | level | protocol | home",
  "status": "active | planned | deprecated",
  "purpose": "Define platform dependency as a merchant sovereignty risk.",
  "canonical_term": "Platform Dependency",
  "required_internal_links": ["/score/", "/lexicon/merchant-sovereignty/"],
  "seo_cluster": "dependency",
  "governance_owner": "lexicon"
}
```

`canonical_term` is required for lexicon, dimension, and level routes; `null` otherwise.

## Route Lifecycle

- **planned** — registered with full purpose and link requirements before any content is written. Sprint 2B builds only from planned routes.
- **active** — content exists, passes the quality gate, is in the sitemap.
- **deprecated** — never deleted from the registry; redirects or successor route must be recorded.

## Current Deployment Constraint

The live site is served by GitHub Pages from the repository root; `index.html` and `CNAME` therefore remain at root and `/` is the only active route until Sprint 2B ships the first content routes. This constraint is recorded here so the registry and the deployment never silently diverge.

## Required Link Topology

The route network must form a meaning system, not a page list:

```
/lexicon/<term>/      → /score/  and at least one related lexicon term
/dimensions/<dim>/    → /score/, its lexicon term, at least one level, /protocol/
/levels/<tier>/       → /score/  and /lexicon/merchant-sovereignty/
/score/               → all eight dimension routes
/protocol/            → /score/ and the doctrine surface
```

The visitor never reads "a page." The visitor enters a system of terms and measurement.

## Change Control

- Adding a route: full schema record in `pages.json`, owner assigned, link requirements declared. No decision log entry needed for routes that follow the topology above.
- Adding a route *type* or changing the topology: requires a `DECISION_LOG.md` entry.
- Activating a route: only through the quality gate.

---

*Governed under the OutMerchant Governance Operating System. Enforced by `main/scripts/validate_routes.py` and `main/scripts/validate_links.py`.*
