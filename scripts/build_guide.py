#!/usr/bin/env python3
"""Build the public guide from four parts and seven appendices.

``guide.template.html`` contains only the hand-maintained page shell.  The
legacy static guide can be converted once with ``--bootstrap-template``;
ordinary builds then render every canonical Markdown source afresh.
"""

from __future__ import annotations

import argparse
import html
import re
import unicodedata
from pathlib import Path
from xml.etree import ElementTree

import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "guide.template.html"
OUTPUT = ROOT / "guide.html"
PLACEHOLDER = "{{CONTENT}}"

CHAPTERS = [
    (ROOT / "part_00_intro.md", "서문"),
    (ROOT / "part_01_records.md", "1부"),
    (ROOT / "part_02_experiment_to_manuscript.md", "2부"),
    (ROOT / "part_03_rules.md", "3부"),
    (ROOT / "part_04_afterword.md", "후기"),
]
APPENDICES = [
    ROOT / "TERMS.md",
    ROOT / "QUICKSTART.md",
    ROOT / "EXAMPLE_WORKSPACE.md",
    ROOT / "PATH.md",
    ROOT / "SOURCES.md",
    ROOT / "ROBOTICS_REFERENCE.md",
    ROOT / "TOOLS.md",
]


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFC", text).lower().strip()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^0-9a-z가-힣\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text[:100] or "section"


class HeadingMetadata(Treeprocessor):
    def __init__(self, md: markdown.Markdown, source: str, used_ids: set[str]):
        super().__init__(md)
        self.source = source
        self.prefix = Path(source).stem.replace("_", "-").lower()
        self.used_ids = used_ids
        self.headings: list[tuple[int, str, str]] = []

    def run(self, root: ElementTree.Element) -> None:
        for element in root.iter():
            if not re.fullmatch(r"h[1-6]", element.tag):
                continue
            level = int(element.tag[1])
            title = "".join(element.itertext()).strip()
            chapter = re.match(r"^Ch\.?\s*(\d+)\s*[—–-]\s*(.+)$", title)
            if level == 1 and chapter:
                candidate = f"ch-{int(chapter.group(1))}-{slugify(chapter.group(2))}"
            else:
                candidate = slugify(title) if level == 1 else f"{self.prefix}-{slugify(title)}"
            heading_id = candidate
            suffix = 2
            while heading_id in self.used_ids:
                heading_id = f"{candidate}-{suffix}"
                suffix += 1
            self.used_ids.add(heading_id)
            element.set("data-source", self.source)
            element.set("id", heading_id)
            self.headings.append((level, title, heading_id))


class HeadingMetadataExtension(Extension):
    def __init__(self, source: str, used_ids: set[str]):
        self.source = source
        self.used_ids = used_ids
        self.processor: HeadingMetadata | None = None
        super().__init__()

    def extendMarkdown(self, md: markdown.Markdown) -> None:  # noqa: N802
        self.processor = HeadingMetadata(md, self.source, self.used_ids)
        md.treeprocessors.register(self.processor, "source_heading_metadata", 5)


def render_source(path: Path, used_ids: set[str]) -> tuple[str, list[tuple[int, str, str]]]:
    extension = HeadingMetadataExtension(path.name, used_ids)
    rendered = markdown.markdown(
        path.read_text(encoding="utf-8"),
        extensions=["extra", "sane_lists", extension],
        output_format="html5",
    )
    assert extension.processor is not None
    return rendered, extension.processor.headings


def overview_entry(path: Path, headings: list[tuple[int, str, str]], label: str) -> str:
    h1 = next((item for item in headings if item[0] == 1), None)
    if h1 is None:
        raise RuntimeError(f"missing H1 in {path.name}")
    sections = [item for item in headings if item[0] == 2]
    section_html = ""
    if sections:
        links = []
        for _, title, heading_id in sections:
            links.append(f'<a href="#{html.escape(heading_id)}">{html.escape(title)}</a>')
        section_html = '<div class="overview-sections">' + '<span class="sep">/</span>'.join(links) + "</div>"
    return (
        '<div class="overview-chapter">'
        f'<a class="overview-chapter-link" href="#{html.escape(h1[2])}">'
        f'<span class="overview-chapter-num">{html.escape(label)}</span>{html.escape(h1[1])}</a>'
        f"{section_html}</div>"
    )


def build_content() -> str:
    sources = [path for path, _ in CHAPTERS] + APPENDICES
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise RuntimeError("missing canonical sources: " + ", ".join(missing))
    used_ids: set[str] = set()
    rendered: list[str] = []
    metadata: list[tuple[Path, list[tuple[int, str, str]]]] = []
    for path in sources:
        fragment, headings = render_source(path, used_ids)
        rendered.append(fragment)
        metadata.append((path, headings))

    guide_entries = "".join(
        overview_entry(path, headings, label)
        for (path, label), (_, headings) in zip(CHAPTERS, metadata[: len(CHAPTERS)])
    )
    appendix_entries = "".join(
        overview_entry(path, headings, "부록")
        for path, headings in metadata[len(CHAPTERS) :]
    )
    overview = (
        '<section class="guide-overview"><div class="overview-header">'
        '<h1 class="overview-title">AI와 로봇 연구하기</h1></div>'
        '<div class="overview-group"><div class="overview-group-label">Guide</div>'
        f"{guide_entries}</div>"
        '<div class="overview-group"><div class="overview-group-label">Appendix</div>'
        f"{appendix_entries}</div></section>"
    )
    return overview + "\n" + "\n".join(rendered)


def bootstrap_template() -> None:
    if TEMPLATE.exists():
        raise RuntimeError(f"template already exists: {TEMPLATE}")
    shell = OUTPUT.read_text(encoding="utf-8")
    pattern = re.compile(
        r'(<main id="main-content"><div id="content">)(.*?)(</div></main>)', re.DOTALL
    )
    match = pattern.search(shell)
    if not match:
        raise RuntimeError("main content container not found in guide.html")
    replacement = match.group(1) + PLACEHOLDER + match.group(3)
    template = shell[: match.start()] + replacement + shell[match.end() :]
    TEMPLATE.write_text(template, encoding="utf-8")
    print(f"Bootstrapped {TEMPLATE}")


def build() -> None:
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count(PLACEHOLDER) != 1:
        raise RuntimeError(f"template must contain exactly one {PLACEHOLDER}")
    content = build_content()
    output = template.replace(PLACEHOLDER, content)
    OUTPUT.write_text(output, encoding="utf-8")
    print(f"Built {OUTPUT}")
    print(f"  source units: {len(CHAPTERS) + len(APPENDICES)}")
    print(f"  content: {len(content):,} chars")
    print(f"  HTML: {len(output):,} chars")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-template", action="store_true")
    args = parser.parse_args()
    if args.bootstrap_template:
        bootstrap_template()
    build()


if __name__ == "__main__":
    main()
