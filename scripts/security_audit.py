#!/usr/bin/env python3
"""Dependency-free security baseline checks for the static SYNTRA website."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import base64
import hashlib
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
        super().__init__(convert_charrefs=False)
        self.ids = set()
        self.links = []
        self.csp = None
        self.referrer = False
        self.inline_scripts = []
        self.inline_event_handlers = []
        self.inline_style_blocks = 0
        self.inline_style_attributes = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "content-security-policy":
            self.csp = attrs.get("content", "")
        if tag == "meta" and attrs.get("name", "").lower() == "referrer":
            self.referrer = True
        for name in attrs:
            if re.fullmatch(r"on[a-z]+", name, re.IGNORECASE):
                self.inline_event_handlers.append(name)
        if "style" in attrs:
            self.inline_style_attributes.append(attrs["style"])
        if tag == "style":
            self.inline_style_blocks += 1
        if tag == "script":
            script_type = attrs.get("type", "").strip().lower()
            is_javascript = script_type in ("", "module", "text/javascript", "application/javascript", "application/ecmascript", "text/ecmascript")
            self._script_is_inline = not attrs.get("src") and is_javascript
            self._script_parts = []

    def handle_data(self, data):
        if getattr(self, "_script_is_inline", False):
            self._script_parts.append(data)

    def handle_entityref(self, name):
        if getattr(self, "_script_is_inline", False):
            self._script_parts.append(f"&{name};")

    def handle_charref(self, name):
        if getattr(self, "_script_is_inline", False):
            self._script_parts.append(f"&#{name};")

    def handle_endtag(self, tag):
        if tag == "script" and getattr(self, "_script_is_inline", False):
            self.inline_scripts.append("".join(self._script_parts))
            self._script_is_inline = False
            self._script_parts = []


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
    relative = page.relative_to(ROOT)
    if not parser.csp:
        errors.append(f"Missing CSP meta policy: {relative}")
    else:
        script_directive = re.search(r"(?:^|;)\s*script-src\s+([^;]+)", parser.csp, re.IGNORECASE)
        if not script_directive:
            errors.append(f"Missing explicit script-src directive: {relative}")
        else:
            sources = script_directive.group(1).split()
            if "'unsafe-inline'" in sources:
                errors.append(f"script-src allows unsafe-inline: {relative}")
            page_content = page.read_text(encoding="utf-8")
            script_pattern = re.compile(r"<script\b([^>]*)>([\s\S]*?)</script\s*>", re.IGNORECASE)
            for match in script_pattern.finditer(page_content):
                attributes, script = match.groups()
                if re.search(r"\bsrc\s*=", attributes, re.IGNORECASE):
                    continue
                type_match = re.search(r"""\btype\s*=\s*["']?([^\s"'>]+)""", attributes, re.IGNORECASE)
                script_type = type_match.group(1).lower() if type_match else ""
                if script_type not in ("", "module", "text/javascript", "application/javascript", "application/ecmascript", "text/ecmascript"):
                    continue
                digest = base64.b64encode(hashlib.sha256(script.encode("utf-8")).digest()).decode("ascii")
                if f"'sha256-{digest}'" not in sources:
                    errors.append(f"Inline script SHA-256 missing from CSP: {relative} ({digest})")
        style_directive = re.search(r"(?:^|;)\s*style-src\s+([^;]+)", parser.csp, re.IGNORECASE)
        if not style_directive:
            errors.append(f"Missing explicit style-src directive: {relative}")
        elif "'unsafe-inline'" in style_directive.group(1).split():
            errors.append(f"style-src allows unsafe-inline: {relative}")
        if parser.inline_style_blocks:
            errors.append(f"Inline style blocks found: {relative} ({parser.inline_style_blocks})")
        if parser.inline_style_attributes:
            errors.append(f"Inline style attributes found: {relative} ({len(parser.inline_style_attributes)})")
        if parser.inline_event_handlers:
            errors.append(f"Inline event handler attributes found: {relative}")
    if not parser.referrer:
        errors.append(f"Missing Referrer-Policy meta: {relative}")

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
