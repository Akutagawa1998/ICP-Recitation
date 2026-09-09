# Recitation 02 source map

依据已批准 schema 2 payload；JSON 是机器可读的权威映射，本文件按相同顺序显示内容。无 unresolved 引用，无 TA approval。

## Source inventory / 来源快照

| source_id | kind | path | 页数 / slide 数 | SHA-256 |
|---|---|---|---:|---|
| recitation-02 | recitation | `recitation/Recitaion 02.pdf` | 4 physical PDF pages | `1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d` |
| lecture-01 | lecture | `lecture/Lecture 01.pdf` | 45 physical PDF pages | `e8d9dc65dd0f21c5f0e8c77ea2e3b96ee0f8e0dc4b7340a44ff2e825ecdb9b31` |
| lecture-02 | lecture | `lecture/Lecture 02.pptx` | 55 slides | `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28` |
| gaddis-python-6e | textbook | `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf` | 917 physical PDF pages | `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c` |

## Lecture selection / 讲课选择

Candidates: lecture-01, lecture-02

Selected: lecture-02

- **user**: The user explicitly requested a Recitation 2 notebook based on lecture 2 and recitation 2.
- **content**: Lecture 02 Slide 1 and Recitation 02 PDF p.1 share Input, Processing, and Output. Lecture 02 Slides 14–25, 29–33, 39–53 cover the numeric types, operators, assignments, input/output, and formatting in Recitation 02 Exercises 1–9. Slide 55 explicitly assigns recitation 02. Lecture 01 PDF pp.41–45 introduces execution modes and assigns recitation 01, so it is a previous-lecture candidate rather than the selected lecture. Selected lecture-02 SHA-256: 48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28

## Ordered exercise mapping / 逐题索引

| Exercise ID | 原题定位 | Concepts | Lecture status / locator | Textbook status / locator |
|---|---|---|---|---|
| R02-E01 | Exercise 1, PDF p. 1 | numeric result types; true and floor division; remainder operation; negative-operand remainder; operator precedence | direct: Slide 14 (PPTX); direct: Slide 19 (PPTX); direct: Slide 20 (PPTX); direct: Slide 22 (PPTX) | direct: Chapter 2, §2.7: Performing Calculations, PDF p. 91; direct: Chapter 2, §2.7: Performing Calculations, PDF p. 84; direct: Chapter 2, §2.7: Performing Calculations, PDF p. 88; prerequisite: Chapter 2, §2.7: Performing Calculations, PDF p. 84; direct: Chapter 2, §2.7: Performing Calculations, PDF p. 85 |
| R02-E02 | Exercise 2, PDF p. 1 | int conversion; str conversion; numeric remainder; string concatenation and operand types; string repetition; integer repetition count; unassigned variable names | direct: Slide 15 (PPTX); direct: Slide 19 (PPTX); direct: Slide 25 (PPTX); direct: Slide 24 (PPTX); direct: Slide 33 (PPTX) | direct: Chapter 2, §2.6: Reading Input from the Keyboard, PDF p. 79; direct: Chapter 6, §6.1: Introduction to File Input and Output, PDF p. 363; direct: Chapter 2, §2.7: Performing Calculations, PDF p. 88; direct: Chapter 2, §2.8: String Concatenation, PDF p. 94; direct: Chapter 8, §8.3: Testing, Searching, and Manipulating Strings, PDF p. 501; prerequisite: Chapter 7, §7.2: Introduction to Lists, PDF p. 407; direct: Chapter 2, §2.5: Variables, PDF p. 69 |
| R02-E03 | Exercise 3, PDF p. 1 | string delimiters and syntax errors; escaped quotation marks; newline and tab characters | direct: Slide 9 (PPTX); direct: Slide 10 (PPTX); direct: Slide 11 (PPTX) | prerequisite: Chapter 2, §2.3: Displaying Output with the print Function, PDF p. 64; direct: Chapter 2, §2.9: More About the print Function, PDF p. 98; direct: Chapter 2, §2.9: More About the print Function, PDF p. 97 |
| R02-E04 | Exercise 4, PDF p. 2 | multiple assignment; old right-hand-side values before rebinding; reassignment and loss of references | direct: Slide 33 (PPTX); prerequisite: Slide 29 (PPTX); direct: Slide 32 (PPTX) | direct: Chapter 2, §2.5: Variables, PDF p. 70; prerequisite: Chapter 2, §2.5: Variables, PDF p. 70; direct: Chapter 2, §2.5: Variables, PDF p. 72 |
| R02-E05 | Exercise 5, PDF p. 3 | string literals versus variable values; print separators and endings; newline and tab characters | direct: Slide 44 (PPTX); direct: Slide 46 (PPTX); direct: Slide 11 (PPTX) | direct: Chapter 2, §2.5: Variables, PDF p. 72; direct: Chapter 2, §2.9: More About the print Function, PDF p. 96; direct: Chapter 2, §2.9: More About the print Function, PDF p. 97 |
| R02-E06 | Exercise 6, PDF p. 3 | f-string placeholders; numeric field width and precision; alignment; custom fill characters; string precision truncation; zero padding with explicit alignment | direct: Slide 48 (PPTX); direct: Slide 53 (PPTX); direct: Slide 51 (PPTX); direct: Slide 52 (PPTX); prerequisite: Slide 53 (PPTX) | direct: Chapter 2, §2.10: Displaying Formatted Output with F-strings, PDF p. 99; direct: Chapter 2, §2.10: Displaying Formatted Output with F-strings, PDF p. 101; direct: Chapter 2, §2.10: Displaying Formatted Output with F-strings, PDF p. 103; direct: Chapter 2, §2.10: Displaying Formatted Output with F-strings, PDF p. 106; prerequisite: Chapter 2, §2.10: Displaying Formatted Output with F-strings, PDF p. 106; prerequisite: Chapter 2, §2.10: Displaying Formatted Output with F-strings, PDF p. 100 |
| R02-E07 | Exercise 7, PDF p. 4 | numeric keyboard input; percentage calculation; displaying computed values | direct: Slide 40 (PPTX); direct: Slide 49 (PPTX); direct: Slide 44 (PPTX) | direct: Chapter 2, §2.6: Reading Input from the Keyboard, PDF p. 79; direct: Chapter 2, §2.7: Performing Calculations, PDF p. 83 |
| R02-E08 | Exercise 8, PDF p. 4 | numeric keyboard input; translating a mathematical formula; displaying computed values | direct: Slide 40 (PPTX); prerequisite: Slide 19 (PPTX); direct: Slide 44 (PPTX) | direct: Chapter 2, §2.6: Reading Input from the Keyboard, PDF p. 79; direct: Chapter 2, §2.7: Performing Calculations, PDF p. 89; direct: Chapter 2, §2.7: Performing Calculations, PDF p. 83 |
| R02-E09 | Exercise 9, PDF p. 4 | numeric keyboard input; proportional ingredient scaling; displaying computed values | direct: Slide 40 (PPTX); prerequisite: Slide 36 (PPTX); direct: Slide 44 (PPTX) | direct: Chapter 2, §2.6: Reading Input from the Keyboard, PDF p. 79; prerequisite: Chapter 2, §2.7: Performing Calculations, PDF p. 89; direct: Chapter 2, §2.7: Performing Calculations, PDF p. 83 |

