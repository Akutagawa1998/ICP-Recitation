---
name: icp-recitation-prep
description: Prepare and review simple English student/instructor Jupyter notebook pairs and readable Python solutions with detailed Chinese comments for NYU Introduction to Computer Programming recitations. Use for recitation materials and explicitly requested source mapping, not grading or unrelated course administration.
---

# ICP Recitation Prep

Create a simple English notebook pair and a separate Chinese-commented solution folder from the requested recitation. Read [references/notebook-contract.md](references/notebook-contract.md) before authoring or reviewing.

Run the Python helpers in an environment with `nbformat`, `nbclient`, and a working `python3` Jupyter kernel (`ipykernel`). Use the available course environment if the system Python lacks these dependencies.

## Default workflow

1. Identify and read the requested file under `recitation/`. Preserve all exercises, subparts, sample data, and their order. Flag ambiguous wording or likely source typos. Preserve all course sources byte-for-byte.
2. Build a concise ordered exercise outline: complete original prompts, stable exercise/subpart IDs, concepts practiced, teaching purpose, and ambiguities. An in-memory handoff is sufficient. Do not require source-map files, hashes, lecture inventories, lecture index searches, page/slide references, or textbook matching.
3. Author the canonical instructor notebook entirely in English, including code comments, docstrings, identifiers, string messages, and explanatory outputs. Use short explanations and straightforward beginner-level code. Keep detailed teaching commentary in `solution/`.
4. Create `solution/README.md` in Chinese describing what the recitation covers and why each exercise is included. Create ordered `solution/exercise-NN.py` files with matching solution logic and detailed Chinese comments explaining every executable line. Follow the notebook contract for readability and verification.
5. Derive the student notebook with `python3 .agents/skills/icp-recitation-prep/scripts/derive_student_notebook.py <instructor.ipynb> <student.ipynb>`. After a repair, verify that the target is the derived student notebook for the same recitation before adding `--force`. Never author the two notebooks independently.
6. Run `python3 .agents/skills/icp-recitation-prep/scripts/validate_simple_pair.py <instructor.ipynb> <student.ipynb> --execute`. It checks derivation and executes both notebooks in fresh kernels and each solution script in a temporary working directory. Independently review completeness against the recitation source, English-only notebook content, simplicity, Chinese explanations, solution parity, and answer leakage. Automated validation alone does not establish classroom readiness.

For a full build, use the project agents sequentially when available: `icp_source_mapper` prepares the exercise outline, `icp_notebook_author` writes the notebooks and solution folder, and `icp_notebook_reviewer` independently audits the result. Do not let agents edit the same bundle concurrently. If unavailable, perform the stages directly and obtain independent review when available; report its absence honestly. Repairs to solution logic must update the corresponding Chinese solution file and regenerate the student notebook.

## Optional citation mapping

Only when the user explicitly requests lecture/textbook mapping, read [references/source-and-citation-contract.md](references/source-and-citation-contract.md) and [references/bundle-manifest-contract.md](references/bundle-manifest-contract.md). Use the existing source discovery and citation validator for that additional work. Existing cited bundles remain supported; do not remove or rewrite their mappings merely to adopt this simpler workflow. Missing lecture or textbook references do not block the default workflow and do not require approval.

For an explicitly requested cited bundle, also run `python3 .agents/skills/icp-recitation-prep/scripts/validate_notebook_pair.py <instructor.ipynb> <student.ipynb> --manifest <source-map.json> --root <repo-root> --execute`. Use `--allow-unresolved` only for actual unresolved entries with explicit persisted TA approval, as described in the optional citation contract.

## Output layout

Follow the repository's established `notebook/recitation-NN/` convention (otherwise use `materials/recitation-NN/`), unless the user specifies another location:

```text
notebook/recitation-NN/
|-- recitation-NN-instructor.ipynb
|-- recitation-NN-student.ipynb
`-- solution/
    |-- README.md
    |-- exercise-01.py
    `-- exercise-02.py
```

Add one solution file per original exercise, preserving subpart order within it. Local `assets/` and `source-map.json`/`source-map.md` are optional and appear only when needed or requested. Keep caches, executed QA copies, and temporary renders outside the repository. Never distribute the instructor notebook or `solution/` as part of student-only materials.
