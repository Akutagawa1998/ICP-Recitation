# Recitation 01 source map

- Title: **First steps with Python**
- Schema: version 1 (`source-map.json`)
- Mapping status: **draft — 9 unresolved reference entries require TA review; no TA approval has been inferred or recorded**
- Expected exercises: **8**
- Recitation source: `recitation-01`

## Relevant source inventory

| Source ID | Kind | Repository-relative path | Physical PDF pages | SHA-256 |
|---|---|---|---:|---|
| `recitation-01` | recitation | `recitation/Recitaion 01.pdf` | 2 | `f34480cf0dbc0fe9b6c4d94e94f852888c1b3116e8ab25ef5105ed7282b2e76b` |
| `lecture-01` | lecture | `lecture/Lecture 01.pdf` | 45 | `e8d9dc65dd0f21c5f0e8c77ea2e3b96ee0f8e0dc4b7340a44ff2e825ecdb9b31` |
| `textbook-starting-out-with-python-revel-tony-gaddis-6e` | textbook | `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf` | 917 | `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c` |

No `syllabus/` source and no non-PDF course source were present in this inventory run.

## Lecture selection

- Candidates considered: `lecture-01`.
- Selected: `lecture-01`.
- Basis: content comparison of `lecture-01` with `recitation-01`. Lecture 01 directly overlaps the recitation on interactive/script modes (Slide 41), binary notation and conversion (Slide 21), hexadecimal representation (Slide 28), and `bin()`/`hex()` checks (Slide 29). The comparison also exposes the unresolved lecture gaps recorded below.
- No syllabus evidence was available. Selection is not based on numbering alone: `lecture-01` is also the only lecture source currently present and its inspected content matches the recitation's principal topics.

## Exercise map

All `PDF p.` values below are one-based physical PDF pages. Printed textbook pages are shown separately.

