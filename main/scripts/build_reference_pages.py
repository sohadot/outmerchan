"""Governed builder for the reference standard pages (Sprint 2C-1, DEC-013).

Generates the eight dimension pages and four level pages from the governed
model files (score_dimensions.json, score_levels.json, score_questions.json)
plus the editorial blocks below. Pages are regenerated, never hand-edited:
run `python3 main/scripts/build_reference_pages.py` after any governed
model change, then run the quality gate.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"
ORIGIN = "https://outmerchant.com"

dims = json.loads((DATA / "score_dimensions.json").read_text())["dimensions"]
levels = json.loads((DATA / "score_levels.json").read_text())["levels"]
questions = [q for q in json.loads((DATA / "score_questions.json").read_text())["questions"]
             if q["status"] == "active"]

# ---------------------------------------------------------------- editorial
DIM_CONTENT = {
    "DEP": {
        "slug": "platform-dependency",
        "meaning": "Platform Dependency measures how much of your trade is exposed to a single platform's unilateral decisions. One algorithm change, one policy update, one account suspension — the dimension asks how much of your commerce survives a decision you did not make and cannot appeal in time.",
        "why": "Dependency is where capture begins. A merchant whose revenue flows through one marketplace is not a business partner of that marketplace; they are a tenant. The platform sets the rent (fees), the visibility (ranking), and the right to exist (account status). Every other dimension of sovereignty is weakened when this one is weak, because the platform that controls your route to the buyer can override your decisions on all of them.",
        "low": "More than 80% of revenue through one platform. No sales channel that a third party cannot switch off. An account suspension means the business stops the same day. Channel strategy is whatever the platform's algorithm rewards this quarter.",
        "high": "No single channel carries more than a quarter of revenue. At least one owned channel — a property no third party can switch off — produces meaningful income. A suspension on any one platform is an inconvenience, not an extinction event.",
        "action": "Map your revenue by channel this week. If one platform carries more than half, open one channel that no third party can switch off — your own storefront on your own domain — and route real traffic to it before you need it.",
        "level": "/levels/captured/",
    },
    "OWN": {
        "slug": "customer-ownership",
        "meaning": "Customer Ownership measures who holds the relationship with your buyer: you, or the marketplace standing between you. It asks whether you can reach your customers directly, whether they could follow you if you left, and who keeps the master record of the data your own sales generate.",
        "why": "The route to the buyer is the most valuable asset a merchant does not own. A customer list inside a platform's database is not your customer list — it is the platform's asset, monetized back to you as advertising. Sovereignty over every other dimension matters little if, at the end of it, the buyer belongs to someone else's algorithm.",
        "low": "All buyer contact is mediated by the platform. Leaving the platform means starting from zero customers. The platform sees your full transaction history; you see what its dashboard chooses to show.",
        "high": "You can contact nearly all of your buyers directly, with consented contact data you store yourself. Most customers could follow you to a new venue. You hold the master record of your own commerce.",
        "action": "Start capturing consented, direct contact for every new buyer this month — even a simple owned mailing list. Measure what share of this month's customers you could reach without any platform's permission.",
        "level": "/levels/dependent/",
    },
    "REP": {
        "slug": "reputation-portability",
        "meaning": "Reputation Portability measures whether your reviews, ratings, and trading history are an asset you can carry — or a hostage held in a platform's proprietary database. It asks whether verifiable proof of your reliability exists anywhere a platform does not control.",
        "why": "Reputation is the merchant's accumulated trust capital, often built over years of flawless trade. When that capital is locked in one platform's system, it silently converts into the platform's strongest retention weapon: the merchant cannot leave without abandoning the very proof that they deserve to be trusted. Portable reputation reverses that lock.",
        "low": "Years of five-star history that evaporates the day the account closes. No independent record of fulfilled orders. Trust exists only where the platform displays it, in the format the platform allows.",
        "high": "Trading history archived and provable outside any single venue. Reviews and trust signals verifiable through independent services. A buyer — or an AI agent — can confirm your record without asking the platform's permission.",
        "action": "Export and archive your complete trading history and reviews from every platform you sell on — this quarter, and on a schedule. Then establish one independent, verifiable trust surface under your own control.",
        "level": "/levels/emerging/",
    },
    "PAY": {
        "slug": "payment-settlement-exposure",
        "meaning": "Payment & Settlement Exposure measures how many independent rails can move your money — and what happens when one of them refuses. It asks how many ways you can be paid, how you survive a payout freeze, and whether you can settle across borders without one intermediary's consent.",
        "why": "Settlement is the bloodstream of commerce, and a single blocked gateway is the fastest way an otherwise healthy merchant dies. Fee structures, payout schedules, reserve policies, and account freezes are all decisions made above the merchant's head when only one rail exists. Multi-rail settlement is what turns those decisions from existential threats into routing choices.",
        "low": "One payment provider processes everything. A payout freeze means a cash-flow crisis within days. Cross-border sales are impossible, or pass through a single intermediary whose terms are non-negotiable.",
        "high": "Three or more genuinely usable rails, including cross-border options. A frozen provider triggers a rerouting procedure, not an emergency. Settlement terms are compared and negotiated, because alternatives are real.",
        "action": "Add and fully test one independent payment rail this quarter — not as a backup in name, but processing a real share of volume so the switch is proven before it is needed.",
        "level": "/levels/dependent/",
    },
    "FEE": {
        "slug": "fee-margin-leakage",
        "meaning": "Fee & Margin Leakage measures how much of your gross margin funds the intermediaries on your route to the buyer: commissions, advertising, processing, fulfillment, returns, and the costs that never appear on one invoice. It asks whether you know your full route-to-buyer cost per sale — and whether that route is profitable at all.",
        "why": "A product can be profitable while its route to market is not. Leakage is the quiet form of capture: the merchant keeps operating, keeps selling, keeps growing volume — while the margin that should compound into their independence compounds into the infrastructure's revenue instead. Unmeasured leakage is not a cost; it is a transfer of ownership in slow motion.",
        "low": "More than half of gross margin goes to intermediaries. The full route-to-buyer cost has never been calculated. Fee increases are absorbed silently because no alternative route exists to compare against.",
        "high": "Intermediaries take less than a fifth of gross margin. Route-to-buyer cost is measured per sale and monitored continuously. Every fee on the route is a known, compared, and chosen cost.",
        "action": "Calculate your full route-to-buyer cost for one representative sale this week — every commission, ad cost, processing fee, fulfillment charge, and return allowance. Most merchants who do this for the first time find a number they cannot unsee.",
        "level": "/levels/captured/",
    },
    "XBR": {
        "slug": "cross-border-trust",
        "meaning": "Cross-Border Trust measures whether a buyer in another country — or another trade zone — can establish that you are trustworthy without a platform vouching for you. It asks whether your commerce can cross the borders of a fragmenting global market on its own credentials.",
        "why": "Global trade is fragmenting into zones: diverging regulations, regional payment systems, separated platform ecosystems. The merchant whose trustworthiness exists only inside one platform's borders inherits all of that platform's geopolitical limits. Independent, verifiable trust is what lets a merchant trade across fragments — non-aligned commerce in practice.",
        "low": "Trust signals exist only inside platforms. A foreign buyer who finds you outside a marketplace finds nothing checkable: no verifiable identity, no provable history, no published terms. Operating in a second trade zone is theoretical.",
        "high": "Identity, terms, and trading history are published and independently verifiable. Buyers in other zones can check you without an intermediary. Operations are structurally multi-zone, not single-market with aspirations.",
        "action": "Publish one independent, checkable trust page under your own domain: verified business identity, complete commercial terms, and provable trading history. Make it the page a cautious foreign buyer would need.",
        "level": "/levels/emerging/",
    },
    "AGT": {
        "slug": "ai-commerce-readiness",
        "meaning": "AI Commerce Readiness measures whether an AI buying agent can find, parse, and trust your commerce. It asks whether your catalog is machine-readable, whether your terms are structured, and whether your identity and trust signals can be verified by software that has no patience for prose.",
        "why": "AI is becoming a control layer in discovery, comparison, trust, and purchase routing. Merchants will increasingly be found, evaluated, and selected by agents acting for buyers. The merchant who is not machine-legible is invisible to that demand layer; the merchant who is legible only through one platform's feed has traded the old capture for a newer one. The goal is to be an agent-selectable merchant — legible and selectable by AI without surrendering sovereignty to AI-controlled market access.",
        "low": "No structured catalog data outside a platform's proprietary system. Terms exist as prose, if at all. An AI agent asked to verify this merchant finds nothing it can check.",
        "high": "Catalog fully structured and openly accessible. Pricing, shipping, and returns published in machine-readable form. Identity and trust signals structured and independently verifiable — the merchant is selectable by an agent on the merchant's own credentials.",
        "action": "Add structured data to your products and commercial terms on your own domain — start with standard schema.org markup for products, offers, and your organization. Make yourself the merchant an agent can verify.",
        "level": "/levels/emerging/",
    },
    "GOV": {
        "slug": "governance-independence",
        "meaning": "Governance Independence measures who writes the rules of your commerce: you, or a terms-of-service document that changes without your consent. It asks how many parties can rewrite your operating conditions unilaterally — and whether you hold a documented exit path from each of them.",
        "why": "This is the deepest dimension, because it governs all the others. A merchant can diversify channels, own customer data, and run multiple rails — and still operate entirely inside rule systems that others rewrite at will. Sovereignty's final test is not whether you can operate today, but whether you decide the terms on which you operate tomorrow. Every layer should serve the merchant; this dimension measures whether any layer owns him.",
        "low": "Several providers can change fees, policies, or access at any time, with no notice and no negotiation. Dependencies have never been mapped. There is no exit plan from anything.",
        "high": "Terms are set or genuinely negotiated by the merchant. Critical dependencies are mapped. A documented, tested exit path exists for every provider whose failure or hostility could stop the business.",
        "action": "List every provider whose decision could stop your business, and write a one-page exit path for the most critical one this month. An exit you have documented is leverage; an exit you have tested is sovereignty.",
        "level": "/levels/outmerchant/",
    },
}

LEVEL_CONTENT = {
    "Captured": {
        "slug": "captured",
        "meaning": "Captured is the lowest tier of the Merchant Sovereignty Score. It names the condition in which the infrastructure owns the merchant: the platform holds the margin, the reputation, the customer relationship, and the route to the buyer. The merchant operates — but only at the infrastructure's pleasure. The standard's lexicon calls the mechanism platform capture: the end-state of unmanaged platform dependency.",
        "who": "Typically: marketplace-only sellers, social-commerce sellers whose entire funnel lives inside one app, and merchants whose storefront, payments, fulfillment, and customer contact all run through a single provider stack. Often successful in volume — capture is a control condition, not a revenue condition. Many captured merchants are profitable right up until the decision that ends them.",
        "pattern": "One dominant channel. One payment rail. Buyer contact mediated entirely by the platform. Reputation hostage to one database. Route-to-buyer costs unmeasured. No exit paths. Rules rewritten above the merchant's head, absorbed silently.",
        "path": "Movement out of Captured starts with the two dimensions that loosen the platform's grip fastest: Platform Dependency and Customer Ownership. Open one channel no third party can switch off, and start holding consented, direct buyer contact. Re-measure. The path runs through Dependent and Emerging — and its terminal state is the rank that carries the standard's name: OutMerchant.",
    },
    "Dependent": {
        "slug": "dependent",
        "meaning": "Dependent is the second tier of the Merchant Sovereignty Score. The merchant is partially free: they operate real channels of their own, but on borrowed infrastructure — platform-dominated revenue, single-rail settlement, and trust that still lives mostly in other people's databases. The cage door is open, but the merchant still sleeps inside.",
        "who": "Typically: merchants with their own storefront whose revenue is still dominated by one marketplace; DTC brands that own their site but depend on one payment provider and one ad platform for nearly all discovery; sellers who hold some customer data but could not survive their primary channel's hostility.",
        "pattern": "Owned channel exists but is secondary. One settlement rail carries everything. A meaningful minority of customers are directly reachable; the majority are not. Reputation partially archived, not independently verifiable. Exit paths known but undocumented.",
        "path": "Movement out of Dependent is about converting partial ownership into structural ownership: make the owned channel carry real revenue, add and test a second independent settlement rail, and make reputation portable and provable. Re-measure quarterly. The destination of the path is the protected highest rank — OutMerchant.",
    },
    "Emerging": {
        "slug": "emerging",
        "meaning": "Emerging is the third tier of the Merchant Sovereignty Score. The merchant sees the cage and is building the exit: channels diversified, direct customer relationships growing, settlement optionality real. What remains are the deeper layers — portable verifiable reputation, machine-readable trust, and governance independence — the dimensions that separate operating freely from ruling your own commerce.",
        "who": "Typically: established DTC brands with diversified acquisition; merchants running genuinely multi-channel operations with meaningful owned revenue; operators who have consciously begun treating sovereignty as a strategy rather than an accident of growth.",
        "pattern": "No single channel above a quarter to a third of revenue. Direct contact with a substantial share of buyers. Two or more usable settlement rails. The remaining gaps are characteristic: reputation not yet independently verifiable, catalog and terms not yet machine-readable, exit paths not yet documented and tested.",
        "path": "The path from Emerging runs through the standard's most forward-looking dimensions: make your trust machine-readable and independently verifiable, become an agent-selectable merchant, and document a tested exit path for every critical provider. The remaining distance is governance, not operations. At its end stands the terminal rank: OutMerchant.",
    },
    "OutMerchant": {
        "slug": "outmerchant",
        "meaning": "OutMerchant is the highest tier of the Merchant Sovereignty Score — and it is a protected rank, not a brand name used decoratively. Under the standard's public governance, the terminal tier permanently carries the name OutMerchant (decisions DEC-001 and DEC-006), and an automated quality gate rejects any change to its name or boundaries. The rank defines the standard's terminal state: a merchant who owns their channels, customers, reputation, settlement options, margin, and the rules of their own commerce. To complete the standard is to become an OutMerchant — the noun is the destination of the verb.",
        "who": "Merchants who have made sovereignty structural: no single point of control can terminate or capture their trade. Their commerce is legible to buyers, to other markets, and to AI agents — on their own credentials, without any platform vouching for them. They use infrastructure everywhere and are owned by it nowhere.",
        "pattern": "All eight dimensions in high control: distributed channels with owned primary revenue; direct consented customer relationships; independently verifiable portable reputation; multi-rail settlement including cross-border; measured and minimized route-to-buyer leakage; structured machine-readable catalog, terms, and trust; documented, tested exit paths from every critical provider. Every layer serves the merchant. No layer owns the merchant.",
        "path": "The movement at this tier is holding the rank. Sovereignty decays silently — a channel quietly grows past its share, a rail consolidates, a new dependency arrives inside a convenient tool. Re-measure on a schedule, re-test exit paths annually, and treat every new provider as a governance decision before it becomes a dependency.",
    },
}

# ---------------------------------------------------------------- template
STYLE = """
  :root {
    --void:#020408; --deep:#050d15; --grid:#0a1628;
    --signal:#00d4ff; --signal-dim:rgba(0,212,255,0.08); --signal-mid:rgba(0,212,255,0.3);
    --gold:#c8a96e; --danger:#ff3d3d;
    --text:#e8f0f8; --text-dim:rgba(232,240,248,0.55); --text-ghost:rgba(232,240,248,0.12);
    --mono:'Space Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
    --display:'Syne', system-ui, sans-serif;
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--void); color:var(--text); font-family:var(--mono); line-height:1.8; }
  a { color:var(--signal); }
  .wrap { max-width:820px; margin:0 auto; padding:0 24px; }
  header { border-bottom:1px solid var(--text-ghost); padding:20px 0; }
  header .wrap { display:flex; justify-content:space-between; align-items:center; }
  .logo { font-family:var(--display); font-weight:800; font-size:16px; letter-spacing:0.3em; text-transform:uppercase; color:var(--text); text-decoration:none; }
  .logo span { color:var(--signal); }
  .header-tag { font-size:10px; letter-spacing:0.2em; color:var(--text-dim); text-transform:uppercase; }
  main { padding:56px 0 96px; }
  .kicker { font-size:10px; letter-spacing:0.4em; color:var(--signal); text-transform:uppercase; margin-bottom:16px; }
  h1 { font-family:var(--display); font-weight:800; font-size:clamp(28px,5vw,44px); line-height:1.15; margin-bottom:20px; }
  h2 { font-family:var(--display); font-weight:700; font-size:18px; margin:40px 0 12px; letter-spacing:0.03em; }
  p { font-size:13px; color:var(--text-dim); margin-bottom:14px; max-width:680px; }
  p strong { color:var(--text); font-weight:400; }
  .compare { display:grid; grid-template-columns:1fr 1fr; gap:2px; margin:20px 0; }
  .compare > div { border:1px solid var(--text-ghost); padding:20px; background:var(--deep); }
  .compare h3 { font-family:var(--display); font-size:13px; margin-bottom:10px; }
  .compare .low h3 { color:var(--danger); }
  .compare .high h3 { color:var(--signal); }
  .compare p { font-size:12px; margin:0; }
  ul.qs { list-style:none; margin:16px 0; }
  ul.qs li { border-left:1px solid var(--signal-mid); padding:8px 16px; margin-bottom:8px; font-size:12px; color:var(--text-dim); }
  .action { border-left:1px solid var(--gold); background:rgba(200,169,110,0.06); padding:18px 22px; margin:20px 0; }
  .action p { margin:0; font-size:13px; }
  .action .label { color:var(--gold); font-size:10px; letter-spacing:0.3em; text-transform:uppercase; display:block; margin-bottom:8px; }
  .range { font-family:var(--display); font-weight:800; font-size:40px; color:var(--signal); margin:8px 0 24px; }
  .crosslinks { border-top:1px solid var(--text-ghost); margin-top:48px; padding-top:24px; }
  .crosslinks p { font-size:12px; }
  .cta { display:inline-block; background:var(--signal); color:var(--void); font-weight:700; font-size:11px; letter-spacing:0.2em; text-transform:uppercase; padding:14px 32px; text-decoration:none; margin:8px 16px 8px 0; }
  .cta-secondary { display:inline-block; border:1px solid var(--text-ghost); color:var(--text); font-size:11px; letter-spacing:0.2em; text-transform:uppercase; padding:14px 32px; text-decoration:none; margin:8px 16px 8px 0; }
  .cta-secondary:hover { border-color:var(--signal-mid); color:var(--signal); }
  footer { border-top:1px solid var(--text-ghost); padding:32px 0; font-size:10px; color:var(--text-dim); letter-spacing:0.15em; }
  footer .wrap { display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px; }
  @media (max-width:640px) { .compare { grid-template-columns:1fr; } }
