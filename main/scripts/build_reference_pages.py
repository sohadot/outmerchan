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
glossary = json.loads((DATA / "glossary_terms.json").read_text())["terms"]
TERM_BY_SLUG = {t["slug"]: t for t in glossary}

# ---------------------------------------------------------------- editorial
DIM_CONTENT = {
    "DEP": {
        "slug": "platform-dependency",
        "meaning": "Platform Dependency measures how much of your trade is exposed to a single platform’s unilateral decisions. One algorithm change, one policy update, one account suspension — the dimension asks how much of your commerce survives a decision you did not make and cannot appeal in time.",
        "why": "Dependency is where capture begins. A merchant whose revenue flows through one marketplace is not a business partner of that marketplace; they are a tenant. The platform sets the rent (fees), the visibility (ranking), and the right to exist (account status). Every other dimension of sovereignty is weakened when this one is weak, because the platform that controls your route to the buyer can override your decisions downstream.",
        "what": "We measure dependency across three axes: revenue concentration (what share of gross revenue requires the platform to function), route exclusivity (whether buyers can find you without the platform), and exit cost (how much revenue would be lost in the first 90 days if the platform were removed). The score aggregates these into a single 0–100 signal."
    },
    "ROT": {
        "slug": "route-to-buyer-control",
        "meaning": "Route-to-Buyer Control measures how directly you can reach the buyers who want what you sell — without the platform deciding whether, when, and at what cost that connection is made.",
        "why": "The route to the buyer is the most contested asset in digital commerce. Platforms are not neutral pipes; they are route controllers. They decide which merchants appear in which searches, which listings get promoted, and which buyers see which offers. A merchant without a direct route is a merchant whose existence depends on the platform’s commercial interest in surfacing them.",
        "what": "We measure route control across three axes: direct traffic share (what fraction of sessions arrives without platform mediation), owned contact reach (what fraction of past buyers can be reached without platform permission), and demand generation independence (whether the merchant can run campaigns that do not depend on a platform’s ad auction)."
    },
    "REP": {
        "slug": "portable-reputation",
        "meaning": "Portable Reputation measures how much of the trust you have earned with buyers travels with you if you leave a platform, rather than staying behind as the platform’s asset.",
        "why": "Reputation is the durable output of good commerce. But most platform reputation is platform-owned: a five-star rating on a marketplace belongs to the marketplace, not the merchant. If the account closes, the reviews disappear. A merchant with only platform-resident reputation must start from zero on every new channel — and is therefore unable to leave without a credibility cost that functions as a lock-in mechanism.",
        "what": "We measure portability across three axes: review exportability (whether ratings can be referenced outside the platform), brand search volume (whether buyers search for the merchant by name, not just by category), and testimonial ownership (whether the merchant controls a body of verifiable social proof that survives channel changes)."
    },
    "OPS": {
        "slug": "operational-independence",
        "meaning": "Operational Independence measures how much of your core commerce infrastructure — payments, fulfilment, inventory, customer service — you operate without requiring a specific platform to function.",
        "why": "Operations are the plumbing of commerce. When the plumbing is owned by a platform, the platform controls the water. A merchant who cannot process a payment, ship an order, or respond to a customer without a specific platform’s infrastructure is operationally captive, regardless of how independent their brand feels. Operational independence is not about avoiding all third-party services; it is about ensuring that no single platform’s removal stops the business from functioning.",
        "what": "We measure operational independence across three axes: payment infrastructure (whether payment processing can continue without the platform), fulfilment control (whether orders can be picked, packed, and shipped without platform logistics), and service continuity (whether customer communication and issue resolution can operate independently)."
    },
    "DAT": {
        "slug": "data-ownership",
        "meaning": "Data Ownership measures how much of the commercial intelligence your business generates — buyer behaviour, demand signals, conversion patterns — you actually possess, rather than it residing only inside a platform’s closed system.",
        "why": "Data is the compounding asset of digital commerce. Every transaction generates signal: who bought, what triggered the decision, what was abandoned, what was returned. Platforms capture this signal and use it to improve their own systems, inform their own private-label decisions, and sell it back to merchants as advertising. A merchant who cannot access their own transaction-level data is operating blind — and subsidising the intelligence of their landlord.",
        "what": "We measure data ownership across three axes: transaction-level access (whether the merchant can export and analyse individual order records), buyer identity ownership (whether the merchant knows who their buyers are, not just that a sale occurred), and behavioural signal access (whether browse, search, and abandonment data is available to the merchant for their own modelling)."
    },
    "FIN": {
        "slug": "financial-independence",
        "meaning": "Financial Independence measures how exposed your cash flow and unit economics are to unilateral changes in platform fees, reserve policies, and payout timing.",
        "why": "Platforms monetise through the merchant’s cash. Fee increases, reserve requirements, and delayed payouts are mechanisms by which platforms extract value without renegotiation. A merchant whose margins are calculated after platform fees, whose cash is held in platform reserves, and whose payout schedule is set by the platform is financially dependent in a way that has direct operational consequences — particularly for inventory-funded businesses.",
        "what": "We measure financial independence across three axes: fee concentration (what share of gross margin is consumed by a single platform’s fees), reserve exposure (what share of receivables is held in platform-controlled escrow), and payout predictability (whether cash can be forecast and controlled independently of platform timing decisions)."
    },
    "GOV": {
        "slug": "governance-independence",
        "meaning": "Governance Independence measures how exposed your ability to trade is to a single platform’s policy decisions, content moderation choices, and account enforcement actions.",
        "why": "Governance risk is the risk of arbitrary exclusion. Platforms are private actors. They can change policies without notice, enforce rules inconsistently, and suspend accounts without meaningful appeal. A merchant whose primary trading channel can be closed by a platform’s unilateral decision faces a form of dependency that no amount of operational or financial independence can fully offset. Governance independence measures how much of your commerce survives a platform decision you did not consent to and cannot reverse.",
        "what": "We measure governance independence across three axes: channel redundancy (whether trade can continue if one platform suspends the account), policy exposure (how many of the merchant’s practices are subject to platform policy rather than law), and appeal capacity (whether the merchant has meaningful recourse when a platform decision is made in error)."
    },
    "AGT": {
        "slug": "agentic-readiness",
        "meaning": "Agentic Readiness measures how prepared a merchant is to be discovered, evaluated, and transacted with by AI agents acting on behalf of buyers — without a human in the loop for each decision.",
        "why": "The next phase of commerce is not search-mediated; it is agent-mediated. Buyers are deploying AI agents to research purchases, evaluate suppliers, compare terms, and execute transactions. A merchant who is not legible to an agent — whose policies are buried in PDFs, whose inventory is not machine-readable, whose trust signals require human interpretation — will be systematically excluded from agent-mediated purchasing flows, regardless of product quality.",
        "what": "We measure agentic readiness across three axes: machine-readable trust (whether the merchant exposes structured, verifiable signals that agents can parse without human mediation), policy legibility (whether terms, returns, and guarantees are available in structured form), and transaction completability (whether an agent can complete a purchase without requiring human handoff)."
    }
}

