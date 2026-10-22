# Recitation 04/05：教师备课包 / Instructor preparation pack

中文：本目录服务于合并版 Recitation 04/05，主题是 `while` / `for` 循环。教师 notebook 是唯一答案源；学生 notebook 必须由官方脚本自动派生。`solution/` 仅供教师备课，不应与学生版一起发放。

English: This folder supports the combined Recitation 04/05 on `while` and `for` loops. The instructor notebook is the canonical answer source, and the student notebook is derived from it. Keep `solution/` instructor-only.

## 从这里开始 / Start here

1. [中英文课堂逐字稿 / Bilingual classroom script](classroom-script.md)：可直接对着讲，包含知识点、英文话术、中文对应讲解、逐题提问与标准答案。
2. [完整备课讲义 / Full teaching guide](teaching-guide.md)：课堂节奏、逐题讲法、答案、边界值、常见误区和检查问题。
3. [符号与代码读法 / Symbol and code reading](symbol-reading.md)：循环、`range`、`break`、`continue`、随机数、索引和嵌套结构的中英文读法。
4. [教师 notebook / Instructor notebook](../recitation-0405-instructor.ipynb)：完整英文题面与简洁参考实现。
5. [学生 notebook / Student notebook](../recitation-0405-student.ipynb)：由教师版自动派生，保留完整题面和可运行的 `TODO` 起始代码。

## 覆盖内容 / Coverage

| # | 文件 / File | 中文教学目的 | English focus |
|---|---|---|---|
| 1 | `exercise-01.py` | 追踪嵌套 `while`，理解连续相同字符分组。 | Trace nested `while` loops and character runs. |
| 2 | `exercise-02.py` | 用两类循环生成固定时间序列并计算。 | Generate regular intervals with both loop types. |
| 3 | `exercise-03.py` | 把 Fibonacci 递推关系变成循环状态。 | Translate a recurrence into loop state. |
| 4 | `exercise-04.py` | 管理随机秘密数、次数、范围与提前结束。 | Manage attempts, bounds, and early success. |
| 5 | `exercise-05.py` | 用 `while` 实现不重叠子串计数。 | Count non-overlapping substring matches. |
| 6 | `exercise-06.py` | 按原题算法递减搜索最大公约数。 | Implement the supplied decrementing GCD algorithm. |
| 7 | `exercise-07.py` | 精确追踪 `range`、嵌套循环、`continue`、`break`。 | Predict five `for`-loop programs. |
| 8 | `exercise-08.py` | 用嵌套循环控制行、列、空格、字母和图案。 | Build four nested-loop patterns. |
| 9 | `exercise-09.py` | 模拟 1000 次掷骰并统计频数。 | Run a reproducible frequency simulation. |
| 10 | `exercise-10.py` | 把资格过滤、容量和提前停止组合起来。 | Combine filtering, capacity, and early termination. |
| 11 | `exercise-11.py` | 在遇到 0 时停止，并逐位生成数字密码。 | Stop at a sentinel and generate digit strings. |

### 多小题教学目的 / Subpart purposes

- **E7-P01：** 追踪负步长 `range` 和循环外累计输出，确认 stop 不包含。
- **E7-P02：** 追踪依赖外层索引的内层范围，并理解 `end=" "` 与换行位置。
- **E7-P03：** 区分 `continue` 的“跳过本轮”和 `break` 的“结束循环”。
- **E7-P04：** 逐步跟踪嵌套字符串迭代、类型转换、乘法与 `//` 写回。
- **E7-P05：** 使用 `len(s)-i` 从字符串末尾向前取值，并识别循环内累计输出。
- **E8-P01：** 把行号映射为递减星号数量。
- **E8-P02：** 用行索引控制两个 `#` 之间递增的空格。
- **E8-P03：** 同时控制领先空格、行内字母数和 A-Z 循环回绕。
- **E8-P04：** 为三层循环分别分配三角形、行和星号三个职责。

## 运行方法 / Running

