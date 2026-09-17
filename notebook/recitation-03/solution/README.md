# Recitation 03：教师备课包 / Instructor preparation pack

中文：本目录是教师专用的完整中英文对照 solution 讲义。英文 notebook 适合投屏；本目录解释每道题的目的、讲授顺序、参考答案、边界情况和代码符号读法。请勿把本目录随学生版 notebook 一起发给学生。

English: This folder contains the complete bilingual instructor solution handout. Use the English notebook for projection and these materials for teaching purposes, delivery steps, answers, boundary cases, and symbol pronunciation. Do not distribute this folder with the student notebook.

## 从这里开始 / Start here

1. [完整备课讲义 / Full teaching guide](teaching-guide.md)：逐题讲解步骤、中英文课堂话术、答案、常见误区与提问。 / Exercise-by-exercise steps, bilingual classroom language, answers, common mistakes, and checking questions.
2. [符号读法 / Symbol pronunciation](symbol-reading.md)：`!`、`!=`、`==`、切片、`\n`、百分号等的名称、含义与整句读法。 / Names, meanings, and natural readings of comparisons, slices, escapes, and other symbols.
3. [教师版 notebook / Instructor notebook](../recitation-03-instructor.ipynb)：简洁英文题目和解答。 / Concise English prompts and solutions.
4. [学生版 notebook / Student notebook](../recitation-03-student.ipynb)：从教师版自动派生，只保留题目和可运行的待完成代码。 / Derived from the instructor version, retaining questions and runnable starter cells.

## 每道题在练什么 / What each exercise practices

| # | 文件 / File | 覆盖内容与目的（中文） | Coverage and purpose (English) |
|---|---|---|---|
| 1 | [exercise-01.py](exercise-01.py) | 布尔优先级、类型比较、反例；区分当前值和“总是”。 | Boolean precedence, type comparisons, and counterexamples; distinguish current truth from “always.” |
| 2 | [exercise-02.py](exercise-02.py) | 正负索引、切片方向与边界、空白字符；学会逐字符追踪。 | Positive/negative indices, slice direction/bounds, and whitespace; trace characters precisely. |
| 3 | [exercise-03.py](exercise-03.py) | 先算面积再比较；覆盖三个互斥结果。 | Calculate areas before comparing; cover three exclusive outcomes. |
| 4 | [exercise-04.py](exercise-04.py) | 年龄范围与端点；由文字写出有序条件。 | Age intervals and boundaries; translate prose into ordered conditions. |
| 5 | [exercise-05.py](exercise-05.py) | 罗马数字映射与范围外错误；练习多分支选择。 | Roman numeral mapping and out-of-range errors; practice multiple branches. |
| 6 | [exercise-06.py](exercise-06.py) | 验证颜色、组合条件、顺序对称；区分验证和计算。 | Validate colors and handle symmetric pairs; separate validation from selection. |
| 7 | [exercise-07.py](exercise-07.py) | 质量换算为重量后判断；理解单位和严格阈值。 | Convert mass to weight before testing; track units and strict thresholds. |
| 8 | [exercise-08.py](exercise-08.py) | 范围、特殊值、奇偶；拆解长规则。 | Ranges, a special case, and parity; break down a longer specification. |
| 9 | [exercise-09.py](exercise-09.py) | 阶梯折扣和百分比；区分折扣率、优惠金额、最终价格。 | Discount tiers and percentages; distinguish rate, discount, and final price. |
| 10 | [exercise-10.py](exercise-10.py) | 单位换算与独立 if；识别多条要求同时成立。 | Unit conversion with independent conditions; recognize simultaneous requirements. |

中文：每个 Python 文件均可单独运行。可执行语句配有中英文逐行注释，保留英文变量名和输出文字；它们和教师 notebook 的解题逻辑一致。解释较长时放在代码上方，以保持缩进和代码可读性。

English: Each Python file runs independently. Executable lines have paired Chinese/English comments, while identifiers and program messages remain English. Their solution logic matches the instructor notebook. Longer explanations sit above the code to preserve indentation and readability.

## 运行方法 / Running the materials

中文：在项目根目录，用已有的课程 Python 环境运行，例如：

English: From the repository root, use your course Python environment, for example:

```bash
python notebook/recitation-03/solution/exercise-01.py
python notebook/recitation-03/solution/exercise-02.py
python notebook/recitation-03/solution/exercise-09.py
```

中文：其余文件同样运行。脚本只使用 Python 标准功能；notebook 需要 Jupyter。若系统 Python 没有 notebook 依赖，本机可使用 `/Users/sihang/opt/anaconda3/bin/python`。修改各题开头的示例变量可以测试其他分支，不需要等待键盘输入。

English: Run the other files in the same way. The scripts use standard Python features; notebooks require Jupyter. On this machine, `/Users/sihang/opt/anaconda3/bin/python` provides the notebook environment. Edit sample variables at the beginning of each exercise to try other branches without waiting for keyboard input.

```bash
python .agents/skills/icp-recitation-prep/scripts/validate_simple_pair.py \
  notebook/recitation-03/recitation-03-instructor.ipynb \
  notebook/recitation-03/recitation-03-student.ipynb --execute
```

## 课堂使用提醒 / Classroom use

中文：题 9 原文缺少具体编程任务；题 6 重复颜色和题 10 时间输出形式也需要约定。[完整讲义](teaching-guide.md) 明确列出了本次采用的解释。所有原题、样例大小写与题序均保留，不进行讲义/课件页码检索。异常题会展示错误类型并继续执行，不会中断后续演示。

English: Exercise 9 lacks an explicit programming task; repeated colors in Exercise 6 and time output in Exercise 10 also require conventions. The [full guide](teaching-guide.md) states these choices. Original exercises, sample capitalization, and order are preserved without lecture-reference searches. Expected-error examples show the error type and continue so later demonstrations can run.

## 验证结果 / Validation results

中文：已通过两个 notebook 的全新内核运行、10 个脚本的独立执行，以及 100 项答案和边界检查。已核对教师 notebook、解答脚本和讲义中的代码一致，学生版为官方脚本派生且没有输出或答案泄漏。独立审阅完成，发现的两处措辞/符号显示问题已修正，无遗留问题。运行检查使用临时副本；交付的 notebook 未保存运行输出，便于课堂先预测、再运行。

English: Both notebooks passed fresh-kernel execution, all ten scripts ran independently, and 100 answer/boundary cases passed. Instructor, script, and handout code agree. The student notebook is officially derived, with no saved outputs or answer leakage. Independent review is complete; two wording/symbol-display issues were corrected, with no remaining findings. Execution checks used temporary copies; delivered notebooks have no saved outputs so students can predict before running.
