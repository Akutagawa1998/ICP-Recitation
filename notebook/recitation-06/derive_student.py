"""Derive the English worked-answer edition requested for Recitation 06.

The course helper still performs the normal metadata and cell sanitization.
This adapter projects each paired cell to its stored English source, keeps the
canonical answers, and removes teacher notes. Do not edit the student copy.
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import io
from pathlib import Path
import re
import tokenize

import nbformat


BUNDLE = Path(__file__).resolve().parent
COURSE_HELPER = (
    BUNDLE.parents[1]
    / ".agents/skills/icp-recitation-prep/scripts/derive_student_notebook.py"
)
CJK = re.compile(r"[\u3400-\u9fff]")


def english_code(source: str) -> str:
    """Remove Chinese comment tokens without changing executable Python."""
    tokens = []
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type == tokenize.COMMENT and CJK.search(token.string):
            token = token._replace(string="")
        tokens.append(token)
    cleaned = tokenize.untokenize(tokens)
    cleaned = "\n".join(line.rstrip() for line in cleaned.splitlines()).strip() + "\n"
    if CJK.search(cleaned):
        raise ValueError("Chinese text remains outside removable code comments.")
    return cleaned


def derive_answers(instructor):
    """Use one bilingual canonical notebook to produce one English answer copy."""
    spec = importlib.util.spec_from_file_location("icp_course_deriver", COURSE_HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    projection = nbformat.from_dict(copy.deepcopy(instructor))
    for cell in projection.cells:
        icp = cell.metadata.get("icp", {})
        english_source = icp.pop("english_source", None)
        if english_source is not None:
            if not isinstance(english_source, str) or CJK.search(english_source):
                raise ValueError(f"Cell {cell.id} needs an English source projection.")
            cell.source = english_source
    student = module.derive_notebook(projection)
    originals = {cell.id: cell for cell in projection.cells}
    for cell in student.cells:
        original = originals[cell.id]
        if "solution" in original.metadata.get("tags", []):
            cell.source = english_code(original.source)
            cell.metadata = copy.deepcopy(original.metadata)
            cell.metadata.icp.pop("student_source", None)
            cell.metadata.icp["role"] = "solution"
            cell.metadata["tags"] = ["solution"]
        elif cell.cell_type == "code":
            cell.source = english_code(cell.source)
        if CJK.search(cell.source):
            raise ValueError(f"Shared cell {cell.id} contains Chinese teaching text.")
    student.metadata.icp["answers_included"] = True
    student.metadata.icp["language"] = "en"
    nbformat.validate(student)
    return student


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    instructor_path = BUNDLE / "recitation-06-instructor.ipynb"
    student_path = BUNDLE / "recitation-06-student.ipynb"
    if student_path.is_symlink():
        raise SystemExit("Refusing to replace a symlink.")
    instructor = nbformat.read(instructor_path, as_version=4)
    if student_path.exists():
        if not args.force:
            raise SystemExit("Student copy exists. Use --force to regenerate it.")
        existing = nbformat.read(student_path, as_version=4)
        identity = existing.metadata.get("icp", {})
        if identity.get("variant") != "student" or identity.get("recitation_id") != "06":
            raise SystemExit("Existing target is not the Recitation 06 student copy.")
    nbformat.write(derive_answers(instructor), student_path)
    print(student_path)


if __name__ == "__main__":
    main()
