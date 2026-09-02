#!/usr/bin/env python3
"""Derive a questions-only notebook from the canonical instructor notebook."""

from __future__ import annotations

import argparse
import ast
import copy
import os
import re
import tempfile
from collections import Counter
from pathlib import Path
from typing import Sequence

try:
    import nbformat
except ImportError as exc:  # pragma: no cover - dependency failure path
    raise SystemExit(
        "nbformat is required. Install it with: python3 -m pip install nbformat"
    ) from exc


REMOVAL_TAGS = {"solution-only", "instructor-only"}
ALLOWED_NOTEBOOK_ICP = {"schema_version", "recitation_id", "title", "variant", "source_map"}
ALLOWED_PROMPT_ICP = {"exercise_id", "role", "concepts", "recitation_source", "references"}
ALLOWED_SHARED_ICP = {"role", "concept_id"}
SAFE_RETAINED_TAGS = {
    "learning-goals",
    "lecture-review",
    "review-example",
    "exercise-prompt",
    "recap",
    "student-work",
}
ANSWER_LIKE_NAME = re.compile(
    r"(?:^|_)(?:answer|result|solution|output|expected|converted|conversion)(?:_|$)",
    re.IGNORECASE,
)


def tags_for(cell: nbformat.NotebookNode) -> set[str]:
    metadata = cell.get("metadata", {})
    if not isinstance(metadata, dict):
        return set()
    tags = metadata.get("tags", [])
    if not isinstance(tags, list):
        return set()
    return {str(tag) for tag in tags}


def without_comments(source: str) -> str:
    lines = [line for line in source.splitlines() if not line.lstrip().startswith("#")]
    return "\n".join(line.rstrip() for line in lines).strip()


def ast_key(node: ast.AST) -> str:
    return ast.dump(node, annotate_fields=True, include_attributes=False)


def target_names(target: ast.AST) -> set[str]:
    if isinstance(target, ast.Name):
        return {target.id}
    if isinstance(target, (ast.Tuple, ast.List)):
        names: set[str] = set()
        for element in target.elts:
            names.update(target_names(element))
        return names
    return set()


def assignment_values(tree: ast.AST) -> dict[str, list[ast.AST]]:
    values: dict[str, list[ast.AST]] = {}
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        value: ast.AST | None = None
        if isinstance(node, ast.Assign):
            targets = list(node.targets)
            value = node.value
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets = [node.target]
            value = node.value
        elif isinstance(node, ast.NamedExpr):
            targets = [node.target]
            value = node.value
        if value is None:
            continue
        for target in targets:
            for name in target_names(target):
                values.setdefault(name, []).append(value)
    return values


def is_placeholder_value(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and node.value in (None, Ellipsis)


def has_executable_placeholder(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Pass):
            return True
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.NamedExpr)):
            value = getattr(node, "value", None)
            if isinstance(value, ast.AST) and is_placeholder_value(value):
                return True
        if isinstance(node, ast.Return) and (node.value is None or is_placeholder_value(node.value)):
            return True
        if isinstance(node, ast.Expr) and is_placeholder_value(node.value):
            return True
    return False


def validate_student_source(student_source: str, solution_source: str, cell_id: str) -> None:
    """Reject starter cells that are invalid, completed, or obvious rewrites of the answer.

    Static checks cannot prove semantic non-equivalence. They deliberately enforce an
    executable placeholder and protect names that the solution itself defines; the
    independent reviewer remains the final semantic leakage gate.
    """

    if "todo" not in student_source.casefold():
        raise ValueError(f"Solution cell {cell_id} student_source must contain a TODO.")
    try:
        student_tree = ast.parse(student_source, filename=f"<{cell_id}-student-source>")
    except SyntaxError as exc:
        raise ValueError(
            f"Solution cell {cell_id} student_source is not valid Python: {exc}"
        ) from exc
    try:
        solution_tree = ast.parse(solution_source, filename=f"<{cell_id}-solution>")
    except SyntaxError as exc:
        raise ValueError(f"Solution cell {cell_id} contains invalid Python: {exc}") from exc

    if ast_key(student_tree) == ast_key(solution_tree) or (
        without_comments(student_source) == without_comments(solution_source)
    ):
        raise ValueError(f"Solution cell {cell_id} student_source duplicates the solution.")
    solution_statements = Counter(ast_key(node) for node in solution_tree.body)
    student_statements = Counter(ast_key(node) for node in student_tree.body)
    if solution_statements and all(
        student_statements[key] >= count for key, count in solution_statements.items()
    ):
        raise ValueError(
            f"Solution cell {cell_id} student_source contains every completed solution statement."
        )
    if not has_executable_placeholder(student_tree):
        raise ValueError(
            f"Solution cell {cell_id} student_source needs an executable placeholder "
            "(`None`, `...`, `pass`, or an empty return) in addition to its TODO."
        )

    solution_values = assignment_values(solution_tree)
    for name, student_values in assignment_values(student_tree).items():
        if name not in solution_values:
            continue
        solution_keys = {ast_key(value) for value in solution_values[name]}
        for value in student_values:
            if is_placeholder_value(value):
                continue
            value_key = ast_key(value)
            if ANSWER_LIKE_NAME.search(name) or value_key not in solution_keys:
                raise ValueError(
                    f"Solution cell {cell_id} student_source pre-fills solution target "
                    f"{name!r}; replace it with an explicit placeholder."
                )