## R02-E01 — order 1

Original normalized exercise SHA-256: `378f942f2a492da62f62ef1b679ba6e4281eab209345e715dfee8c7ff97b8976`

### Original prompt

```text
Exercises 1 – Numeric values and operations 
Evaluate the following expressions and specify their type.  
5 * -6 
 
34 / 10 
 
(34 // 10) * (1.0 + 2) 
 
34 % 10 
 
23 % 4.0 
 
25 + 30 / 6 
 
-7 % 3 
 
100 - 25 * 3 % 4
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 1,
  "item_label": "Exercise 1",
  "anchor": "Numeric values and operations"
}
```

### Ordered numbered subparts

None declared by the numbered source parser. Unnumbered expressions/programs remain fully included in the original prompt and notebook.

### Concepts

- numeric result types
- true and floor division
- remainder operation
- negative-operand remainder
- operator precedence

### References (original order)

- Lecture: *Lecture 02*, Slide 14 (PPTX), “Mixing numeric types” — **direct**；覆盖：numeric result types。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Mixing numeric types; anchor: `mix numeric types during arithmetic operations`
- Lecture: *Lecture 02*, Slide 19 (PPTX), “Operators on int and float” — **direct**；覆盖：true and floor division / remainder operation。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Operators on int and float; anchor: `return the remainder of the division`
- Lecture: *Lecture 02*, Slide 20 (PPTX), “Operators on int and float” — **direct**；覆盖：negative-operand remainder。 This slide includes a negative-dividend modulo example; its separate 10 // 0.25 output contains a typo.
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Operators on int and float; anchor: `Modulo Division (%)`
- Lecture: *Lecture 02*, Slide 22 (PPTX), “Operators Precedence” — **direct**；覆盖：operator precedence。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Operators Precedence; anchor: `Parentheses tell Python to do these operations first.`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 90 (PDF p. 91) — **direct**；覆盖：numeric result types。 Read the general mixed-type rules together with the explicit / exception on PDF p.84.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Mixed-Type Expressions and Data Type Conversion; anchor: `Mixed-Type Expressions and Data Type Conversion`
  - PDF page_label: `90`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 83 (PDF p. 84) — **direct**；覆盖：true and floor division。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Floating-Point and Integer Division; anchor: `Python has two different division operators`
  - PDF page_label: `83`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 87 (PDF p. 88) — **direct**；覆盖：remainder operation。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: The Remainder Operator; anchor: `The Remainder Operator`
  - PDF page_label: `87`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 83 (PDF p. 84) — **prerequisite**；覆盖：negative-operand remainder。 Teaches negative floor division, a prerequisite for interpreting negative modulo; does not explicitly demonstrate negative-dividend %.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Floating-Point and Integer Division; anchor: `when the result is negative`
  - PDF page_label: `83`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 84 (PDF p. 85) — **direct**；覆盖：operator precedence。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Operator Precedence; anchor: `operators execute from left to right`
  - PDF page_label: `84`

