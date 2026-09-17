# Notebook and solution contract

## Deliverables

Author `recitation-NN-instructor.ipynb` as the canonical solution. Derive `recitation-NN-student.ipynb` with `scripts/derive_student_notebook.py` after every instructor change. Keep a sibling `solution/` folder for detailed Chinese explanations. Source maps and lecture/textbook references are not required by default.

## English-only, simple notebooks

- Write all instructor Markdown and code in English: headings, prompts, notes, comments, docstrings, identifiers, displayed messages, and explanatory outputs. Student starter code must also be English. Keep Chinese explanations exclusively in `solution/`.
- Preserve original exercise meaning, data, and order. Translate non-English source prose faithfully and disclose ambiguities. If required literal data conflicts with English-only output, flag the conflict rather than silently changing the data.
- Use a short title and learning goals, complete exercise prompts followed by concise solutions, and an optional brief recap. Add a short concept reminder or runnable example only when needed. Do not require a lecture review, pacing table, reference blocks, or repeated explanations.
- Use descriptive variable names, normal indentation, short statements, and course-level syntax. Avoid clever one-liners, unnecessary helpers, classes, extra libraries, and abstraction that makes a beginner's task harder to read.
- Keep code and prose focused on the assignment. Put detailed reasoning, pitfalls, and teaching notes in the Chinese solution files.

## Metadata and student derivation

Use existing version-1 metadata for ordinary notebooks; no new schema is needed:

```json
{
  "icp": {
    "schema_version": 1,
    "recitation_id": "01",
    "title": "First steps with Python",
    "variant": "instructor"
  },
  "kernelspec": {
    "name": "python3",
    "language": "python",
    "display_name": "Python 3"
  }
}
```

Give each cell a stable Jupyter ID. Start each exercise with a Markdown cell tagged `exercise-prompt`, with `metadata.icp.exercise_id`, `role: "prompt"`, and a short `concepts` list. Keep the complete prompt visible. Give every numbered subpart a stable ID and at least one matching solution cell.

Each solution code cell has the `solution` tag and metadata such as:

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

Omit `subpart_id` when the source has no subparts. Each `student_source` must be valid runnable Python, contain `TODO` and an executable placeholder (`None`, `...`, `pass`, or an empty return), and provide useful scaffolding without a completed or precomputed answer.

Use `solution-only` for removable answer explanations and `instructor-only` for facilitation notes; these must also be English. Never put required prompts in removable cells. The derivation script removes these cells, replaces solutions with starter code, sanitizes metadata, and clears outputs/counts. Do not hand-edit the derived student notebook. Shared prose, examples, metadata, links, and starter values must not reveal answers or link students to `solution/`.

## Chinese solution folder

- `solution/README.md`: write in Chinese. Explain overall coverage, prerequisites evident from the exercises, learning goals, and each exercise/subpart's purpose. List files in source order and explain how to run them. Include source ambiguities and stated assumptions. Do not add lecture indexes or citation tables by default.
- `solution/exercise-NN.py`: one UTF-8 Python file per original exercise. Begin with Chinese `#` comments identifying the exercise, concepts, teaching purpose, approach, and common mistakes. Label subparts in their original order.
- Explain every executable code line in Chinese with a comment immediately above it or a short inline comment. Explain what it does and why, including relevant values, types, conditions, or expected results. Do not annotate blank lines or punctuation-only continuation lines. Keep long explanations above the code instead of creating oversized inline comments.
- Keep identifiers, string messages, and program behavior in English. Use Chinese comments for explanations, not Chinese identifiers or extra explanatory print statements. Preserve ordinary indentation and blank lines between logical steps.
- Reuse the instructor's solution logic, names, data, and subpart order. Add only necessary standalone setup and explicit `print` calls for values that Jupyter normally displays. Explain such adaptations. Do not invent a second algorithm or maintain divergent answers.
- For conceptual or non-programming exercises, use ordered Chinese comment blocks explaining every subpart; do not invent executable code just to fill a file.
- Each file must run independently without blocking input. Verify its results against matching instructor cells. After changing a notebook answer, synchronize its solution file.

Example style inside `solution/`:

```python
# 本题练习变量赋值和乘法，目的是理解如何用程序计算长方形面积。
# 保存长方形的长度，后续计算会使用这个值。
length = 5
# 保存长方形的宽度，与长度使用相同的单位。
width = 3
# 将长度乘以宽度，得到面积并保存在描述性变量中。
area = length * width
# 显示计算结果，便于核对面积是否为 15。
print(area)
```

## Execution and review

Use deterministic sample values and fixed random seeds when needed. Avoid network access and unnecessary dependencies. Replace blocking input with editable variables or function parameters. Demonstrate expected errors safely with `try`/`except` or `compile`. Use temporary directories for exercises that write files.

Run `scripts/validate_simple_pair.py <instructor.ipynb> <student.ipynb> --execute`. Without `--execute`, this is only a structural check. It does not prove English language, completeness against the original assignment, line-by-line comment quality, or semantic parity: the independent reviewer must verify those, plus simplicity and student answer leakage. Only call a bundle classroom-ready once both fresh-kernel executions, standalone solution execution, and independent review pass.

## Optional cited bundles

Only for explicitly requested citation work, also use the source/citation and manifest contracts. Add `metadata.icp.source_map: "source-map.json"`, the manifest's schema version (1 for PDF, 2 for native PPTX), and per-prompt `recitation_source` and `references` copied from the approved map. Include visible English reference blocks. The legacy citation validator also requires `learning-goals`, `lecture-review`, `review-example`, and `recap` tags and complete prompt/subpart provenance. Those additional requirements apply only to that optional workflow. Preserve existing cited bundles unless the user requests changes.
