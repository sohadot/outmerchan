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
        "why": "Dependency is where capture begins. A merchant whose revenue flows through one marketplace is not a business partner of that marketplace; they are a tenant. The platform sets the rent (fees), the visibility (ranking), and the right to exist (account status). Every other dimension of sovereignty is weakened when this one is weak, because the platform that controls your route to the buyer can override your decision-making in every other area.",
        "signals_intro": "Low scores appear as: a single channel accounting for the majority of revenue; no direct relationship with buyers; reliance on platform fulfilment or logistics with no alternative; catalogue and content locked inside the platform’s proprietary format.",
        "improvement_intro": "Every improvement on this dimension reduces the blast radius of a platform decision. Begin by mapping the single highest-concentration exposure — usually a channel that accounts for more than 40 % of revenue — and opening one alternative route to the same buyer segment. Diversification is not the goal; reducing single-point-of-failure risk is."
    },
    "CAP": {
        "slug": "platform-capture",
        "meaning": "Platform Capture measures whether your pricing, discounting, and promotional decisions are yours to make — or whether they are made for you by platform policy, algorithmic pressure, or contractual obligation.",
        "why": "Pricing is the most direct expression of commercial judgment. A merchant who cannot set a price without platform approval, who is penalised algorithmically for offering a lower price elsewhere, or who is required to participate in platform-defined sale events has surrendered the most fundamental lever of trade. Capture here bleeds into every margin calculation and long-term brand position.",
        "signals_intro": "Low scores appear as: price-parity clauses that prevent lower pricing on other channels; mandatory participation in platform discount events; algorithmic demotion for refusing promotional programmes; inability to set or test prices without platform permission.",
        "improvement_intro": "Audit every pricing constraint currently imposed by platform agreements. Identify which constraints are contractual (enforceable), which are algorithmic (soft enforcement through visibility penalties), and which are assumed but not written. Contractual constraints require renegotiation or exit; algorithmic constraints require testing to understand actual enforcement."
    },
    "RTC": {
        "slug": "route-to-buyer-control",
        "meaning": "Route-to-Buyer Control measures whether you own the path between your products and your buyers, or whether that path is licensed from a platform that can revoke, restrict, or reprice it.",
        "why": "A merchant without a direct route to the buyer is entirely dependent on the platform’s continued willingness to show their products. Ownership of a direct channel — email list, direct site, community — is not about bypassing platforms; it is about ensuring that platform decisions do not sever the merchant-buyer relationship entirely.",
        "signals_intro": "Low scores appear as: no direct buyer contact information; all discovery mediated by platform search and recommendation; no ability to communicate with past buyers outside the platform; no owned digital presence that can transact independently.",
        "improvement_intro": "The first objective is to establish at least one owned contact point with buyers — an email address, a direct subscriber, a contactable customer record. Even a small owned list changes the risk profile of platform dependency. The second objective is to ensure that owned presence can transact: a storefront, a booking system, a direct payment method."
    },
    "REP": {
        "slug": "portable-reputation",
        "meaning": "Portable Reputation measures whether the trust and credibility you have built with buyers exists in a form you can carry with you — or whether it is trapped inside a platform’s proprietary review and rating system.",
        "why": "Reputation is commercial capital. A merchant with five thousand reviews on a single platform has built that capital entirely on rented land. If the account is suspended, if the platform changes its review display algorithm, or if the merchant moves channels, that capital is gone. Portable reputation is reputation that survives platform transitions.",
        "signals_intro": "Low scores appear as: all reviews and ratings held by the platform with no export mechanism; no independent review presence; testimonials and social proof locked inside platform profiles; no mechanism for buyers to verify reputation outside the platform.",
        "improvement_intro": "Begin with systematic capture of buyer feedback through owned channels: post-purchase email sequences that direct buyers to independent review platforms, direct testimonial collection, case studies published on owned properties. The goal is not to abandon platform reviews but to ensure that reputation evidence exists in at least one portable form."
    },
    "AI": {
        "slug": "ai-merchant-sovereignty",
        "meaning": "AI Merchant Sovereignty measures how well your business is positioned to trade with and through AI agents — and to maintain control of your commercial identity as AI-mediated commerce becomes a primary buyer behaviour.",
        "why": "AI agents are becoming buyers, curators, and intermediaries. A merchant whose product data is incomplete, whose commercial terms are not machine-readable, and whose brand identity is not legible to AI systems is already invisible in the channel that is growing fastest. Sovereignty here means your products are findable, your terms are interpretable, and your identity is not defined by what a platform’s AI has inferred about you.",
        "signals_intro": "Low scores appear as: product data in formats that AI agents cannot parse; commercial terms not expressed as structured data; no mechanism for AI agents to verify merchant identity or authority; brand and product descriptions that exist only on platform-controlled pages.",
        "improvement_intro": "Structured data is the foundation. Ensure that product information, pricing, availability, and commercial terms are expressed in formats that AI agents can read and act on — schema.org markup, machine-readable pricing files, structured catalogue exports. Identity verification comes next: claimed profiles, verified business information, and authoritative sources that AI systems can use to confirm who you are."
    },
    "AGT": {
        "slug": "agentic-commerce-readiness",
        "meaning": "Agentic Commerce Readiness measures whether your infrastructure, data, and processes are prepared for commerce that is initiated, mediated, and completed by AI agents acting on behalf of buyers.",
        "why": "Agentic commerce is not a future scenario; it is a present capability that is scaling. Buyers are already delegating purchase decisions to AI systems. Those systems need clean product data, reliable availability signals, machine-readable terms, and transactional infrastructure that does not require human intervention at every step. Merchants who are not readable by agents are not in consideration.",
        "signals_intro": "Low scores appear as: product data that requires human interpretation; availability and pricing that is not programmatically accessible; checkout and transaction flows that require human completion; no API or structured data layer that agents can query.",
        "improvement_intro": "Audit your product data for machine readability first. Then examine your transaction flow: can an agent complete a purchase without human intervention? If not, identify the specific steps that require human action and determine whether each is a genuine requirement or a legacy design assumption. Agent-readable commerce is built incrementally; start with the data layer."
    },
    "MRT": {
        "slug": "machine-readable-trust",
        "meaning": "Machine-Readable Trust measures whether AI systems, buying agents, and automated platforms can verify your trustworthiness from structured signals — or whether your reputation exists only in forms that require human interpretation.",
        "why": "Trust signals that only humans can read are trust signals that AI agents cannot use. As AI mediation of commerce increases, the ability of automated systems to verify merchant identity, commercial history, and reliability becomes a prerequisite for inclusion. Merchants whose trust evidence is unstructured, platform-locked, or human-only are invisible to the systems that are increasingly making or influencing purchase decisions.",
        "signals_intro": "Low scores appear as: trust signals that exist only as unstructured text; reviews and ratings that cannot be accessed programmatically; no machine-verifiable identity claims; commercial history that exists only inside platform databases.",
        "improvement_intro": "Structured trust signals are the objective. This includes schema.org markup for business identity and reviews, programmatic access to aggregated rating data, machine-verifiable credentials where they exist, and structured representations of commercial history. The goal is that an AI agent encountering your business for the first time can form a trust assessment from structured signals alone."
    },
    "GOV": {
        "slug": "governance-independence",
        "meaning": "Governance Independence measures whether the rules that govern your commerce — pricing policy, returns policy, dispute resolution, terms of trade — are set by you, or imposed on you by platforms whose interests are not aligned with yours.",
        "why": "Commercial governance is the framework within which every transaction occurs. A merchant who cannot set their own returns policy, who must accept the platform’s dispute resolution as final, or who has no recourse when platform decisions are incorrect has surrendered governance of their own trade. Independence here is not about avoiding all external rules; it is about ensuring that the rules that govern your commerce reflect your commercial judgment, not a platform’s unilateral policy.",
        "signals_intro": "Low scores appear as: returns and refund policies set by the platform with no merchant override; dispute resolution that the platform controls with the merchant as a respondent, not a party; pricing rules imposed by platform policy; no direct legal relationship with buyers.",
        "improvement_intro": "Map every governance constraint currently imposed by platform agreements. Identify which rules are contractual, which are platform policy enforced algorithmically, and which are legal requirements that would apply regardless of platform. For each contractual or algorithmic constraint, assess the cost of exit versus the cost of continued imposition. Governance independence is built by moving commercial relationships to terms you control."
    }
}

