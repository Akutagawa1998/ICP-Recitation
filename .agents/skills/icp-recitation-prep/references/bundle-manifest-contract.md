# Bundle manifest contract

Use this contract only for explicitly requested citation mapping or maintenance of an existing cited bundle. The default workflow in `../SKILL.md` does not require a manifest, lecture selection, or textbook references. In the optional cited workflow, `source-map.json` is the machine-readable handoff and `source-map.md` is its human-readable companion. English-only notebooks and the Chinese `solution/` folder are still required for new builds.

## Required files

Place both files beside the notebook pair:

```text
materials/recitation-NN/
|-- source-map.json
|-- source-map.md
|-- recitation-NN-instructor.ipynb
`-- recitation-NN-student.ipynb
```

The instructor and student notebooks set `metadata.icp.source_map` to `source-map.json`.

The validator rejects a different manifest basename for classroom bundles. Objects reject unknown fields; extend the contract, derivation, and validator together under a new schema version rather than hiding extra payloads in metadata.

## Version 2: native PowerPoint lecture sources

Version 1 remains supported unchanged for PDF-only bundles. Use `schema_version: 2` in the manifest and both notebooks when a lecture is a PPTX file. All version-1 fields and invariants remain in force except for the following format-specific alternatives:

- A PPTX lecture inventory record has `slide_count` instead of `page_count`. Its `path` and `sha256` refer to the original PPTX, not a converted copy. Other source kinds remain PDF in version 2.
- A resolved PPTX lecture reference has `slide_number` instead of `pdf_page`, and `locator: "Slide N"`. The slide number is the one-based position in the presentation's slide list, including hidden slides. It must not contain `pdf_page`, `page_label`, or `printed_page`.
- A PDF inventory record still requires `page_count` and forbids `slide_count`; a PDF reference still requires `pdf_page` and forbids `slide_number`.
- Anchors are verified against native visible DrawingML text in the specified slide. Speaker notes are excluded. Slides with important image-only content still require visual review; a rendered copy never supplies invented PDF provenance.

Do not rewrite existing version-1 bundles just to adopt version 2.

## JSON schema

Use this version-1 shape:

```json
{
  "schema_version": 1,
  "recitation_id": "01",
  "title": "First steps with Python",
  "expected_exercise_count": 1,
  "source_inventory": [
    {
      "source_id": "recitation-01",
      "kind": "recitation",
      "path": "recitation/Recitaion 01.pdf",
      "sha256": "<64 lowercase hex characters>",
      "page_count": 2
    },
    {
      "source_id": "lecture-01",
      "kind": "lecture",
      "path": "lecture/Lecture 01.pdf",
      "sha256": "<64 lowercase hex characters>",
      "page_count": 45
    },
    {
      "source_id": "gaddis-python-6e",
      "kind": "textbook",
      "path": "textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf",
      "sha256": "<64 lowercase hex characters>",
      "page_count": 917
    }
  ],
  "recitation_source_id": "recitation-01",
  "lecture_selection": {
    "candidate_source_ids": ["lecture-01"],
    "selected_source_ids": ["lecture-01"],
    "basis": [
      {
        "kind": "content",
        "source_ids": ["lecture-01", "recitation-01"],
        "evidence": "Lecture 01 covers the interactive/script modes and number systems used by Recitation 01."
      }
    ]
  },
  "exercises": [
    {
      "exercise_id": "R01-E01",
      "order": 1,
      "prompt": "Exercises 1 – Try Python in Two Modes ...",
      "original_prompt_sha256": "<SHA-256 of the normalized complete PDF exercise block>",
      "subparts": [
        {
          "subpart_id": "R01-E01-P01",
          "label": "1)",
          "prompt": "1) Type 6 + 4 * 9 in the Python prompt and hit enter. Check what happens.",
          "original_prompt_sha256": "<SHA-256 of the normalized complete PDF subpart block>"
        }
      ],
      "concepts": ["interactive and script modes"],
      "recitation_source": {
        "source_id": "recitation-01",
        "path": "recitation/Recitaion 01.pdf",
        "sha256": "<64 lowercase hex characters>",
        "pdf_page": 1,
        "item_label": "Exercise 1",
        "anchor": "Try Python in Two Modes"
      },
      "references": [
        {
          "kind": "lecture",
          "status": "unresolved",
          "covers": ["interactive and script modes"],
          "note": "Replace this draft entry with verified evidence or a persisted TA decision."
        },
        {
          "kind": "textbook",
          "status": "unresolved",
          "covers": ["interactive and script modes"],
          "note": "Replace this draft entry with verified evidence or a persisted TA decision."
        }
      ]
    }
  ]
}
```

Populate `references` exactly as defined in `source-and-citation-contract.md`. The `path`, `sha256`, `kind`, and `source_id` of every resolved reference must agree with one unique `source_inventory` record.

## Invariants

- `recitation_id` is a string and preserves leading zeros.
- `expected_exercise_count` equals the length of `exercises`.
- Exercise `order` values are consecutive starting at 1; IDs are unique and remain stable across notebook variants.
- `prompt` faithfully contains the complete original wording for the exercise, including subparts and sample data. Formatting may be normalized, but content may not be shortened.
- `original_prompt_sha256` is SHA-256 over the UTF-8 bytes of the complete source block after Unicode-preserving case-folding and collapsing all whitespace to single spaces (the helper's `normalize_text`). The validator independently extracts the numbered block from the recitation PDF and requires both the declared hash and normalized `prompt` to match it.
- `subparts` is always a list. For each numbered subpart exposed by the source block, include one ordered object with stable `subpart_id`, the exact label (for example `1)`), complete subpart text, and its independently computed `original_prompt_sha256`. Use an empty list only when the source block has no numbered subparts.
- `recitation_source` records the exact original page, source hash, item label, and anchor.
- Every concept is covered by both a lecture entry and a textbook entry, including honest unresolved entries where needed.
- `source_inventory` IDs and paths are unique. Include the selected sources and all plausible lecture candidates considered for this recitation.
- `lecture_selection.selected_source_ids` is a non-empty subset of its candidates; `basis` records syllabus evidence, content evidence, or explicit user direction.
- Every `lecture_selection.basis` item has `kind` equal to `content`, `syllabus`, or `user`, plus non-empty `evidence`. A `syllabus` basis also identifies its `source_id`, one-based `pdf_page` or format-appropriate locator, and a short verified `anchor`; a `content` basis names the lecture/recitation source IDs it compares; a `user` basis records only an explicit direction actually supplied by the user.
- Agents copy the approved exercise records into notebook metadata without semantic edits. A citation correction goes back to the source mapper.

## Human-readable companion

`source-map.md` must show:

- the relevant inventory snapshot and hashes;
- lecture candidates, selection, and basis;
- one row per exercise in JSON order;
- the complete concept list;
- lecture and textbook statuses and locators;
- source typos, ambiguities, and persisted TA approvals.

The validator checks file presence, IDs, and notebook agreement. The independent reviewer checks that the Markdown faithfully communicates the JSON mapping and that the manifest itself contains every original exercise.