| Exercise | Original recitation locator | Normalized source-block SHA-256 | Concepts | Lecture mapping | Textbook mapping | Notes |
|---|---|---|---|---|---|---|
| `R01-E01` | `recitation-01`, PDF p.1, `Exercises 1`, anchor “Try Python in Two Modes” | `9c888932b65a238ab43b9c1ae99b1bb3d1d898178d251c9a3ec75ced3e6ab887` | interactive and script modes; displaying script output with print | **direct:** `lecture-01`, Slide 41 (PDF p.41), “Pyrhon IDE,” anchor “Shell (Interactive) mode,” for modes. **unresolved:** no Lecture 01 page teaches Python `print` or explicit script output. | **direct:** Chapter 1, §1.5 “Using Python,” printed p.46 (PDF p.47), anchor “interactive mode and script mode”; and printed p.48 (PDF p.49), “Writing Python Programs and Running Them in Script Mode,” anchor “program that displays the following three lines of text.” | Source subpart 2 creates `test1.py`, while subpart 3 says `text1.py`; preserved verbatim as a likely typo. |
| `R01-E02` | `recitation-01`, PDF p.1, `Exercises 2`, anchor “Evaluate expression” | `f886ffe0efb9617aa70c625050f974392ca3ee852d115bae7a4089d46c3d54a9` | evaluating arithmetic expressions interactively; Python multiplication and exponentiation operators | **direct:** `lecture-01`, Slide 41 (PDF p.41), “Pyrhon IDE,” anchor “Best for quick tests and calculations,” for interactive evaluation. **unresolved:** Lecture 01 does not teach Python `*`/`**` syntax. | **direct:** Chapter 2, §2.7 “Performing Calculations,” printed p.80 (PDF p.81), anchor “Python has numerous operators that can be used to perform mathematical calculations.” | None beyond the unresolved lecture gap. |
| `R01-E03` | `recitation-01`, PDF p.1, `Exercises 3`, anchor “Syntax error” | `241b1d56e82186d1def06783f413665e0a86a33e04683e7847900bd173520d3d` | Python syntax errors | **unresolved:** no Lecture 01 page teaches syntax rules or Python syntax errors. | **direct:** Chapter 1, §1.4 “(Noninteractive) Checkpoint Questions from the Book,” printed p.45 (PDF p.46), page heading “Executing a high-level program with an interpreter,” anchor “A syntax error is a mistake.” | The exact active PDF TOC entry at physical p.46 is the §1.4 checkpoint title even though the explanatory paragraph precedes that checkpoint heading on the same page. |
| `R01-E04` | `recitation-01`, PDF p.1, `Exercises 4`, anchor “Print hello” | `3ad02ae6c23adcd2b6e1e8f24a8d8fe71d7daf3033993e75eb2052ad16e36cdf` | using print to display a string; string literals and quotation marks | **unresolved:** Lecture 01 does not teach Python `print` or string-literal quotation. | **direct:** Chapter 2, §2.3 “Displaying Output with the print Function,” printed p.62 (PDF p.63), anchor “the print function, which displays output on the screen”; and printed p.63 (PDF p.64), “Strings and String Literals,” anchor “string literals must be enclosed in quote marks.” | None beyond the unresolved lecture gap. |
| `R01-E05` | `recitation-01`, PDF p.1, `Exercises 5`, anchor “Say \"cheese\"” | `a120bb1a040fd30f0e50e6993a928ffc83e5836d9f70491fe7828d2e269a95ea` | string literals and quotation marks; undefined-name errors | **unresolved:** Lecture 01 teaches neither concept. | **direct:** Chapter 2, §2.3, printed p.63 (PDF p.64), “Strings and String Literals,” anchor “string literals must be enclosed in quote marks,” for quotation. **unresolved:** no locator safely identifies the `NameError` type requested by the exercise; a “name is not defined” sentence occurs across a TOC section boundary and does not name `NameError`. | Requires TA review for both the lecture gap and the textbook error-type gap. |
| `R01-E06` | `recitation-01`, PDF p.2, `Exercises 6`, anchor “Getting to know print” | `4d173e02cb7d373279456d366e102b06ae5bc2afcc551b1b05700c0aa19af1c7` | displaying multiple lines with print; blank-line formatting | **unresolved:** Lecture 01 does not teach Python print calls or newline/blank-line formatting. | **direct:** Chapter 2, §2.3, printed p.62 (PDF p.63), anchor “the statements in this program execute in the order that they appear”; and §2.9 “More About the print Function,” printed p.96 (PDF p.97), “Escape Characters,” anchor “causes output to advance to the next line.” | None beyond the unresolved lecture gap. |
| `R01-E07` | `recitation-01`, PDF p.2, `Exercises 7`, anchor “Binary Numbering System” | `3fae5afaedc70efcebd346d774ef2177817cc5cb0c3ff82c18556deea9875511` | binary-to-decimal conversion; Python binary literals and `bin()` | **direct:** `lecture-01`, Slide 21 (PDF p.21), “Storing integers,” anchor “a binary preceded by ‘0b’”; and Slide 29 (PDF p.29), “You Try it!,” anchor “Try bin() and hex() functions in interactive mode.” | **direct:** Chapter 1, §1.3 “How Computers Store Data,” printed p.35 (PDF p.36), “Determining the value of a binary number,” anchor “To determine the value of a binary number,” for conversion. **unresolved:** no direct textbook coverage of Python `0b` literals or `bin()` was located. | Textbook number-system theory is present; Python-specific syntax is not. |
| `R01-E08` | `recitation-01`, PDF p.2, `Exercises 8`, anchor “Hexadecimal Numbering System” | `9a0f5e5ae2e937350b4cea4d9f53bf7cd1dd356dc2746cedcbb1c27addfc0ebd` | hexadecimal-to-decimal conversion; converting among decimal, binary, and hexadecimal; Python hexadecimal literals and `hex()` | **direct:** `lecture-01`, Slide 28 (PDF p.28), “Hexadecimal,” anchor “One hexadecimal digit represents four binary bits”; and Slide 29 (PDF p.29), “You Try it!,” anchor “Try bin() and hex() functions in interactive mode.” | **prerequisite:** Chapter 1, §1.3, printed p.34 (PDF p.35), “Storing Numbers,” anchor “the binary numbering system,” for binary positional-value background only. **unresolved:** no substantive textbook coverage of hexadecimal conversion, Python `0x`, or `hex()` was located. | The final conversion table is unnumbered; the v1 extractor attaches it to numbered subpart 3. Ask the TA whether it should be a separate pedagogical subpart, while preserving the manifest shape for validation. |

