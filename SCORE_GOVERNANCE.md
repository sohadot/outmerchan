# Score Governance

> The law of the measurement instrument. What the Merchant Sovereignty Score is, what it measures, what it cannot become, and what governs it.
>
> **Every layer serves the merchant. No layer owns the merchant.**

---

## What the Score Is

The Merchant Sovereignty Score is a diagnostic measurement of a merchant's commercial sovereignty posture. It is a 0–100 index produced by applying a weighted average across eight governed dimensions of merchant control. It is not financial advice, investment advice, legal advice, or a guarantee of commercial outcome.

## What the Score Measures

Eight dimensions, each weighted equally at 12.5% of the total:

| Code | Dimension |
|------|-----------|
| DEP | Platform Dependency |
| OWN | Customer Ownership |
| REP | Reputation Portability |
| PAY | Payment & Settlement Exposure |
| FEE | Fee & Margin Leakage |
| XBR | Cross-Border Trust |
| AGT | AI Commerce Readiness |
| GOV | Governance Independence |

## The Four Tiers (Inviolable — DEC-006)

| Tier | Range | Meaning |
|------|-------|---------|
| Captured | 0–25 | Fully platform-dependent. Commerce survives only at the infrastructure's pleasure. |
| Dependent | 26–50 | Partially free. Significant single-point-of-control exposure. |
| Emerging | 51–75 | Building sovereignty. The merchant sees the cage and is constructing the exit. |
| Outmerchant | 76–100 | Sovereign. Channels, customers, reputation, settlement, and margin owned. |

The boundaries, tier names, and terminal tier name (*Outmerchant*) are inviolable. A proposal to change them requires a decision log entry that supersedes DEC-006.

## What the Score Cannot Become

- A ranking of merchants relative to each other (it is an absolute measure, not a relative one)
- A certification system that Outmerchant issues for a fee (before DEC-005 is superseded)
- A tool that can be gamed by any action other than genuinely improving the measured conditions
- A surface for monetization before the allowed phase (DEC-005)

## Governed Artifacts

| File | Role |
|------|------|
| `main/data/score_dimensions.json` | 8 dimensions, codes, weights, names |
| `main/data/score_questions.json` | 20 governed questions, one per dimension |
| `main/data/score_levels.json` | 4 tier definitions with boundaries |
| `main/data/engine_guidance.json` | Text for score result surfaces |

## Change Control

- Dimension codes, weights, and count: inviolable (DEC-008)
- Tier boundaries and terminal tier name: inviolable (DEC-006)
- Questions: may be refined editorially without a decision; meaning changes require a decision entry
- Engine guidance text: editorial changes allowed; structural changes require a decision entry

---

*Governed under the Outmerchant Governance Operating System. Enforced by `main/scripts/validate_score_model.py`.*
