#!/usr/bin/env python3
"""Dependency-free security baseline checks for the static SYNTRA website."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".html", ".htm", ".js", ".css", ".json", ".md", ".svg", ".xml", ".txt", ".yml", ".yaml"}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    re.compile(r"-----BEGIN PGP PRIVATE KEY BLOCK-----"),
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.csp = False
        self.referrer = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        for key in ("href", "src"):
            if a.get(key):
                self.links.append(a[key])
        if tag == "meta" and a.get("http-equiv", "").lower() == "content-security-policy":
            self.csp = True
        if tag == "meta" and a.get("name", "").lower() == "referrer":
            self.referrer = True

def local_target(page, raw):
    parts = urlsplit(raw)
    if parts.scheme or parts.netloc or raw.startswith("//") or parts.path == "":
        return page if parts.fragment else None, unquote(parts.fragment)
    path = unquote(parts.path)
    target = (ROOT / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
    target = target.resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return None, ""
    if target.is_dir() or not target.suffix:
        target = target / "index.html"
    return target, unquote(parts.fragment)

errors = []
files = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES and ".git" not in p.parts]
for path in files:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for pattern in SECRET_PATTERNS:
        if pattern.search(content):
            errors.append(f"Possible exposed credential pattern: {path.relative_to(ROOT)}")
            break

html_pages = [p for p in ROOT.rglob("*.html") if ".git" not in p.parts]
parsed = {}
for page in html_pages:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    parsed[page.resolve()] = parser
    if not parser.csp:
        errors.append(f"Missing CSP meta policy: {page.relative_to(ROOT)}")
    if not parser.referrer:
        errors.append(f"Missing Referrer-Policy meta: {page.relative_to(ROOT)}")

for page, parser in parsed.items():
    for raw in parser.links:
        target, fragment = local_target(page, raw)
        if target is None:
            continue
        if not target.exists():
            errors.append(f"Broken local link: {page.relative_to(ROOT)} -> {raw}")
            continue
        if fragment and target.suffix.lower() in {".html", ".htm"}:
            target_parser = parsed.get(target.resolve())
            if target_parser and fragment not in target_parser.ids:
                errors.append(f"Broken anchor: {page.relative_to(ROOT)} -> {raw}")

if errors:
    print("SYNTRA security baseline: FAILED")
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)
print(f"SYNTRA security baseline: PASS ({len(html_pages)} HTML pages, {len(files)} text files checked)")