LEVEL_CONTENT = {
    "captured": {
        "what_it_means": "Captured merchants are commercially operational but structurally exposed. Revenue flows, but the conditions of that flow are set by platforms, not by the merchant. The business functions inside a system it does not control and could not replicate if the platform withdrew access.",
        "why_it_matters": "Capture is not a temporary state for new merchants; it is the default equilibrium of platform commerce. Platforms are designed to make capture self-reinforcing: the longer a merchant trades within a platform’s system, the more their reputation, data, and buyer relationships become platform-resident rather than merchant-owned. Capture is stable until the platform changes the terms — at which point the merchant has no leverage.",
        "what_moves_you": "The primary exit from Capture is channel diversification backed by owned buyer contact. A merchant who can reach 30% of past buyers directly, processes payment independently, and has a non-platform traffic source has begun to build the operational floor that makes the next level achievable. Most merchants leave Capture through a crisis — a suspension, a fee increase, an algorithm change — rather than by design."
    },
    "dependent": {
        "what_it_means": "Dependent merchants have begun to build alternatives but remain structurally reliant on platforms for the majority of revenue, discovery, and operational function. They have a direct channel but it is not yet self-sustaining; they have buyer data but have not operationalised it; they have diversified but the primary platform remains dominant.",
        "why_it_matters": "Dependence is the most common operating state for merchants with 2–5 years of digital commerce experience. They have learned the risks of capture and have begun to hedge, but the hedges are partial. A platform withdrawal would be damaging rather than terminal, but still damaging enough to threaten business continuity. The key risk at this level is complacency: having done enough to feel safer without having done enough to actually be safe.",
        "what_moves_you": "The transition from Dependent to Resilient requires operationalising the assets the merchant already holds. Direct channel revenue needs to exceed 40% of gross. Owned contact reach needs to cover a majority of active buyers. Operational infrastructure needs to be tested without the primary platform. Most merchants at this level have the components of resilience; they have not yet integrated them."
    },
    "resilient": {
        "what_it_means": "Resilient merchants have achieved genuine structural diversification. No single platform controls more than 50% of revenue. Buyers can be reached, orders can be fulfilled, and payments can be processed without any specific platform’s participation. The business would be disrupted by a major platform withdrawal but would not be destroyed by it.",
        "why_it_matters": "Resilience is the threshold at which platform relationships become commercial negotiations rather than dependencies. A resilient merchant can respond to a fee increase by reducing volume on that platform. They can respond to a policy change by accelerating their direct channel. The platform’s leverage over the merchant is bounded by the merchant’s alternatives. Resilience does not mean platform-free; it means platform-optional.",
        "what_moves_you": "The transition from Resilient to Sovereign requires converting operational independence into commercial intelligence and forward positioning. Data needs to be owned and used for decisions. Reputation needs to be portable across channels. Governance exposure needs to be understood and managed. And for merchants who intend to remain competitive through the agentic transition, machine-readable trust infrastructure needs to be in place."
    },
    "sovereign": {
        "what_it_means": "Sovereign merchants have achieved full structural independence across all eight dimensions. They use platforms as distribution channels rather than existing within them as tenants. Platform relationships are managed as commercial decisions, not as existential constraints. The merchant controls their route to the buyer, owns their commercial data, holds portable reputation, and has begun to build the infrastructure required for agent-mediated commerce.",
        "why_it_matters": "Sovereignty is not the end state; it is the operating position from which the next phase of commerce can be navigated from strength rather than from exposure. The agentic transition will restructure discovery, evaluation, and transaction in ways that are not yet fully predictable. A sovereign merchant has the structural position to participate in that transition on their own terms. A captured merchant will find that the new intermediaries — the AI agents and the platforms that train them — replicate the same dependency dynamics as the platforms that preceded them.",
        "what_moves_you": "Sovereignty is not permanent. Platform landscapes change, new intermediaries emerge, and the conditions that define independence in one period may not be the conditions that define it in the next. Maintaining sovereignty requires ongoing attention to agentic readiness, data infrastructure, and the portability of trust signals as commerce shifts toward machine-mediated discovery and transaction."
    }
}


