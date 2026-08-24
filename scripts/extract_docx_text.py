#!/usr/bin/env python3
"""Extract plain text from a .docx file's paragraphs.

A .docx is a zip archive with the document body as XML at
word/document.xml - this reads that directly with only the standard
library (zipfile + xml.etree), rather than depending on python-docx/lxml,
since this ships inside a Claude Code plugin and can't assume anything
beyond Python itself is installed on the user's machine.

Note: unlike MyJobMatch.ai's own resume parser (backend/app/resume_parser.py,
which uses python-docx's `document.paragraphs` - body-level paragraphs
only), this walks every <w:p> in the document, including ones nested
inside tables. That's a deliberate difference, not a bug: resumes
sometimes use tables for layout, and pulling that text too only helps a
fit analysis, never hurts it.
"""
import sys
import zipfile
from xml.etree import ElementTree as ET

WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def extract_text(path: str) -> str:
    with zipfile.ZipFile(path) as archive:
        xml_bytes = archive.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    paragraphs = []
    for p in root.iter(f"{WORD_NS}p"):
        run_text = "".join(t.text or "" for t in p.iter(f"{WORD_NS}t"))
        paragraphs.append(run_text)
    return "\n".join(paragraphs)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_docx_text.py <path-to-docx>", file=sys.stderr)
        sys.exit(1)

    try:
        text = extract_text(sys.argv[1])
    except Exception as exc:  # noqa: BLE001 - report and exit, not a library
        print(f"Could not parse .docx file: {exc}", file=sys.stderr)
        sys.exit(1)

    if not text.strip():
        print("No text could be extracted from the file", file=sys.stderr)
        sys.exit(1)

    print(text)