## R02-E02 — order 2

Original normalized exercise SHA-256: `7eacb7d81f04aba9e31bc0c8603591b153da093a441827f88d62281de5ef771f`

### Original prompt

```text
Exercise 2 - Looking for Prints  
Write out the output of each line in the space provided. If the line results in an error, 
write "error". 
print(5 + "5")  
 
 
    print(5 + int("5")) 
print(str(5) + int("5"))    
    print(15 % 2) 
print("hey" + "yo")  
 
    print(2 * "go") 
print("yo" * 4.0) 
 
 
    print("hi" + there) 
print("go" * 2 + "!" * 2)
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 1,
  "item_label": "Exercise 2",
  "anchor": "Looking for Prints"
}
```

### Ordered numbered subparts

None declared by the numbered source parser. Unnumbered expressions/programs remain fully included in the original prompt and notebook.

### Concepts

- int conversion
- str conversion
- numeric remainder
- string concatenation and operand types
- string repetition
- integer repetition count
- unassigned variable names

### References (original order)

- Lecture: *Lecture 02*, Slide 15 (PPTX), “Data Type Conversion” — **direct**；覆盖：int conversion / str conversion。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Data Type Conversion; anchor: `int(), float(), and str()`
- Lecture: *Lecture 02*, Slide 19 (PPTX), “Operators on int and float” — **direct**；覆盖：numeric remainder。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Operators on int and float; anchor: `return the remainder of the division`
- Lecture: *Lecture 02*, Slide 25 (PPTX), “Operations Summary” — **direct**；覆盖：string concatenation and operand types。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Operations Summary; anchor: `both operands must be a string`
- Lecture: *Lecture 02*, Slide 24 (PPTX), “Operator on String” — **direct**；覆盖：string repetition / integer repetition count。 The slide directly shows both operand orders and a float-count TypeError; its separate Hello + ICP example has an incorrect displayed result.
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Operator on String; anchor: `n must be an int`
- Lecture: *Lecture 02*, Slide 33 (PPTX), “Variables” — **direct**；覆盖：unassigned variable names。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Variables; anchor: `Before using any variable, it needs to be assigned`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.6: Reading Input from the Keyboard, printed p. 78 (PDF p. 79) — **direct**；覆盖：int conversion。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Reading Numbers with the input Function; anchor: `converted to an int and assigned to the hours variable`
  - PDF page_label: `78`
- Textbook: Gaddis, 6th ed., Chapter 6, §6.1: Introduction to File Input and Output, printed p. 362 (PDF p. 363) — **direct**；覆盖：str conversion。 Targeted later-chapter reference for str() only; file handling is outside this recitation.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Writing and Reading Numeric Data; anchor: `Python has a built-in function named str`
  - PDF page_label: `362`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 87 (PDF p. 88) — **direct**；覆盖：numeric remainder。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: The Remainder Operator; anchor: `The Remainder Operator`
  - PDF page_label: `87`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.8: String Concatenation, printed p. 93 (PDF p. 94) — **direct**；覆盖：string concatenation and operand types。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: String Concatenation; anchor: `the combination of the two strings used as its operands`
  - PDF page_label: `93`
- Textbook: Gaddis, 6th ed., Chapter 8, §8.3: Testing, Searching, and Manipulating Strings, printed p. 500 (PDF p. 501) — **direct**；覆盖：string repetition。 Targeted later-chapter reference for string repetition only; loops and password validation are outside this recitation.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: The Repetition Operator; anchor: `The repetition operator works with strings as well`
  - PDF page_label: `500`
- Textbook: Gaddis, 6th ed., Chapter 7, §7.2: Introduction to Lists, printed p. 406 (PDF p. 407) — **prerequisite**；覆盖：integer repetition count。 States the integer operand requirement for sequence repetition using lists; string repetition is separately demonstrated on PDF p.501.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: The Repetition Operator; anchor: `the operand on the right side is an integer`
  - PDF page_label: `406`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.5: Variables, printed p. 68 (PDF p. 69) — **direct**；覆盖：unassigned variable names。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Multiple Assignment; anchor: `You cannot use a variable until you have assigned a value`
  - PDF page_label: `68`

