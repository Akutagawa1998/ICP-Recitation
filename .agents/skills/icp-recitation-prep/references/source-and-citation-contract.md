# Source and citation contract

Use this contract whenever locating course material, mapping an exercise, or writing a visible citation.

## Source discovery

The repository source of truth is the material currently stored under these directories:

- `lecture/`: instructor lecture files
- `recitation/`: original recitation prompts
- `textbook/`: assigned textbook editions
- `syllabus/`: optional schedules or course policies when present

Re-scan on every preparation run. Match extensions case-insensitively and do not hardcode the number of weeks. The bundled `scripts/course_sources.py` helper inventories and searches PDFs and PPTX decks. Manifest version 2 supports native PPTX lecture citations as specified in the bundle manifest contract. Detect other source formats separately; do not silently ignore them or force a PDF locator onto them. Unsupported formats need a format-specific locator and validator extension before they can support a classroom-ready mapping.

When saving an inventory with `--output`, use a `.json` path outside all immutable source directories. The helper rejects source-directory targets and symlink output files even with `--force`, and replaces an approved JSON output atomically.

When saving an inventory with `--output`, use a `.json` path outside all immutable source directories. The helper rejects source-directory targets and symlink output files even with `--force`, and replaces an approved JSON output atomically.

Do not infer an authoritative relationship from filenames alone. A matching week number is a candidate; confirm it from topics, schedule information, or user direction. Preserve misspelled source filenames and record ambiguities explicitly.

## Locator semantics

All `pdf_page` values are one-based physical PDF pages.

For a native PPTX lecture in schema 2, use one-based `slide_number` in presentation order and `locator: "Slide N"`, along with the original file's path, SHA-256, slide title, anchor, status, and covers. Never use PDF page fields for PPTX. Visible references say `Lecture: Lecture 02, Slide N (PPTX)` and show the mapping status. The validator checks the anchor against that slide's text; image-only evidence needs visual inspection. All remaining rules below apply to PDFs unchanged.

For a lecture reference, record:

- stable `source_id`;
- repository-relative `path`;
- `pdf_page`;
- human locator such as `Slide 41` when available;
- actual PDF `page_label` only when the file exposes one;
- page heading;
- short `anchor` text found on that page;
- source file `sha256`; and
- mapping `status`.

For a textbook reference, also record:

- textbook edition in `source_id` or title;
- chapter;
- section number and title when the source exposes a section hierarchy;
- printed page or PDF page label when reliable; and
- physical `pdf_page` separately.

Never call a physical PDF page a printed textbook page. If a displayed label is absent or unreliable, omit it and keep the PDF page.

For a resolved textbook reference, use a numbered `section` value whenever the PDF exposes numbered sections. The section number and title must both agree with the active section at the cited page; a match elsewhere in the book is not sufficient. If the source genuinely exposes chapters but no section hierarchy, set `section` to `null`, `section_status` to `not_exposed`, and add a non-empty `section_note`. Do not use this representation to bypass an available table of contents or section structure.

## Mapping status

Use exactly one status:

- `direct`: the cited page explicitly teaches the concept tested by the exercise.
- `prerequisite`: the page teaches necessary background but not the exact syntax or operation in the exercise.
- `unresolved`: no defensible source was found or the source is ambiguous.

Do not use a nearby page as a `direct` match merely to make the reference list complete. An exercise with an `unresolved` lecture or textbook entry is a draft and must be brought to the TA's attention before it is called classroom-ready.

## Machine-readable reference

Put references on the exercise prompt cell at `cell.metadata.icp.references`. Use this shape:

```json
[
  {
    "kind": "lecture",
    "status": "direct",
    "covers": ["interactive and script modes"],
    "source_id": "lecture-01",
    "path": "lecture/Lecture 01.pdf",
    "sha256": "<64 lowercase hex characters>",
    "pdf_page": 41,
    "locator": "Slide 41",
    "title": "Python IDE",
    "anchor": "Shell (Interactive) mode"
  },
  {
    "kind": "textbook",
    "status": "direct",
    "covers": ["interactive and script modes"],
    "source_id": "gaddis-python-6e",
    "path": "textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf",
    "sha256": "<64 lowercase hex characters>",
    "chapter": "Chapter 1",
    "section": "1.5: Using Python",
    "printed_page": "46",
    "pdf_page": 47,
    "title": "Using Python",
    "anchor": "interactive mode and script mode"
  }
]
```

Keep anchors short enough to avoid reproducing source material, but distinctive enough for normalized exact matching. Prefer a heading or a phrase of roughly 3-12 words. Do not store full textbook paragraphs or page images as citation evidence.

For `unresolved`, include `kind`, `status`, `source_id` when known, the affected `covers` concepts, and a concise `note`; omit invented page fields.

Every exercise prompt declares a short `concepts` list. Every reference declares a `covers` list containing one or more exact values from that exercise's concepts. Taken together, the lecture entries must cover every declared concept, and the textbook entries must cover every declared concept; an `unresolved` entry can record the honest gap for a concept.

An unresolved mapping can be accepted for classroom use only when the TA explicitly approves it. Persist that decision on the unresolved entry instead of relying on chat history:

```json
{
  "approval": {
    "decision": "approved",
    "approver": "TA",
    "date": "2026-09-01",
    "note": "No assigned source covers this operation; keep the gap visible."
  }
}
```

Agents must never invent or infer this approval object.

## Visible reference block

Directly below each exercise prompt, show a compact block such as:

```markdown
**Knowledge references**

- Lecture: *Lecture 01*, Slide 41 (PDF p. 41), “Python IDE” — direct.
- Textbook: Gaddis, 6th ed., Chapter 1, §1.5 “Using Python,” printed p. 46 (PDF p. 47) — direct.
```

For prerequisite coverage, say so. For unresolved coverage, write `No direct coverage located` and explain the gap in one sentence. Do not hide unresolved mappings only in metadata.

Use repository-relative links when the notebook location makes them portable. Percent-encode spaces only when required by the notebook renderer.

## Source map

Write `source-map.md` beside the notebook pair with one row per exercise or subexercise. Include:

- a relevant-source inventory snapshot with source IDs, paths, and hashes;
- a `lecture selection` section listing candidates, selected lecture(s), and the syllabus locator, content evidence, user instruction, or other basis for the choice;
- stable exercise ID and original recitation locator;
- normalized source-block hash and the ordered subpart IDs/hashes;
- concepts tested;
- lecture locator and status;
- textbook chapter/section locator and status;
- short notes for ambiguities, source typos, or prerequisite-only matches.

The map is an audit summary, not a substitute for the visible per-exercise references or the machine-readable metadata.

The prompt cell's `metadata.icp.recitation_source` must also record the original recitation PDF's repository-relative path, SHA-256, one-based `pdf_page`, item label, and a short exact anchor from the exercise heading or prompt. This lets validation detect both source replacement and accidental transcription drift.

## Verification

For every non-unresolved reference:

1. Confirm the path exists under the repository root.
2. Confirm the one-based page is in range.
3. Confirm the normalized anchor occurs on that exact page.
4. Confirm a declared page label matches the PDF label when the file exposes labels.
5. Require `sha256` and confirm the file hash still matches.
6. Visually inspect pages with sparse or image-heavy extracted text.

If any check fails, mark the mapping stale or unresolved and remap it. Never silently preserve an old locator after a PDF is replaced.
