# Score Governance

> Governs the Merchant Sovereignty Score: its model, its data, its change control, and its inviolable elements.
>
> **Every layer serves the merchant. No layer owns the merchant.**

## Governed Artifacts

The score model lives in exactly three data files. No score logic may exist anywhere else.

| File | Role |
|------|------|
| `main/data/score_dimensions.json` | The eight dimensions of merchant control — codes, names, weights |
| `main/data/score_questions.json` | The governed question bank — 20 questions mapped to dimensions |
| `main/data/score_levels.json` | The four classification tiers — fixed boundaries and names |

Any tool, page, or report that computes or displays a score MUST read from these files. A score surface that hardcodes its own model is a governance violation.

## Inviolable Elements

The following may not be changed by any sprint, redesign, or integration without a constitutional-level decision recorded in `DECISION_LOG.md`:

1. **The eight dimensions.** Platform Dependency (DEP), Customer Ownership (OWN), Reputation Portability (REP), Payment & Settlement Exposure (PAY), Fee & Margin Leakage (FEE), Cross-Border Trust (XBR), AI Commerce Readiness (AGT), Governance Independence (GOV).
2. **The four tiers and their boundaries.** 0–25 Captured, 26–50 Dependent, 51–75 Emerging, 76–100 OutMerchant.
3. **The terminal-tier name.** The highest tier carries the asset's own name. This is the asset's inevitability mechanism: the framework cannot be used without aiming at the brand. Removing this closure removes the asset's core structural property. (DEC-001, DEC-006)

## Change Control

- Every change to dimensions, weights, questions, options, points, or tier semantics requires an entry in `DECISION_LOG.md` **before** merge.
- Question wording may be refined editorially, but a change that alters what a question measures is a model change.
- Weights must always sum to 100 across dimensions. The quality gate enforces this.
- Question identifiers (Q01–Q20) are permanent. Retired questions are marked `"status": "retired"`, never deleted, never reused.

## Scoring Contract

- Each question offers ordered options with integer points from 0 (captured behavior) to the question maximum (sovereign behavior).
- Dimension score = (points earned in that dimension / maximum points in that dimension) × 100.
- Total score = weighted average of dimension scores using the weights in `score_dimensions.json`.
- The total score maps to exactly one tier in `score_levels.json`. Boundaries are inclusive.
- Output must always include: total score, tier name, and all eight dimension scores. A score without its dimension breakdown is not a Sovereignty Score.

## Score Surface Rules

- The diagnostic must remain free to run. Monetization, if ever applied, gates the *delivered report*, never the measurement itself (see `MONETIZATION_PRINCIPLES.md`, future).
- The score must never be used to rank, shame, or expose individual merchants publicly.
- No "instant score" marketing gimmicks. The score is a standard, not a quiz funnel.
- Structured (machine-readable) score results are a planned requirement under `AI_READABILITY_POLICY.md`.

## Prohibited

- Hardcoded score logic outside the three data files
- Random or A/B-tested changes to the model
- Adding a fifth tier, renaming tiers, or shifting boundaries for marketing reasons
- Publishing benchmark claims ("the average merchant scores 47") without real data and `CLAIM_POLICY.md` compliance

---

*Governed under the OutMerchant Governance Operating System. Enforced by `main/scripts/validate_score_model.py`.*
