"""Governed builder for the canonical lexicon pages (Sprint 2C-2, DEC-014).

Generates /lexicon/ (the canonical DefinedTermSet surface) and one page per
canonical term from glossary_terms.json. The published definition is the
governed definition, verbatim — pages are regenerated, never hand-edited.
Run after any glossary change, then run the quality gate.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"
ORIGIN = "https://outmerchant.com"

from build_reference_pages import STYLE  # shared clinic-grade style

terms = json.loads((DATA / "glossary_terms.json").read_text())["terms"]
dims = json.loads((DATA / "score_dimensions.json").read_text())["dimensions"]
levels = json.loads((DATA / "score_levels.json").read_text())["levels"]

DIM_ROUTE = {d["code"]: d["route"] for d in dims}
DIM_NAME = {d["code"]: d["name"] for d in dims}

# Per-slug editorial layer: context paragraph + usage sentence.
EDITORIAL = {
    "merchant-sovereignty": {
        "context": "This is the category itself — the conceptual center every page, term, and measurement on this asset serves. Sovereignty here is not isolation: a sovereign merchant may use platforms, marketplaces, and intermediaries everywhere. The condition is about control with optionality — the standard asks whether any single external party can terminate or capture the trade, not whether external parties are present. The eight dimensions of the Merchant Sovereignty Score decompose this condition into measurable parts.",
        "usage": "Sovereignty is not whether you use platforms; it is whether any single one of them can end you.",
    },
    "route-to-buyer-control": {
        "context": "This term names the asset's central thesis. The route to the buyer is the full path of a sale — discovery, relationship, transaction, settlement, and post-sale trust — and in modern commerce nearly every segment of that path is owned by someone other than the merchant. The term reframes familiar costs (commissions, ad spend, processing fees) as what they structurally are: rent paid on a route the merchant does not own.",
        "usage": "Their product margin was healthy; their route-to-buyer control was zero — the platform owned every step between them and the customer.",
    },
    "platform-capture": {
        "context": "Capture is a ratchet, not an event. Each year inside a single platform deepens the asymmetry: more revenue concentrated, more reputation locked in, more customer relationships mediated, until leaving costs more than staying — regardless of how the terms degrade. The standard treats capture as the measurable end-state of unmanaged platform dependency, and names its lowest tier after the condition.",
        "usage": "The store was profitable until the day it was suspended; that is what platform capture means — profitability at someone else's pleasure.",
    },
    "platform-dependency": {
        "context": "Dependency is the standard's entry concept because it is the sovereignty risk merchants feel first and most concretely: the algorithm change that halves traffic overnight, the policy update that re-prices the business, the suspension that stops it entirely. Dimension 01 measures it through revenue concentration, suspension survival time, and the existence of channels no third party can switch off.",
        "usage": "A merchant with 90% of revenue on one marketplace does not have a platform strategy; they have platform dependency.",
    },
    "portable-reputation": {
        "context": "Reputation is the merchant's accumulated trust capital, and its portability decides whether that capital belongs to the merchant or functions as the platform's retention weapon. A five-star history that evaporates on account closure is not an asset — it is a hostage. The standard measures portability through dimension 03: whether trading history and trust signals can be carried, proven, and re-deployed outside any single database.",
        "usage": "Ten years of flawless trade meant nothing the day the account closed — reputation that cannot leave with you was never yours.",
    },
    "ai-merchant-sovereignty": {
        "context": "AI is becoming a control layer in discovery, comparison, trust, and purchase routing. This term names the asset's doctrine for that shift: the merchant must become legible, trustworthy, and selectable by AI agents without surrendering sovereignty to AI-controlled market access. It is the same anti-single-point-of-control principle, applied to the newest layer that could become one.",
        "usage": "Being invisible to AI agents is the new platform dependency; being visible only through one AI gatekeeper is the next platform capture.",
    },
    "agentic-commerce-readiness": {
        "context": "Dimension 07 of the standard operationalizes the AI doctrine as a measurable state: machine-readable catalog, structured commercial terms, and independently verifiable identity and trust signals. Readiness is deliberately defined on the merchant's own surfaces — a merchant who is agent-ready only inside one platform's proprietary feed has converted an old dependency into a newer one.",
        "usage": "The agent could parse her catalog, check her terms, and verify her history in seconds — that is agentic commerce readiness.",
    },
    "machine-readable-trust": {
        "context": "This is the bridge concept between portable reputation and agentic readiness: trust signals published in structured, verifiable form that software can check without asking a platform to vouch. Human buyers read testimonials; AI agents verify claims. The merchant whose trust exists only as prose — or only inside someone else's database — is unverifiable to the demand layer now forming.",
        "usage": "A wall of five-star reviews is trust an agent cannot read; a verifiable, structured trading record is machine-readable trust.",
    },
    "non-aligned-commerce": {
        "context": "Global trade is fragmenting into zones — diverging regulations, regional payment systems, separated platform ecosystems. This term names the standard's geopolitical posture: commerce structured to operate across fragments without binding its continuity to any single bloc, platform, or intermediary. The discipline of the term matters: not anti-platform, not anti-state, not anti-bank — anti-single-point-of-control.",
        "usage": "When the rail between two markets closed, the non-aligned merchant rerouted; the aligned one waited for permission.",
    },
    "settlement-exposure": {
        "context": "Settlement is the bloodstream of commerce, and exposure measures how much of it flows through rails the merchant does not control. Dimension 04 asks three questions: how many independent rails can accept payment today, what happens when the primary provider freezes payouts, and whether cross-border settlement depends on a single intermediary's consent. A frozen payout is the fastest way a healthy merchant dies.",
        "usage": "One gateway, one currency corridor, one provider's risk policy — that is settlement exposure wearing the costume of simplicity.",
    },
    "governance-independence": {
        "context": "The deepest dimension of the standard, because it governs all the others: who writes the rules of the merchant's commerce, and does the merchant hold a documented exit path from every party that could rewrite them unilaterally. Dimension 08 is where the standard's governing sentence becomes measurable — every layer should serve the merchant; this dimension measures whether any layer owns him.",
        "usage": "She mapped every provider that could stop her business and wrote an exit path for each — governance independence is sovereignty made procedural.",
    },
    "agent-selectable-merchant": {
        "context": "The end-state capability that dimension 07 measures toward: a merchant who can be discovered, evaluated, and selected by an AI buying agent on their own credentials — structured identity, parseable terms, verifiable trust — with no platform intermediary vouching for them. As agent-mediated buying grows, agent-selectability becomes what storefront visibility was to the last era of commerce.",
        "usage": "The buyer never saw the website; their agent verified the merchant, compared the terms, and placed the order — the sale went to the agent-selectable merchant.",
    },
}

OUTMERCHANT_PAGE = {
    "route": "/lexicon/outmerchant/",
    "context": "The headword carries the asset's deepest structural property: the verb names the act, the noun names the rank, and the rank is the terminal tier of the standard's own score. A merchant who measures Captured, Dependent, or Emerging has one natural path forward — and the destination permanently carries the standard's name, protected by recorded decisions (DEC-001, DEC-006) and an automated quality gate. The framework cannot be used without the name becoming the goal: that is the referential closure at the center of Outmerchant.",
    "usage_verb": "They stopped renting their route to market and started owning it — channel by channel, rail by rail, they outmerchanted competitors twice their size.",
    "usage_noun": "At 81 on the Sovereignty Score, no single platform, gateway, or intermediary could end her trade: she is an Outmerchant.",
}


def relation_link(term):
    rel = term["score_relation"]
    if rel in DIM_ROUTE:
        return DIM_ROUTE[rel], f"dimension {rel} — {DIM_NAME[rel]}"
    if rel == "instrument":
        return "/score/", "the Merchant Sovereignty Score"
    if rel == "tier":
        return ("/levels/outmerchant/", "the Outmerchant tier") if term["slug"] == "outmerchant-noun" \
            else ("/levels/captured/", "the Captured tier")
    return "/protocol/", "the Outmerchant Protocol"


def head(route, title, description, jsonld):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{ORIGIN}{route}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#020408">
<meta property="og:type" content="article">
<meta property="og:url" content="{ORIGIN}{route}">
<meta property="og:site_name" content="Outmerchant">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<script type="application/ld+json">
{jsonld}
</script>
<style>{STYLE}
  .canon-def {{ border-left:1px solid var(--signal); background:var(--signal-dim); padding:20px 24px; margin:20px 0; }}
  .canon-def p {{ margin:0; font-size:14px; color:var(--text); }}
  .pos {{ font-style:italic; color:var(--gold); font-size:14px; }}
  .term-list a {{ display:block; border:1px solid var(--text-ghost); padding:16px 20px; margin-bottom:8px; text-decoration:none; }}
  .term-list a:hover {{ border-color:var(--signal-mid); }}
  .term-list .t {{ font-family:var(--display); font-weight:700; font-size:15px; color:var(--text); }}
  .term-list .t em {{ color:var(--gold); font-size:12px; font-weight:400; margin-left:8px; }}
  .term-list .d {{ font-size:12px; color:var(--text-dim); margin-top:4px; display:block; }}
</style>
</head>
<body>
<header>
  <div class="wrap">
    <a class="logo" href="/">OUT<span>MERCHANT</span></a>
    <div class="header-tag">The Merchant Sovereignty Standard</div>
  </div>
</header>
"""

