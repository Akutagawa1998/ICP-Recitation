#!/usr/bin/env python3
"""Validate an ICP recitation notebook pair and its native PDF/PPTX citations."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Sequence
from unittest.mock import patch

try:
    import nbformat
    from nbclient import NotebookClient
except ImportError as exc:  # pragma: no cover - dependency failure path
    raise SystemExit(
        "nbformat and nbclient are required. Install them with: "
        "python3 -m pip install nbformat nbclient"
    ) from exc

try:
    import pymupdf as fitz
except ImportError:  # pragma: no cover - compatibility path
    try:
        import fitz  # type: ignore[no-redef]
    except ImportError as exc:
        raise SystemExit(
            "PyMuPDF is required. Install it with: python3 -m pip install pymupdf"
        ) from exc

from course_sources import (
    PptxDocument, SUPPORTED_SCHEMA_VERSIONS, normalize_text, open_source_document,
    sha256_file, source_kind, toc_title,
)
from derive_student_notebook import REMOVAL_TAGS, derive_notebook, tags_for, validate_student_source


VALID_STATUSES = {"direct", "prerequisite", "unresolved"}
SOURCE_KINDS = {"lecture", "recitation", "textbook", "syllabus"}
EXERCISE_HEADING_RE = re.compile(
    r"(?im)^\s*(?:exercises?|questions?|problems?)\s+(\d+)\b[^\n]*"
)
SUBPART_RE = re.compile(r"(?m)^\s*(\d+)\)\s+")


def active_toc(document: fitz.Document, page_number: int) -> dict[int, str]:
    active: dict[int, str] = {}
    for entry in document.get_toc(simple=True):
        if len(entry) < 3 or int(entry[2]) > page_number:
            continue
        level = int(entry[0])
        active[level] = str(entry[1]).strip()
        for deeper in [known for known in active if known > level]:
            del active[deeper]
    return active


def anchor_word_count(value: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+", value))


def normalized_sha256(value: str) -> str:
    return hashlib.sha256(normalize_text(value).encode("utf-8")).hexdigest()


def numbered_exercise_blocks(document: fitz.Document) -> list[dict[str, object]]:
    """Extract standard numbered exercise blocks and their numbered subparts."""

    full_text = "\n".join(page.get_text("text") for page in document)
    matches = list(EXERCISE_HEADING_RE.finditer(full_text))
    blocks: list[dict[str, object]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(full_text)
        text = full_text[match.start() : end].strip()
        subpart_matches = list(SUBPART_RE.finditer(text))
        subparts: list[dict[str, str]] = []
        for sub_index, subpart_match in enumerate(subpart_matches):
            sub_end = (
                subpart_matches[sub_index + 1].start()
                if sub_index + 1 < len(subpart_matches)
                else len(text)
            )
            subpart_text = text[subpart_match.start() : sub_end].strip()
            subparts.append(
                {
                    "label": f"{subpart_match.group(1)})",
                    "prompt": subpart_text,
                    "original_prompt_sha256": normalized_sha256(subpart_text),
                }
            )
        blocks.append(
            {
                "number": int(match.group(1)),
                "prompt": text,
                "original_prompt_sha256": normalized_sha256(text),
                "subparts": subparts,
            }
        )
    return blocks


@dataclass(frozen=True)
class Issue:
    level: str
    code: str
    message: str


class Validator:
    def __init__(self, root: Path, allow_unresolved: bool) -> None:
        self.root = root.resolve()
        self.allow_unresolved = allow_unresolved
        self.issues: list[Issue] = []
        self._documents: dict[Path, fitz.Document | PptxDocument] = {}
        self._hashes: dict[Path, str] = {}
        self.registry: dict[str, dict[str, object]] = {}
        self.manifest_exercises: list[dict[str, object]] = []
        self.unresolved_count = 0
        self.schema_version = 1

    def close(self) -> None:
        for document in self._documents.values():
            document.close()

    def error(self, code: str, message: str) -> None:
        self.issues.append(Issue("error", code, message))

    def warning(self, code: str, message: str) -> None:
        self.issues.append(Issue("warning", code, message))

    def reject_unknown_fields(
        self,
        value: dict[str, object],
        allowed: set[str],
        context: str,
    ) -> None:
        unknown = sorted(str(key) for key in value if key not in allowed)
        if unknown:
            self.error(
                "schema.unknown_fields",
                f"{context}: unknown fields {unknown}; bump the schema and validator for extensions.",
            )

    def safe_source_path(self, relative_path: object, context: str) -> Path | None:
        if not isinstance(relative_path, str) or not relative_path.strip():
            self.error("source.path", f"{context}: missing repository-relative path.")
            return None
        candidate = (self.root / relative_path).resolve()
        try:
            candidate.relative_to(self.root)
        except ValueError:
            self.error("source.path_escape", f"{context}: path leaves repository root: {relative_path}")
            return None
        if not candidate.is_file():
            self.error("source.missing", f"{context}: source file does not exist: {relative_path}")
            return None
        supported = {".pdf", ".pptx"} if self.schema_version == 2 else {".pdf"}
        if candidate.suffix.casefold() not in supported:
            self.error("source.format", f"{context}: unsupported source format for schema {self.schema_version}: {relative_path}")
            return None
        return candidate

    def document(self, path: Path, context: str) -> fitz.Document | PptxDocument | None:
        if path not in self._documents:
            try:
                self._documents[path] = open_source_document(path)
            except Exception as exc:  # pragma: no cover - corrupt input path
                self.error("source.open", f"{context}: cannot open {path}: {exc}")
                return None
        return self._documents[path]

    def validate_hash(self, path: Path, expected: object, context: str) -> None:
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
            self.error("source.sha256", f"{context}: sha256 must be 64 lowercase hexadecimal characters.")
            return
        if path not in self._hashes:
            self._hashes[path] = sha256_file(path)
        if self._hashes[path] != expected:
            self.error("source.stale", f"{context}: source hash changed; remap citations for {path}.")

    def validate_page(
        self,
        document: fitz.Document | PptxDocument,
        page_value: object,
        context: str,
    ) -> int | None:
        field = "slide_number" if isinstance(document, PptxDocument) else "pdf_page"
        if not isinstance(page_value, int) or isinstance(page_value, bool):
            self.error(f"source.{field}", f"{context}: {field} must be a one-based integer.")
            return None
        if not 1 <= page_value <= document.page_count:
            self.error(
                "source.page_range",
                f"{context}: {field} {page_value} is outside 1..{document.page_count}.",
            )
            return None
        return page_value

    def validate_manifest(self, manifest: object) -> None:
        if not isinstance(manifest, dict):
            self.error("manifest.shape", "source-map.json must contain a JSON object.")
            return
        self.reject_unknown_fields(
            manifest,
            {
                "schema_version",
                "recitation_id",
                "title",
                "expected_exercise_count",
                "source_inventory",
                "recitation_source_id",
                "lecture_selection",
                "exercises",
            },
            "manifest",
        )
        version = manifest.get("schema_version")
        if type(version) is not int or version not in SUPPORTED_SCHEMA_VERSIONS:
            self.error("manifest.schema_version", "Manifest schema_version must be 1 or 2.")
        else:
            self.schema_version = version
        recitation_id = manifest.get("recitation_id")
        if not isinstance(recitation_id, str) or not recitation_id:
            self.error("manifest.recitation_id", "Manifest recitation_id must be a non-empty string.")
        title = manifest.get("title")
        if not isinstance(title, str) or not title.strip():
            self.error("manifest.title", "Manifest title must be a non-empty string.")

        inventory = manifest.get("source_inventory")
        if not isinstance(inventory, list) or not inventory:
            self.error("manifest.inventory", "Manifest source_inventory must be a non-empty list.")
            inventory = []
        seen_paths: set[str] = set()
        for index, record in enumerate(inventory, start=1):
            context = f"source_inventory record {index}"
            if not isinstance(record, dict):
                self.error("manifest.source_shape", f"{context}: expected an object.")
                continue
            self.reject_unknown_fields(
                record,
                {"source_id", "kind", "path", "sha256", "page_count"}
                | ({"slide_count"} if self.schema_version == 2 else set()),
                context,
            )
            source_id = record.get("source_id")
            kind = record.get("kind")
            relative_path = record.get("path")
            if not isinstance(source_id, str) or not source_id.strip():
                self.error("manifest.source_id", f"{context}: source_id is required.")
                continue
            if source_id in self.registry:
                self.error("manifest.source_id_duplicate", f"Duplicate source_id {source_id!r}.")
                continue
            if kind not in SOURCE_KINDS:
                self.error("manifest.source_kind", f"{context}: invalid kind {kind!r}.")
            if isinstance(relative_path, str):
                if relative_path in seen_paths:
                    self.error("manifest.source_path_duplicate", f"Duplicate source path {relative_path!r}.")
                seen_paths.add(relative_path)
                inferred = source_kind(Path(relative_path))
                if inferred != "other" and inferred != kind:
                    self.error(
                        "manifest.source_kind_path",
                        f"{context}: kind {kind!r} conflicts with path-derived kind {inferred!r}.",
                    )
            path = self.safe_source_path(relative_path, context)
            if path is not None:
                document = self.document(path, context)
                self.validate_hash(path, record.get("sha256"), context)
                is_pptx = path.suffix.casefold() == ".pptx"
                if is_pptx and kind != "lecture":
                    self.error("source.pptx_kind", f"{context}: schema 2 supports PPTX lecture sources only.")
                count_field = "slide_count" if is_pptx else "page_count"
                wrong_field = "page_count" if is_pptx else "slide_count"
                if wrong_field in record:
                    self.error("source.locator_format", f"{context}: {wrong_field} is invalid for this source format.")
                page_count = record.get(count_field)
                if not isinstance(page_count, int) or isinstance(page_count, bool):
                    self.error("manifest.page_count", f"{context}: {count_field} must be an integer.")
                elif document is not None and page_count != document.page_count:
                    self.error(
                        "manifest.page_count_stale",
                        f"{context}: {count_field} {page_count} does not match current {document.page_count}.",
                    )
            self.registry[source_id] = record

        recitation_source_id = manifest.get("recitation_source_id")
        recitation_record = self.registry.get(recitation_source_id) if isinstance(recitation_source_id, str) else None
        if recitation_record is None or recitation_record.get("kind") != "recitation":
            self.error(
                "manifest.recitation_source",
                "recitation_source_id must identify one recitation source in source_inventory.",
            )

        selection = manifest.get("lecture_selection")
        if not isinstance(selection, dict):
            self.error("manifest.lecture_selection", "lecture_selection object is required.")
        else:
            self.reject_unknown_fields(
                selection,
                {"candidate_source_ids", "selected_source_ids", "basis"},
                "lecture_selection",
            )
            candidates = selection.get("candidate_source_ids")
            selected = selection.get("selected_source_ids")
            basis = selection.get("basis")
            if not isinstance(candidates, list) or not candidates:
                self.error("manifest.lecture_candidates", "lecture candidate_source_ids must be non-empty.")
                candidates = []
            if not isinstance(selected, list) or not selected:
                self.error("manifest.lecture_selected", "lecture selected_source_ids must be non-empty.")
                selected = []
            valid_candidates: list[str] = []
            valid_selected: list[str] = []
            for field_name, values, valid_values in (
                ("candidate_source_ids", candidates, valid_candidates),
                ("selected_source_ids", selected, valid_selected),
            ):
                for item_index, source_id in enumerate(values, start=1):
                    if not isinstance(source_id, str) or not source_id.strip():
                        self.error(
                            "manifest.lecture_id_type",
                            f"lecture_selection.{field_name}[{item_index}] must be a non-empty string.",
                        )
                    else:
                        valid_values.append(source_id)
            for source_id in set(valid_candidates + valid_selected):
                record = self.registry.get(source_id)
                if record is None or record.get("kind") != "lecture":
                    self.error(
                        "manifest.lecture_source",
                        f"Lecture selection ID {source_id!r} is not a lecture source in inventory.",
                    )
            if not set(valid_selected).issubset(set(valid_candidates)):
                self.error("manifest.lecture_subset", "Selected lectures must be a subset of candidates.")
            if not isinstance(basis, list) or not basis:
                self.error("manifest.lecture_basis", "lecture_selection.basis must be non-empty.")
            else:
                for index, item in enumerate(basis, start=1):
                    if not isinstance(item, dict) or not isinstance(item.get("evidence"), str) or not item["evidence"].strip():
                        self.error(
                            "manifest.lecture_basis_item",
                            f"lecture_selection basis {index} needs non-empty evidence.",
                        )
                        continue
                    basis_kind = item.get("kind")
                    allowed_basis_fields = {"kind", "evidence"}
                    if basis_kind == "content":
                        allowed_basis_fields.add("source_ids")
                    elif basis_kind == "syllabus":
                        allowed_basis_fields.update({"source_id", "pdf_page", "locator", "anchor"})
                    self.reject_unknown_fields(
                        item,
                        allowed_basis_fields,
                        f"lecture_selection basis {index}",
                    )
                    if basis_kind not in {"content", "syllabus", "user"}:
                        self.error(
                            "manifest.lecture_basis_kind",
                            f"lecture_selection basis {index} has invalid kind {basis_kind!r}.",
                        )
                    if basis_kind == "content":
                        source_ids = item.get("source_ids")
                        if (
                            not isinstance(source_ids, list)
                            or not source_ids
                            or any(not isinstance(value, str) or not value for value in source_ids)
                        ):
                            self.error(
                                "manifest.lecture_basis_sources",
                                f"lecture_selection content basis {index} needs non-empty string source_ids.",
                            )
                        elif any(value not in self.registry for value in source_ids):
                            self.error(
                                "manifest.lecture_basis_source",
                                f"lecture_selection content basis {index} names an unknown source ID.",
                            )
                        else:
                            source_kinds = {self.registry[value].get("kind") for value in source_ids}
                            if not {"lecture", "recitation"}.issubset(source_kinds):
                                self.error(
                                    "manifest.lecture_basis_content_kinds",
                                    f"lecture_selection content basis {index} must compare at least "
                                    "one lecture and one recitation source.",
                                )
                            if not set(valid_selected).issubset(set(source_ids)):
                                self.error(
                                    "manifest.lecture_basis_selected",
                                    f"lecture_selection content basis {index} must name every selected lecture.",
                                )
                            if recitation_source_id not in source_ids:
                                self.error(
                                    "manifest.lecture_basis_recitation",
                                    f"lecture_selection content basis {index} must name the current recitation source.",
                                )
                    elif basis_kind == "syllabus":
                        syllabus_source_id = item.get("source_id")
                        if not isinstance(syllabus_source_id, str):
                            self.error(
                                "manifest.lecture_basis_syllabus_source",
                                f"lecture_selection syllabus basis {index} needs source_id.",
                            )
                        elif (
                            syllabus_source_id not in self.registry
                            or self.registry[syllabus_source_id].get("kind") != "syllabus"
                        ):
                            self.error(
                                "manifest.lecture_basis_syllabus_source",
                                f"lecture_selection syllabus basis {index} must name a syllabus source.",
                            )
                        if not isinstance(item.get("anchor"), str) or not item["anchor"].strip():
                            self.error(
                                "manifest.lecture_basis_syllabus_anchor",
                                f"lecture_selection syllabus basis {index} needs an anchor.",
                            )
                        if (
                            not isinstance(item.get("pdf_page"), int)
                            or isinstance(item.get("pdf_page"), bool)
                            or item["pdf_page"] < 1
                        ):
                            self.error(
                                "manifest.lecture_basis_syllabus_page",
                                f"lecture_selection syllabus basis {index} needs one-based pdf_page.",
                            )
                        if (
                            isinstance(syllabus_source_id, str)
                            and syllabus_source_id in self.registry
                            and self.registry[syllabus_source_id].get("kind") == "syllabus"
                        ):
                            syllabus_context = f"lecture_selection syllabus basis {index}"
                            syllabus_path = self.safe_source_path(
                                self.registry[syllabus_source_id].get("path"),
                                syllabus_context,
                            )
                            syllabus_document = (
                                self.document(syllabus_path, syllabus_context)
                                if syllabus_path is not None
                                else None
                            )
                            syllabus_page = (
                                self.validate_page(
                                    syllabus_document,
                                    item.get("pdf_page"),
                                    syllabus_context,
                                )
                                if syllabus_document is not None
                                else None
                            )
                            syllabus_anchor = item.get("anchor")
                            if (
                                syllabus_document is not None
                                and syllabus_page is not None
                                and isinstance(syllabus_anchor, str)
                                and syllabus_anchor.strip()
                                and normalize_text(syllabus_anchor)
                                not in normalize_text(
                                    syllabus_document[syllabus_page - 1].get_text("text")
                                )
                            ):
                                self.error(
                                    "manifest.lecture_basis_syllabus_anchor",
                                    f"{syllabus_context}: anchor is not on PDF page {syllabus_page}.",
                                )

        exercises = manifest.get("exercises")
        if not isinstance(exercises, list) or not exercises:
            self.error("manifest.exercises", "Manifest exercises must be a non-empty list.")
            exercises = []
        expected_count = manifest.get("expected_exercise_count")
        if expected_count != len(exercises):
            self.error(
                "manifest.exercise_count",
                f"expected_exercise_count {expected_count!r} does not match {len(exercises)} exercise records.",
            )
        seen_ids: set[str] = set()
        seen_subpart_ids: set[str] = set()
        for position, exercise in enumerate(exercises, start=1):
            context = f"manifest exercise {position}"
            if not isinstance(exercise, dict):
                self.error("manifest.exercise_shape", f"{context}: expected an object.")
                continue
            self.reject_unknown_fields(
                exercise,
                {
                    "exercise_id",
                    "order",
                    "prompt",
                    "original_prompt_sha256",
                    "subparts",
                    "concepts",
                    "recitation_source",
                    "references",
                    "notes",
                },
                context,
            )
            exercise_id = exercise.get("exercise_id")
            if not isinstance(exercise_id, str) or not exercise_id.strip():
                self.error("manifest.exercise_id", f"{context}: exercise_id is required.")
                continue
            if exercise_id in seen_ids:
                self.error("manifest.exercise_id_duplicate", f"Duplicate exercise_id {exercise_id!r}.")
            seen_ids.add(exercise_id)
            if exercise.get("order") != position:
                self.error(
                    "manifest.exercise_order",
                    f"{exercise_id}: order must be consecutive and equal {position}.",
                )
            prompt = exercise.get("prompt")
            if not isinstance(prompt, str) or len(normalize_text(prompt)) < 20:
                self.error("manifest.exercise_prompt", f"{exercise_id}: complete prompt text is required.")
            prompt_hash = exercise.get("original_prompt_sha256")
            if not isinstance(prompt_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", prompt_hash):
                self.error(
                    "manifest.exercise_prompt_hash",
                    f"{exercise_id}: original_prompt_sha256 must be 64 lowercase hex characters.",
                )
            subparts = exercise.get("subparts")
            if not isinstance(subparts, list):
                self.error("manifest.exercise_subparts", f"{exercise_id}: subparts must be a list.")
                subparts = []
            for subpart_index, subpart in enumerate(subparts, start=1):
                sub_context = f"{exercise_id} subpart {subpart_index}"
                if not isinstance(subpart, dict):
                    self.error("manifest.subpart_shape", f"{sub_context}: expected an object.")
                    continue
                self.reject_unknown_fields(
                    subpart,
                    {"subpart_id", "label", "prompt", "original_prompt_sha256"},
                    sub_context,
                )
                subpart_id = subpart.get("subpart_id")
                if not isinstance(subpart_id, str) or not subpart_id.strip():
                    self.error("manifest.subpart_id", f"{sub_context}: subpart_id is required.")
                elif subpart_id in seen_subpart_ids:
                    self.error("manifest.subpart_id_duplicate", f"Duplicate subpart_id {subpart_id!r}.")
                else:
                    seen_subpart_ids.add(subpart_id)
                label = subpart.get("label")
                if not isinstance(label, str) or not label.strip():
                    self.error("manifest.subpart_label", f"{sub_context}: label is required.")
                subpart_prompt = subpart.get("prompt")
                if not isinstance(subpart_prompt, str) or not normalize_text(subpart_prompt):
                    self.error("manifest.subpart_prompt", f"{sub_context}: complete prompt is required.")
                subpart_hash = subpart.get("original_prompt_sha256")
                if not isinstance(subpart_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", subpart_hash):
                    self.error(
                        "manifest.subpart_prompt_hash",
                        f"{sub_context}: original_prompt_sha256 must be 64 lowercase hex characters.",
                    )
            concepts_value = exercise.get("concepts")
            concepts: set[str] = set()
            if not isinstance(concepts_value, list) or not concepts_value:
                self.error("manifest.exercise_concepts", f"{exercise_id}: concepts must be non-empty.")
            else:
                for concept in concepts_value:
                    if not isinstance(concept, str) or not concept.strip():
                        self.error("manifest.exercise_concept", f"{exercise_id}: concepts must be strings.")
                    else:
                        concepts.add(concept)
            self.validate_recitation_source(exercise.get("recitation_source"), exercise_id)
            references = exercise.get("references")
            if not isinstance(references, list) or not references:
                self.error("manifest.exercise_references", f"{exercise_id}: references must be non-empty.")
                references = []
            coverage = {"lecture": set(), "textbook": set()}
            for ref_index, reference in enumerate(references, start=1):
                kind, covered = self.validate_reference(reference, exercise_id, ref_index, concepts)
                if kind in coverage:
                    coverage[kind].update(covered)
            for kind in ("lecture", "textbook"):
                missing = concepts - coverage[kind]
                if missing:
                    self.error(
                        "manifest.exercise_coverage",
                        f"{exercise_id}: {kind} references do not cover {sorted(missing)}.",
                    )
        if recitation_record is not None:
            recitation_path = self.safe_source_path(recitation_record.get("path"), "manifest recitation source")
            document = self.document(recitation_path, "manifest recitation source") if recitation_path else None
            if document is not None:
                blocks = numbered_exercise_blocks(document)
                detected = [int(block["number"]) for block in blocks]
                manifest_numbers: list[int] = []
                for exercise in exercises:
                    if isinstance(exercise, dict):
                        source = exercise.get("recitation_source", {})
                        label = source.get("item_label") if isinstance(source, dict) else None
                        match = re.search(r"\d+", str(label)) if label is not None else None
                        if match:
                            manifest_numbers.append(int(match.group()))
                if detected and detected != manifest_numbers:
                    self.error(
                        "manifest.source_exercise_count",
                        f"Recitation PDF exposes numbered items {detected}, but manifest records "
                        f"{manifest_numbers}.",
                    )
                elif not detected:
                    self.error(
                        "manifest.source_exercise_manual",
                        "No standard numbered exercise headings were detected; automatic completeness "
                        "cannot be established. Extend the format-specific extractor before classroom use.",
                    )
                if len(set(detected)) != len(detected):
                    self.error(
                        "manifest.source_exercise_duplicate",
                        f"Recitation PDF repeats numbered headings {detected}; source spans are ambiguous.",
                    )
                block_by_number = {
                    int(block["number"]): block
                    for block in blocks
                    if detected.count(int(block["number"])) == 1
                }
                for exercise in exercises:
                    if not isinstance(exercise, dict):
                        continue
                    exercise_id = str(exercise.get("exercise_id", "<unknown>"))
                    source = exercise.get("recitation_source", {})
                    label = source.get("item_label") if isinstance(source, dict) else None
                    number_match = re.search(r"\d+", str(label)) if label is not None else None
                    if number_match is None:
                        continue
                    block = block_by_number.get(int(number_match.group()))
                    if block is None:
                        continue
                    source_hash = str(block["original_prompt_sha256"])
                    declared_hash = exercise.get("original_prompt_sha256")
                    if declared_hash != source_hash:
                        self.error(
                            "manifest.exercise_source_hash",
                            f"{exercise_id}: original_prompt_sha256 does not match the extracted PDF block.",
                        )
                    prompt = exercise.get("prompt")
                    if isinstance(prompt, str) and normalized_sha256(prompt) != source_hash:
                        self.error(
                            "manifest.exercise_prompt_truncated",
                            f"{exercise_id}: prompt is not a complete normalized transcription of its PDF block.",
                        )
                    declared_subparts = exercise.get("subparts")
                    source_subparts = block.get("subparts", [])
                    if not isinstance(declared_subparts, list):
                        continue
                    if len(declared_subparts) != len(source_subparts):
                        self.error(
                            "manifest.subpart_count",
                            f"{exercise_id}: PDF exposes {len(source_subparts)} numbered subparts, "
                            f"manifest records {len(declared_subparts)}.",
                        )
                    for subpart_index, (declared, extracted) in enumerate(
                        zip(declared_subparts, source_subparts),
                        start=1,
                    ):
                        if not isinstance(declared, dict) or not isinstance(extracted, dict):
                            continue
                        subpart_id = declared.get("subpart_id", f"subpart {subpart_index}")
                        for field in ("label", "original_prompt_sha256"):
                            if declared.get(field) != extracted.get(field):
                                self.error(
                                    f"manifest.subpart_{field}",
                                    f"{exercise_id} {subpart_id}: {field} does not match the PDF block.",
                                )
                        declared_prompt = declared.get("prompt")
                        extracted_hash = extracted.get("original_prompt_sha256")
                        if (
                            isinstance(declared_prompt, str)
                            and normalized_sha256(declared_prompt) != extracted_hash
                        ):
                            self.error(
                                "manifest.subpart_prompt_truncated",
                                f"{exercise_id} {subpart_id}: prompt is not a complete normalized "
                                "transcription of the PDF subpart.",
                            )
        self.manifest_exercises = [item for item in exercises if isinstance(item, dict)]

    def registry_record(
        self,
        source_id: object,
        kind: str,
        context: str,
    ) -> dict[str, object] | None:
        if not isinstance(source_id, str) or not source_id.strip():
            self.error("reference.source_id", f"{context}: source_id is required for resolved references.")
            return None
        record = self.registry.get(source_id)
        if record is None:
            self.error("reference.source_registry", f"{context}: unknown source_id {source_id!r}.")
            return None
        if record.get("kind") != kind:
            self.error(
                "reference.source_kind",
                f"{context}: source_id {source_id!r} is {record.get('kind')!r}, not {kind!r}.",
            )
        return record

    def validate_reference(
        self,
        reference: object,
        exercise_id: str,
        index: int,
        concepts: set[str],
    ) -> tuple[str | None, set[str]]:
        context = f"{exercise_id} reference {index}"
        if not isinstance(reference, dict):
            self.error("reference.shape", f"{context}: reference must be an object.")
            return None, set()
        kind = reference.get("kind")
        if kind not in {"lecture", "textbook"}:
            self.error("reference.kind", f"{context}: kind must be lecture or textbook.")
            return None, set()
        covers_value = reference.get("covers")
        covers: set[str] = set()
        if not isinstance(covers_value, list) or not covers_value:
            self.error("reference.covers", f"{context}: covers must be a non-empty list.")
        else:
            for concept in covers_value:
                if not isinstance(concept, str) or not concept.strip():
                    self.error("reference.covers_value", f"{context}: covers values must be non-empty strings.")
                    continue
                covers.add(concept)
                if concept not in concepts:
                    self.error(
                        "reference.covers_unknown",
                        f"{context}: covers value {concept!r} is not declared in exercise concepts.",
                    )
        status = reference.get("status")
        if status not in VALID_STATUSES:
            self.error("reference.status", f"{context}: invalid status {status!r}.")
            return str(kind), covers
        if status == "unresolved":
            self.unresolved_count += 1
            self.reject_unknown_fields(
                reference,
                {"kind", "status", "covers", "source_id", "note", "approval"},
                context,
            )
            source_id = reference.get("source_id")
            if source_id is not None:
                record = self.registry.get(source_id) if isinstance(source_id, str) else None
                if record is None:
                    self.error("reference.unresolved_source", f"{context}: unknown source_id {source_id!r}.")
                elif record.get("kind") != kind:
                    self.error(
                        "reference.unresolved_kind",
                        f"{context}: source_id {source_id!r} is not a {kind} source.",
                    )
            forbidden = {
                "path",
                "sha256",
                "pdf_page",
                "page_label",
                "printed_page",
                "locator",
                "anchor",
                "title",
                "chapter",
                "section",
                "section_status",
                "section_note",
            }
            invented = sorted(forbidden & set(reference))
            if invented:
                self.error(
                    "reference.unresolved_fields",
                    f"{context}: unresolved reference must omit locator fields {invented}.",
                )
            note = reference.get("note")
            if not isinstance(note, str) or not note.strip():
                self.error("reference.unresolved_note", f"{context}: unresolved reference needs a note.")
            approval = reference.get("approval")
            approved = False
            if isinstance(approval, dict):
                self.reject_unknown_fields(
                    approval,
                    {"decision", "approver", "date", "note"},
                    f"{context} approval",
                )
                approver = approval.get("approver")
                approval_note = approval.get("note")
                approval_date = approval.get("date")
                approved = (
                    approval.get("decision") == "approved"
                    and approver == "TA"
                    and isinstance(approval_note, str)
                    and bool(approval_note.strip())
                    and isinstance(approval_date, str)
                )
                if approved:
                    try:
                        date.fromisoformat(approval_date)
                    except ValueError:
                        approved = False
            message = f"{context}: unresolved {kind} mapping."
            if self.allow_unresolved and approved:
                self.warning("reference.unresolved", message)
            elif self.allow_unresolved:
                self.error(
                    "reference.unresolved_approval",
                    message + " A persisted TA approval object is required.",
                )
            else:
                self.error("reference.unresolved", message + " Use --allow-unresolved only after TA review.")
            return str(kind), covers

        resolved_fields = {
            "kind",
            "status",
            "covers",
            "source_id",
            "path",
            "sha256",
            "pdf_page",
            "page_label",
            "locator",
            "title",
            "anchor",
            "note",
        }
        if self.schema_version == 2 and kind == "lecture":
            resolved_fields.add("slide_number")
        if kind == "textbook":
            resolved_fields.update(
                {"chapter", "section", "section_status", "section_note", "printed_page"}
            )
        self.reject_unknown_fields(reference, resolved_fields, context)

        source_id = reference.get("source_id")
        registry_record = self.registry_record(source_id, str(kind), context)
        if registry_record is not None:
            for field in ("path", "sha256"):
                if reference.get(field) != registry_record.get(field):
                    self.error(
                        "reference.registry_mismatch",
                        f"{context}: {field} does not match source_inventory for {source_id!r}.",
                    )
        path = self.safe_source_path(reference.get("path"), context)
        if path is None:
            return str(kind), covers
        document = self.document(path, context)
        if document is None:
            return str(kind), covers
        is_pptx = isinstance(document, PptxDocument)
        forbidden_locators = {"pdf_page", "page_label", "printed_page"} if is_pptx else {"slide_number"}
        if forbidden_locators & set(reference):
            self.error("reference.locator_format", f"{context}: locator fields disagree with the native source format.")
        field = "slide_number" if is_pptx else "pdf_page"
        page_number = self.validate_page(document, reference.get(field), context)
        self.validate_hash(path, reference.get("sha256"), context)
        if page_number is None:
            return str(kind), covers

        title = reference.get("title")
        if not isinstance(title, str) or not title.strip():
            self.error("reference.title", f"{context}: title is required.")
        anchor = reference.get("anchor")
        if not isinstance(anchor, str) or not anchor.strip():
            self.error("reference.anchor", f"{context}: a short anchor is required.")
        else:
            word_count = anchor_word_count(anchor)
            if len(anchor.strip()) < 8 or not 2 <= word_count <= 16:
                self.error(
                    "reference.anchor_length",
                    f"{context}: anchor must be distinctive (2-16 words and at least 8 characters).",
                )
            page_text = document[page_number - 1].get_text("text")
            if normalize_text(anchor) not in normalize_text(page_text):
                self.error(
                    "reference.anchor_missing",
                    f"{context}: anchor not found at {field} {page_number}: {anchor!r}.",
                )

        actual_label = document[page_number - 1].get_label().strip()
        declared_label = reference.get("page_label")
        if declared_label is not None and str(declared_label) != actual_label:
            self.error(
                "reference.page_label",
                f"{context}: declared page_label {declared_label!r} does not match {actual_label!r}.",
            )

        locator = reference.get("locator")
        if kind == "lecture" and (not isinstance(locator, str) or not locator.strip()):
            self.error("reference.locator", f"{context}: lecture locator is required.")
        elif is_pptx and locator != f"Slide {page_number}":
            self.error("reference.locator", f"{context}: PPTX locator must be 'Slide {page_number}'.")
        elif locator:
            page_toc = toc_title(document.get_toc(simple=True), page_number)
            if page_toc and normalize_text(str(locator)) not in normalize_text(page_toc):
                self.error(
                    "reference.locator",
                    f"{context}: locator {locator!r} does not match page TOC title {page_toc!r}.",
                )

        if kind == "textbook":
            chapter = reference.get("chapter")
            section = reference.get("section")
            if not isinstance(chapter, str) or not chapter.strip():
                self.error("reference.chapter", f"{context}: textbook chapter is required.")
            toc_entries = document.get_toc(simple=True)
            toc_text = [normalize_text(str(entry[1])) for entry in toc_entries]
            active = active_toc(document, page_number)
            numbered_section_entries = [
                entry for entry in toc_text if re.match(r"^\d+\.\d+\s*:", entry)
            ]
            has_numbered_sections = bool(numbered_section_entries)
            if isinstance(chapter, str) and chapter.strip():
                chapter_match = re.search(r"\d+", chapter)
                if not chapter_match:
                    self.error(
                        "reference.chapter_number",
                        f"{context}: chapter must contain a chapter number: {chapter!r}.",
                    )
                else:
                    chapter_number = int(chapter_match.group())
                    chapter_pattern = re.compile(rf"^(?:chapter\s+)?{chapter_number}\s*:")
                    if toc_entries:
                        active_chapter = next(
                            (
                                title
                                for level, title in sorted(active.items())
                                if re.match(r"^\d+\s*:", normalize_text(title))
                            ),
                            None,
                        )
                        if active_chapter and not chapter_pattern.search(normalize_text(active_chapter)):
                            self.error(
                                "reference.chapter_page",
                                f"{context}: page belongs to {active_chapter!r}, not {chapter!r}.",
                            )
                        elif not any(chapter_pattern.search(entry) for entry in toc_text):
                            self.error(
                                "reference.chapter_toc",
                                f"{context}: {chapter!r} was not found in the PDF table of contents.",
                            )
                    elif normalize_text(str(chapter_number)) not in normalize_text(document[page_number - 1].get_text("text")):
                        self.warning(
                            "reference.chapter_manual",
                            f"{context}: PDF has no TOC; chapter needs manual visual confirmation.",
                        )
                    if isinstance(section, str):
                        section_match = re.match(r"\s*(\d+)\.", section)
                        if section_match and int(section_match.group(1)) != chapter_number:
                            self.error(
                                "reference.chapter_section",
                                f"{context}: chapter {chapter_number} conflicts with section {section!r}.",
                            )
            if has_numbered_sections:
                if reference.get("section_status") == "not_exposed":
                    self.error(
                        "reference.section_bypass",
                        f"{context}: PDF exposes numbered sections; not_exposed is invalid.",
                    )
                if not isinstance(section, str) or not section.strip():
                    self.error("reference.section", f"{context}: numbered textbook section is required.")
                else:
                    declared_match = re.match(r"\s*(\d+\.\d+)\s*:\s*(.+?)\s*$", section)
                    if declared_match is None:
                        self.error(
                            "reference.section_number",
                            f"{context}: section must include its number and title, for example '1.5: Using Python'.",
                        )
                    else:
                        declared_number = declared_match.group(1)
                        # Checkpoint children can repeat a section number; the active
                        # parent section remains a valid, more useful citation title.
                        active_sections = [
                            normalize_text(title)
                            for title in active.values()
                            if re.match(r"^\d+\.\d+\s*:", normalize_text(title))
                        ]
                        if not active_sections:
                            self.error(
                                "reference.section_page_unknown",
                                f"{context}: no active numbered section was found at PDF page {page_number}.",
                            )
                        else:
                            active_section = active_sections[-1]
                            active_match = re.match(r"(\d+\.\d+)\s*:\s*(.+)$", active_section)
                            if active_match is None:
                                self.error(
                                    "reference.section_page_unknown",
                                    f"{context}: cannot parse active section {active_section!r}.",
                                )
                            elif (
                                declared_number != active_match.group(1)
                                or normalize_text(f"{declared_number}: {declared_match.group(2)}")
                                not in active_sections
                            ):
                                self.error(
                                    "reference.section_page",
                                    f"{context}: page's active section {active_section!r} "
                                    f"does not exactly match {section!r}.",
                                )
                        declared_normalized = normalize_text(
                            f"{declared_number}: {declared_match.group(2)}"
                        )
                        if declared_normalized not in numbered_section_entries:
                            self.error(
                                "reference.section_toc",
                                f"{context}: section {section!r} was not found exactly in the PDF TOC.",
                            )
            elif section is None:
                if reference.get("section_status") != "not_exposed":
                    self.error(
                        "reference.section_status",
                        f"{context}: section=null requires section_status='not_exposed'.",
                    )
                section_note = reference.get("section_note")
                if not isinstance(section_note, str) or not section_note.strip():
                    self.error(
                        "reference.section_note",
                        f"{context}: section=null requires a non-empty section_note.",
                    )
            elif not isinstance(section, str) or not section.strip():
                self.error("reference.section", f"{context}: textbook section must be text or null.")
            elif normalize_text(section) not in normalize_text(
                document[page_number - 1].get_text("text")
            ):
                self.error(
                    "reference.section_manual",
                    f"{context}: unnumbered section title was not found on the cited page.",
                )
            printed_page = reference.get("printed_page")
            if printed_page is not None and actual_label and str(printed_page) != actual_label:
                self.error(
                    "reference.printed_page",
                    f"{context}: printed_page {printed_page!r} does not match PDF label {actual_label!r}.",
                )

        return str(kind), covers

    def validate_recitation_source(self, source: object, exercise_id: str) -> None:
        context = f"{exercise_id} recitation source"
        if not isinstance(source, dict):
            self.error("recitation_source.shape", f"{context}: metadata object is required.")
            return
        self.reject_unknown_fields(
            source,
            {"source_id", "path", "sha256", "pdf_page", "item_label", "anchor"},
            context,
        )
        source_id = source.get("source_id")
        record = self.registry_record(source_id, "recitation", context)
        if record is not None:
            for field in ("path", "sha256"):
                if source.get(field) != record.get(field):
                    self.error(
                        "recitation_source.registry_mismatch",
                        f"{context}: {field} does not match source_inventory for {source_id!r}.",
                    )
        path = self.safe_source_path(source.get("path"), context)
        if path is None:
            return
        document = self.document(path, context)
        if document is not None:
            page_number = self.validate_page(document, source.get("pdf_page"), context)
            self.validate_hash(path, source.get("sha256"), context)
            anchor = source.get("anchor")
            if not isinstance(anchor, str) or not anchor.strip():
                self.error("recitation_source.anchor", f"{context}: a short anchor is required.")
            elif page_number is not None:
                if len(anchor.strip()) < 8 or not 2 <= anchor_word_count(anchor) <= 16:
                    self.error(
                        "recitation_source.anchor_length",
                        f"{context}: anchor must be distinctive (2-16 words and at least 8 characters).",
                    )
                page_text = document[page_number - 1].get_text("text")
                if normalize_text(anchor) not in normalize_text(page_text):
                    self.error(
                        "recitation_source.anchor_missing",
                        f"{context}: anchor not found on PDF page {page_number}: {anchor!r}.",
                    )
        label = source.get("item_label")
        if not isinstance(label, str) or not label.strip():
            self.error("recitation_source.label", f"{context}: item_label is required.")


def validate_notebook_metadata(
    validator: Validator,
    notebook: nbformat.NotebookNode,
    expected_variant: str,
    label: str,
    manifest: dict[str, object],
    manifest_name: str,
) -> None:
    try:
        nbformat.validate(notebook)
    except Exception as exc:
        validator.error("notebook.schema", f"{label}: nbformat validation failed: {exc}")
    metadata = notebook.get("metadata", {})
    if not isinstance(metadata, dict):
        validator.error("notebook.metadata", f"{label}: metadata must be an object.")
        return
    icp = metadata.get("icp")
    if not isinstance(icp, dict):
        validator.error("notebook.icp", f"{label}: missing metadata.icp.")
        return
    version = icp.get("schema_version")
    if type(version) is not int or version not in SUPPORTED_SCHEMA_VERSIONS:
        validator.error("notebook.schema_version", f"{label}: schema_version must be 1 or 2.")
    elif version != manifest.get("schema_version"):
        validator.error("notebook.schema_version", f"{label}: schema_version must match source-map.json.")
    if not isinstance(icp.get("recitation_id"), str) or not icp.get("recitation_id"):
        validator.error("notebook.recitation_id", f"{label}: recitation_id must be a non-empty string.")
    if icp.get("variant") != expected_variant:
        validator.error(
            "notebook.variant",
            f"{label}: expected variant {expected_variant!r}, found {icp.get('variant')!r}.",
        )
    if icp.get("recitation_id") != manifest.get("recitation_id"):
        validator.error("notebook.manifest_id", f"{label}: recitation_id differs from source-map.json.")
    if icp.get("title") != manifest.get("title"):
        validator.error("notebook.manifest_title", f"{label}: title differs from source-map.json.")
    if icp.get("source_map") != manifest_name:
        validator.error(
            "notebook.source_map",
            f"{label}: metadata.icp.source_map must be {manifest_name!r}.",
        )
    kernelspec = metadata.get("kernelspec", {})
    if not isinstance(kernelspec, dict) or kernelspec.get("name") != "python3":
        validator.error("notebook.kernel", f"{label}: kernelspec.name must be 'python3'.")


def validate_source_map_markdown(
    validator: Validator,
    manifest_path: Path,
    manifest: dict[str, object],
) -> None:
    markdown_path = manifest_path.with_suffix(".md")
    if not markdown_path.is_file():
        validator.error("source_map.markdown_missing", f"Missing human-readable source map: {markdown_path}")
        return
    text = markdown_path.read_text(encoding="utf-8")
    normalized = normalize_text(text)
    for exercise in manifest.get("exercises", []):
        if isinstance(exercise, dict):
            exercise_id = exercise.get("exercise_id")
            if isinstance(exercise_id, str) and normalize_text(exercise_id) not in normalized:
                validator.error(
                    "source_map.exercise_missing",
                    f"source-map.md omits exercise ID {exercise_id!r}.",
                )
            for subpart in exercise.get("subparts", []):
                subpart_id = subpart.get("subpart_id") if isinstance(subpart, dict) else None
                if isinstance(subpart_id, str) and normalize_text(subpart_id) not in normalized:
                    validator.error(
                        "source_map.subpart_missing",
                        f"source-map.md omits subpart ID {subpart_id!r}.",
                    )
    selection = manifest.get("lecture_selection", {})
    if isinstance(selection, dict):
        for source_id in selection.get("selected_source_ids", []):
            if isinstance(source_id, str) and normalize_text(source_id) not in normalized:
                validator.error(
                    "source_map.lecture_missing",
                    f"source-map.md omits selected lecture {source_id!r}.",
                )


def validate_cell_ids(validator: Validator, notebook: nbformat.NotebookNode, label: str) -> None:
    seen: set[str] = set()
    for index, cell in enumerate(notebook.cells, start=1):
        cell_id = cell.get("id")
        if not isinstance(cell_id, str) or not cell_id:
            validator.error("cell.id", f"{label} cell {index}: stable cell id is required.")
        elif cell_id in seen:
            validator.error("cell.id_duplicate", f"{label}: duplicate cell id {cell_id!r}.")
        else:
            seen.add(cell_id)


def validate_visible_reference(
    validator: Validator,
    source_text: str,
    reference: object,
    exercise_id: str,
    index: int,
) -> None:
    if not isinstance(reference, dict):
        return
    normalized = normalize_text(source_text)
    context = f"{exercise_id} visible reference {index}"
    kind = str(reference.get("kind", ""))
    status = str(reference.get("status", ""))
    if kind not in normalized:
        validator.error("exercise.visible_kind", f"{context}: visible block omits {kind!r}.")
    if status not in normalized:
        validator.error("exercise.visible_status", f"{context}: visible block omits status {status!r}.")
    if status == "unresolved":
        if "no direct coverage located" not in normalized:
            validator.error(
                "exercise.visible_unresolved",
                f"{context}: unresolved mapping must visibly say 'No direct coverage located'.",
            )
        return
    slide_number = reference.get("slide_number")
    page_number = reference.get("pdf_page")
    page_tokens = ((f"slide {slide_number}",) if slide_number is not None else
                   (f"pdf p. {page_number}", f"pdf page {page_number}"))
    if not any(normalize_text(token) in normalized for token in page_tokens):
        validator.error("exercise.visible_page", f"{context}: visible block omits native locator {page_tokens[0]}.")
    if kind == "lecture" and reference.get("locator"):
        if normalize_text(str(reference["locator"])) not in normalized:
            validator.error(
                "exercise.visible_locator",
                f"{context}: visible block omits locator {reference['locator']!r}.",
            )
    if kind == "textbook":
        for field in ("chapter", "section"):
            value = reference.get(field)
            visible = True
            if value and field == "section":
                match = re.match(r"\s*(\d+\.\d+)\s*:\s*(.*)", str(value))
                if match:
                    visible = (
                        normalize_text(match.group(1)) in normalized
                        and normalize_text(match.group(2)) in normalized
                    )
                else:
                    visible = normalize_text(str(value)) in normalized
            elif value:
                visible = normalize_text(str(value)) in normalized
            if value and not visible:
                validator.error(
                    f"exercise.visible_{field}",
                    f"{context}: visible block omits {field} {value!r}.",
                )
        printed_page = reference.get("printed_page")
        if printed_page is not None:
            printed_tokens = (
                f"printed p. {printed_page}",
                f"printed page {printed_page}",
            )
            if not any(normalize_text(token) in normalized for token in printed_tokens):
                validator.error(
                    "exercise.visible_printed_page",
                    f"{context}: visible block omits printed page {printed_page}.",
                )
        if reference.get("section") is None and reference.get("section_status") == "not_exposed":
            if "no section hierarchy" not in normalized:
                validator.error(
                    "exercise.visible_section_status",
                    f"{context}: visible block must say 'no section hierarchy'.",
                )


def validate_instructor_cells(validator: Validator, notebook: nbformat.NotebookNode) -> None:
    expected = validator.manifest_exercises
    expected_ids = [str(item.get("exercise_id")) for item in expected]
    prompt_cells: list[tuple[int, nbformat.NotebookNode]] = []
    solution_units: list[tuple[str, str | None]] = []
    required_tags = {"learning-goals", "lecture-review", "review-example", "recap"}
    seen_required: set[str] = set()

    for index, cell in enumerate(notebook.cells, start=1):
        tags = tags_for(cell)
        seen_required.update(required_tags & tags)
        metadata = cell.get("metadata", {})
        if not isinstance(metadata, dict):
            validator.error("cell.metadata", f"Instructor cell {index}: metadata must be an object.")
            metadata = {}
        icp = metadata.get("icp", {})
        if cell.get("attachments"):
            validator.error(
                "cell.attachments",
                f"Instructor cell {index}: embedded attachments are forbidden; use local asset files.",
            )
        if "exercise-prompt" in tags:
            if tags & (REMOVAL_TAGS | {"solution"}):
                validator.error(
                    "exercise.conflicting_tags",
                    f"Instructor cell {index}: exercise-prompt cannot be removable or a solution.",
                )
            if cell.cell_type != "markdown":
                validator.error("exercise.type", f"Instructor cell {index}: exercise-prompt must be Markdown.")
            prompt_cells.append((index, cell))
        if "review-example" in tags and cell.cell_type != "code":
            validator.error("review.example_type", f"Instructor cell {index}: review-example must be code.")
        if "solution" in tags:
            if tags & REMOVAL_TAGS:
                validator.error(
                    "solution.conflicting_tags",
                    f"Instructor cell {index}: solution cannot also use a removal tag.",
                )
            if cell.cell_type != "code":
                validator.error("solution.type", f"Instructor cell {index}: solution tag is only for code cells.")
                continue
            if not isinstance(icp, dict):
                validator.error("solution.metadata", f"Instructor cell {index}: missing metadata.icp.")
                continue
            exercise_id = icp.get("exercise_id")
            if icp.get("role") != "solution":
                validator.error("solution.role", f"Instructor cell {index}: role must be 'solution'.")
            if not isinstance(exercise_id, str) or not exercise_id:
                validator.error("solution.exercise_id", f"Instructor cell {index}: exercise_id is required.")
            else:
                subpart_id = icp.get("subpart_id")
                if subpart_id is not None and (
                    not isinstance(subpart_id, str) or not subpart_id.strip()
                ):
                    validator.error(
                        "solution.subpart_id",
                        f"Instructor cell {index}: subpart_id must be a non-empty string when present.",
                    )
                else:
                    solution_units.append((exercise_id, subpart_id))
            student_source = icp.get("student_source")
            if not isinstance(student_source, str) or not student_source.strip():
                validator.error("solution.student_source", f"Instructor cell {index}: student_source is required.")
            else:
                try:
                    validate_student_source(
                        student_source,
                        str(cell.source),
                        str(cell.get("id", f"cell-{index}")),
                    )
                except ValueError as exc:
                    validator.error("solution.student_source_safety", str(exc))

    missing_sections = required_tags - seen_required
    if missing_sections:
        validator.error(
            "notebook.teaching_sequence",
            f"Instructor notebook is missing required teaching tags {sorted(missing_sections)}.",
        )
    if len(prompt_cells) != len(expected):
        validator.error(
            "exercise.prompt_count",
            f"Instructor has {len(prompt_cells)} prompts; manifest requires {len(expected)}.",
        )

    for position, ((cell_index, cell), manifest_exercise) in enumerate(
        zip(prompt_cells, expected),
        start=1,
    ):
        metadata = cell.get("metadata", {})
        icp = metadata.get("icp", {}) if isinstance(metadata, dict) else {}
        exercise_id = manifest_exercise.get("exercise_id")
        if not isinstance(icp, dict):
            validator.error("exercise.metadata", f"Instructor cell {cell_index}: metadata.icp must be an object.")
            continue
        if icp.get("exercise_id") != exercise_id:
            validator.error(
                "exercise.order",
                f"Prompt {position} ID {icp.get('exercise_id')!r} does not match manifest {exercise_id!r}.",
            )
        if icp.get("role") != "prompt":
            validator.error("exercise.role", f"{exercise_id}: role must be 'prompt'.")
        for field in ("concepts", "recitation_source", "references"):
            if icp.get(field) != manifest_exercise.get(field):
                validator.error(
                    "exercise.manifest_mismatch",
                    f"{exercise_id}: notebook {field} differs from source-map.json.",
                )
        prompt = manifest_exercise.get("prompt")
        if isinstance(prompt, str) and normalize_text(prompt) not in normalize_text(str(cell.source)):
            validator.error(
                "exercise.prompt_text",
                f"{exercise_id}: notebook does not contain the complete manifest prompt text.",
            )
        source_text = str(cell.source)
        if "Knowledge references" not in source_text and "知识点出处" not in source_text:
            validator.error(
                "exercise.visible_references",
                f"{exercise_id}: prompt cell needs a visible Knowledge references block.",
            )
        references = manifest_exercise.get("references", [])
        if isinstance(references, list):
            for ref_index, reference in enumerate(references, start=1):
                validate_visible_reference(validator, source_text, reference, str(exercise_id), ref_index)

    solution_exercise_ids = {exercise_id for exercise_id, _ in solution_units}
    for exercise in expected:
        exercise_id = str(exercise.get("exercise_id"))
        declared_subparts = exercise.get("subparts", [])
        expected_subpart_ids = {
            str(subpart.get("subpart_id"))
            for subpart in declared_subparts
            if isinstance(subpart, dict) and isinstance(subpart.get("subpart_id"), str)
        }
        actual_subpart_ids = {
            subpart_id
            for actual_exercise_id, subpart_id in solution_units
            if actual_exercise_id == exercise_id and subpart_id is not None
        }
        if expected_subpart_ids:
            for subpart_id in sorted(expected_subpart_ids - actual_subpart_ids):
                validator.error(
                    "solution.subpart_missing",
                    f"{exercise_id} {subpart_id}: at least one solution code cell is required.",
                )
            for subpart_id in sorted(actual_subpart_ids - expected_subpart_ids):
                validator.error(
                    "solution.subpart_orphan",
                    f"{exercise_id}: solution references unknown subpart_id {subpart_id!r}.",
                )
        elif exercise_id not in solution_exercise_ids:
            validator.error("solution.missing", f"{exercise_id}: at least one solution code cell is required.")
        elif actual_subpart_ids:
            validator.error(
                "solution.subpart_unexpected",
                f"{exercise_id}: solution declares subparts but the manifest has none.",
            )
    for exercise_id in solution_exercise_ids - set(expected_ids):
        validator.error("solution.orphan", f"Solution references unknown exercise_id {exercise_id!r}.")


def compare_pair(
    validator: Validator,
    instructor: nbformat.NotebookNode,
    student: nbformat.NotebookNode,
) -> None:
    try:
        expected = derive_notebook(instructor)
    except (ValueError, TypeError, AttributeError) as exc:
        validator.error("pair.derive", f"Cannot derive expected student notebook: {exc}")
        return
    instructor_metadata = instructor.get("metadata", {})
    student_metadata = student.get("metadata", {})
    instructor_icp = instructor_metadata.get("icp", {}) if isinstance(instructor_metadata, dict) else {}
    student_icp = student_metadata.get("icp", {}) if isinstance(student_metadata, dict) else {}
    if not isinstance(instructor_icp, dict) or not isinstance(student_icp, dict):
        validator.error("pair.icp_metadata", "Both notebook metadata.icp values must be objects.")
        return
    if instructor_icp.get("recitation_id") != student_icp.get("recitation_id"):
        validator.error("pair.recitation_id", "Instructor and student recitation IDs differ.")
    if not isinstance(student_metadata, dict) or dict(expected.metadata) != dict(student_metadata):
        validator.error("pair.notebook_metadata", "Student notebook metadata differs from official derivation.")
    if len(expected.cells) != len(student.cells):
        validator.error(
            "pair.cell_count",
            f"Student has {len(student.cells)} cells; deterministic derivation expects {len(expected.cells)}.",
        )
        return
    for index, (expected_cell, actual_cell) in enumerate(zip(expected.cells, student.cells), start=1):
        if dict(expected_cell) != dict(actual_cell):
            validator.error("pair.cell_mismatch", f"Student cell {index} differs from official derivation.")


def validate_student_cells(validator: Validator, notebook: nbformat.NotebookNode) -> None:
    notebook_metadata = notebook.get("metadata", {})
    notebook_icp = notebook_metadata.get("icp", {}) if isinstance(notebook_metadata, dict) else {}
    if isinstance(notebook_icp, dict):
        for key in notebook_icp:
            if str(key).casefold().startswith(("instructor", "solution", "answer")):
                validator.error(
                    "student.hidden_notebook_metadata",
                    f"Student notebook contains answer-bearing metadata key {key!r}.",
                )
    for index, cell in enumerate(notebook.cells, start=1):
        tags = tags_for(cell)
        forbidden = tags & (REMOVAL_TAGS | {"solution"})
        if forbidden:
            validator.error("student.forbidden_tag", f"Student cell {index}: forbidden tags {sorted(forbidden)}.")
        metadata = cell.get("metadata", {})
        if not isinstance(metadata, dict):
            validator.error("student.metadata", f"Student cell {index}: metadata must be an object.")
            metadata = {}
        icp = metadata.get("icp", {})
        if isinstance(icp, dict) and "student_source" in icp:
            validator.error("student.hidden_answer", f"Student cell {index}: student_source leaked into metadata.")
        if cell.cell_type == "code":
            if cell.get("outputs"):
                validator.error("student.outputs", f"Student code cell {index}: outputs must be empty.")
            if cell.get("execution_count") is not None:
                validator.error("student.execution_count", f"Student code cell {index}: execution_count must be null.")


def execute_notebook(
    validator: Validator,
    notebook: nbformat.NotebookNode,
    label: str,
    timeout: int,
) -> None:
    with tempfile.TemporaryDirectory(prefix="icp-notebook-") as temporary:
        temporary_path = Path(temporary)
        env_dirs = {
            "IPYTHONDIR": str(temporary_path / "ipython"),
            "JUPYTER_CONFIG_DIR": str(temporary_path / "jupyter-config"),
            "JUPYTER_RUNTIME_DIR": str(temporary_path / "jupyter-runtime"),
            "MPLBACKEND": "Agg",
        }
        for key in ("IPYTHONDIR", "JUPYTER_CONFIG_DIR", "JUPYTER_RUNTIME_DIR"):
            Path(env_dirs[key]).mkdir(parents=True, exist_ok=True)
        execution_copy = nbformat.from_dict(copy.deepcopy(notebook))
        notebook_metadata = notebook.get("metadata", {})
        kernelspec = notebook_metadata.get("kernelspec", {}) if isinstance(notebook_metadata, dict) else {}
        kernel_name = kernelspec.get("name", "python3") if isinstance(kernelspec, dict) else "python3"
        try:
            with patch.dict(os.environ, env_dirs, clear=False):
                client = NotebookClient(
                    execution_copy,
                    timeout=timeout,
                    kernel_name=kernel_name,
                    allow_errors=False,
                )
                client.execute(cwd=temporary)
        except Exception as exc:
            validator.error("notebook.execute", f"{label}: fresh-kernel execution failed: {exc}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("instructor", type=Path)
    parser.add_argument("student", type=Path)
    parser.add_argument("--manifest", type=Path, required=True, help="Machine-readable source-map.json.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--execute", action="store_true", help="Execute both notebooks in clean temp dirs.")
    parser.add_argument("--timeout", type=int, default=120, help="Per-cell execution timeout in seconds.")
    parser.add_argument(
        "--allow-unresolved",
        action="store_true",
        help="Downgrade unresolved mappings with persisted TA approval to warnings.",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    for path, label in (
        (args.instructor, "Instructor"),
        (args.student, "Student"),
        (args.manifest, "Manifest"),
    ):
        if not path.is_file():
            raise SystemExit(f"{label} file does not exist: {path}")

    try:
        instructor = nbformat.read(args.instructor, as_version=4)
        student = nbformat.read(args.student, as_version=4)
    except Exception as exc:
        raise SystemExit(f"Cannot read notebook pair: {exc}") from exc
    validator = Validator(args.root, args.allow_unresolved)
    try:
        bundle_directory = args.manifest.resolve().parent
        for notebook_path, label in (
            (args.instructor, "Instructor"),
            (args.student, "Student"),
        ):
            if notebook_path.resolve().parent != bundle_directory:
                validator.error(
                    "bundle.location",
                    f"{label} notebook and source-map.json must be in the same bundle directory.",
                )
        if args.manifest.name != "source-map.json":
            validator.error(
                "manifest.filename",
                "Classroom bundles must name the machine manifest 'source-map.json'.",
            )
        try:
            manifest_value = json.loads(args.manifest.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            manifest_value = {}
            validator.error("manifest.read", f"Cannot read source-map.json: {exc}")
        manifest = manifest_value if isinstance(manifest_value, dict) else {}
        validator.validate_manifest(manifest_value)
        if args.allow_unresolved and validator.unresolved_count == 0:
            validator.error(
                "reference.allow_unresolved_unused",
                "--allow-unresolved was supplied, but the manifest has no unresolved references.",
            )
        validate_source_map_markdown(validator, args.manifest, manifest)
        validate_notebook_metadata(
            validator,
            instructor,
            "instructor",
            "Instructor",
            manifest,
            args.manifest.name,
        )
        validate_notebook_metadata(
            validator,
            student,
            "student",
            "Student",
            manifest,
            args.manifest.name,
        )
        validate_cell_ids(validator, instructor, "Instructor")
        validate_cell_ids(validator, student, "Student")
        validate_instructor_cells(validator, instructor)
        validate_student_cells(validator, student)
        compare_pair(validator, instructor, student)
        if args.execute:
            execute_notebook(validator, instructor, "Instructor", args.timeout)
            execute_notebook(validator, student, "Student", args.timeout)
    finally:
        validator.close()

    errors = sum(issue.level == "error" for issue in validator.issues)
    warnings = sum(issue.level == "warning" for issue in validator.issues)
    status = "fail" if errors else ("pass" if args.execute else "structural_pass")
    payload = {
        "status": status,
        "executed": bool(args.execute),
        "errors": errors,
        "warnings": warnings,
        "issues": [asdict(issue) for issue in validator.issues],
    }
    if args.format == "json":
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        for issue in validator.issues:
            print(f"{issue.level.upper()} [{issue.code}] {issue.message}")
        print(f"{status.upper()}: {errors} error(s), {warnings} warning(s)")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
