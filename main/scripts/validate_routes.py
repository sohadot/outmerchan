"""Enforces ROUTE_GOVERNANCE.md — the route laws — against pages.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"

VALID_TYPES = {"home", "score", "dimension", "level", "protocol", "lexicon"}
VALID_STATUS = {"active", "planned", "deprecated"}
VALID_OWNERS = {"lexicon", "score", "protocol", "doctrine", "governance", "home"}
TERM_REQUIRED_TYPES = {"dimension", "level"}


def route_to_file(route: str) -> Path:
    """GitHub Pages serves from repo root: '/' -> index.html, '/x/' -> x/index.html."""
    if route == "/":
        return ROOT / "index.html"
    return ROOT / route.strip("/") / "index.html"


def run():
    errors = []
    pages = json.loads((DATA / "pages.json").read_text())["pages"]
    routes = [p["route"] for p in pages]
    routeset = set(routes)

    if len(routeset) != len(routes):
        dupes = sorted({r for r in routes if routes.count(r) > 1})
        errors.append(f"routes: duplicate routes {dupes}")

    for p in pages:
        r = p.get("route", "?")
        for field in ("route", "type", "status", "purpose", "seo_cluster", "governance_owner"):
            if not p.get(field):
                errors.append(f"routes: {r} missing {field} — no page without a function")
        if p.get("type") not in VALID_TYPES:
            errors.append(f"routes: {r} invalid type '{p.get('type')}'")
        if p.get("status") not in VALID_STATUS:
            errors.append(f"routes: {r} invalid status '{p.get('status')}'")
        if p.get("governance_owner") not in VALID_OWNERS:
            errors.append(f"routes: {r} invalid governance_owner '{p.get('governance_owner')}'")
        if p.get("type") in TERM_REQUIRED_TYPES and not p.get("canonical_term"):
            errors.append(f"routes: {r} ({p['type']}) requires canonical_term")
        if p.get("type") == "lexicon" and r not in ("/lexicon/",) and not p.get("canonical_term"):
            errors.append(f"routes: lexicon term page {r} requires canonical_term")
        for target in p.get("required_internal_links", []):
            if target not in routeset:
                errors.append(f"routes: {r} requires link to unregistered route {target}")
        if p.get("status") == "active" and not route_to_file(r).exists():
            errors.append(f"routes: active route {r} has no file at {route_to_file(r).relative_to(ROOT)}")

    # Orphan law: every active route must be reachable from '/'
    nav = json.loads((DATA / "navigation.json").read_text())
    edges = {}
    for p in pages:
        edges.setdefault(p["route"], set()).update(p.get("required_internal_links", []))
    for item in nav.get("primary", []) + nav.get("planned", []):
        target = item["target"].split("#")[0] or "/"
        edges.setdefault("/", set()).add(target)
    reachable, stack = set(), ["/"]
    while stack:
        node = stack.pop()
        if node in reachable:
            continue
        reachable.add(node)
        stack.extend(edges.get(node, ()))
    for p in pages:
        if p["status"] == "active" and p["route"] not in reachable:
            errors.append(f"routes: active route {p['route']} is an orphan — unreachable from '/'")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("routes: OK" if not errs else f"routes: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