## Ordered subpart audit

Prompts below are whitespace-normalized faithful transcriptions. Hashes are SHA-256 over Unicode-preserving case-folded text with whitespace collapsed to single spaces.

| Subpart ID | Label | Complete normalized prompt | Normalized SHA-256 |
|---|---|---|---|
| `R01-E01-P01` | `1)` | 1) Type 6 + 4 * 9 in the Python prompt and hit enter. Check what happens. | `107d0f3e835d71449fba3a52a90ee00c208d60712213be54660aca6d4427cebc` |
| `R01-E01-P02` | `2)` | 2) Now create a python script named test1.py with the following contents: 6+4*9 What happens when you run this script? | `8aaf25d278c2ab4276da59fd3f00ee52973d7bc11f6728bd0a19aa7005c6c533` |
| `R01-E01-P03` | `3)` | 3) Now change the contents in text1.py to: print (6 + 4 * 9) What happens when you run the script? | `c2dc7e7d6d14891204a76677330f7bbd552ddbdc1c56293c2b7c0bb774b95313` |
| `R01-E02-P01` | `1)` | 1) Using the Python interpreter, type 1 + 2 and then hit return. Check out what happens. | `b286f3c0bcb3979295685e3ea806a5e5e77d38bca955a1742e66c8495bf4ca9b` |
| `R01-E02-P02` | `2)` | 2) \* is the multiplication operator, and \*\* is the exponentiation operator. Experiment by entering different expressions and recording what is displayed by the Python interpreter. | `63481304ef9a538cd4fb0f598b851b6f19e6a5e1d1a68d0f51fb4e369cf97d65` |
| `R01-E03-P01` | `1)` | 1) Type 1 2 and then hit return. Check out what happens this time. In many cases, Python indicates where the syntax error occurred, but it is not always right, and it doesn’t give you much information about what is wrong. So, for the most part, the burden is on you to learn the syntax rules. | `7f236b82c67e3dc559b7d73debe148128b9b17188e2ca1a8cdee4e2f55123b66` |
| `R01-E04-P01` | `1)` | 1) Type `print(\"hello\")` at the Python prompt. Check out what happens. | `b334f62f67a930f060a8985adf318613936ebf3134bf8729a74461436a21c510` |
| `R01-E04-P02` | `2)` | 2) Now type `\"hello\"` and check your result. | `735b547f00df4033e8c0e88c79f59a8b97d5ec0312cf18e1141abda3cabedb87` |
| `R01-E06-P01` | `1)` | 1) Write a program named using_print1.py that displays the following then run from the command prompt: This is line 1. This is line 2, with a blank line above it. | `8e276d55c9a3548e2bd156d623b08022c6e6325c6ed9c5463851fa3460a3c665` |
| `R01-E07-P01` | `1)` | 1) Type in the interpreter 0b10011010 and check out what happens. | `efea656f1a064fbadb12e2b8a08655e976e0cd6c37d0129e6699c49803923e88` |
| `R01-E07-P02` | `2)` | 2) Try different binary values and check if the conversion is correct. Python also has a built-in function that allows one to display numbers in binary representation. | `7bee38c0f7d1225857ffb05ca92696b486e9f37bd6ab6c625aa239e6c1f81ce2` |
| `R01-E07-P03` | `3)` | 3) Type bin(100) and check out what happens. What kind of output is displayed? Try with different values. | `c12a03fb7a586c7329f30d39c2fb186c91236c93710cf764291fa7a66ffa3cf9` |
| `R01-E08-P01` | `1)` | 1) Type in the interpreter 0xAB and check out what happens. | `86b0c55f5aadca5206b2750fe1969b703650b4ff372955330134da60991fcc08` |
| `R01-E08-P02` | `2)` | 2) Try different hexadecimal values and check if the conversion is correct. Python also has a built-in function that allows you to display numbers in hexadecimal representation. | `64b94594d2f8e4a32b00b4a2c30b54eba31fb43bb0e8efd52ab8ce93fa06adf7` |
| `R01-E08-P03` | `3)` | 3) Type hex(100) and check out what happens. What kind of output is displayed? Fill the following table by converting the values provided in one of the columns to corresponding missing representation. Use Python’s built-in functions to check if the conversions are correct. Decimal Binary Hexadecimal 0b1100 100 0xA4 247 0x12C | `46aee7bbad2c9cba7cf04ca1fbb28bae6c1a5e31612b0588a30b6acf446bbd14` |

