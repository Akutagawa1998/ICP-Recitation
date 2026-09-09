# Notebook contract

Use this contract whenever creating, deriving, executing, or reviewing a recitation notebook pair.

## Deliverables and source of truth

For recitation `NN`, deliver exactly two classroom notebooks:

- `recitation-NN-instructor.ipynb`: canonical authored notebook with solutions and optional instructor notes.
- `recitation-NN-student.ipynb`: deterministically derived question version.

Do not maintain the two versions independently. Derive the student notebook with `.agents/skills/icp-recitation-prep/scripts/derive_student_notebook.py` after every instructor change.

Keep a human-readable `source-map.md` beside them. Local images, if any, belong in a sibling `assets/` directory and use relative links.

## Notebook-level metadata

Both notebooks must contain:

```json
{
  "metadata": {
    "icp": {
      "schema_version": 1,
      "recitation_id": "01",
      "title": "First steps with Python",
      "variant": "instructor",
      "source_map": "source-map.json"
    },
    "kernelspec": {
      "name": "python3",
      "language": "python",
      "display_name": "Python 3"
    }
  }
}
```

The derived notebook changes only `metadata.icp.variant` to `student`. Use strings for recitation IDs so leading zeros are preserved.

Use `schema_version: 2` in both notebooks when the manifest uses native PPTX lecture references. The notebook and manifest versions must match. Version-1 PDF bundles remain supported, and the same derivation, solution tagging, and execution rules apply to both versions.

## Required teaching sequence

Use this order unless the source material clearly calls for a different flow:

1. Title, learning goals, estimated pacing, and source-version note (`learning-goals` tag).
2. Lecture review in Markdown, organized around the few concepts students need today (`lecture-review` tag).
3. Small executable examples immediately following each review concept (`review-example` tag).
4. Every original recitation exercise and subexercise in its original order.
5. A short recap or exit check (`recap` tag).

Do not turn the lecture review into a slide-by-slide transcript. Explain ideas in fresh wording, and use images only when they make the explanation clearer.

## Exercise cells

Each exercise starts with a Markdown cell tagged `exercise-prompt`. Its metadata must include:

```json
{
  "tags": ["exercise-prompt"],
  "icp": {
    "exercise_id": "R01-E01",
    "role": "prompt",
    "concepts": ["interactive and script modes"],
    "recitation_source": {
      "source_id": "recitation-01",
      "path": "recitation/Recitaion 01.pdf",
      "sha256": "<64 lowercase hex characters>",
      "pdf_page": 1,
      "item_label": "Exercise 1",
      "anchor": "Try Python in Two Modes"
    },
    "references": []
  }
}
```

The cell source contains the faithful exercise wording followed immediately by the visible reference block. Give subexercises stable IDs such as `R01-E01-A` when separate code demonstrations or references are needed.

Every value in `concepts` must be covered by at least one lecture reference and one textbook reference in that prompt's `references`. Use an unresolved reference to represent a genuine source gap rather than dropping the concept.

Every solution code cell must:

- have a stable Jupyter cell ID;
- carry the `solution` tag;
- set `metadata.icp.exercise_id` to the exercise it answers;
- set `metadata.icp.subpart_id` when it answers a numbered subpart declared in the manifest;
- set `metadata.icp.role` to `solution`; and
- set `metadata.icp.student_source` to a useful, syntactically valid starter cell.

Every `student_source` must contain a literal `TODO` marker, remain executable as-is, and contain an executable placeholder (`None`, `...`, `pass`, or an empty `return`). It may provide a function signature, sample input data, or targeted scaffolding, but it must not pre-fill a target computed by the solution, contain a completed answer, or substitute an equivalent precomputed result. Static checks are conservative rather than a proof of semantic non-equivalence, so the independent leakage review remains mandatory.

Example metadata:

```json
{
  "tags": ["solution"],
  "icp": {
    "exercise_id": "R01-E01",
    "subpart_id": "R01-E01-P01",
    "role": "solution",
    "student_source": "result = None  # TODO: Evaluate the expression.\n"
  }
}
```

Use `solution-only` for instructor explanations that should be removed entirely from the student notebook. Use `instructor-only` for facilitation notes. Do not place required problem wording or source references in cells with either removal tag.

## Student scaffolding

The student version keeps:

- learning goals and review explanations;
- review demo code that students are meant to see;
- complete exercise wording and references;
- code cells with targeted TODOs, function signatures, sample data, or partially completed tables when helpful.

The student version removes:

- completed answer code;
- solution reasoning and instructor notes;
- answer-bearing outputs and execution counts;
- answer summaries hidden in metadata.

During derivation, each instructor `solution` code cell becomes a `student-work` code cell with `metadata.icp.role = "student-work"`; it retains only the exercise ID and non-answer metadata required by the derivation script.

More precisely, a derived `student-work` cell's `metadata.icp` allowlist is `exercise_id`, optional declared `subpart_id`, and `role = "student-work"`. The derived notebook's top-level metadata allowlist is `icp` plus a reconstructed `kernelspec`; `language_info` and other arbitrary notebook metadata are dropped. The `kernelspec` allowlist is `name`, `language`, and `display_name`. Cell metadata is reconstructed from `tags` and the role-specific `icp` allowlist; arbitrary nested metadata, including grading keys, answer keys, instructor notes, and slideshow payloads, is forbidden.

For retained prompt cells, the `metadata.icp` allowlist is `exercise_id`, `role`, `concepts`, `recitation_source`, and `references`. For other retained shared cells, it is `role` and `concept_id`. The derivation script, rather than the author, is the source of truth for this sanitization.

Do not use a bare `pass` when a more informative TODO or starter signature would help. Do not use an uncaught `NotImplementedError`; the student notebook should still execute from top to bottom.

## Code and execution rules

- Target the course's current Python level; do not introduce advanced syntax merely to shorten an answer.
- Keep examples short, observable, and easy to modify live.
- Use deterministic values and fixed random seeds.
- Avoid network calls and unnecessary third-party dependencies.
- Avoid blocking `input()` during automated execution. Demonstrate input through function parameters or clearly marked editable variables unless live input is essential.
- Do not create persistent files during ordinary examples. If file creation is the lesson, use a temporary directory or clean up the exact generated file.
- Demonstrate expected errors without stopping the kernel. For example, compile invalid source inside `try`/`except SyntaxError`, or execute a name lookup inside `try`/`except NameError`.
- The instructor notebook and the derived student notebook must both execute from a fresh `python3` kernel with no uncaught exception.

## Images

Images are optional. Prefer original diagrams or course-owned lecture figures over full-page textbook reproductions. Every reused image needs nearby source attribution with the same page semantics as text citations. Check that relative image paths render from the delivered notebook directory.

## Classroom-ready gate

A pair is classroom-ready only when:

- all original exercises and subexercises are present once and in order;
- each normalized exercise/subpart prompt hash matches the independently extracted recitation PDF block, and every declared subpart has a solution cell;
- all non-unresolved references pass anchor/page/hash validation;
- every unresolved reference has a persisted TA approval object and validation is run with `--allow-unresolved`;
- the student notebook contains no solution or instructor-only cells and no outputs;
- the pair passes structural comparison;
- both notebooks execute from a fresh kernel; and
- an independent review finds no blocking pedagogical or citation issue.

Running the validator without `--execute` reports `structural_pass`, never full `pass`; it is useful during authoring but does not satisfy this gate. Supplying `--allow-unresolved` when the manifest contains no unresolved entries is also an error, so the final command records the actual review state rather than a blanket exception.