## R02-E03 — order 3

Original normalized exercise SHA-256: `e79d82d859acd8972b1ab5c90b6367053d2bcf42cb30367ecb20dff5ab9d3e65`

### Original prompt

```text
Exercises 3 - Escape sequence 
Write the output, or Error if an error occurs. 
print("Welcome to \'ICP\'") 
 
print("Welcome to "ICP") 
 
print('Welcome to "ICP') 
print('Welcome to \"ICP') 
 
print("Welcome to \"ICP\"") 
 
print("Today is\t\"Tuesday\"\nWelcome to\t\"ICP\"")
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 1,
  "item_label": "Exercise 3",
  "anchor": "Escape sequence"
}
```

### Ordered numbered subparts

None declared by the numbered source parser. Unnumbered expressions/programs remain fully included in the original prompt and notebook.

### Concepts

- string delimiters and syntax errors
- escaped quotation marks
- newline and tab characters

### References (original order)

- Lecture: *Lecture 02*, Slide 9 (PPTX), “Strings” — **direct**；覆盖：string delimiters and syntax errors。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Strings; anchor: `starting and ending quotes`
- Lecture: *Lecture 02*, Slide 10 (PPTX), “Strings” — **direct**；覆盖：escaped quotation marks。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Strings; anchor: `Escape sequence can be used to obtain quote character`
- Lecture: *Lecture 02*, Slide 11 (PPTX), “Escape Sequence” — **direct**；覆盖：newline and tab characters。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Escape Sequence; anchor: `ASCII Horizontal Tab`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.3: Displaying Output with the print Function, printed p. 63 (PDF p. 64) — **prerequisite**；覆盖：string delimiters and syntax errors。 Teaches matching delimiters and mixed quote styles; does not explicitly trace the malformed print line in this exercise.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Strings and String Literals; anchor: `string literals must be enclosed in quote marks`
  - PDF page_label: `63`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.9: More About the print Function, printed p. 97 (PDF p. 98) — **direct**；覆盖：escaped quotation marks。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Escape Characters; anchor: `advances the output to the next horizontal tab position`
  - PDF page_label: `97`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.9: More About the print Function, printed p. 96 (PDF p. 97) — **direct**；覆盖：newline and tab characters。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Escape Characters; anchor: `newline escape character`
  - PDF page_label: `96`

## R02-E04 — order 4

Original normalized exercise SHA-256: `29226a7a3ea29f2b7b05991e290b7be521bb82e994aaaa68d6d44b9e5a107268`

### Original prompt

```text
Exercise 4 | Variable assignment 
Consider the following variable assignments:  
 
Left = "Lady" 
 
Middle = "Jack" 
 
Right = "Ace"  
Figure out where the 'Lady' is (Left, Middle, Right) after running the following programs: 
Left, Right, Middle = Left, Middle, Right 
 
Left, Right, Middle = Middle, Right, Left 
 
Left, Middle, Right = Middle, Right, Left 
 
Left, Middle, Right = Middle, Right, Left 
Left, Middle, Right = Middle, Right, Left 
 
Left, Middle, Right = Middle, Right, Left 
Left, Middle, Right = Middle, Right, Left 
Left, Middle, Right = Middle, Right, Left 
 
Left, Middle, Right = Right, Right, Right 
Left, Middle, Right = Left, Left, Left 
Left, Middle, Right = Middle, Middle, Middle
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 2,
  "item_label": "Exercise 4",
  "anchor": "Variable assignment"
}
```

### Ordered numbered subparts

None declared by the numbered source parser. Unnumbered expressions/programs remain fully included in the original prompt and notebook.

### Concepts

- multiple assignment
- old right-hand-side values before rebinding
- reassignment and loss of references

### References (original order)

- Lecture: *Lecture 02*, Slide 33 (PPTX), “Variables” — **direct**；覆盖：multiple assignment。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Variables; anchor: `assign values to multiple variables in a single statement`
- Lecture: *Lecture 02*, Slide 29 (PPTX), “How do variables actually work?” — **prerequisite**；覆盖：old right-hand-side values before rebinding。 Teaches evaluate-then-bind for ordinary assignment; applying that order to every RHS value in a multiple assignment requires an explicit teaching step.
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: How do variables actually work?; anchor: `The expression on the right hand side is evaluated`
- Lecture: *Lecture 02*, Slide 32 (PPTX), “Reassignment of Variables” — **direct**；覆盖：reassignment and loss of references。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Reassignment of Variables; anchor: `no longer associated with the variable`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.5: Variables, printed p. 69 (PDF p. 70) — **direct**；覆盖：multiple assignment。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Multiple Assignment; anchor: `three variable names are shown on the left side`
  - PDF page_label: `69`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.5: Variables, printed p. 69 (PDF p. 70) — **prerequisite**；覆盖：old right-hand-side values before rebinding。 Demonstrates multiple assignment of literals; does not explicitly explain taking all old RHS values before rebinding existing names.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Multiple Assignment; anchor: `assigned their respective values shown on the right side`
  - PDF page_label: `69`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.5: Variables, printed p. 71 (PDF p. 72) — **direct**；覆盖：reassignment and loss of references。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Variable Reassignment; anchor: `it can no longer be used because it isn’t referenced by a variable`
  - PDF page_label: `71`