FOOTER = """<footer>
  <div class="wrap">
    <div>THE OUTMERCHANT LEXICON — CANONICAL DEFINITIONS</div>
    <div><a href="/">OUTMERCHANT.COM</a> — EVERY LAYER SERVES THE MERCHANT. NO LAYER OWNS THE MERCHANT.</div>
  </div>
</footer>
</body>
</html>
"""

CANON_NOTE = """    <h2>Canonical Source</h2>
    <p>This definition is first articulated, formally governed, and machine-published at Outmerchant.com. The text above is the governed definition, verbatim — it is generated from the same structured lexicon that machines read, and an automated quality gate rejects any divergence between the published page and the governed record. Definition changes happen only through a recorded decision, never silently.</p>"""


def defined_term_jsonld(ts, route):
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "DefinedTerm",
                "@id": f"{ORIGIN}/#term-{t['slug']}",
                "name": t["term"],
                "description": t["definition"],
                "url": f"{ORIGIN}{route}",
                "inDefinedTermSet": {"@id": f"{ORIGIN}/#lexicon"},
            } for t in ts
        ] + [{
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Outmerchant", "item": f"{ORIGIN}/"},
                {"@type": "ListItem", "position": 2, "name": "Lexicon", "item": f"{ORIGIN}/lexicon/"},
                {"@type": "ListItem", "position": 3, "name": ts[0]["term"], "item": f"{ORIGIN}{route}"},
            ],
        }],
    }, indent=2)


