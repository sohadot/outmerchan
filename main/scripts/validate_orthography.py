"""Enforces DEC-016 official orthography.

Outmerchant is the official form for the asset, rank, protocol, and public
standard. The lowercase form is allowed for the verb, lexical headword, domain,
and route/path contexts. Legacy split or camel-case forms are never allowed on
current canonical surfaces.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

FORBIDDEN = ("OutMerchant", "Out Merchant", "outMerchant")
LOWERCASE_ALLOWED_HINTS = (
    "outmerchant.com",
    "/outmerchant/",
    "outmerchant-",
    "to outmerchant",
    "outmerchant (v",
    "*outmerchant* (v",
    "outmerchant, verb",
    "definitions of outmerchant",
    "cannot outmerchant",
    "lowercase",
    "verb",
    "headword",
    '"outmerchant"',
    "slug",
    "route",
    "canonical",
)


def scan_files():
    files = []
    files.extend(ROOT.glob("*.html"))
    files.extend(path for path in ROOT.rglob("index.html") if ".git" not in path.parts)
    files.extend(ROOT.glob("*.md"))
    files.extend((ROOT / "main" / "data").glob("*.json"))
    reports = ROOT / "main" / "reports"
    if reports.exists():
        files.extend(reports.glob("*.md"))
    return sorted(set(files))


def line_context(line, match_start, match_end):
    start = max(0, match_start - 48)
    end = min(len(line), match_end + 48)
    return line[start:end].strip()


def suspicious_lowercase(line, match):
    lower = line.lower()
    context = line_context(line, match.start(), match.end()).lower()
    if any(hint in context for hint in LOWERCASE_ALLOWED_HINTS):
        return False
    if re.search(r"\b(outmerchanted|outmerchants|outmerchanting)\b", lower):
        return False
    if re.search(r"[/#._-]outmerchant|outmerchant[/#._-]|outmerchant\.com", lower):
        return False
    return True


def run():
    errors = []
    for path in scan_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(text.splitlines(), start=1):
            for token in FORBIDDEN:
                if token in line:
                    if rel == "DECISION_LOG.md" and "The forms" in line:
                        continue
                    errors.append(f"orthography: {rel}:{lineno} contains forbidden form '{token}'")
            for match in re.finditer(r"\boutmerchant\b", line):
                if suspicious_lowercase(line, match):
                    errors.append(
                        f"orthography: {rel}:{lineno} uses lowercase 'outmerchant' outside verb/domain/path context"
                    )
    return errors


if __name__ == "__main__":
    errs = run()
    for e in errs:
        print(f"FAIL {e}")
    print("orthography: OK" if not errs else f"orthography: {len(errs)} failure(s)")
    raise SystemExit(1 if errs else 0)
