#!/usr/bin/env python3
"""Inventory and search course PDFs and PPTX decks with native locators."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence
from xml.etree import ElementTree as ET
from zipfile import ZipFile

try:
    import pymupdf as fitz
except ImportError:  # PyMuPDF historically exposed the top-level name ``fitz``.
    try:
        import fitz  # type: ignore[no-redef]
    except ImportError as exc:  # pragma: no cover - dependency failure path
        raise SystemExit(
            "PyMuPDF is required. Install it with: python3 -m pip install pymupdf"
        ) from exc


KNOWN_KINDS = ("lecture", "recitation", "textbook", "syllabus", "other")
SUPPORTED_SCHEMA_VERSIONS = (1, 2)


class PptxSlide:
    """Read visible DrawingML paragraphs, excluding speaker notes."""

    def __init__(self, xml: bytes) -> None:
        drawing = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
        paragraphs = []
        for paragraph in ET.fromstring(xml).iter(drawing + "p"):
            paragraphs.append("".join(
                (node.text or "") if node.tag == drawing + "t" else "\n"
                for node in paragraph.iter()
                if node.tag in {drawing + "t", drawing + "br"}
            ))
        self.text = "\n".join(paragraphs)

    def get_text(self, mode: str = "text") -> str:
        return self.text

    def get_label(self) -> str:
        return ""


class PptxDocument:
    """Minimal read interface; order comes from presentation relationships."""

    def __init__(self, path: Path) -> None:
        p = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
        r = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
        with ZipFile(path) as archive:
            relations = ET.fromstring(archive.read("ppt/_rels/presentation.xml.rels"))
            targets = {
                item.attrib["Id"]: item.attrib["Target"]
                for item in relations
                if item.get("TargetMode") != "External"
            }
            presentation = ET.fromstring(archive.read("ppt/presentation.xml"))
            self.slides = []
            for item in presentation.findall(f"{p}sldIdLst/{p}sldId"):
                target = targets[item.attrib[r + "id"]]
                member = (target.lstrip("/") if target.startswith("/")
                          else posixpath.normpath(posixpath.join("ppt", target)))
                self.slides.append(PptxSlide(archive.read(member)))
        self.page_count = len(self.slides)  # Internal reader interface, not a PDF locator.

    def __getitem__(self, index: int) -> PptxSlide:
        return self.slides[index]

    def get_toc(self, simple: bool = True) -> list[list[object]]:
        return [[1, f"Slide {index + 1}", index + 1] for index in range(self.page_count)]

    def close(self) -> None:
        pass

    def __enter__(self) -> PptxDocument:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()


def open_source_document(path: Path) -> fitz.Document | PptxDocument:
    return PptxDocument(path) if path.suffix.casefold() == ".pptx" else fitz.open(path)


KIND_DIRECTORIES = {
    "lecture": {"lecture", "lectures", "lec"},
    "recitation": {"recitation", "recitations", "recitaion", "rec"},
    "textbook": {"textbook", "textbooks", "book", "books"},
    "syllabus": {"syllabus", "syllabi"},
}


@dataclass(frozen=True)
class Source:
    path: Path
    relative_path: str
    kind: str
    source_id: str


def normalize_text(value: str) -> str:
    """Case-fold text and collapse all whitespace for stable anchor matching."""

    return " ".join(value.casefold().split())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def natural_key(value: str) -> list[object]:
    return [int(part) if part.isdigit() else part.casefold() for part in re.split(r"(\d+)", value)]


def source_kind(relative_path: Path) -> str:
    lowered_parts = {part.casefold() for part in relative_path.parts[:-1]}
    for kind, directory_names in KIND_DIRECTORIES.items():
        if lowered_parts & directory_names:
            return kind

    stem = relative_path.stem.casefold()
    if re.search(r"\b(?:lecture|lec)\s*[-_ ]*\d+", stem):
        return "lecture"
    if re.search(r"\b(?:recitation|recitaion|rec)\s*[-_ ]*\d+", stem):
        return "recitation"
    if "syllabus" in stem:
        return "syllabus"
    return "other"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug or "source"


def infer_source_id(relative_path: Path, kind: str) -> str:
    stem = relative_path.stem
    patterns = {
        "lecture": r"(?i)\b(?:lecture|lec)\s*[-_ ]*0*(\d+)\b",
        "recitation": r"(?i)\b(?:recitation|recitaion|rec)\s*[-_ ]*0*(\d+)\b",
    }
    if kind in patterns:
        match = re.search(patterns[kind], stem)
        if match:
            number = int(match.group(1))
            return f"{kind}-{number:02d}"

    if kind == "textbook":
        edition = re.search(r"(?i)\b(\d+)(?:st|nd|rd|th)\s+edition\b", stem)
        cleaned = re.sub(r"(?i)\b\d+(?:st|nd|rd|th)\s+edition\b", "", stem)
        base = slugify(cleaned)[:48].rstrip("-")
        suffix = f"-{int(edition.group(1))}e" if edition else ""
        return f"textbook-{base}{suffix}"

    return f"{kind}-{slugify(stem)[:56].rstrip('-')}"


def find_sources(
    root: Path,
    scopes: set[str] | None = None,
    diagnostics: list[str] | None = None,
) -> list[Source]:
    root = root.resolve()
    sources: list[Source] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.casefold() not in {".pdf", ".pptx"}:
            continue
        resolved = path.resolve()
        try:
            relative = resolved.relative_to(root)
        except ValueError:
            if diagnostics is not None:
                diagnostics.append(f"Skipping source symlink outside repository root: {path}")
            continue
        if any(part in {".git", ".ipynb_checkpoints", ".cache"} for part in relative.parts):
            continue
        kind = source_kind(relative)
        if scopes and kind not in scopes:
            continue
        sources.append(
            Source(
                path=resolved,
                relative_path=relative.as_posix(),
                kind=kind,
                source_id=infer_source_id(relative, kind),
            )
        )
    return sorted(sources, key=lambda source: natural_key(source.relative_path))


def page_label(document: fitz.Document | PptxDocument, page_number: int) -> str | None:
    label = document[page_number - 1].get_label().strip()
    return label or None


def toc_title(toc: Sequence[Sequence[object]], page_number: int) -> str | None:
    candidates = [entry for entry in toc if len(entry) >= 3 and int(entry[2]) <= page_number]
    if not candidates:
        return None
    exact = [entry for entry in candidates if int(entry[2]) == page_number]
    chosen = exact[-1] if exact else candidates[-1]
    title = str(chosen[1]).strip()
    return title or None


def source_inventory(source: Source, include_hash: bool) -> dict[str, object]:
    with open_source_document(source.path) as document:
        labels = [document[index].get_label().strip() for index in range(document.page_count)]
        nonempty_labels = [label for label in labels if label]
        record: dict[str, object] = {
            "source_id": source.source_id,
            "kind": source.kind,
            "path": source.relative_path,
            "size_bytes": source.path.stat().st_size,
            "page_count": document.page_count,
            "toc_entries": len(document.get_toc(simple=True)),
            "first_page_label": nonempty_labels[0] if nonempty_labels else None,
            "last_page_label": nonempty_labels[-1] if nonempty_labels else None,
        }
    if source.path.suffix.casefold() == ".pptx":
        record["slide_count"] = record.pop("page_count")
    if include_hash:
        record["sha256"] = sha256_file(source.path)
    return record


def collapsed_page_text(document: fitz.Document | PptxDocument, page_index: int) -> str:
    return " ".join(document[page_index].get_text("text").split())


def make_excerpt(text: str, normalized_queries: Sequence[str]) -> str:
    normalized = normalize_text(text)
    positions = [normalized.find(query) for query in normalized_queries]
    positions = [position for position in positions if position >= 0]
    start = max(0, (min(positions) if positions else 0) - 100)
    end = min(len(text), start + 420)
    excerpt = text[start:end]
    if start:
        excerpt = "…" + excerpt
    if end < len(text):
        excerpt += "…"
    return excerpt


def search_source(
    source: Source,
    queries: Sequence[str],
    match_mode: str,
) -> Iterable[dict[str, object]]:
    normalized_queries = [normalize_text(query) for query in queries]
    with open_source_document(source.path) as document:
        toc = document.get_toc(simple=True)
        for page_index in range(document.page_count):
            text = collapsed_page_text(document, page_index)
            normalized = normalize_text(text)
            matches = [query in normalized for query in normalized_queries]
            matched = all(matches) if match_mode == "all" else any(matches)
            if not matched:
                continue
            page_number = page_index + 1
            yield {
                "source_id": source.source_id,
                "kind": source.kind,
                "path": source.relative_path,
                ("slide_number" if isinstance(document, PptxDocument) else "pdf_page"): page_number,
                "page_label": page_label(document, page_number),
                "toc_title": toc_title(toc, page_number),
                "text_chars": len(text),
                "matched_queries": [query for query, did_match in zip(queries, matches) if did_match],
                "excerpt": make_excerpt(text, normalized_queries),
            }


def write_or_print(
    payload: dict[str, object],
    output: Path | None,
    force: bool,
    root: Path,
) -> None:
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if output is None:
        sys.stdout.write(serialized)
        return
    if output.suffix.casefold() != ".json":
        raise SystemExit("--output must use a .json filename.")
    if output.is_symlink():
        raise SystemExit(f"Refusing to replace a symlink output path: {output}")
    lexical_output = output.absolute()
    resolved_output = output.resolve()
    protected_names = {
        name.casefold()
        for directory_names in KIND_DIRECTORIES.values()
        for name in directory_names
    }
    for candidate in (lexical_output, resolved_output):
        try:
            relative = candidate.relative_to(root)
        except ValueError:
            continue
        if relative.parts and relative.parts[0].casefold() in protected_names:
            raise SystemExit(
                f"Refusing to write inventory output inside immutable source directory: {output}"
            )
    if lexical_output.exists() and not force:
        raise SystemExit(f"Refusing to overwrite {lexical_output}; pass --force to replace it.")
    lexical_output.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=lexical_output.parent,
            prefix=f".{lexical_output.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            stream.write(serialized)
            stream.flush()
            os.fsync(stream.fileno())
            temporary_name = stream.name
        os.replace(temporary_name, lexical_output)
    finally:
        if temporary_name is not None:
            Path(temporary_name).unlink(missing_ok=True)
    print(lexical_output)


def print_inventory_text(records: Sequence[dict[str, object]]) -> None:
    if not records:
        print("No PDF or PPTX sources found.")
        return
    for record in records:
        hash_suffix = f" sha256={record['sha256']}" if "sha256" in record else ""
        labels = ""
        if record["first_page_label"] or record["last_page_label"]:
            labels = f" labels={record['first_page_label']}..{record['last_page_label']}"
        count = (f"slides={record['slide_count']}" if "slide_count" in record
                 else f"pages={record['page_count']}")
        print(
            f"{record['source_id']} [{record['kind']}] {record['path']} "
            f"{count} toc={record['toc_entries']}{labels}{hash_suffix}"
        )


def print_search_text(matches: Sequence[dict[str, object]]) -> None:
    if not matches:
        print("No matching pages found.")
        return
    for match in matches:
        label = f" label={match['page_label']}" if match["page_label"] else ""
        title = f" title={match['toc_title']}" if match["toc_title"] else ""
        locator = (f"Slide {match['slide_number']}" if "slide_number" in match
                   else f"PDF p.{match['pdf_page']}")
        print(f"{match['path']} {locator}{label}{title}")
        print(f"  {match['excerpt']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    inventory = subparsers.add_parser("inventory", help="List discovered PDF and PPTX sources.")
    inventory.add_argument("--root", type=Path, default=Path.cwd())
    inventory.add_argument("--scope", action="append", choices=KNOWN_KINDS)
    inventory.add_argument("--hash", action="store_true", help="Include SHA-256 hashes.")
    inventory.add_argument("--format", choices=("text", "json"), default="text")
    inventory.add_argument("--output", type=Path, help="Write JSON output to a new file.")
    inventory.add_argument("--force", action="store_true", help="Replace --output if it exists.")

    search = subparsers.add_parser("search", help="Search PDF pages and PPTX slides.")
    search.add_argument("--root", type=Path, default=Path.cwd())
    search.add_argument("--query", action="append", required=True, help="Term or phrase; repeatable.")
    search.add_argument("--match", choices=("all", "any"), default="all")
    search.add_argument("--scope", action="append", choices=KNOWN_KINDS)
    search.add_argument("--max-results", type=int, default=30)
    search.add_argument("--format", choices=("text", "json"), default="text")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Repository root does not exist: {root}")
    scopes = set(args.scope) if args.scope else set(KNOWN_KINDS) - {"other"}
    discovery_errors: list[str] = []
    sources = find_sources(root, scopes, discovery_errors)

    if args.command == "inventory":
        records: list[dict[str, object]] = []
        source_errors = list(discovery_errors)
        for source in sources:
            try:
                records.append(source_inventory(source, args.hash))
            except Exception as exc:
                source_errors.append(f"Cannot inspect {source.relative_path}: {exc}")
        duplicates: dict[str, list[str]] = {}
        for record in records:
            duplicates.setdefault(str(record["source_id"]), []).append(str(record["path"]))
        duplicate_ids = {key: value for key, value in duplicates.items() if len(value) > 1}
        payload: dict[str, object] = {
            "schema_version": 2,
            "root": root.as_posix(),
            "sources": records,
            "duplicate_source_ids": duplicate_ids,
            "errors": source_errors,
        }
        if args.output or args.format == "json":
            write_or_print(payload, args.output, args.force, root)
        else:
            print_inventory_text(records)
            if duplicate_ids:
                print(f"WARNING: duplicate source IDs: {json.dumps(duplicate_ids, ensure_ascii=False)}")
            for message in source_errors:
                print(f"ERROR: {message}")
        return 2 if duplicate_ids or source_errors else 0

    matches: list[dict[str, object]] = []
    source_errors = list(discovery_errors)
    for source in sources:
        try:
            matches.extend(search_source(source, args.query, args.match))
        except Exception as exc:
            source_errors.append(f"Cannot search {source.relative_path}: {exc}")
            continue
        if len(matches) >= args.max_results:
            matches = matches[: args.max_results]
            break
    payload = {
        "schema_version": 2,
        "root": root.as_posix(),
        "queries": args.query,
        "match": args.match,
        "matches": matches,
        "errors": source_errors,
    }
    if args.format == "json":
        write_or_print(payload, None, False)
    else:
        print_search_text(matches)
        for message in source_errors:
            print(f"ERROR: {message}")
    if source_errors:
        return 2
    return 0 if matches else 1


if __name__ == "__main__":
    raise SystemExit(main())