## R02-E05 — order 5

Original normalized exercise SHA-256: `8ce3018e6903dd44d33bc3d03655acdcdcc3b1fadcb9e5d6dee4a164d9e6d2d4`

### Original prompt

```text
Exercise 5 | Print arguments  
a = 5 
print("a", a, sep=' = ') 
 
a = 5 
print("a = ", a, sep="0000") 
 
a = 5 
print("a = ", a, sep="'", end="'") 
 
a, b = 'b', 'a' 
print(a, 'b', sep='>>>', end='\t') 
print('a', b, sep='***', end='\n\n') 
print(a, b, sep='\t')
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 3,
  "item_label": "Exercise 5",
  "anchor": "Print arguments"
}
```

### Ordered numbered subparts

None declared by the numbered source parser. Unnumbered expressions/programs remain fully included in the original prompt and notebook.

### Concepts

- string literals versus variable values
- print separators and endings
- newline and tab characters

### References (original order)

- Lecture: *Lecture 02*, Slide 44 (PPTX), “print function” — **direct**；覆盖：string literals versus variable values。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: print function; anchor: `print() can display strings, numbers, variables, and expressions.`
- Lecture: *Lecture 02*, Slide 46 (PPTX), “print – sep and end arguments” — **direct**；覆盖：print separators and endings。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: print – sep and end arguments; anchor: `sep and end arguments`
- Lecture: *Lecture 02*, Slide 11 (PPTX), “Escape Sequence” — **direct**；覆盖：newline and tab characters。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Escape Sequence; anchor: `ASCII Horizontal Tab`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.5: Variables, printed p. 71 (PDF p. 72) — **direct**；覆盖：string literals versus variable values。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Displaying Multiple Items with the print Function; anchor: `The first argument is the string literal`
  - PDF page_label: `71`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.9: More About the print Function, printed p. 95 (PDF p. 96) — **direct**；覆盖：print separators and endings。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: More About the print Function; anchor: `Specifying an Item Separator`
  - PDF page_label: `95`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.9: More About the print Function, printed p. 96 (PDF p. 97) — **direct**；覆盖：newline and tab characters。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Escape Characters; anchor: `newline escape character`
  - PDF page_label: `96`

## R02-E06 — order 6

Original normalized exercise SHA-256: `f47cd1946b5cb9e861b94c0df29fe5675f0b77d489b0f91fb3518b59818b3002`

### Original prompt

```text
Exercise 6 | String formatting 
print(f"{12:8d}") 
 
print(f"{'12':0>8}") 
 
num = 12.34567890 
print(f"{num:8.3f}") 
 
print(f"{12.34567890:<08.3f}") 
 
name = 'dolphin' 
res1 = f'{name:->10}' 
res2 = f'{name:<10.3}' 
print(res1) 
print(res2)
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 3,
  "item_label": "Exercise 6",
  "anchor": "String formatting"
}
```

### Ordered numbered subparts

None declared by the numbered source parser. Unnumbered expressions/programs remain fully included in the original prompt and notebook.

### Concepts

- f-string placeholders
- numeric field width and precision
- alignment
- custom fill characters
- string precision truncation
- zero padding with explicit alignment

### References (original order)

