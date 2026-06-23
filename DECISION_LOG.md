# Decision Log

> The asset does not merely have pages. It has a history of decisions explaining why everything was built the way it was. This log is part of what makes the structure impossible to imitate: a copier can clone a page; they cannot clone the reasoning record.

Every entry is permanent. Decisions are superseded by later entries, never edited away.

---

## DEC-001 — Outmerchant defined as both verb and rank

**Date:** 2025-09-01 · **Layer:** Constitutional / Lexicon / Score

The founding duality is established and inviolable: *outmerchant* (v.) is the act of trading without ceding control of the route to the buyer. *Outmerchant* (n.) is the rank earned when that act is complete: a merchant who has achieved measurable commercial sovereignty across the eight governed dimensions. This duality is not decoration — it is the asset's structural premise. The verb names what the merchant does; the noun names what the merchant becomes. This entry cannot be superseded on the noun/verb relationship, only extended.

---

## DEC-002 — Lexicon as the asset's primary definitional authority

**Date:** 2025-09-01 · **Layer:** Constitutional / Lexicon

The lexicon is not a glossary appended to content. It is the asset's primary definitional authority: every term used in the standard must be defined here first, governed here, and exposed to machines here. Content that uses a term before it exists in the lexicon is a quality failure. The lexicon precedes everything.

---

## DEC-003 — Route registry as the canonical source for all pages

**Date:** 2025-09-01 · **Layer:** Constitutional / Routes

The route registry (`main/data/pages.json`) is the single source of truth for what pages exist, what they are called, and whether they are active. A page that is not in the registry does not officially exist. No page is created without a registry entry. The quality gate enforces this.

---

## DEC-004 — Lexicon admission law

**Date:** 2025-09-01 · **Layer:** Constitutional / Lexicon

No term enters the canonical lexicon without: a complete definition, a system function (what the term *does* inside the asset), at least one relationship to another canonical term, a route entry, and a score relation. The quality gate rejects entries missing any of these. This prevents accumulation of decorative vocabulary.

---

## DEC-005 — No monetization before the score exists and is indexed

**Date:** 2025-09-01 · **Layer:** Constitutional / Monetization

No revenue surface, affiliate link, or acquisition signal is placed on the asset until: (1) the Merchant Sovereignty Score is live and functional, (2) the score has been indexed by search engines, and (3) at least one dimension has demonstrated organic traffic. This decision is enforced by the quality gate and by convention: the gate checks for monetization elements before the allowed phase. The rationale: monetization before proof destroys the epistemic authority the asset needs to be acquirable.

---

## DEC-006 — Score tiers, boundaries, and terminal tier name are inviolable

**Date:** 2025-09-01 · **Layer:** Constitutional / Score

The four tiers of the Merchant Sovereignty Score are fixed: Captured (0–25), Dependent (26–50), Emerging (51–75), Outmerchant (76–100). These boundaries, the number of tiers, and the terminal tier name are inviolable. Any proposal to change them must supersede this decision on the record first. The quality gate enforces the terminal tier name and boundaries on every push.

---

## DEC-007 — SEO and AI-readability are first-class citizens, not afterthoughts

**Date:** 2025-09-01 · **Layer:** Constitutional / SEO / AI Readability

Every page published by this asset carries: a canonical URL, a title, a meta description, and JSON-LD structured data. These are not optional enrichments — they are part of the definition of a page. A page without them is not a page; it is a file. The quality gate rejects pages missing any of these.

---

## DEC-008 — Eight dimensions, fixed codes, equal weights

**Date:** 2025-09-01 · **Layer:** Constitutional / Score

The Merchant Sovereignty Score measures eight dimensions, each weighted equally at 12.5% of the total. The dimension codes are fixed: DEP, OWN, REP, PAY, FEE, XBR, AGT, GOV. These codes, the number of dimensions, and the equal-weight architecture are inviolable. A proposal to change the number of dimensions or their weights must supersede this decision on the record first.

