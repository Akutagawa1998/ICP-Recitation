---
name: icp-recitation-prep
description: Prepare NYU Introduction to Computer Programming recitations from lecture, recitation, and textbook source files. Use when creating or updating paired Jupyter notebooks (student questions and instructor solutions), mapping exercises to exact lecture PDF pages and textbook chapters/sections, or validating recitation materials. Do not use for unrelated course administration or grading.
---

# ICP Recitation Prep

Produce a classroom-ready notebook pair grounded in the repository's current course materials. Preserve the source PDFs and make every exercise traceable to both a lecture location and a textbook location.

## Route the work

1. Identify the requested recitation and the lecture(s) it follows. Discover files by content and natural-numbered names; do not assume the repository stops at the currently present week.
2. Read [references/source-and-citation-contract.md](references/source-and-citation-contract.md) before mapping sources or writing citations.
3. Read [references/bundle-manifest-contract.md](references/bundle-manifest-contract.md) for a full build or audit.
4. Read [references/notebook-contract.md](references/notebook-contract.md) before authoring, deriving, or reviewing notebooks.
5. For a full recitation build, use the project custom agents when available:
   - Delegate source and exercise mapping to `icp_source_mapper`; require a complete, schema-valid v1 `source-map.json` payload, not a prose summary or partial map.
   - Delegate notebook implementation to `icp_notebook_author` after the source map is stable.
   - Delegate independent final review to `icp_notebook_reviewer` after both notebooks exist.
   Keep the main agent responsible for resolving disagreements and delivering the final artifacts.
6. When custom agents are unavailable, follow the same stages directly. Do not treat delegation as a prerequisite for completion.
7. Route review defects by ownership:
   - source evidence, locator, status, lecture selection, or manifest meaning -> source mapper;
   - JSON/Markdown persistence, notebook projection, derivation, or execution -> notebook author;
   - TA approval provenance or a disputed pedagogical choice -> main agent and TA.
   After any repair, derive the student version again, rerun validation, and request a fresh independent review.

## Required workflow

### 1. Inventory and inspect

- Treat `lecture/`, `recitation/`, `textbook/`, and optional `syllabus/` as source directories. Search recursively and case-insensitively for supported files.
- Preserve every source file byte-for-byte. Never rename or correct a source filename merely because it contains a typo.
- Run `python3 .agents/skills/icp-recitation-prep/scripts/course_sources.py inventory --root <repo-root>` to list PDFs and page metadata.
- Use the same helper's `search` subcommand to locate candidate pages, then inspect the full relevant pages. Search results are leads, not proof of pedagogical alignment.
- If a required lecture, recitation, or textbook is missing or ambiguous, stop before inventing content. Report the exact missing source or unresolved choice.

### 2. Build a source map

- Transcribe each recitation exercise faithfully, correcting only obvious formatting artifacts. Record substantive ambiguities or likely typos instead of silently changing the assignment. Bind every complete numbered exercise and subpart to the normalized source-block hashes required by the manifest contract.
- For every exercise, map the concepts it actually tests to:
  - at least one precise lecture page or slide; and
  - at least one precise textbook chapter and section when the textbook exposes sections.
- Store the approved machine-readable mapping as `source-map.json` and its human-readable companion as `source-map.md`, without changing the mapper's meaning or status labels.
- Require the mapping payload to satisfy the complete version-1 manifest contract, including the source inventory, lecture selection evidence, full ordered prompts, prompt provenance fields, concepts, and references.
- Every non-unresolved reference must include a short anchor that appears on the cited source page plus its exact locator and source hash. If no trustworthy mapping exists, label the reference `unresolved`, include a reason, and do not invent page fields.

### 3. Author the instructor notebook

- Make the instructor notebook the canonical source. Use Markdown and executable Python code, with optional local images only when they materially improve teaching.
- Start with a concise lecture review organized by concepts rather than by reproducing slides. Follow each concept with a small executable example.
- Then cover every recitation exercise in the original order. Keep the original task visible, add the standardized source block, and demonstrate every declared numbered subpart in its own tagged code cell (or cells).
- The notebook must run top-to-bottom without uncaught exceptions. Demonstrate syntax/runtime errors with safe wrappers such as `compile`, `exec`, or `try`/`except` so execution can continue.
- Tag answer cells and add the required `metadata.icp` fields from the notebook contract. Do not hand-author the student notebook independently.
- Copy the approved per-exercise `recitation_source` and source references into cell metadata; do not ask the author agent to reconstruct provenance from prose.

### 4. Derive the student notebook

- On first creation, run `python3 .agents/skills/icp-recitation-prep/scripts/derive_student_notebook.py <instructor.ipynb> <student.ipynb>`.
- After an instructor repair, first confirm that `<student.ipynb>` is the expected derived path for the same recitation, then rerun with `--force`. Never use `--force` on an arbitrary or user-authored notebook.
- The derivation must remove instructor-only commentary, replace solution cells with their declared student stubs, and clear all outputs and execution counts.
- Do not leak answers through Markdown, output, metadata, filenames embedded in cells, or pre-filled variable values.

### 5. Execute and validate

- Execute the instructor notebook from a clean temporary working directory. Save verified outputs in the delivered instructor notebook when practical.
- Run the complete gate: `python3 .agents/skills/icp-recitation-prep/scripts/validate_notebook_pair.py <instructor.ipynb> <student.ipynb> --manifest <source-map.json> --root <repo-root> --execute`.
- If there are no unresolved references, do not add `--allow-unresolved`. If and only if every unresolved entry contains an explicit, valid TA approval object that was not inferred by an agent, append `--allow-unresolved`. Otherwise keep the bundle blocked as a draft.
- Resolve all validation errors. Review warnings rather than suppressing them automatically.
- Independently check pedagogical pacing, question/answer parity, source accuracy, and whether the student version leaves useful scaffolding without revealing the solution.
- Treat duplicate inferred source IDs or multiple unresolved candidates for the same week as blocking ambiguities until explicitly disambiguated.

## Output layout

For recitation `NN`, default to:

```text
materials/recitation-NN/
|-- recitation-NN-instructor.ipynb
|-- recitation-NN-student.ipynb
|-- source-map.json
|-- source-map.md
`-- assets/                       # only when the notebooks use local images
```

Use a different location only when the repository already establishes a stronger convention or the user requests one.

## Adaptation rules

- Re-scan sources on every build so newly added lectures and recitations are discovered automatically.
- Match weeks by explicit identifiers and content. A similarly numbered file is a candidate, not automatic evidence that it is the correct lecture.
- Keep notebook and citation metadata schema-versioned. When extending the schema, update the derivation and validation scripts together.
- Prefer small, backward-compatible changes to the contract so older recitations remain reproducible.
- Do not add concepts, libraries, or syntax that students have not yet encountered unless clearly marked as optional enrichment.
