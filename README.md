# Outmerchant

**The reference standard for Merchant Sovereignty.**

Outmerchant.com defines, measures, and protects the condition in which a merchant owns the route to the buyer: channels, customers, reputation, settlement rails, margin, machine readability, and governance.

## Current Architecture

The live asset contains 29 governed public routes beyond the home surface, 15 governed lexicon terms, 8 score dimensions, 4 sovereignty levels, and the protected Outmerchant rank. The route registry currently contains 30 active entries including `/`.

Core public layers:

- `/score/` - governed Merchant Sovereignty diagnostic engine
- `/protocol/` - the protocol binding score, lexicon, reference pages, and governance
- `/lexicon/` - canonical Merchant Sovereignty vocabulary
- `/agentic-commerce/` - AI-mediated commerce and machine-legibility layer

The internal link registry records 118 governed internal links, including the 114-link baseline plus the active Agentic Commerce reinforcement edges.

## Governance

The repository is governed by:

- `DECISION_LOG.md` - constitutional and operational decisions through DEC-016
- `QUALITY_GATE.md` - the enforcement layer
- `SCORE_GOVERNANCE.md` - score dimensions, tiers, and diagnostic rules
- `LEXICON_GOVERNANCE.md` - lexicon admission law
- `ROUTE_GOVERNANCE.md` - route registry and internal topology
- `AI_READABILITY_POLICY.md` - metadata and machine-readable clarity rules
- `CLAIM_POLICY.md` - claim discipline and bounded AI language

DEC-016 locks the official spelling: **Outmerchant** for the asset, rank, protocol, and standard; **outmerchant** only for the verb or lexical headword; **outmerchant.com** only for the domain.

## Quality Gate

```bash
python main/scripts/quality_gate.py
```

The gate now runs 9 validators:

1. Score model
2. Lexicon
3. Routes
4. Internal links
5. SEO / AI readability
6. Reference standard
7. Definitional authority
8. Score engine governance
9. Official orthography

Google Search Console and Bing Webmaster discovery are recorded in the indexation intelligence log. The next phase waits for real Google/Bing indexation data before corrective authority reinforcement begins.

---

*Every layer serves the merchant. No layer owns the merchant.*