`R01-E05` exposes no numbered subpart in the source block, so its manifest `subparts` list is empty.

## Source wording and ambiguity log

1. The repository filename and PDF heading spell **Recitaion**. The source path and source wording are preserved unchanged.
2. `R01-E01` changes the filename from `test1.py` in item 2 to `text1.py` in item 3. This is likely a source typo; it is not silently corrected.
3. Lecture Slide 41 spells its heading **Pyrhon IDE**. The page title is preserved in the mapping.
4. `R01-E08` places the conversion table after numbered item 3 without a new number. The version-1 extractor therefore includes the entire table in `R01-E08-P03`; the table must not be dropped or independently renumbered without a contract/TA decision.

## Appendix: unresolved decisions

These are mapping decisions, not missing manifest fields. No approval object is present because no TA approval was supplied.

1. `R01-E01` lecture coverage for **displaying script output with print**: Lecture 01 distinguishes modes but never teaches Python `print` or explicit script output.
2. `R01-E02` lecture coverage for **Python multiplication and exponentiation operators**: Lecture 01 lacks `*`/`**` syntax.
3. `R01-E03` lecture coverage for **Python syntax errors**: no relevant lecture page was found.
4. `R01-E04` lecture coverage for **using print to display a string** and **string literals and quotation marks**: no relevant lecture page was found.
5. `R01-E05` lecture coverage for **string literals and quotation marks** and **undefined-name errors**: no relevant lecture page was found.
6. `R01-E05` textbook coverage for **undefined-name errors**: the textbook does not safely provide an exact, section-consistent locator that identifies the `NameError` type requested by the exercise.
7. `R01-E06` lecture coverage for **displaying multiple lines with print** and **blank-line formatting**: no relevant lecture page was found.
8. `R01-E07` textbook coverage for **Python binary literals and bin()**: binary theory is covered, but Python `0b`/`bin()` is not.
9. `R01-E08` textbook coverage for **hexadecimal-to-decimal conversion** and **Python hexadecimal literals and hex()**: no substantive instruction was located; §1.3 supplies only prerequisite binary material.
10. TA wording decision: should `text1.py` in `R01-E01-P03` remain literal classroom wording, or be visibly annotated as likely intended to mean `test1.py`? The source-map JSON preserves it either way.
11. TA structure decision: should the unnumbered conversion table in `R01-E08` be taught as a separate pedagogical unit? The current v1 manifest must still keep it inside `R01-E08-P03` to match the source extractor and hashes.

Until the nine unresolved reference entries receive verified replacements or explicit persisted TA approvals, the bundle is a draft and must not be called classroom-ready.