def sanitize_shared_metadata(cell: nbformat.NotebookNode, tags: set[str]) -> None:
    original = cell.metadata
    if not isinstance(original, dict):
        raise ValueError(f"Cell {cell.get('id', '<no id>')} metadata must be an object.")
    sanitized = nbformat.NotebookNode()
    sanitized["tags"] = sorted(tags & SAFE_RETAINED_TAGS)
    icp = original.get("icp", {})
    if isinstance(icp, dict):
        allowed = ALLOWED_PROMPT_ICP if "exercise-prompt" in tags else ALLOWED_SHARED_ICP
        kept = {key: copy.deepcopy(value) for key, value in icp.items() if key in allowed}
        if kept:
            sanitized["icp"] = kept
    cell.metadata = sanitized


def derive_notebook(instructor: nbformat.NotebookNode) -> nbformat.NotebookNode:
    """Return a sanitized student copy without mutating the input notebook."""

    student = nbformat.from_dict(copy.deepcopy(instructor))
    notebook_metadata = student.get("metadata", {})
    if not isinstance(notebook_metadata, dict):
        raise ValueError("Instructor notebook metadata must be an object.")
    icp_metadata = notebook_metadata.get("icp")
    if not isinstance(icp_metadata, dict):
        raise ValueError("Instructor notebook is missing metadata.icp.")
    if icp_metadata.get("schema_version") != 1:
        raise ValueError("Only metadata.icp.schema_version = 1 is supported.")
    if icp_metadata.get("variant") != "instructor":
        raise ValueError("Canonical notebook must set metadata.icp.variant to 'instructor'.")

    sanitized_notebook_metadata = nbformat.NotebookNode()
    sanitized_icp = copy.deepcopy(student.metadata.get("icp", {}))
    if not isinstance(sanitized_icp, dict):
        raise ValueError("Instructor notebook metadata.icp must be an object.")
    sanitized_notebook_metadata["icp"] = nbformat.NotebookNode(
        {
            key: copy.deepcopy(value)
            for key, value in sanitized_icp.items()
            if key in ALLOWED_NOTEBOOK_ICP
        }
    )
    sanitized_notebook_metadata["kernelspec"] = nbformat.NotebookNode(
        {"name": "python3", "language": "python", "display_name": "Python 3"}
    )
    student.metadata = sanitized_notebook_metadata

    new_cells: list[nbformat.NotebookNode] = []
    for cell in student.cells:
        tags = tags_for(cell)
        if cell.get("attachments"):
            raise ValueError(
                f"Cell {cell.get('id', '<no id>')} contains embedded attachments. "
                "Use a source-cited local asset file instead."
            )
        if tags & REMOVAL_TAGS:
            continue

        if "solution" in tags:
            if cell.cell_type != "code":
                raise ValueError(
                    f"Cell {cell.get('id', '<no id>')} uses the solution tag but is not code; "
                    "use solution-only for removable Markdown explanations."
                )
            icp = cell.metadata.get("icp")
            if not isinstance(icp, dict):
                raise ValueError(f"Solution cell {cell.get('id', '<no id>')} is missing metadata.icp.")
            student_source = icp.get("student_source")
            if not isinstance(student_source, str) or not student_source.strip():
                raise ValueError(
                    f"Solution cell {cell.get('id', '<no id>')} needs a non-empty "
                    "metadata.icp.student_source."
                )
            validate_student_source(
                student_source,
                str(cell.source),
                str(cell.get("id", "<no id>")),
            )
            exercise_id = icp.get("exercise_id")
            if not isinstance(exercise_id, str) or not exercise_id.strip():
                raise ValueError(
                    f"Solution cell {cell.get('id', '<no id>')} needs metadata.icp.exercise_id."
                )
            subpart_id = icp.get("subpart_id")
            if subpart_id is not None and (
                not isinstance(subpart_id, str) or not subpart_id.strip()
            ):
                raise ValueError(
                    f"Solution cell {cell.get('id', '<no id>')} metadata.icp.subpart_id "
                    "must be a non-empty string when present."
                )

            cell.source = student_source
            student_icp = {
                "exercise_id": exercise_id,
                "role": "student-work",
            }
            if subpart_id is not None:
                student_icp["subpart_id"] = subpart_id
            cell.metadata = nbformat.NotebookNode(
                {
                    "tags": sorted((tags & SAFE_RETAINED_TAGS) | {"student-work"}),
                    "icp": student_icp,
                }
            )

        else:
            sanitize_shared_metadata(cell, tags)

        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
        new_cells.append(cell)

    student.cells = new_cells
    student.metadata.icp["variant"] = "student"
    nbformat.validate(student)
    return student


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("instructor", type=Path, help="Canonical instructor notebook.")
    parser.add_argument("student", type=Path, help="Student notebook to create.")
    parser.add_argument("--force", action="store_true", help="Replace an existing student notebook.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    instructor_path = args.instructor.resolve()
    student_path = args.student.resolve()
    if not instructor_path.is_file():
        raise SystemExit(f"Instructor notebook does not exist: {instructor_path}")
    if instructor_path == student_path:
        raise SystemExit("Instructor and student notebook paths must differ.")
    if student_path.suffix.casefold() != ".ipynb":
        raise SystemExit("Student output must use the .ipynb extension.")
    protected_directories = {"lecture", "lectures", "recitation", "recitations", "textbook", "textbooks", "syllabus"}
    if any(part.casefold() in protected_directories for part in student_path.parts[:-1]):
        raise SystemExit(f"Refusing to write a derived notebook inside a source directory: {student_path}")
    expected_name = instructor_path.name.removesuffix("-instructor.ipynb") + "-student.ipynb"
    if not instructor_path.name.endswith("-instructor.ipynb") or student_path.name != expected_name:
        raise SystemExit(
            "Notebook pair must use matching '<name>-instructor.ipynb' and '<name>-student.ipynb' filenames."
        )
    if student_path.is_symlink():
        raise SystemExit(f"Refusing to replace a symlink student path: {student_path}")
    try:
        instructor = nbformat.read(instructor_path, as_version=4)
    except Exception as exc:
        raise SystemExit(f"Cannot read instructor notebook: {exc}") from exc
    if student_path.exists():
        if not args.force:
            raise SystemExit(f"Refusing to overwrite {student_path}; pass --force to replace it.")
        try:
            existing = nbformat.read(student_path, as_version=4)
        except Exception as exc:
            raise SystemExit(
                f"Refusing --force because the existing target is not a readable notebook: {exc}"
            ) from exc
        instructor_icp = instructor.get("metadata", {}).get("icp", {})
        existing_icp = existing.get("metadata", {}).get("icp", {})
        same_identity = (
            isinstance(instructor_icp, dict)
            and isinstance(existing_icp, dict)
            and existing_icp.get("variant") == "student"
            and existing_icp.get("recitation_id") == instructor_icp.get("recitation_id")
            and existing_icp.get("source_map") == instructor_icp.get("source_map")
        )
        if not same_identity:
            raise SystemExit(
                "Refusing --force because the existing target is not the derived student notebook "
                "for this instructor/source map."
            )
    try:
        student = derive_notebook(instructor)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    student_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=student_path.parent,
            prefix=f".{student_path.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            temporary_name = stream.name
        nbformat.write(student, temporary_name)
        os.replace(temporary_name, student_path)
    finally:
        if temporary_name is not None:
            Path(temporary_name).unlink(missing_ok=True)
    print(student_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