- Lecture: *Lecture 02*, Slide 48 (PPTX), “f-string” — **direct**；覆盖：f-string placeholders。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: f-string; anchor: `Inside {}, we can put variables, expressions, and formatting instructions.`
- Lecture: *Lecture 02*, Slide 53 (PPTX), “f-string - number formatting” — **direct**；覆盖：numeric field width and precision。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: f-string - number formatting; anchor: `f-string - number formatting`
- Lecture: *Lecture 02*, Slide 51 (PPTX), “f-string – string formatting” — **direct**；覆盖：alignment / custom fill characters。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: f-string – string formatting; anchor: `Padding and Aligning Strings`
- Lecture: *Lecture 02*, Slide 52 (PPTX), “f-string – string formatting” — **direct**；覆盖：string precision truncation。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: f-string – string formatting; anchor: `Truncating and Padding Strings`
- Lecture: *Lecture 02*, Slide 53 (PPTX), “f-string - number formatting” — **prerequisite**；覆盖：zero padding with explicit alignment。 Shows zero-padded numeric fields without an explicit alignment character. Slide 51 supplies alignment background; the combination <08.3f is not directly demonstrated.
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: f-string - number formatting; anchor: `f-string - number formatting`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.10: Displaying Formatted Output with F-strings, printed p. 98 (PDF p. 99) — **direct**；覆盖：f-string placeholders。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Displaying Formatted Output with F-strings; anchor: `An f-string can contain placeholders`
  - PDF page_label: `98`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.10: Displaying Formatted Output with F-strings, printed p. 100 (PDF p. 101) — **direct**；覆盖：numeric field width and precision。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Rounding Floating-Point Numbers; anchor: `a precision designator that indicates the number`
  - PDF page_label: `100`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.10: Displaying Formatted Output with F-strings, printed p. 102 (PDF p. 103) — **direct**；覆盖：numeric field width and precision。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Specifying a Minimum Field Width; anchor: `Specifying a Minimum Field Width`
  - PDF page_label: `102`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.10: Displaying Formatted Output with F-strings, printed p. 105 (PDF p. 106) — **direct**；覆盖：alignment。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Aligning Values; anchor: `left-aligns the variable’s value in a field`
  - PDF page_label: `105`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.10: Displaying Formatted Output with F-strings, printed p. 105 (PDF p. 106) — **prerequisite**；覆盖：custom fill characters / zero padding with explicit alignment。 Teaches alignment and width, but not arbitrary fill characters, zero padding, or zero padding combined with explicit alignment.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Aligning Values; anchor: `left-aligns the variable’s value in a field`
  - PDF page_label: `105`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.10: Displaying Formatted Output with F-strings, printed p. 99 (PDF p. 100) — **prerequisite**；覆盖：string precision truncation。 Teaches the format-specifier grammar; this textbook section does not explain string precision as truncation.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Formatting Values; anchor: `the placeholder and the format specifier are separated by a colon`
  - PDF page_label: `99`

## R02-E07 — order 7

Original normalized exercise SHA-256: `a1b97d12755dca4bd5dd425c10d1c731f4cbc3211e2691bd7dad30da64f5a721`

### Original prompt

```text
Exercise 7 | Sales Prediction  
A company has determined that its annual profit is typically 23 percent of total sales. 
Write a program that asks the user to enter the projected amount of total sales, and 
then displays the profit that will be made from that amount.
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 4,
  "item_label": "Exercise 7",
  "anchor": "Sales Prediction"
}
```

### Ordered numbered subparts

None declared by the numbered source parser. Unnumbered expressions/programs remain fully included in the original prompt and notebook.

### Concepts

- numeric keyboard input
- percentage calculation
- displaying computed values

### References (original order)

- Lecture: *Lecture 02*, Slide 40 (PPTX), “Input function” — **direct**；覆盖：numeric keyboard input。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Input function; anchor: `Use conversion built-in functions: int(), float()`
- Lecture: *Lecture 02*, Slide 49 (PPTX), “f-string” — **direct**；覆盖：percentage calculation。 The example relates a fractional multiplier to a percentage; its printed f-string quotes and :2f explanatory label have typos.
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: f-string; anchor: `1000.0 is 33.33333333333333% of 3000`
- Lecture: *Lecture 02*, Slide 44 (PPTX), “print function” — **direct**；覆盖：displaying computed values。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: print function; anchor: `print() can display strings, numbers, variables, and expressions.`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.6: Reading Input from the Keyboard, printed p. 78 (PDF p. 79) — **direct**；覆盖：numeric keyboard input。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Reading Numbers with the input Function; anchor: `pay_rate = float(input`
  - PDF page_label: `78`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 82 (PDF p. 83) — **direct**；覆盖：percentage calculation / displaying computed values。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Calculating a Percentage; anchor: `we multiply the original price by 20 percent`
  - PDF page_label: `82`

## R02-E08 — order 8

Original normalized exercise SHA-256: `b25b2f44a48deda52af9e77e6efe9f21c480168a95d6ad413b31b84d2829536b`

### Original prompt

```text
Exercise 8 | Celsius to Fahrenheit Temperature Converter 
Write a program that converts Celsius temperatures to Fahrenheit temperatures. The 
formula is as follows: 
𝐹= 9
5 𝐶+ 32 
The program should ask the user to enter a temperature in Celsius, then display the 
temperature converted to Fahrenheit.
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 4,
  "item_label": "Exercise 8",
  "anchor": "Celsius to Fahrenheit Temperature Converter"
}
```

### Ordered numbered subparts

None declared by the numbered source parser. Unnumbered expressions/programs remain fully included in the original prompt and notebook.

### Concepts

- numeric keyboard input
- translating a mathematical formula
- displaying computed values

### References (original order)

