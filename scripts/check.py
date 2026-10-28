#!/usr/bin/env python3
"""Offline checks for this repository's Markdown subset and version markers."""

import re
import sys
import xml.etree.ElementTree as ET
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])
        for key in ("id", "name"):
            if key in attrs:
                self.ids.add(attrs[key])


def prose(text):
    # Ignore fenced examples, but preserve inline code in heading slugs.
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def anchors(text):
    parser = HTMLLinks()
    parser.feed(prose(text))
    found = set(parser.ids)
    counts = {}
    for title in re.findall(r"^#{1,6}\s+(.+?)(?:\s+#+)?$", prose(text), re.M):
        title = re.sub(r"<[^>]+>", "", title)
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", title)
        slug = re.sub(r"[^\w\- ]", "", unescape(title).lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        found.add(slug + ("-" + str(count) if count else ""))
    return found


def markdown_links(text):
    # Balanced destinations allow parentheses in URLs; titles are not used here.
    text = re.sub(r"`[^`\n]*`", "", prose(text))
    for match in re.finditer(r"!?\[[^\]\n]*\]\(", text):
        start = match.end()
        depth = 1
        end = start
        while end < len(text) and depth:
            char = text[end]
            if char == "\\":
                end += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            end += 1
        if depth:
            raise ValueError("unclosed inline link")
        destination = text[start:end - 1].strip()
        if destination.startswith("<") and destination.endswith(">"):
            destination = destination[1:-1]
        yield destination
    parser = HTMLLinks()
    parser.feed(text)
    yield from parser.links


def check(root):
    errors = []
    docs = sorted(root.rglob("*.md"))
    docs = [p for p in docs if ".git" not in p.relative_to(root).parts]
    texts = {p.resolve(): p.read_text(encoding="utf-8") for p in docs}
    count = 0
    for path, text in texts.items():
        if re.search(r"^\s*\[[^]]+\]:", prose(text), re.M):
            errors.append(f"{path.relative_to(root)}: reference-style links are unsupported")
        try:
            links = list(markdown_links(text))
        except ValueError as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        for link in links:
            url = urlsplit(unescape(link))
            if url.scheme or url.netloc:
                continue
            count += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"{path.relative_to(root)}: link escapes repository: {link}")
                continue
            if not target.exists():
                errors.append(f"{path.relative_to(root)}: missing target: {link}")
            elif url.fragment and target.suffix == ".md":
                if unquote(url.fragment) not in anchors(texts.get(target, target.read_text(encoding="utf-8"))):
                    errors.append(f"{path.relative_to(root)}: missing anchor: {link}")

    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"^version: (\d+\.\d+\.\d+)$", skill, re.M)
    version = match.group(1) if match else "INVALID"
    if not match:
        errors.append("SKILL.md: missing semantic version")
    for name in ("README.md", "README.zh-CN.md"):
        markers = re.findall(r"\*\*v(\d+\.\d+\.\d+) ·", (root / name).read_text(encoding="utf-8"))
        if markers != [version]:
            errors.append(f"{name}: version marker does not match SKILL.md")
    history = (root / "references/changelog.md").read_text(encoding="utf-8")
    first = re.search(r"^## v(\d+\.\d+\.\d+)", history, re.M)
    if not first or first.group(1) != version:
        errors.append("changelog: latest version does not match SKILL.md")

    svg_path = root / "assets/learning-loop.svg"
    try:
        svg = ET.parse(svg_path).getroot()
        ns = "{http://www.w3.org/2000/svg}"
        if svg.tag != ns + "svg" or not svg.get("viewBox"):
            errors.append("diagram: missing SVG root/viewBox")
        ids = {el.get("id") for el in svg.iter() if el.get("id")}
        if svg.get("role") != "img" or not svg.get("aria-labelledby"):
            errors.append("diagram: missing accessible name")
        for name in svg.get("aria-labelledby", "").split():
            if name not in ids:
                errors.append("diagram: unresolved accessible name")
        for el in svg.iter():
            if el.tag in {ns + "script", ns + "foreignObject", ns + "image"}:
                errors.append("diagram: unsupported active or external content")
            for key, value in el.attrib.items():
                if key.lower().startswith("on") or (key.endswith("href") and not value.startswith("#")):
                    errors.append("diagram: active or external attribute")
    except (OSError, ET.ParseError) as exc:
        errors.append(f"diagram: {exc}")

    for path in root.rglob("*"):
        if ".git" not in path.relative_to(root).parts and path.is_symlink():
            errors.append(f"symlink not allowed in portable payload: {path.relative_to(root)}")
    return errors, version, len(docs), count


if __name__ == "__main__":
    errors, version, documents, links = check(ROOT)
    if errors:
        print("FAIL\n" + "\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"PASS v{version}: {documents} Markdown files, {links} local links; version and SVG checks")