LEVEL_CONTENT = {
    "exposed": {
        "narrative": "At the Exposed level, the business is structurally dependent on platform decisions it cannot influence and cannot survive without. Revenue, visibility, pricing, and buyer relationships are all mediated by platforms that the merchant did not choose as partners so much as default to as the only available route to market. The risk is not theoretical; it is a function of the gap between what the platform controls and what the merchant can replace if access is withdrawn.",
        "transition_prompt": "The first move out of Exposed is not diversification across more platforms — it is establishing one owned asset that the merchant controls regardless of platform decisions. For most merchants, this is a direct buyer contact list or an owned transactional presence, however small. The goal is to reduce the blast radius of the most critical single-point-of-failure, not to eliminate platform dependency immediately."
    },
    "dependent": {
        "narrative": "At the Dependent level, the business has some awareness of its platform exposure but has not yet translated that awareness into structural change. There may be multiple channels, but one still dominates in ways that create existential risk. There may be some owned buyer relationships, but they are not sufficient to sustain the business if primary platform access were withdrawn. The merchant can see the dependency but has not yet built the infrastructure to reduce it.",
        "transition_prompt": "The transition from Dependent to Resilient requires converting awareness into infrastructure. This means building owned channels to a scale where they could absorb a significant portion of platform revenue if needed, establishing direct buyer relationships that are independent of platform mediation, and testing the actual cost of reducing platform reliance through deliberate experiments."
    },
    "resilient": {
        "narrative": "At the Resilient level, the business has built enough structural independence that no single platform decision is existentially threatening. Revenue is distributed across channels with no single point of catastrophic failure. Buyer relationships exist in owned forms. The merchant has some pricing and governance independence. Resilience at this level is not the same as sovereignty — platforms still have significant influence — but the business can survive adverse platform decisions and has the infrastructure to respond.",
        "transition_prompt": "The move from Resilient to Sovereign requires shifting from defensive diversification to active sovereignty. This means building commercial infrastructure that operates independently of platform permission: owned transactional capability, portable reputation systems, machine-readable commercial identity, and governance frameworks that reflect the merchant’s own terms of trade."
    },
    "sovereign": {
        "narrative": "At the Sovereign level, the business operates with commercial independence that does not depend on any single platform’s continued goodwill. Platforms are used as distribution channels, not as the infrastructure of the business itself. The merchant controls their route to buyers, their pricing and governance, their reputation evidence, and their commercial identity in forms that are portable, independent, and machine-readable. Sovereignty is not isolation from platforms; it is the ability to use them on terms you have chosen rather than terms imposed on you.",
        "transition_prompt": "Sovereign merchants focus on maintaining and extending their independence as platform dynamics change — particularly as AI-mediated commerce creates new forms of dependency. The priority is ensuring that the infrastructure of sovereignty — owned buyer relationships, portable reputation, machine-readable identity, direct transactional capability — is built for the commercial environment that is emerging, not just the one that exists today."
    }
}