"""


def page(route, title, description, kicker, h1, body, breadcrumb_name):
    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": f"{ORIGIN}{route}#article",
                "headline": h1,
                "description": description,
                "url": f"{ORIGIN}{route}",
                "isPartOf": {"@id": f"{ORIGIN}/#website"},
                "publisher": {"@id": f"{ORIGIN}/#organization"},
                "about": {"@id": f"{ORIGIN}/#term-sovereignty-score"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "OutMerchant", "item": f"{ORIGIN}/"},
                    {"@type": "ListItem", "position": 2, "name": "Merchant Sovereignty Score", "item": f"{ORIGIN}/score/"},
                    {"@type": "ListItem", "position": 3, "name": breadcrumb_name, "item": f"{ORIGIN}{route}"},
                ],
            },
        ],
    }, indent=2)
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
<meta property="og:site_name" content="OutMerchant">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<script type="application/ld+json">
{jsonld}
</script>
<style>{STYLE}</style>
</head>
<body>
<header>
  <div class="wrap">
    <a class="logo" href="/">OUT<span>MERCHANT</span></a>
    <div class="header-tag">The Merchant Sovereignty Standard</div>
  </div>
</header>
<main>
  <div class="wrap">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
{body}
  </div>
</main>
<footer>
  <div class="wrap">
    <div>MERCHANT SOVEREIGNTY SCORE — REFERENCE STANDARD</div>
    <div><a href="/">OUTMERCHANT.COM</a> — EVERY LAYER SERVES THE MERCHANT. NO LAYER OWNS THE MERCHANT.</div>
  </div>
</footer>
</body>
</html>
"""


