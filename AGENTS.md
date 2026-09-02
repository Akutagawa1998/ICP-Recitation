# ICP Recitation repository instructions

## Source preservation

- Treat files under `lecture/`, `recitation/`, `textbook/`, and optional `syllabus/` as immutable course sources.
- Do not rename a source to correct spelling, replace a PDF, or change source content unless the user explicitly asks.
- Distinguish one-based physical PDF pages from slide numbers, printed textbook pages, and PDF page labels.
- Never invent a lecture or textbook match. Mark missing or ambiguous coverage explicitly.

## Recitation preparation

- Use `$icp-recitation-prep` for creating, updating, or auditing recitation notebooks and source mappings.
- A full build should use the project custom agents sequentially when available: `icp_source_mapper`, then `icp_notebook_author`, then `icp_notebook_reviewer`. Do not allow agents to edit the same recitation bundle concurrently.
- Author one canonical instructor notebook and derive the student notebook with the skill script. Never maintain question and answer versions independently.
- Preserve the original exercise and subexercise order. Surface likely source typos or ambiguous wording instead of silently changing the assignment.
- Call a notebook pair classroom-ready only after citations validate, both variants execute from a fresh kernel, and an independent review has no blocking findings.

## Output convention

- By default, put generated materials for recitation `NN` under `materials/recitation-NN/`; follow an explicit user request or an established repository convention when one exists.
- Keep source mappings and local image assets beside the notebook pair.
- Keep caches, executed QA copies, and temporary renders out of the repository.
