"""Enforces Score Engine governance (Sprint 3A, DEC-015):
the engine is a governed diagnostic — explainable, privacy-preserving,
guidance-driven from governed data, with no monetization, no email capture,
no marketplace claims, and no false default result."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"

EXPORT_FIELDS = [
    "engine_version", "generated_at", "total_score", "level_id", "level_name",
    "level_range", "dimension_scores", "weakest_dimensions",
    "canonical_terms_used", "protocol_url", "score_url", "boundary_statement",
]
EMAIL_CAPTURE = ['type="email"', "newsletter", "subscribe", "sign up", "mailing list"]
PAYMENT_LANGUAGE = [r"\$\d", r"\bbuy now\b", r"\bcheckout\b", r"\bpay now\b",
                    r"\bpurchase\b", r"\bupgrade to\b", r"\bpremium report\b"]
MARKETPLACE_CLAIMS = ["our marketplace", "join the marketplace", "list your products",
                      "list your store", "become a seller", "start selling on outmerchant"]


def run():
    errors = []

    # Governed guidance layer
    try:
        guidance = json.loads((DATA / "engine_guidance.json").read_text())
    except FileNotFoundError:
        return ["engine: engine_guidance.json missing"]
    except json.JSONDecodeError as exc:
        return [f"engine: engine_guidance.json does not parse ({exc})"]

    dims = json.loads((DATA / "score_dimensions.json").read_text())["dimensions"]
    levels = json.loads((DATA / "score_levels.json").read_text())["levels"]
    dim_codes = {d["code"] for d in dims}
    gdims = guidance.get("dimensions", {})

    for code in dim_codes:
        if code not in gdims:
            errors.append(f"engine: dimension {code} has no guidance in engine_guidance.json")
        else:
            for field in ("weak_interpretation", "next_action"):
                if not gdims[code].get(field, "").strip():
                    errors.append(f"engine: guidance for {code} has empty {field}")
    for code in gdims:
        if code not in dim_codes:
            errors.append(f"engine: guidance for unknown dimension code {code}")
    for lvl in levels:
        if not guidance.get("route_to_buyer", {}).get(lvl["name"], "").strip():
            errors.append(f"engine: route_to_buyer interpretation missing for tier {lvl['name']}")
    if not guidance.get("boundary_statement", "").strip():
        errors.append("engine: boundary_statement missing from engine_guidance.json")
    if not guidance.get("engine_version", "").strip():
        errors.append("engine: engine_version missing from engine_guidance.json")

    # The engine surface
    html = (ROOT / "score" / "index.html").read_text()
    low = html.lower()

    if "engine boundary" not in low and "diagnostic boundary" not in low:
        errors.append("engine: /score/ missing the Engine Boundary section")

    m = re.search(r'id="resultTotal">([^<]*)<', html)
    if not m:
        errors.append("engine: /score/ result element not found")
    elif m.group(1).strip() == "0":
        errors.append("engine: /score/ shows a default result of 0 before completion")
    if "Result appears after completing the diagnostic" not in html:
        errors.append("engine: /score/ missing the neutral pre-completion state")

    for marker in EMAIL_CAPTURE:
        if marker in low:
            errors.append(f"engine: /score/ contains email-capture language: '{marker}'")
    for pattern in PAYMENT_LANGUAGE:
        if re.search(pattern, low):
            errors.append(f"engine: /score/ contains payment language matching '{pattern}'")
    for claim in MARKETPLACE_CLAIMS:
        if claim in low:
            errors.append(f"engine: /score/ contains marketplace claim: '{claim}'")

    if re.search(r"<script[^>]*\bsrc=", html):
        errors.append("engine: /score/ has an external JavaScript dependency")

    for field in EXPORT_FIELDS:
        if field not in html:
            errors.append(f"engine: export schema field '{field}' absent from /score/")

    # Guidance must be read from governed data, not hardcoded interpretive copy
    if "engine_guidance.json" not in html:
        errors.append("engine: /score/ does not read the governed guidance layer")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("engine: OK" if not errs else f"engine: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
