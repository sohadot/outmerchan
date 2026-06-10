"""Enforces the internal link laws of ROUTE_GOVERNANCE.md: graph consistency and live-surface anchors."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "main" / "data"


def run():
    errors = []
    pages = json.loads((DATA / "pages.json").read_text())["pages"]
    links = json.loads((DATA / "internal_links.json").read_text())["links"]
    nav = json.loads((DATA / "navigation.json").read_text())
    routeset = {p["route"] for p in pages}

    # Every edge must connect registered routes
    edge_set = set()
    for link in links:
        frm, to = link.get("from"), link.get("to")
        if frm not in routeset:
            errors.append(f"links: edge from unregistered route {frm}")
        if to not in routeset:
            errors.append(f"links: edge to unregistered route {to}")
        edge_set.add((frm, to))

    # Every required link in pages.json must exist as an edge in the graph
    for p in pages:
        for target in p.get("required_internal_links", []):
            if (p["route"], target) not in edge_set:
                errors.append(f"links: required edge missing from graph: {p['route']} -> {target}")

    # Live surface: anchor links and navigation must resolve
    html = (ROOT / "index.html").read_text()
    ids = set(re.findall(r'id="([^"]+)"', html))
    for href in re.findall(r'href="(#[^"]+)"', html):
        if href[1:] not in ids:
            errors.append(f"links: broken anchor on live surface: {href}")
    for href in re.findall(r'href="(/[^"#]*)"', html):
        route = href if href.endswith("/") else href + "/"
        if href != "/" and route not in routeset and href not in routeset:
            errors.append(f"links: live surface links to unregistered route {href}")
    for item in nav.get("primary", []):
        target = item["target"]
        if target.startswith("/#") and target[2:] not in ids:
            errors.append(f"links: navigation anchor {target} does not resolve on live surface")
        elif not target.startswith("/#"):
            base = target.split("#")[0] or "/"
            if base not in routeset:
                errors.append(f"links: navigation target {target} not registered")
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("links: OK" if not errs else f"links: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