def related_links(term, slug_route):
    seen, parts = set(), []
    for rel in term["related"]:
        r = slug_route.get(rel)
        name = next(t["term"] for t in terms if t["slug"] == rel)
        if r and r not in seen and r != term["route"]:
            seen.add(r)
            parts.append(f'<a href="{r}">{name}</a>')
    return ", ".join(parts)


def build_term_page(term, slug_route):
    e = EDITORIAL[term["slug"]]
    route = term["route"]
    rel_route, rel_label = relation_link(term)
    title = f"{term['term']} — Canonical Definition | The Outmerchant Lexicon"
    desc = term["definition"][:300]
    body = f"""    <p class="kicker">// The Lexicon — Canonical Definition</p>
    <h1>{term['term']} <span class="pos">{term['type']}</span></h1>
    <div class="canon-def"><p>{term['definition']}</p></div>
    <h2>In the Standard</h2>
    <p>{term['system_function']}</p>
    <p>{e['context']}</p>
    <h2>Usage</h2>
    <p><em>“{e['usage']}”</em></p>
    <h2>Related Terms</h2>
    <p>{related_links(term, slug_route)}</p>
{CANON_NOTE}
    <div class="crosslinks">
      <p>This term operates inside <a href="{rel_route}">{rel_label}</a> and is governed by <a href="/protocol/">the Outmerchant Protocol</a>.</p>
      <a class="cta" href="/score/">→ Measure Your Sovereignty</a>
      <a class="cta-secondary" href="/lexicon/">Full Lexicon</a>
    </div>"""
    return head(route, title, desc, defined_term_jsonld([term], route)) + \
        f"<main>\n  <div class=\"wrap\">\n{body}\n  </div>\n</main>\n" + FOOTER


def build_outmerchant_page(slug_route):
    verb = next(t for t in terms if t["slug"] == "outmerchant-verb")
    noun = next(t for t in terms if t["slug"] == "outmerchant-noun")
    p = OUTMERCHANT_PAGE
    route = p["route"]
    title = "outmerchant (v.) / Outmerchant (n.) — Canonical Definition | The Outmerchant Lexicon"
    desc = ("outmerchant, verb: to out-trade competitors by owning, rather than renting, the route to the buyer. "
            "Outmerchant, noun: the protected highest rank (76–100) of the Merchant Sovereignty Score.")
    body = f"""    <p class="kicker">// The Lexicon — Canonical Definition — The Headword</p>
    <h1>outmerchant <span class="pos">verb</span> / Outmerchant <span class="pos">noun</span></h1>
    <h2>outmerchant <span class="pos">verb</span></h2>
    <div class="canon-def"><p>{verb['definition']}</p></div>
    <p><em>“{p['usage_verb']}”</em></p>
    <h2>Outmerchant <span class="pos">noun</span></h2>
    <div class="canon-def"><p>{noun['definition']}</p></div>
    <p><em>“{p['usage_noun']}”</em></p>
    <h2>The Referential Closure</h2>
    <p>{p['context']}</p>
{CANON_NOTE}
    <div class="crosslinks">
      <p>The noun is formally defined as a tier at <a href="/levels/outmerchant/">the Outmerchant rank</a>; the act is measured by <a href="/score/">the Merchant Sovereignty Score</a>; both are governed by <a href="/protocol/">the Outmerchant Protocol</a>. Related: <a href="/lexicon/merchant-sovereignty/">Merchant Sovereignty</a>, <a href="/lexicon/route-to-buyer-control/">Route-to-Buyer Control</a>.</p>
      <a class="cta" href="/score/">→ Measure Your Sovereignty</a>
      <a class="cta-secondary" href="/lexicon/">Full Lexicon</a>
    </div>"""
    return head(route, title, desc, defined_term_jsonld([verb, noun], route)) + \
        f"<main>\n  <div class=\"wrap\">\n{body}\n  </div>\n</main>\n" + FOOTER