def build_dimension(dim):
    c = DIM_CONTENT[dim["code"]]
    qs = [q for q in questions if q["dimension"] == dim["code"]]
    q_items = "\n".join(f"      <li>{q['text']}</li>" for q in qs)
    route = dim["route"]
    title = f"{dim['name']} — Dimension {dim['order']:02d} of the Merchant Sovereignty Score | OutMerchant"
    desc = (f"{dim['name']} is dimension {dim['order']:02d} ({dim['code']}) of the Merchant Sovereignty Score: "
            f"{dim['question']} What it means, why it matters to merchant sovereignty, and what low and high control look like.")
    level_name = next(l["name"] for l in levels if l["route"] == c["level"])
    body = f"""    <h2>What This Dimension Means</h2>
    <p>{c['meaning']}</p>
    <h2>Why It Matters to Merchant Sovereignty</h2>
    <p>{c['why']}</p>
    <h2>How the Score Measures It</h2>
    <p>The Merchant Sovereignty Score assesses this dimension through {len(qs)} governed questions, weighted at {dim['weight']:g}% of the total score. The questions are fixed under public score governance — they change only through a recorded decision, never silently:</p>
    <ul class="qs">
{q_items}
    </ul>
    <p>Each answer is scored from captured behavior (0 points) to sovereign behavior (maximum points). The dimension score is the share of sovereign points earned, from 0 to 100.</p>
    <h2>Low Control vs. High Control</h2>
    <div class="compare">
      <div class="low"><h3>What low control looks like</h3><p>{c['low']}</p></div>
      <div class="high"><h3>What high control looks like</h3><p>{c['high']}</p></div>
    </div>
    <div class="action">
      <span class="label">One Next Action</span>
      <p>{c['action']}</p>
    </div>
    <div class="crosslinks">
      <p>Persistent low control on this dimension is characteristic of the <a href="{c['level']}">{level_name}</a> tier. High control across all eight dimensions defines the standard's protected highest rank: <a href="/levels/outmerchant/">OutMerchant</a>.</p>
      <a class="cta" href="/score/">→ Measure This Dimension</a>
      <a class="cta-secondary" href="/">The Standard</a>
    </div>"""
    kicker = f"// Dimension {dim['order']:02d} / {dim['code']} — {dim['weight']:g}% of the score"
    return route, page(route, title, desc, kicker, dim["name"], body, dim["name"])


