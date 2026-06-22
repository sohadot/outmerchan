"""Enforces SCORE_GOVERNANCE.md against the governed score model files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"

FIXED_CODES = {"DEP", "OWN", "REP", "PAY", "FEE", "XBR", "AGT", "GOV"}
FIXED_TIERS = [("Captured", 0, 25), ("Dependent", 26, 50), ("Emerging", 51, 75), ("Outmerchant", 76, 100)]


def run():
    errors = []
    dims = json.loads((DATA / "score_dimensions.json").read_text())["dimensions"]
    questions = json.loads((DATA / "score_questions.json").read_text())["questions"]
    levels = json.loads((DATA / "score_levels.json").read_text())["levels"]

    codes = [d["code"] for d in dims]
    if len(dims) != 8:
        errors.append(f"score: expected 8 dimensions, found {len(dims)}")
    if set(codes) != FIXED_CODES:
        errors.append(f"score: dimension codes drifted from inviolable set: {sorted(set(codes) ^ FIXED_CODES)}")
    if len(set(codes)) != len(codes):
        errors.append("score: duplicate dimension codes")
    if sorted(d["order"] for d in dims) != list(range(1, len(dims) + 1)):
        errors.append("score: dimension orders must be 1..8 with no gaps")
    total_weight = sum(d["weight"] for d in dims)
    if abs(total_weight - 100) > 1e-9:
        errors.append(f"score: dimension weights must sum to 100, got {total_weight}")
    for d in dims:
        for field in ("name", "question", "lexicon_term", "route"):
            if not d.get(field):
                errors.append(f"score: dimension {d.get('code')} missing {field}")

    active = [q for q in questions if q.get("status") == "active"]
    if len(active) != 20:
        errors.append(f"score: expected 20 active questions, found {len(active)}")
    ids = [q["id"] for q in questions]
    if len(set(ids)) != len(ids):
        errors.append("score: duplicate question ids")
    covered = set()
    for q in questions:
        if q["dimension"] not in FIXED_CODES:
            errors.append(f"score: {q['id']} maps to invalid dimension {q['dimension']}")
        covered.add(q["dimension"])
        opts = q.get("options", [])
        if len(opts) < 2:
            errors.append(f"score: {q['id']} has fewer than 2 options")
        pts = [o.get("points") for o in opts]
        if any(not isinstance(p, int) or p < 0 for p in pts):
            errors.append(f"score: {q['id']} has invalid option points")
        elif max(pts) == 0:
            errors.append(f"score: {q['id']} has no sovereign-behavior option (max points 0)")
        elif min(pts) != 0:
            errors.append(f"score: {q['id']} has no captured-behavior option (min points must be 0)")
        if not q.get("text"):
            errors.append(f"score: {q['id']} missing text")
    missing_dims = FIXED_CODES - covered
    if missing_dims:
        errors.append(f"score: dimensions with no questions: {sorted(missing_dims)}")

    if len(levels) != 4:
        errors.append(f"score: expected 4 tiers, found {len(levels)}")
    for lvl, (name, lo, hi) in zip(sorted(levels, key=lambda x: x["min"]), FIXED_TIERS):
        if (lvl["name"], lvl["min"], lvl["max"]) != (name, lo, hi):
            errors.append(
                f"score: tier drift — expected {name} {lo}-{hi}, got {lvl['name']} {lvl['min']}-{lvl['max']} (inviolable, DEC-006)")
    terminal = max(levels, key=lambda x: x["max"])
    if terminal["name"] != "Outmerchant" or terminal["max"] != 100:
        errors.append("score: terminal tier must be 'Outmerchant' ending at 100 (inviolable, DEC-001/DEC-006)")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("score model: OK" if not errs else f"score model: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