与原题要求一致，凡是原题写明“由用户输入”的题目（第 1、3、4、5、6、8、10、11 题），notebook 与对应脚本都使用 `input()` 读取输入；第 2、7、9 题没有输入。在 Jupyter 中运行这些单元格时，单元格下方会出现输入框，输入后按回车即可。

在项目根目录交互运行脚本，例如：

```bash
python notebook/recitation-0405/solution/exercise-03.py
python notebook/recitation-0405/solution/exercise-11.py
```

也可以用管道一次性提供输入（每行一个值），方便快速核对：

```bash
printf '8\n8\n' | python notebook/recitation-0405/solution/exercise-03.py
printf '4\n9\n1\n0\n' | python notebook/recitation-0405/solution/exercise-11.py
```

注意：W/F 题的脚本依次运行 `while` 与 `for` 两个版本，所以需要输入两组数据；第 1 题每次运行只处理一个字符串，原题表格的三个输入需要运行三次。

随机数约定：第 4 题（秘密数）和第 11 题（密码）每次运行都随机产生，与原题一致。课堂需要固定演示时，在**每次**运行游戏或密码单元格之前紧接着执行一次 `random.seed(405)`（第 4 题秘密数为 6）或 `random.seed(411)`（第 11 题依次输入 4、9、1 得到 `3053`、`933763088`、`1`）。只设一次种子再连续运行 while 和 for 两局时，第二局的秘密数会不同（为 24）。第 9 题没有输入，仍使用局部固定种子 409，便于复现计数。

English: Exercises whose source says the user enters values now call `input()` in both the notebook and the scripts. Run scripts interactively or pipe one value per line. Exercises 4 and 11 are truly random on every run; Exercise 9 keeps its local fixed seed.

## 原题歧义与约定 / Source ambiguities and conventions

- 源文件名和标题中的 `Recitaion` 拼写保持不动；第 9 题标题 `Dice statics` 很可能应为 `Dice statistics`，notebook 明示但不静默改写。
- `W/F` 题同时提供 `while` 与 `for` 两个版本；`W`、`F` 题遵守指定循环类型。
- 第 3 题按 `F_0` 到 `F_n`（含两端）解释。
- 第 5 题第二个样例证明匹配不重叠；匹配区分大小写，子串假设非空。
- 第 6 题 PDF 的项目符号没有清楚缩进；本材料把“d 减 1”解释为 while 循环体，把“报告 d”解释为循环结束后的语句。
- 第 8 题字母超过 `Z` 后回到 `A`；三角形之间不留空行；输入提示统一写作 `Enter the number of rows: `（原题第 1、2 部分写作 “numbers of rows”）。
- 第 10 题输入提示沿用原题样例格式 `Person N - Enter height: `。
- 第 11 题的 `F` 标签与“反复询问直到 0”存在张力：请求次数事先未知，无法用普通 `for` 循环表达。本材料外层使用 `while True` 读取长度、输入 0 时 `break`，题目要求的 `for` 循环用于逐位生成 X 个数字。
- 所有输入题假设用户输入合法（正整数、非空子串等），不做输入校验，保持代码简单。

## 验证结果 / Validation results

中文：官方 `validate_simple_pair.py`（不带 `--execute`）结构检查通过，学生版由官方脚本重新派生。由于 notebook 和脚本现在按原题使用 `input()`，而该验证脚本在没有标准输入的环境中执行（notebook 会抛出 `StdinNotImplementedError`，脚本会遇到 `EOFError`），`--execute` 模式不再适用。替代验证：两个 notebook 均在全新 Jupyter 内核中用脚本化输入（原题样例输入）完整运行；8 个改动脚本用管道输入运行，输出与 notebook 单元格逐字一致；另检查了 `n = 1`、第 7 次才猜中、范围外猜测、`<=` 边界、互质数、全部低于 120、未满员、长度 0 立即结束等情况。交付 notebook 不保存运行输出。

English: The structural check passes and the student notebook was re-derived with the official script. Because the materials now call `input()`, `validate_simple_pair.py --execute` (which runs without stdin) no longer applies. Instead, both notebooks were executed in fresh kernels with scripted source-example input, and every changed script matched its notebook cells when fed the same input through a pipe. Delivered notebooks contain no saved outputs.