# ---------------------------------------------------------------- helpers
def _qs_link(q: dict) -> str:
    label = q["question_id"]
    return f'<a href="/score/questions/#{q["question_id"]}" class="qs-ref">{label}</a>'


def _dim_questions(dim_code: str) -> list:
    return [q for q in questions if q["dimension"] == dim_code]


def _breadcrumb(*crumbs) -> str:
    parts = []
    for label, href in crumbs:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return '<nav class="breadcrumb">' + ' › '.join(parts) + '</nav>'


def _canonical(path: str) -> str:
    return f'<link rel="canonical" href="{ORIGIN}{path}">'


def _head(title: str, description: str, path: str, extra: str = "") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{_canonical(path)}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{ORIGIN}{path}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="/assets/css/main.css">
{extra}
</head>"""


def _foot() -> str:
    return """<footer class="site-footer">
<div class="footer-inner">
<p class="footer-copy">&copy; 2025 Outmerchant. Built for independent commerce.</p>
</div>
</footer>
</body></html>"""


def _nav(active: str = "") -> str:
    links = [
        ("/", "Home"),
        ("/score/", "Score"),
        ("/lexicon/", "Lexicon"),
        ("/about/", "About"),
    ]
    items = []
    for href, label in links:
        cls = ' class="active"' if label.lower() == active.lower() else ""
        items.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    return '<nav class="site-nav"><ul>' + "".join(items) + "</ul></nav>"


# ================================================================ builders
def _build_dimension_page(code: str, dim: dict) -> None:
    ed = DIM_CONTENT.get(code, {})
    slug = ed.get("slug", dim["name"].lower().replace(" ", "-"))
    label = dim["name"]
    path = f"/score/dimensions/{slug}/"
    qs = _dim_questions(code)
    qs_links = ", ".join(_qs_link(q) for q in qs) if qs else "(none active)"
    meaning = ed.get("meaning", dim.get("description", ""))
    why = ed.get("why", "")
    signals_intro = ed.get("signals_intro", "")
    improvement_intro = ed.get("improvement_intro", "")
    short_label = label.split(" ")[-1]  # last word as short label

    # JSON-LD
    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": label,
        "description": meaning,
        "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "Outmerchant Score",
                             "url": f"{ORIGIN}/score/"}
    }, indent=2)

    page = f"""{_head(
        title=f"{label} | Outmerchant Score",
        description=meaning[:155],
        path=path,
        extra=f'<script type="application/ld+json">{jsonld}</script>'
    )}