# ---------------------------------------------------------------- helpers
def nav_html(active: str = "") -> str:
    links = [
        ("/", "Home"),
        ("/score/", "Score"),
        ("/reference/", "Reference"),
        ("/lexicon/", "Lexicon"),
    ]
    items = []
    for href, label in links:
        cls = ' class="active"' if label == active else ""
        items.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    return "<ul>" + "".join(items) + "</ul>"


def footer_html() -> str:
    return (
        '<footer>'
        '<p>© 2025 OutMerchant. Built for merchants who intend to remain independent.</p>'
        '</footer>'
    )


def glossary_link(text: str, slug: str) -> str:
    return f'<a href="/lexicon/{slug}/" class="glossary-ref">{text}</a>'


def render_questions(dim_code: str) -> str:
    qs = [q for q in questions if q["dimension"] == dim_code]
    if not qs:
        return ""
    rows = []
    for q in qs:
        rows.append(
            f"<tr><td>{q['text']}</td>"
            f"<td>{q['weight']}</td>"
            f"<td>{q.get('rationale', '')}</td></tr>"
        )
    return (
        "<h2>Scoring questions</h2>"
        "<table><thead><tr>"
        "<th>Question</th><th>Weight</th><th>Rationale</th>"
        "</tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table>"
    )


def dim_page(d: dict) -> str:
    code = d["code"]
    ed = DIM_CONTENT.get(code, {})
    slug = ed.get("slug", code.lower())
    title = d["name"]
    meaning = ed.get("meaning", "")
    why = ed.get("why", "")
    what = ed.get("what", "")
    questions_html = render_questions(code)
    canonical = f"{ORIGIN}/reference/{slug}/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — OutMerchant Reference</title>
<meta name="description" content="{meaning[:155]}">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<header>
<a href="/" class="logo">OutMerchant</a>
<nav>{nav_html('Reference')}</nav>
</header>
<main>
<article class="reference-page">
<h1>{title}</h1>
<p class="dimension-code">Dimension code: <strong>{code}</strong></p>
<section>
<h2>What this dimension measures</h2>
<p>{meaning}</p>
</section>
<section>
<h2>Why it matters</h2>
<p>{why}</p>
</section>
<section>
<h2>How we measure it</h2>
<p>{what}</p>
</section>
{questions_html}
</article>
</main>
{footer_html()}
</body>
</html>"""


def level_page(lv: dict) -> str:
    key = lv["key"]
    ed = LEVEL_CONTENT.get(key, {})
    title = lv["label"]
    band = lv["band"]
    description = lv.get("description", "")
    what_it_means = ed.get("what_it_means", "")
    why_it_matters = ed.get("why_it_matters", "")
    what_moves_you = ed.get("what_moves_you", "")
    canonical = f"{ORIGIN}/reference/{key}/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — OutMerchant Reference</title>
<meta name="description" content="{description[:155]}">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<header>
<a href="/" class="logo">OutMerchant</a>
<nav>{nav_html('Reference')}</nav>
</header>
<main>
<article class="reference-page">
<h1>{title}</h1>
<p class="score-band">Score band: <strong>{band}</strong></p>
<section>
<h2>What it means</h2>
<p>{what_it_means}</p>
</section>
<section>
<h2>Why it matters</h2>
<p>{why_it_matters}</p>
</section>
<section>
<h2>What moves you to the next level</h2>
<p>{what_moves_you}</p>
</section>
</article>
</main>
{footer_html()}
</body>
</html>"""


# ---------------------------------------------------------------- write
OUT = ROOT / "reference"

for d in dims:
    ed = DIM_CONTENT.get(d["code"], {})
    slug = ed.get("slug", d["code"].lower())
    dest = OUT / slug / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(dim_page(d), encoding="utf-8")
    print(f"  wrote {dest.relative_to(ROOT)}")

for lv in levels:
    dest = OUT / lv["key"] / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(level_page(lv), encoding="utf-8")
    print(f"  wrote {dest.relative_to(ROOT)}")

print("build_reference_pages: done")
