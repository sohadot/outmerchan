# Decision Log

> The asset does not merely have pages. It has a history of decisions explaining why everything was built the way it was. This log is part of what makes the structure impossible to imitate: a copier can clone a page; they cannot clone the reasoning record.

Every entry is permanent. Decisions are superseded by later entries, never edited away.

---

## DEC-001 — OutMerchant defined as both verb and rank

**Date:** 2025-12-01 · **Layer:** Constitutional / Lexicon

"outmerchant" (lowercase) is the verb: to out-trade competitors by owning, rather than renting, the route to the buyer. "OutMerchant" (CamelCase) is the noun and the rank: the merchant who has achieved measurable commercial sovereignty. The duality is constitutional; all copy, structured data, and tooling must preserve it. **Why it matters:** the verb gives instant legibility; the rank gives the framework its destination.

## DEC-002 — Merchant is the foundation; every layer serves the merchant

**Date:** 2025-12-01 · **Layer:** Constitutional

The governing sentence of the entire system: **"Every layer serves the merchant. No layer owns the merchant."** Any feature, page, monetization, or integration that inverts this relationship — that makes the merchant serve the layer — is rejected regardless of revenue or reach. This sentence appears at the head of every governance document as a standing test.

## DEC-003 — AI is treated as the future control layer of commerce

**Date:** 2026-06-10 · **Layer:** Constitutional / AI Commerce

Approved formulation (binding under `CLAIM_POLICY.md`): "AI is becoming a control layer in discovery, comparison, trust, and purchase routing." OutMerchant is therefore built AI-native: machine-legible lexicon, structured data on every surface, and a planned agentic commerce standard. Absolute formulations ("AI will control everything") are prohibited.

## DEC-004 — Web3 is the trust/ownership layer, not a hype layer

**Date:** 2026-06-10 · **Layer:** Constitutional

Decentralized infrastructure is adopted where it serves merchant sovereignty (portable reputation, settlement optionality, ownership records) and ignored where it does not. No token promotion, no NFT hype, no crypto-cultural register. "Protocol" language on the asset means governed standard, not chain product.

## DEC-005 — No monetization before the diagnostic layer

**Date:** 2026-06-10 · **Layer:** Monetization

No revenue surface of any kind ships before the Sovereignty Score diagnostic layer is live and the reference layer is established. Rationale: a sovereignty standard that monetizes before it measures looks commercially captured and refutes its own authority. When monetization opens, it follows `MONETIZATION_PRINCIPLES.md` (constitutional layer, forthcoming) — revenue may not compromise reference authority.

## DEC-006 — Score levels fixed: Captured, Dependent, Emerging, OutMerchant

**Date:** 2026-06-10 · **Layer:** Score

The four tiers and boundaries are fixed: 0–25 Captured, 26–50 Dependent, 51–75 Emerging, 76–100 OutMerchant. The terminal tier deliberately carries the asset's name — the self-referential closure that makes the framework aim at the brand. This element is inviolable under `SCORE_GOVERNANCE.md`; changing it requires a constitutional decision superseding this entry.

## DEC-007 — No marketplace claim before governance and score foundation

**Date:** 2026-06-10 · **Layer:** Constitutional / Claims

OutMerchant makes no marketplace, buyer-network, or transaction-capability claims while no such capability exists. The asset is a standard first. Any future marketplace layer requires: governance foundation complete, score layer live and adopted, and a dedicated constitutional decision. Premature marketplace framing is the fastest route to becoming an ordinary, dismissible commerce site.

## DEC-008 — Governance Operating System installed (Sprint 2A)

**Date:** 2026-06-10 · **Layer:** Governance