<body>
{_nav('score')}
<main class="page-content">
{_breadcrumb(('Home','/'),('Score','/score/'),('Dimensions','/score/dimensions/'),(label,None))}
<article class="score-dimension-page">
  <header class="dim-header">
    <span class="dim-code">{code}</span>
    <h1>{label}</h1>
  </header>

  <section class="dim-section" id="meaning">
    <h2>What this dimension measures</h2>
    <p>{meaning}</p>
  </section>

  <section class="dim-section" id="why">
    <h2>Why it matters</h2>
    <p>{why}</p>
  </section>

  <section class="dim-section" id="questions">
    <h2>Score questions in this dimension</h2>
    <p>{qs_links}</p>
  </section>

  <section class="dim-section" id="signals">
    <h2>What low scores look like</h2>
    <p>{signals_intro}</p>
  </section>

  <section class="dim-section" id="improve">
    <h2>How to improve</h2>
    <p>{improvement_intro}</p>
  </section>
</article>
</main>
{_foot()}"""

    out = ROOT / path.lstrip("/")
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page)
    print(f"  wrote {path}")


def _build_level_page(lv: dict) -> None:
    key = lv["level"].lower()
    label = lv["label"]
    path = f"/score/levels/{key}/"
    ed = LEVEL_CONTENT.get(key, {})
    description = lv.get("description", "")
    narrative = ed.get("narrative", description)
    transition = ed.get("transition_prompt", "")
    lo = lv["score_range"]["min"]
    hi = lv["score_range"]["max"]

    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": f"{label} — Outmerchant Score Level",
        "description": narrative[:200],
        "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "Outmerchant Score",
                             "url": f"{ORIGIN}/score/"}
    }, indent=2)

    page = f"""{_head(
        title=f"{label} | Outmerchant Score Level",
        description=narrative[:155],
        path=path,
        extra=f'<script type="application/ld+json">{jsonld}</script>'
    )}
<body>
{_nav('score')}
<main class="page-content">
{_breadcrumb(('Home','/'),('Score','/score/'),('Levels','/score/levels/'),(label,None))}
<article class="score-level-page">
  <header class="level-header level-{key}">
    <span class="level-badge">{label}</span>
    <span class="level-range">Score range: {lo}–{hi}</span>
  </header>

  <section class="level-section" id="narrative">
    <h1>What {label} means</h1>
    <p>{narrative}</p>
  </section>

  {f'<section class="level-section" id="transition"><h2>Moving to the next level</h2><p>{transition}</p></section>' if transition else ''}
</article>
</main>
{_foot()}"""

    out = ROOT / path.lstrip("/")
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page)
    print(f"  wrote {path}")


# ================================================================ main
if __name__ == "__main__":
    print("Building reference pages …")
    for dim in dims:
        code = dim["code"]
        if code in DIM_CONTENT:
            _build_dimension_page(code, dim)
    for lv in levels:
        _build_level_page(lv)
    print("Done.")
