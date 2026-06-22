# Lexicon Governance

> Outmerchant must own its vocabulary, not merely use the market's. This file governs how terms enter, live in, and leave the canonical lexicon.
>
> **Every layer serves the merchant. No layer owns the merchant.**

## Canonical Source Rule

Outmerchant.com is the canonical source of definition for every term in its lexicon. Definitions are first articulated here, governed here, and exposed to machines here (JSON-LD `DefinedTermSet`, see `AI_READABILITY_POLICY.md`).

The lexicon is the asset's definitional priority made operational: any serious discussion of merchant sovereignty either uses this vocabulary or defines itself against it.

## Governed Artifacts

| File | Role |
|------|------|
| `main/data/glossary_terms.json` | The single source of truth for all canonical terms |
| `main/content/lexicon/` | One reference page per term (Sprint 2B+) |
| `index.html` lexicon section + JSON-LD | The live definitional surface |

## The Admission Law

> **No term is added unless it has: a definition, a function inside the system, an internal link, a relationship to the score, and a place in the ontology.**

Concretely, every entry in `glossary_terms.json` must carry:

1. **`definition`** — a complete, precise definition in the asset's register
2. **`system_function`** — what the term *does* inside Outmerchant (names a risk, names a capability, names a measurement, names a tier)
3. **`related`** — at least one relationship to another canonical term
4. **`route`** — the page (active or planned) where the term is canonically defined
5. **`score_relation`** — the dimension, tier, or instrument the term connects to, or an explicit `"doctrine"` for constitutional terms

The quality gate rejects entries missing any of these.

## Founding Terms

The founding lexicon (v1) consists of: outmerchant (v.), Outmerchant (n.), Merchant Sovereignty, Merchant Sovereignty Score, Route-to-Buyer Control, Platform Capture, Platform Dependency, Portable Reputation, AI Merchant Sovereignty, Agentic Commerce Readiness, Machine-Readable Trust, Non-Aligned Commerce, Settlement Exposure, Governance Independence.

## Casing and Form Rules

- **outmerchant** — lowercase, the verb. To out-trade by owning, rather than renting, the route to the buyer.
- **Outmerchant** — initial capital only, the noun, rank, protocol, asset, and standard. (DEC-001, superseded by DEC-016 on spelling)
- The verb/rank duality is constitutional (DEC-001). Copy that blurs it is a quality failure.
- Term names in body copy must match the canonical form exactly. No improvised synonyms for governed terms.

## Change Control

- New terms: require the full admission record plus a `DECISION_LOG.md` entry stating why the system needs the term.
- Definition changes: editorial sharpening is allowed; meaning changes require a decision log entry.
- Removal: terms are deprecated (`"status": "deprecated"`), never silently deleted. Deprecation requires a decision log entry.
- The lexicon must never import undefined market jargon. If a market term is used in content, it is either admitted to the lexicon or used descriptively without canonical claim.

## Prohibited

- Terms added for SEO volume without system function
- Competing or duplicate definitions across pages (one term, one canonical route)
- Crypto/web3 vocabulary used as hype rather than as defined trust/ownership concepts (see `DECENTRALIZED_COMMERCE_BOUNDARIES.md`, constitutional layer)
- Definitions that contradict the doctrine sentence: *every layer serves the merchant; no layer owns the merchant*

---

*Governed under the Outmerchant Governance Operating System. Enforced by `main/scripts/validate_glossary.py`.*
