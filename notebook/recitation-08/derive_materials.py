"""Derive the answered English student copy and bilingual teaching copy.

The English instructor notebook is the canonical answer source. The standard
course helper sanitizes its ordinary student projection. This task's adapter
then retains worked answers because the user explicitly requested them.
Chinese code blocks come from solution/exercise-NN.py and must have the same
Python AST as the matching canonical solution cell. The teaching translation
resource adds paired English/Chinese prose and comments without changing code.
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

import nbformat


sys.dont_write_bytecode = True
BUNDLE = Path(__file__).resolve().parent
INSTRUCTOR = BUNDLE / "recitation-08-instructor.ipynb"
STUDENT = BUNDLE / "recitation-08-student.ipynb"
TEACHING = BUNDLE / "solution/recitation-08-teaching.ipynb"
TRANSLATIONS = BUNDLE / "solution/teaching-translations.json"
COURSE_HELPER = BUNDLE.parents[1] / ".agents/skills/icp-recitation-prep/scripts/derive_student_notebook.py"
CJK = re.compile(r"[\u3400-\u9fff]")
BLOCK_PATTERN = re.compile(r"^# %% (R08-E\d{2}(?:-P\d{2}|-DEMO)?)\s*$", re.MULTILINE)


def course_deriver():
    spec = importlib.util.spec_from_file_location("icp_course_deriver_r08", COURSE_HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.derive_notebook


def annotated_blocks():
    blocks = {}
    for path in sorted((BUNDLE / "solution").glob("exercise-*.py")):
        pieces = BLOCK_PATTERN.split(path.read_text(encoding="utf-8"))
        for index in range(1, len(pieces), 2):
            block_id = pieces[index]
            if block_id in blocks:
                raise ValueError(f"Duplicate solution block: {block_id}")
            blocks[block_id] = pieces[index + 1].strip() + "\n"
    return blocks


def ast_key(source):
    return ast.dump(ast.parse(source), include_attributes=False)


def clear_execution(notebook):
    for cell in notebook.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None


def derive_student(instructor):
    """Sanitize with the course helper, then restore requested English answers."""
    student = course_deriver()(instructor)
    shared = {cell.id: cell for cell in student.cells}
    cells = []
    for original in instructor.cells:
        tags = set(original.metadata.get("tags", []))
        if "instructor-only" in tags:
            continue
        if "solution-only" in tags:
            cell = copy.deepcopy(original)
            cell.metadata = nbformat.NotebookNode({"tags": ["worked-answer"]})
        elif "solution" in tags:
            cell = copy.deepcopy(shared[original.id])
            cell.source = original.source
            identity = original.metadata.icp
            cell.metadata = nbformat.NotebookNode({
                "tags": ["solution"],
                "icp": {
                    key: copy.deepcopy(value)
                    for key, value in identity.items()
                    if key in {"exercise_id", "subpart_id", "role"}
                },
            })
        else:
            cell = copy.deepcopy(shared[original.id])
        if CJK.search(cell.source):
            raise ValueError(f"Student cell {cell.id} contains Chinese text.")
        cells.append(cell)
    student.cells = cells
    student.metadata.icp["answers_included"] = True
    student.metadata.icp["language"] = "en"
    clear_execution(student)
    nbformat.validate(student)
    return student


def teaching_translations(instructor):
    """Require current translations for every canonical Markdown cell."""
    translations = json.loads(TRANSLATIONS.read_text(encoding="utf-8"))
    if translations.get("schema_version") != 1:
        raise ValueError("Unsupported teaching translation schema.")
    markdown = translations.get("markdown", {})
    expected = {
        cell.id for cell in instructor.cells
        if cell.cell_type == "markdown"
        and "instructor-only" not in cell.metadata.get("tags", [])
    }
    if set(markdown) != expected:
        raise ValueError("Teaching translations must cover all Markdown cells.")
    for cell in instructor.cells:
        if cell.id not in expected:
            continue
        entry = markdown[cell.id]
        digest = hashlib.sha256(cell.source.encode("utf-8")).hexdigest()
        if entry.get("source_sha256") != digest:
            raise ValueError(f"Update the teaching translation for changed cell: {cell.id}")
        paired = entry.get("paired", "")
        if not isinstance(paired, str) or not paired.strip() or not CJK.search(paired):
            raise ValueError(f"Missing bilingual Markdown for {cell.id}")
        fences = r"```[^\n]*\n[\s\S]*?```"
        if re.findall(fences, paired) != re.findall(fences, cell.source):
            raise ValueError(f"Teaching translation changed literal examples: {cell.id}")
    return translations


def english_comment(chinese, comments):
    english = comments.get(chinese)
    if (
        not isinstance(english, str) or not english.strip()
        or CJK.search(english) or "\n" in english or "\r" in english
    ):
        raise ValueError(f"Missing English teaching comment for: {chinese}")
    return english


def bilingual_code(source, comments):
    """Put a matching English comment directly above each Chinese comment."""
    lines = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#") and CJK.search(stripped):
            indent = line[:len(line) - len(stripped)]
            chinese = stripped[1:].strip()
            lines.append(indent + "# " + english_comment(chinese, comments))
        lines.append(line)
    paired = "\n".join(lines) + "\n"
    if ast_key(paired) != ast_key(source):
        raise ValueError("Bilingual comments changed executable Python.")
    return paired


def teaching_notes(source, comments):
    notes = []
    for line in source.splitlines():
        if line.startswith(("# 任务：", "# 思路：", "# 易错点：")):
            chinese = line[2:]
            english = english_comment(chinese, comments)
            notes.append(f"**EN:** {english}\n\n**中：** {chinese}")
        elif line.strip() and not line.lstrip().startswith("#"):
            break
    return "\n\n".join(notes)


def derive_teaching(instructor):
    """Pair all teaching prose and comments while preserving canonical code."""
    translations = teaching_translations(instructor)
    comments = translations["comments"]
    blocks = annotated_blocks()
    teaching = copy.deepcopy(instructor)
    cells = []
    seen_blocks = set()
    for original in instructor.cells:
        tags = set(original.metadata.get("tags", []))
        if "instructor-only" in tags:
            continue
        cell = copy.deepcopy(original)
        if cell.cell_type == "markdown":
            cell.source = translations["markdown"][cell.id]["paired"]
        if "solution" in tags:
            block_id = cell.id.upper()
            if block_id not in blocks:
                raise ValueError(f"No Chinese block for {cell.id}")
            annotated = blocks[block_id]
            if ast_key(annotated) != ast_key(original.source):
                raise ValueError(f"Chinese and canonical code differ: {block_id}")
            notes = teaching_notes(annotated, comments)
            cells.append(nbformat.v4.new_markdown_cell(
                notes,
                id=cell.id + "-zh-notes",
                metadata={"tags": ["teaching-notes"]},
            ))
            cell.source = bilingual_code(annotated, comments)
            cell.metadata.icp.pop("student_source", None)
            seen_blocks.add(block_id)
        cells.append(cell)
    if seen_blocks != set(blocks):
        raise ValueError("Chinese scripts contain unmatched solution blocks.")
    teaching.cells = cells
    teaching.metadata.icp["variant"] = "teaching"
    teaching.metadata.icp["language"] = "en-zh"
    teaching.metadata.icp["answers_included"] = True
    clear_execution(teaching)
    nbformat.validate(teaching)
    return teaching


def verify_target(path, variant):
    if path.is_symlink():
        raise ValueError(f"Refusing to replace a symlink: {path}")
    if path.exists():
        old = nbformat.read(path, as_version=4)
        identity = old.metadata.get("icp", {})
        if identity.get("recitation_id") != "08" or identity.get("variant") != variant:
            raise ValueError(f"Existing target is not the matching derived notebook: {path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Regenerate matching derived copies.")
    args = parser.parse_args()
    instructor = nbformat.read(INSTRUCTOR, as_version=4)
    if instructor.metadata.icp.get("variant") != "instructor":
        raise SystemExit("The canonical notebook must have variant instructor.")
    if instructor.metadata.icp.get("recitation_id") != "08":
        raise SystemExit("The canonical notebook must be Recitation 08.")
    for cell in instructor.cells:
        if CJK.search(cell.source):
            raise SystemExit(f"Canonical cell {cell.id} contains Chinese text.")
    for path, variant in ((STUDENT, "student"), (TEACHING, "teaching")):
        verify_target(path, variant)
        if path.exists() and not args.force:
            raise SystemExit(f"Target exists; use --force: {path}")
    student = derive_student(instructor)
    teaching = derive_teaching(instructor)
    nbformat.write(student, STUDENT)
    nbformat.write(teaching, TEACHING)
    print(STUDENT)
    print(TEACHING)


if __name__ == "__main__":
    main()