The governance layer ships before the score tool, so that Sprint 2B builds a *governed* instrument, not an arbitrary one. Installed: `SCORE_GOVERNANCE.md`, `LEXICON_GOVERNANCE.md`, `ROUTE_GOVERNANCE.md`, `CLAIM_POLICY.md`, `AI_READABILITY_POLICY.md`, `QUALITY_GATE.md`, this log; the governed data layer (`main/data/`: score model, glossary, route registry, navigation, internal link graph); and the mechanical quality gate (`main/scripts/` + CI workflow). **Why it matters:** the order is the strategy — own the dictionary, the standard, the measurement, the governance, and the decision record before owning the market.

## DEC-009 — Category named "Merchant Sovereignty"

**Date:** 2026-06-10 · **Layer:** Constitutional / Category

The category the asset owns is named **Merchant Sovereignty** — two words, sayable by others without effort. The full formulation ("merchant sovereignty in the AI-mediated, decentralized, and fragmented commerce era") is the category's *definition* and thesis sentence, not its name; "AI-Native Merchant Sovereignty" is a secondary distinguishing formulation. **Why it matters:** category names that win are the ones other people can repeat; a definition cannot be a name.

## DEC-010 — Audience layering doctrine

**Date:** 2026-06-10 · **Layer:** Constitutional / Audience

Audiences are enrichment layers served in strict order, not parallel launch targets: (1) merchants — they use the instrument; (2) companies and investors — they see the standard; (3) analysts and journalists — they carry the narrative; (4) researchers, students, governments, and AI systems — they institutionalize the reference. Later layers arrive on their own because genuine reference status is discovered, not marketed. Each layer enriches the asset and makes it a real reference.

## DEC-011 — "Agent-Selectable Merchant" admitted to the lexicon; other proposed terms deferred

**Date:** 2026-06-10 · **Layer:** Lexicon

"Agent-Selectable Merchant" passes the admission law: it names the end-state capability dimension 07 (AGT) measures toward, has no prior owner, and serves Cluster A SEO. Admitted as founding term 15. Proposed terms "Smart Commercial Escrow", "Merchant Passport", and "Multi-Rail Commerce" are deferred until pages exist that need them — a lexicon of 15 governed terms is stronger than 25 with idle entries.

## DEC-012 — /score/ ships as Phase 3: free measurement, governed model only, machine-readable results

**Date:** 2026-06-10 · **Layer:** Score / Build

The Merchant Sovereignty Score diagnostic ships at `/score/` as a static, client-side instrument that reads exclusively from the three governed model files (`score_dimensions.json`, `score_questions.json`, `score_levels.json`) — no hardcoded score logic. The measurement is free and ungated; results include the full dimension breakdown and a machine-readable JSON export per `AI_READABILITY_POLICY.md`. The instrument surface is clinic-grade: fast, restrained, indexable, accessible — concept first, performance second, beauty third. Links to dimension and level pages activate in Phase 4; until then the instrument references them as registered routes without rendering dead links.

## DEC-013 — OutMerchant moves from diagnostic product to reference standard surface

**Date:** 2026-06-10 · **Layer:** Build / Reference Standard

The governed dimension and level pages are activated: eight dimension reference pages (`/dimensions/…`) and four tier definition pages (`/levels/…`), generated exclusively from the governed model files by `main/scripts/build_reference_pages.py` — pages are regenerated, never hand-edited, so the reference layer cannot drift from the standard it documents. `/levels/outmerchant/` formally defines OutMerchant as the protected highest sovereignty rank, citing DEC-001/DEC-006. The quality gate gains a sixth validator (`validate_reference.py`) enforcing name/ID/range fidelity against the model, the protected-rank statement, and the cross-link topology; SEO and link validators are tightened (robots meta, exactly one H1, thin-content floor, no non-active routes in the sitemap, no live links to non-active routes, inbound/outbound link coverage). **Why it matters:** with measurement (Phase 3) and formal definitions (this phase) both live and mutually linked, the asset is no longer a tool with a story — it is a reference standard surface: every term it measures is now a citable page.

---

*Maintained under the OutMerchant Governance Operating System. New entries require: ID, date, layer, decision, rationale.*
