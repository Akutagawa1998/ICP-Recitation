#!/usr/bin/env python3
"""Check a simple notebook pair and solution folder without citation searches.

Completeness against the assignment, English prose, Chinese comment quality, and
semantic agreement between notebook and scripts still require independent review.
"""

from __future__ import annotations

import argparse
import copy
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

import nbformat
from nbclient import NotebookClient

from derive_student_notebook import REMOVAL_TAGS, derive_notebook, tags_for


def validate(instructor_path: Path, student_path: Path, execute: bool, timeout: int) -> None:
    if instructor_path.resolve().parent != student_path.resolve().parent:
        raise ValueError("Both notebooks must be in the same recitation folder.")
    if not instructor_path.name.endswith("-instructor.ipynb"):
        raise ValueError("Instructor filename must end in -instructor.ipynb.")
    expected_name = instructor_path.name.removesuffix("-instructor.ipynb") + "-student.ipynb"
    if student_path.name != expected_name:
        raise ValueError("Student filename must match the instructor filename.")
    instructor = nbformat.read(instructor_path, as_version=4)
    student = nbformat.read(student_path, as_version=4)
    for notebook in (instructor, student):
        nbformat.validate(notebook)
        ids = [cell.get("id") for cell in notebook.cells]
        if any(not cell_id for cell_id in ids) or len(set(ids)) != len(ids):
            raise ValueError("Every cell needs a unique, nonempty ID.")
        recitation_id = notebook.metadata.get("icp", {}).get("recitation_id")
        if not isinstance(recitation_id, str) or not recitation_id.strip():
            raise ValueError("metadata.icp.recitation_id must be a nonempty string.")
    expected = derive_notebook(instructor)
    if dict(expected) != dict(student):
        raise ValueError("Student notebook differs from the official derivation.")

    prompt_ids: list[str] = []
    solution_ids: list[str] = []
    for cell in instructor.cells:
        tags = tags_for(cell)
        icp = cell.metadata.get("icp", {})
        if "exercise-prompt" in tags:
            if cell.cell_type != "markdown" or tags & (REMOVAL_TAGS | {"solution"}):
                raise ValueError("Exercise prompts must be shared Markdown cells.")
            exercise_id = icp.get("exercise_id")
            if not isinstance(exercise_id, str) or not exercise_id.strip() or icp.get("role") != "prompt":
                raise ValueError("Each exercise prompt needs an exercise_id and prompt role.")
            prompt_ids.append(exercise_id)
        if "solution" in tags:
            if tags & REMOVAL_TAGS or icp.get("role") != "solution":
                raise ValueError("Solution cells need the solution role and cannot be removal-only.")
            solution_ids.append(icp["exercise_id"])
    if not prompt_ids or len(set(prompt_ids)) != len(prompt_ids):
        raise ValueError("Exercise prompt IDs must be present and unique.")
    if set(solution_ids) != set(prompt_ids):
        raise ValueError("Every exercise needs a solution cell; orphan solutions are forbidden.")

    solution_dir = instructor_path.resolve().parent / "solution"
    overview = solution_dir / "README.md"
    if not overview.is_file() or not overview.read_text(encoding="utf-8").strip():
        raise ValueError("solution/README.md must contain the Chinese teaching overview.")
    scripts = sorted(solution_dir.glob("exercise-*.py"))
    expected_scripts = [f"exercise-{number:02d}.py" for number in range(1, len(prompt_ids) + 1)]
    if [script.name for script in scripts] != expected_scripts:
        raise ValueError("solution/ needs one consecutively numbered exercise-NN.py per exercise.")
    for script in scripts:
        source = script.read_text(encoding="utf-8")
        if not source.strip():
            raise ValueError(f"{script.name} is empty.")
        compile(source, str(script), "exec")

    if execute:
        for label, notebook in (("instructor", instructor), ("student", student)):
            with tempfile.TemporaryDirectory(prefix=f"icp-{label}-") as temporary:
                env = {
                    "IPYTHONDIR": str(Path(temporary) / "ipython"),
                    "JUPYTER_CONFIG_DIR": str(Path(temporary) / "jupyter-config"),
                    "JUPYTER_RUNTIME_DIR": str(Path(temporary) / "jupyter-runtime"),
                    "MPLBACKEND": "Agg",
                }
                for key in ("IPYTHONDIR", "JUPYTER_CONFIG_DIR", "JUPYTER_RUNTIME_DIR"):
                    Path(env[key]).mkdir()
                with patch.dict(os.environ, env):
                    NotebookClient(
                        copy.deepcopy(notebook),
                        timeout=timeout,
                        kernel_name="python3",
                        allow_errors=False,
                    ).execute(cwd=temporary)
        for script in scripts:
            with tempfile.TemporaryDirectory(prefix="icp-solution-") as temporary:
                completed = subprocess.run(
                    [sys.executable, "-B", str(script)],
                    cwd=temporary,
                    stdin=subprocess.DEVNULL,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    check=False,
                )
                if completed.returncode:
                    raise ValueError(f"{script.name} execution failed:\n{completed.stderr}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("instructor", type=Path)
    parser.add_argument("student", type=Path)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    try:
        validate(args.instructor, args.student, args.execute, args.timeout)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    status = "PASS" if args.execute else "STRUCTURAL_PASS"
    print(f"{status}: notebook pair and solution files checked; independent content review still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