- Lecture: *Lecture 02*, Slide 40 (PPTX), “Input function” — **direct**；覆盖：numeric keyboard input。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Input function; anchor: `Use conversion built-in functions: int(), float()`
- Lecture: *Lecture 02*, Slide 19 (PPTX), “Operators on int and float” — **prerequisite**；覆盖：translating a mathematical formula。 Teaches the arithmetic operators needed to implement the supplied formula, but does not teach Celsius conversion or the translation of mathematical notation.
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Operators on int and float; anchor: `Operators on int and float`
- Lecture: *Lecture 02*, Slide 44 (PPTX), “print function” — **direct**；覆盖：displaying computed values。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: print function; anchor: `print() can display strings, numbers, variables, and expressions.`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.6: Reading Input from the Keyboard, printed p. 78 (PDF p. 79) — **direct**；覆盖：numeric keyboard input。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Reading Numbers with the input Function; anchor: `pay_rate = float(input`
  - PDF page_label: `78`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 88 (PDF p. 89) — **direct**；覆盖：translating a mathematical formula。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Converting Math Formulas to Programming Statements; anchor: `Converting Math Formulas to Programming Statements`
  - PDF page_label: `88`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 82 (PDF p. 83) — **direct**；覆盖：displaying computed values。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Calculating a Percentage; anchor: `statement to display the sale price`
  - PDF page_label: `82`

## R02-E09 — order 9

Original normalized exercise SHA-256: `27c59be46e04ee90c94483845ca1978894927958decc3d65898cc2e83b8b5fb6`

### Original prompt

```text
Exercise 9 | Ingredient Adjuster   
A cookie recipe calls for the following ingredients:  
1) 1.5 cups of sugar 
2) 1 cup of butter 
3) 2.75 cups of flour  
The recipe produces 48 cookies with this amount of the ingredients. 
Write a program that asks the user how many cookies he or she wants to make, and 
then displays the number of cups of each ingredient needed for the specified number of 
cookies.
```

### Recitation provenance

```json
{
  "source_id": "recitation-02",
  "path": "recitation/Recitaion 02.pdf",
  "sha256": "1f5abeb0607bd7bb4327d458816d10aedc8ebf25ddbe5908453159fd55aa5b0d",
  "pdf_page": 4,
  "item_label": "Exercise 9",
  "anchor": "Ingredient Adjuster"
}
```

### Ordered numbered subparts

- **R02-E09-P01** / label `1)` / normalized SHA-256 `5ea13840264a0390b1f1aef7e7916a2fd8801349d8e8a565191d0b262f7cc53a`

```text
1) 1.5 cups of sugar
```

- **R02-E09-P02** / label `2)` / normalized SHA-256 `81f94942731e9a97f93df7d45493cb03f72eb953dd43a67790939dcb8e4aff14`

```text
2) 1 cup of butter
```

- **R02-E09-P03** / label `3)` / normalized SHA-256 `558f8a2da047d024eecb66c343b3e24d95c601c6aa21e258aa287c6a850d5def`

```text
3) 2.75 cups of flour  
The recipe produces 48 cookies with this amount of the ingredients. 
Write a program that asks the user how many cookies he or she wants to make, and 
then displays the number of cups of each ingredient needed for the specified number of 
cookies.
```


### Concepts

- numeric keyboard input
- proportional ingredient scaling
- displaying computed values

### References (original order)

- Lecture: *Lecture 02*, Slide 40 (PPTX), “Input function” — **direct**；覆盖：numeric keyboard input。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: Input function; anchor: `Use conversion built-in functions: int(), float()`
- Lecture: *Lecture 02*, Slide 36 (PPTX), “You Try it!” — **prerequisite**；覆盖：proportional ingredient scaling。 Uses price-times-quantity as proportional calculation background; it does not derive scaling from a 48-cookie reference recipe.
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: You Try it!; anchor: `buy different numbers of notebooks`
- Lecture: *Lecture 02*, Slide 44 (PPTX), “print function” — **direct**；覆盖：displaying computed values。
  - source_id: `lecture-02`; path: `lecture/Lecture 02.pptx`; SHA-256: `48546c643b31a6784eae8fdfb3288f3839098200d5a313889b22558a6b7f1e28`
  - title: print function; anchor: `print() can display strings, numbers, variables, and expressions.`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.6: Reading Input from the Keyboard, printed p. 78 (PDF p. 79) — **direct**；覆盖：numeric keyboard input。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Reading Numbers with the input Function; anchor: `hours = int(input`
  - PDF page_label: `78`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 88 (PDF p. 89) — **prerequisite**；覆盖：proportional ingredient scaling。 Teaches multiplication, division, and formula translation, but does not derive the recipe scaling factor. The matching original textbook exercise is on PDF p.147, printed p.146.
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Converting Math Formulas to Programming Statements; anchor: `Converting Math Formulas to Programming Statements`
  - PDF page_label: `88`