def build_level(lvl):
    c = LEVEL_CONTENT[lvl["name"]]
    route = lvl["route"]
    title = f"{lvl['name']} ({lvl['min']}–{lvl['max']}) — Merchant Sovereignty Score Tier | OutMerchant"
    desc = (f"{lvl['name']} is the Merchant Sovereignty Score tier covering {lvl['min']}–{lvl['max']}: "
            f"{lvl['meaning']}")
    is_terminal = lvl["name"] == "OutMerchant"
    path_links = "" if is_terminal else (
        f"""      <p>The terminal state of this path carries the standard's name — the protected highest rank: <a href="/levels/outmerchant/">OutMerchant</a>.</p>\n""")
    terminal_note = ""
    if is_terminal:
        terminal_note = """    <h2>A Protected Rank, Not a Brand Label</h2>
    <p><strong>OutMerchant is the standard's terminal classification.</strong> The tier's name and boundaries (76–100) are inviolable under public score governance: they are fixed by recorded decisions (DEC-001, DEC-006) and protected by an automated quality gate that rejects any change. This closure is deliberate — the framework cannot be used without its highest tier being the destination, and the destination permanently carries the standard's name. <em>to outmerchant</em> is the verb; <em>an OutMerchant</em> is the rank at the end of it.</p>
"""
    body = f"""    <div class="range">{lvl['min']} — {lvl['max']}</div>
    <h2>What This Level Means</h2>
    <p>{c['meaning']}</p>
{terminal_note}    <h2>Who Falls Into This Tier</h2>
    <p>{c['who']}</p>
    <h2>The Common Control Pattern</h2>
    <p>{c['pattern']}</p>
    <h2>{'Holding the Rank' if is_terminal else 'The Path Toward OutMerchant'}</h2>
    <p>{c['path']}</p>
    <div class="crosslinks">
{path_links}      <a class="cta" href="/score/">→ Measure Your Tier</a>
      <a class="cta-secondary" href="/levels/outmerchant/">The OutMerchant Rank</a>
    </div>"""
    kicker = f"// Tier {lvl['order']} of 4 — Merchant Sovereignty Score"
    return route, page(route, title, desc, kicker,
                       f"{lvl['name']}: Sovereignty Tier {lvl['min']}–{lvl['max']}", body, lvl["name"])


def main():
    built = []
    for dim in sorted(dims, key=lambda d: d["order"]):
        route, html = build_dimension(dim)
        out = ROOT / route.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        built.append(route)
    for lvl in sorted(levels, key=lambda l: l["order"]):
        route, html = build_level(lvl)
        out = ROOT / route.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        built.append(route)
    print(f"built {len(built)} reference pages:")
    for r in built:
        print(f"  {r}")


if __name__ == "__main__":
    main()