def build_index(slug_route):
    route = "/lexicon/"
    title = "The Outmerchant Lexicon — Canonical Definitions of Merchant Sovereignty | Outmerchant"
    desc = ("The canonical lexicon of the Merchant Sovereignty standard: governed definitions of outmerchant, "
            "Outmerchant, Merchant Sovereignty, Platform Capture, Machine-Readable Trust, Agent-Selectable "
            "Merchant, and every term the standard names and measures.")
    active_terms = [t for t in terms if t["status"] == "active"]
    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "DefinedTermSet",
                "@id": f"{ORIGIN}/#lexicon",
                "name": "The Outmerchant Lexicon",
                "url": f"{ORIGIN}/lexicon/",
                "description": "Canonical definitions of the merchant sovereignty vocabulary, first articulated and governed at Outmerchant.com.",
                "hasDefinedTerm": [
                    {
                        "@type": "DefinedTerm",
                        "@id": f"{ORIGIN}/#term-{t['slug']}",
                        "name": t["term"],
                        "description": t["definition"],
                        "url": f"{ORIGIN}{t['route']}",
                    } for t in active_terms
                ],
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Outmerchant", "item": f"{ORIGIN}/"},
                    {"@type": "ListItem", "position": 2, "name": "Lexicon", "item": f"{ORIGIN}/lexicon/"},
                ],
            },
        ],
    }, indent=2)
    seen, items = set(), []
    for t in active_terms:
        if t["route"] in seen:
            continue
        seen.add(t["route"])
        if t["route"] == "/lexicon/outmerchant/":
            name, typ = "outmerchant / Outmerchant", "verb / noun"
            d = "The headword: the verb names the act of out-trading by ownership; the noun names the protected highest rank of the Sovereignty Score."
        else:
            name, typ, d = t["term"], t["type"], t["definition"]
        items.append(f'      <a href="{t["route"]}"><span class="t">{name}<em>{typ}</em></span><span class="d">{d}</span></a>')
    body = f"""    <p class="kicker">// The Lexicon — The Language of the Category</p>
    <h1>The Outmerchant Lexicon</h1>
    <p>Every strong category needs a dictionary. This is the canonical lexicon of <strong>Merchant Sovereignty</strong>: the governed vocabulary through which the condition is named, measured by <a href="/score/">the Sovereignty Score</a>, and protected under <a href="/protocol/">the Outmerchant Protocol</a>.</p>
    <p>Admission to this lexicon is governed by law, not by convenience: no term enters without a definition, a function inside the system, a relationship to other terms, and a place in the measurement. The lexicon a machine reads and the lexicon a human reads are the same lexicon — every definition below is published verbatim from the governed structured record.</p>
    <div class="term-list">
{chr(10).join(items)}
    </div>
    <div class="crosslinks">
      <a class="cta" href="/score/">→ Measure Your Sovereignty</a>
      <a class="cta-secondary" href="/protocol/">The Protocol</a>
    </div>"""
    return head(route, title, desc, jsonld) + \
        f"<main>\n  <div class=\"wrap\">\n{body}\n  </div>\n</main>\n" + FOOTER


def main():
    slug_route = {t["slug"]: t["route"] for t in terms}
    built = []
    out = ROOT / "lexicon" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_index(slug_route), encoding="utf-8")
    built.append("/lexicon/")
    out = ROOT / "lexicon" / "outmerchant" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_outmerchant_page(slug_route), encoding="utf-8")
    built.append("/lexicon/outmerchant/")
    for t in terms:
        if t["slug"] in ("outmerchant-verb", "outmerchant-noun") or t["route"] == "/score/":
            continue
        if t["status"] != "active":
            continue
        path = ROOT / t["route"].strip("/") / "index.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(build_term_page(t, slug_route), encoding="utf-8")
        built.append(t["route"])
    print(f"built {len(built)} lexicon pages:")
    for r in built:
        print(f"  {r}")


if __name__ == "__main__":
    main()