---

## DEC-009 — "Merchant Sovereignty" is the category name

**Date:** 2025-09-01 · **Layer:** Constitutional / Category

"Merchant Sovereignty" is the two-word name of the category the asset defines, owns, and measures. It is sayable, searchable, and distinct. No synonym replaces it. Content that introduces competing category labels without superseding this decision is a quality failure.

---

## DEC-010 — Doctrine sentence is inviolable

**Date:** 2025-09-01 · **Layer:** Constitutional / Doctrine

The doctrine sentence is: *Every layer serves the merchant. No layer owns the merchant.* This sentence appears in every governance document and on every governed page. It is not a tagline — it is a constitutional statement of what the asset is for. No layer, no tool, no platform, and no acquirer changes what the asset is built to serve.

---

## DEC-011 — No external JavaScript dependencies without approval

**Date:** 2025-09-01 · **Layer:** Constitutional / Technical

No external JavaScript dependency is introduced without explicit approval and a decision log entry. Every external script is a trust, performance, and sovereignty risk. The asset's surface must remain controllable without third-party permission.

---

## DEC-012 — Crypto and web3 vocabulary boundaries

**Date:** 2025-09-01 · **Layer:** Constitutional / Lexicon

Crypto and web3 vocabulary is permitted only as defined trust and ownership concepts — not as hype. If a web3 term is used, it is admitted to the lexicon with a precise definition, or used only descriptively without canonical claim. This prevents the asset from being categorised as crypto content by search engines or by acquirers who would discount that positioning.

---

## DEC-013 — Reference pages must be generated from the governed model

**Date:** 2025-11-15 · **Layer:** Operational / Reference Standard

All dimension and level reference pages must be generated from the governed data model, not written separately. The explanation cannot drift from the thing it explains. A reference page that contradicts the governed model is a quality failure. The build script (`build_reference_pages.py`) and its quality gate validator (`validate_reference.py`) enforce this.

---

## DEC-014 — Definitional authority pages must be generated from the lexicon

**Date:** 2025-11-15 · **Layer:** Operational / Lexicon / Reference

All lexicon term pages (under `/lexicon/`) must be generated from the governed lexicon data (`glossary_terms.json`), not written separately. A term page that contradicts or extends the governed definition without a lexicon update is a quality failure. The build script (`build_lexicon_pages.py`) and its quality gate validator (`validate_definitional.py`) enforce this.

---

## DEC-015 — Engine guidance file governs all score result surfaces

**Date:** 2025-11-15 · **Layer:** Operational / Score Engine

The `engine_guidance.json` file is the single source of truth for all text surfaces generated by the score engine: weak interpretations per dimension, next actions per dimension, boundary statements, and route-to-buyer descriptions per tier. No score surface may carry its own copy of this text. The quality gate validator (`validate_engine.py`) enforces this.

---

## DEC-016 — Official Orthography: Outmerchant as a Unified Word

**Date:** 2026-06-23 · **Layer:** Constitutional / Lexicon / Orthography

Outmerchant is the official written form of the asset, protected rank, protocol, and public standard. The spelling is intentionally unified to preserve the value of the word as a single canonical term, not a camel-cased composition. The lowercase form "outmerchant" may be used only when referring to the verb or lexical headword. The forms "OutMerchant," "Out Merchant," and "outMerchant" are not allowed in public-facing canonical surfaces, metadata, generated reference pages, structured data, reports, or governance documents except where explicitly preserved as superseded historical wording.

**Rationale:** A category-origin asset must stabilize its name before it can stabilize its category. Outmerchant is intended to become a single canonical word: the asset, the rank, and the terminal state of the standard. Orthographic drift weakens memory, search consistency, machine readability, and conceptual authority.

---

*Maintained under the Outmerchant Governance Operating System. New entries require: ID, date, layer, decision, rationale.*
