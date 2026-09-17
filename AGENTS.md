# ICP Recitation repository instructions

## Source preservation

- Treat files under `lecture/`, `recitation/`, `textbook/`, and optional `syllabus/` as immutable course sources.
- Do not rename a source to correct spelling, replace a PDF, or change source content unless the user explicitly asks.
- When citations are requested, distinguish physical PDF pages from slide numbers, printed pages, and PDF page labels. Never invent a match.

## Recitation preparation

- Use `$icp-recitation-prep` for creating, updating, or auditing recitation notebooks and their solution folders.
- Do not search lecture indexes, lecture page/slide references, or textbook mappings by default. Read the requested recitation source; citation mapping is optional and only done when explicitly requested.
- A full build should use the project agents sequentially when available: `icp_source_mapper` for an ordered exercise outline, then `icp_notebook_author`, then `icp_notebook_reviewer`. Do not allow agents to edit the same bundle concurrently.
- Author one canonical instructor notebook and derive the student notebook with the skill script. Never maintain them independently.
- Write the instructor notebook entirely in English, including Markdown, code comments, docstrings, identifiers, string messages, and explanatory outputs. Keep its structure, prose, and code simple and appropriate for beginners.
- Create `solution/` beside each notebook pair. Include a Chinese overview of coverage and teaching purpose, plus readable Python solutions with detailed Chinese comments explaining every executable line and each exercise's purpose. Keep identifiers and program messages in English, and keep solution logic consistent with the instructor notebook.
- Preserve the original exercise and subexercise order. Surface likely source typos or ambiguous wording instead of silently changing the assignment.
- Call a bundle classroom-ready only after both notebook variants execute from fresh kernels, the Chinese solution files are verified, and an independent review has no blocking findings. Validate citations only when citation mapping was requested.

## Output convention

- Follow the established `notebook/recitation-NN/` convention; otherwise default to `materials/recitation-NN/`. An explicit user path takes precedence.
- Keep `solution/`, optional source mappings, and local image assets beside the notebook pair.
- Keep caches, executed QA copies, and temporary renders out of the repository.
