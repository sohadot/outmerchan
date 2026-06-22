# Outmerchant

**The reference standard for Merchant Sovereignty.**

Outmerchant.com defines, measures, and names the condition in which a merchant owns their route to the buyer — channels, customers, reputation, settlement rails, and margin — without depending on any single platform to hold any of it.

## What This Repository Contains

| Path | What It Is |
|------|------------|
| `/` | The live standard — HTML surface, JSON-LD, sitemap, robots |
| `main/data/` | The governed data model — score dimensions, questions, levels, lexicon, pages |
| `main/scripts/` | Quality gate validators and build scripts |
| `DECISION_LOG.md` | Every significant decision about the system, recorded |
| `QUALITY_GATE.md` | The enforcement layer — what is checked and how |
| `SCORE_GOVERNANCE.md` | The Merchant Sovereignty Score governance |
| `LEXICON_GOVERNANCE.md` | Lexicon admission law and casing rules |
| `ASSET_THESIS.md` | The strategic thesis — why this asset exists and what it becomes |

## The Standard

The **Merchant Sovereignty Score** (0–100) measures commercial independence across eight dimensions:

| # | Code | Dimension |
|---|------|-----------|
| 01 | DEP | Platform Dependency |
| 02 | OWN | Customer Ownership |
| 03 | REP | Reputation Portability |
| 04 | PAY | Payment & Settlement Exposure |
| 05 | FEE | Fee & Margin Leakage |
| 06 | XBR | Cross-Border Trust |
| 07 | AGT | AI Commerce Readiness |
| 08 | GOV | Governance Independence |

Four tiers classify the result: **Captured** (0–25) · **Dependent** (26–50) · **Emerging** (51–75) · **Outmerchant** (76–100).

The terminal tier — Outmerchant — is inviolable by DEC-001 and DEC-006. Its spelling is governed by DEC-016.

## The Quality Gate

```
python3 main/scripts/quality_gate.py
```

Runs 9 validators. Exits non-zero on any governance violation. Runs in CI on every push. A red gate blocks merge.

## Governance

Every significant decision is recorded in `DECISION_LOG.md` with an ID, date, layer, decision, and rationale. The current record runs to DEC-016. Nothing significant changes silently.

**Orthography:** "Outmerchant" (initial capital only) is the official form per DEC-016. Validator 9 (`validate_orthography.py`) enforces this automatically.

---

*Every layer serves the merchant. No layer owns the merchant.*
