# OutMerchant.com

> OutMerchant is not built as a website. It is built as a miniature commercial state: it has a constitution, a lexicon, a measurement standard, a decision record, boundaries, quality courts, and execution layers.
>
> **Every layer serves the merchant. No layer owns the merchant.**

Live surface: [outmerchant.com](https://outmerchant.com/) — the doctrine, the canonical lexicon, the eight-dimension architecture, and the entry to the Merchant Sovereignty Score.

## Governance Operating System

Every page, tool, term, link, claim, monetization, and build decision in this repository is subject to OutMerchant logic. The system is layered; no layer may be bypassed.

| Layer | Governing files |
|-------|----------------|
| Score & Standard | `SCORE_GOVERNANCE.md` |
| Canonical Lexicon | `LEXICON_GOVERNANCE.md` |
| Routes & Pages | `ROUTE_GOVERNANCE.md` |
| Claims & Sources | `CLAIM_POLICY.md` |
| AI Readability | `AI_READABILITY_POLICY.md` |
| Quality Court | `QUALITY_GATE.md` |
| Decision Record | `DECISION_LOG.md` |

## Governed Data Layer

The single sources of truth. No logic may exist outside them.

```
main/data/
├── score_dimensions.json   # the eight dimensions of merchant control
├── score_questions.json    # the governed 20-question bank
├── score_levels.json       # Captured / Dependent / Emerging / OutMerchant (inviolable)
├── glossary_terms.json     # the canonical lexicon (14 founding terms)
├── pages.json              # the route registry (28 routes)
├── internal_links.json     # the required link graph (85 edges)
└── navigation.json         # the governed navigation
```

## The Quality Gate

```
python3 main/scripts/quality_gate.py
```

Runs on every push via `.github/workflows/quality-gate.yml`. A red gate blocks merge: either the change is fixed to comply, or the law itself is changed explicitly with a `DECISION_LOG.md` entry. There is no third path.

## Deployment

GitHub Pages serves from the repository root (`index.html`, `CNAME`). GitHub is the source of truth. Content routes (`/score/`, `/lexicon/…`, `/dimensions/…`, `/levels/…`, `/protocol/`) are registered as `planned` in `pages.json` and ship in Sprint 2B through the gate.

## Why the structure resists imitation

A copier can clone a page. They cannot clone: a name that is a verb and a rank, a canonical lexicon, a governed score model whose terminal tier carries the asset's name, a required link topology, an AI-native readability layer, mechanical quality enforcement, and a permanent record of why every decision was made. The composition is the moat.

---

*Strategic doctrine for this asset is maintained in the Sovereign Asset System repository (`portfolio/asset-dossiers/outmerchant.com/`).*