- Textbook: Gaddis, 6th ed., Chapter 2, §2.7: Performing Calculations, printed p. 82 (PDF p. 83) — **direct**；覆盖：displaying computed values。
  - source_id: `gaddis-python-6e`; path: `textbook/Starting Out With Python -- Revel 6th Edition (Tony Gaddis).pdf`; SHA-256: `8f004ab35661ad80e0c4324bc0b0caa111e5f5ec9295192fe340a71aa76a270c`
  - title: Calculating a Percentage; anchor: `statement to display the sale price`
  - PDF page_label: `82`

## 来源歧义与教学边界

本讲义的完整映射见同目录 [source-map.json](source-map.json)。9 道原题及 3 个编号小项的规范化哈希与来源一致；67 条引用均已验证。原题保留 PDF 提取文本的空白形式。教材 PDF p. 98 的引用已核对其当前所属章节。

- **引用范围：** 没有 unresolved 引用，也没有 TA approval 条目。标记为 prerequisite 的引用只提供背景，不能理解为直接演示了原题的完整语法组合；具体限制见各条引用。
- **来源清单：** 仓库扫描发现两份 lecture、两份 recitation 和一本教材，没有 syllabus。本讲义的清单收录 Lecture 01、Lecture 02、Recitation 02 和教材；Recitation 01 不属于本次练习，未收录。Recitation 01 有 2 个物理 PDF 页，SHA-256 为 `f34480cf0dbc0fe9b6c4d94e94f852888c1b3116e8ab25ef5105ed7282b2e76b`。
- **题 1–3 的排版：** Recitation 02 的 4 个物理页均已逐页核对。题 1 有 8 个表达式；题 2 有 9 条 print，顺序为表格逐行、从左到右，右列的提取缩进属于排版。题 3 有 6 条 print，其中第 3、4 行共处一格，仍是两个待判断项目。原题中的错误代码按原样保留。
- **题 4 的程序边界：** 六段程序各自从 `Left='Lady'`、`Middle='Jack'`、`Right='Ace'` 开始，赋值行数依次为 1、1、1、2、3、3。第 1 段为 `Left, Right, Middle = Left, Middle, Right`；第 2 段为 `Left, Right, Middle = Middle, Right, Left`；第 3 段为 `Left, Middle, Right = Middle, Right, Left`；第 4、5 段分别将第 3 段的赋值执行两次、三次。第 6 段依次为 `Left, Middle, Right = Right, Right, Right`、`Left, Middle, Right = Left, Left, Left`、`Left, Middle, Right = Middle, Middle, Middle`。原题仅列 Left/Middle/Right 选项，讲义允许在没有变量保存 Lady 时回答“无”，但这里不指定对应哪一段。
- **题 5–6 的任务表述：** 题 5 有 4 段程序；题 6 有 5 段，最后一段有两次输出。两题原表格没有单独的英文指令句，因此“预测输出”是依据留白表格给出的中文教学解释，不是新增的原文。
- **题 8 的公式：** PDF 中的竖式分数提取为 `𝐹= 9\n5 𝐶+ 32`。讲义保留该原始文本，并另行恢复已核对的排版 $F = \frac{9}{5}C + 32$；两者表示同一来源公式。
- **题 9 的编号：** 1)、2)、3) 指同一配方的三种原料，不是三个独立应用。源块解析得到的 P03 包含三种配料共同适用的末尾要求。讲义保留这一来源关系，并将三种原料组织在同一个程序内，各自对应一个编号代码单元格。
- **阅读要求不一致：** Lecture 02 Slide 55 写有 “Read chapter 3”，而本次知识点主要对应教材 Chapter 2。匹配的教材练习为：题 7 对应 Chapter 2 Exercise 2（PDF p. 145 / printed p. 144）；题 8 对应 Exercise 9（PDF pp. 146–147 / printed pp. 145–146）；题 9 对应 Exercise 10（PDF p. 147 / printed p. 146）。讲义标出差异，保留教师原阅读要求。
- **Lecture 02 的疑似笔误：** Slide 20 的 `10 // 0.25` 显示结果有误；Slide 24 的 `"Hello" + "ICP"` 显示结果有误；Slide 33 的 `z=1` 后注释及大小写敏感性注释有误；Slide 49 的 f-string 引号不匹配，且两位小数说明中的 `:2f` 缺少小数点。原文件保持不变，核对说明见教师版。
- **教材表述限制：** PDF p. 91 对数值运算结果类型的概括过宽，需要结合 PDF p. 84 对真除法的明确例外。PDF p. 103 将整数格式写为 “d or D”，但大写 D 不是有效的 Python 整数格式；本题使用的是 d。
- **后续章节引用：** 题 2 的后续章节只用于定位 `str()` 和字符串重复语法，不表示本次要求学习文件、列表、循环或其他后续主题。
- **不可见字符：** 讲义用普通输出配合 repr 帮助观察空白；repr 的外层引号是表示法。制表符移动到下一个制表位，显示距离不是固定的空格数。
