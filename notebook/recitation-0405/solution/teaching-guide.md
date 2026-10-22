# Recitation 04/05 备课讲义 / Teaching guide

## 使用方法与建议节奏 / Use and pacing

中文：投屏使用全英文 instructor notebook；本讲义用于课前准备和课堂提示。推荐节奏是“预测 → 画状态表 → 单步实现 → 运行 → 用边界值复查”。不要在学生预测前一次性运行所有答案。

English: Project the English instructor notebook and use this guide for preparation. Repeat the rhythm: predict, trace state, implement one step, run, and check a boundary.

建议 85–95 分钟：开场 5 分钟；题 1–3 约 20 分钟；题 4–6 约 22 分钟；题 7 约 15 分钟；题 8 约 15 分钟；题 9–11 约 15 分钟；总结 3 分钟。课时较短时保留原题顺序，把部分图案或双实现留作课后练习。

Prerequisites visible in the source are variables, strings, lists, arithmetic, comparisons, `if`, functions, `print`, and `input` with `int` conversion. Helper functions and the Exercise 9 seed support clear demonstrations; they are not the conceptual focus.

### 开场话术 / Opening

> “A loop is not magic repetition. It has a state, a rule for changing that state, and a reason to stop.”
>
> “循环不是神奇的重复；它有状态、状态更新规则，以及停止的理由。”

## 全局约定 / Global conventions

| 项目 | 中文说明 | English explanation |
|---|---|---|
| W / F / W/F | `W` 只用 `while`，`F` 只用 `for`，`W/F` 展示两个版本。 | `W` uses `while`, `F` uses `for`, and `W/F` shows both. |
| 输入 | 与原题一致，需要用户输入的题目用 `input()` 读取；数字用 `int(...)` 转换。运行单元格时在下方输入框输入。 | Exercises that ask the user call `input()`; numbers are converted with `int(...)`. |
| 随机数 | 第 4、11 题每次运行都随机；需要固定演示时，每次运行前紧接着执行 `random.seed(405)` / `random.seed(411)`。第 9 题保留局部固定种子 409。 | Exercises 4 and 11 are random each run (seed manually for a fixed demo); Exercise 9 keeps seed 409. |
| 第 3 题 | 输出 `F_0` 到 `F_n`，共 `n + 1` 个值。 | Output `F_0` through `F_n`, inclusive. |
| 第 5 题 | 按样例采用不重叠、区分大小写的匹配，子串非空。 | Matches are non-overlapping, case-sensitive, and nonempty. |
| 第 9 题 | 保留原题标题 `Dice statics`，同时指出可能是拼写错误。 | Preserve and disclose the likely title typo. |
| 第 11 题 | 外层 `while True` 反复读取长度，遇到 0 用 `break`；内层 `for` 生成数字（原题标注 F）。 | An outer `while True` reads sizes until `0`; the inner `for` builds digits. |

## 1. Predict the output (W)

**目的 / Purpose.** 追踪两个索引如何跳过一整段连续重复字符。Trace how two indices skip a complete run of equal characters.

课堂步骤：先让学生标出每轮开始时的 `i`，再追踪 `j`，最后才写输出。`j` 停下的位置是下一段的起点，所以 `i = j` 不会逐字符移动。

Talk track: “The inner loop finds the first different character. The outer loop prints one representative and jumps to that boundary.”

| 输入 | 精确输出 |
|---|---|
| `abcdeabcdeabcde` | `abcdeabcdeabcde` |
| `aabbccddeeff` | `abcdef` |
| `abcaabbccaaabbbcccddd` | `abcabcabcd` |

常见误区：把算法当成“删除所有重复字符”。它只压缩**相邻连续**重复；后面再次出现的字符仍保留。检查问题：“如果输入是 `ababa`，为什么输出仍是 `ababa`？”

## 2. Calories Burned (W/F)

**目的 / Purpose.** 同一固定序列分别用条件控制和 `range` 生成。Generate the same regular sequence with two loop styles.

结果：10→42.0，15→63.0，20→84.0，25→105.0，30→126.0 calories。`while` 版本必须更新 `minute += 5`；`for` 版本的停止值写 31，因为 `range` 不包含 stop。

Talk track: “The loop chooses the minutes; multiplication computes the calories.”

边界检查：确认没有 35 分钟，也没有漏掉 30。常见误区是写 `range(10, 30, 5)` 导致缺少 30。

## 3. Fibonacci (W/F)

**目的 / Purpose.** 把数学递推翻译成“已有两个值 → 算下一个值 → 保存”。Translate a recurrence into changing program state.

本材料约定用户输入 `n = 8` 时输出 `[0, 1, 1, 2, 3, 5, 8, 13, 21]`，因为包含 `F_0` 和 `F_8`。先问学生“`n = 1` 应输出几个值？”答案是两个：`0, 1`。

Talk track: “Index two is the first index that needs the recurrence. Each new value uses the two previous stored values.”

常见误区：把“第 n 个”理解成总共 n 个值；或在追加后使用错误索引。检查 `n = 1`、`n = 2`、`n = 8`。

## 4. Guessing Competition (W/F)

**目的 / Purpose.** 同时维护秘密数、尝试次数和仍可能的闭区间。Coordinate a random target, attempt limit, and changing inclusive range.

秘密数每次运行都随机。需要固定演示时，每局开始前紧接着运行 `random.seed(405)`，秘密数为 6：依次输入 `50, 25, 12, 6` 会在第 4 次成功，前三次范围依次变为 `1-49`、`1-24`、`1-11`；再次运行 `random.seed(405)` 后输入 `50, 25, 12, 3, 9, 4, 8` 可演示 7 次失败。

Talk track: “A high guess changes only the upper bound; a low guess changes only the lower bound. A correct guess ends the loop immediately.”

边界与误区：1 和 100 都合法；第 7 次错误后仍先显示更新范围，再 `Game over!`。不要用猜测值本身作为仍可能边界，高猜应减 1，低猜应加 1。

## 5. Repetition of a substring (W)

**目的 / Purpose.** 根据样例辨认“不重叠”语义，并决定索引移动距离。Infer non-overlap semantics and choose the index step.

匹配成功时索引前进 `len(substring)`；失败时只前进 1。`aaabcaa` 中 `aa` 的不重叠结果是 2；若允许重叠会是 3，因此原样例决定了算法。

Talk track: “A match consumes the whole substring. A miss moves one character and tries again.”

检查：`abcabc`/`abc`→2，`aaaa`/`aa`→2，`abc`/`z`→0。空子串行为未定义，本材料假设非空。

## 6. Greatest Common Divisor (W)

**目的 / Purpose.** 忠实实现原题给出的递减搜索，而不是换成更高级算法。Implement the supplied decrementing search exactly.

例：84 与 30 从 30 开始向下检查，最终得到 6。循环条件使用 `or`：只要有一个数不能整除，就必须继续。

Talk track: “We stop only when the candidate divides both numbers evenly.”

常见误区：把 `or` 写成 `and` 会在只整除一个数时错误停止；从较大数开始虽可能得到答案，但违背原算法且多做检查。

## 7. Predict the output (F)

**目的 / Purpose.** 精确处理 `range` 的 stop、缩进、`continue`、`break` 和整除更新。Trace control flow and state exactly.

**Program 1:** `108`

**Program 2:**

```text
1 4 3 2 
2 4 3 
3 4 
```

**Program 3:**

```text
1 1
2 3
3 6
5 11
6 17
7 24
8 32
```

`4` 被 `continue` 跳过，`9` 触发 `break`，因此两者都不加入且不打印。

**Program 4:** `0`。第一次 `1 // 3` 已变为 0，之后乘除仍为 0。

**Program 5:**

```text
5
9
12
14
15
```

`print(t)` 在循环内部，所以打印五个累计值。检查问题：“如果它取消缩进，会打印几行？”

## 8. Patterns (F)

**目的 / Purpose.** 把图案拆成外层行循环和内层字符/空格循环。Decompose patterns into row and column responsibilities.

- Part 1：第 1 行 5 个星号，之后每行少 1 个。
- Part 2：每行先后各一个 `#`，内部空格数等于从 0 开始的行索引。
- Part 3：领先空格数递减；本行字母数递增；全局字母索引持续并用 `% 26` 回绕。
- Part 4：三层循环分别控制三角形、行和星号；三角形之间无空行。

Talk track: “Name one job for each loop before writing code.”

常见误区：每行重置字母导致每行都从 A 开始；用字符串乘法绕过“nested loops”要求；多打印空行改变原图案。

## 9. Dice statics (F)

**目的 / Purpose.** 将每次随机结果映射到六个频数槽位。Map each random face to one of six counters.

固定种子 409 的 1000 次结果为：1→180，2→145，3→186，4→163，5→169，6→157；总和必须是 1000。真实随机运行的各项可以不同，但总和不变。

Talk track: “The face value is one through six, while list indices are zero through five, so use `face - 1`.”

常见误区：把 `counts[face]` 用在长度 6 的列表上，导致面 6 越界；或忘记验证计数总和。

## 10. Theme Park Ride Admission (W/F)

**目的 / Purpose.** 将资格过滤、`continue`、容量计数和提前停止组合起来。Combine filtering, capacity, and early termination.

课堂演示可依次输入 `135, 110, 121, 119, 150, 120, 140`：第 1、3、5、6、7 人合格，第 7 人后达到 5 人并停止，不再询问后面的人；恰好 120 cm 合格。`The ride is full!` 只在人数等于 5 时显示，最终人数始终显示。

Talk track: “A short rider consumes one checked person but no seat. A tall rider consumes one seat. Capacity ends the loop.”

边界检查：10 人全部不足 120 时人数 0 且不说 full；第 5 位合格者出现后不再询问后续人员。`while` 版本的人号更新必须写在 `continue` 之前，否则身高不足时会死循环。

## 11. Password Generator (F)

**目的 / Purpose.** 使用 `break` 处理 0，并用内层 `for` 精确生成指定字符数。Use a sentinel and generate exactly the requested number of characters.

密码每次运行都随机。需要固定演示时先运行 `random.seed(411)`，再依次输入 `4, 9, 1, 0`，得到 `3053`、`933763088`、`1`，然后停止。密码必须是字符串，否则前导 0 会丢失。原题标注 F，但请求次数未知，所以外层用 `while True` + `break`，`for` 用于逐位生成数字。

Talk track: “The outer loop handles requests; the inner loop handles digits. Zero creates no password and stops future requests.”

常见误区：用整数累积密码、遇到 0 后仍继续、随机范围写成 1–9。检查每个密码的 `len` 是否等于请求长度。

## 总结 / Wrap-up

请学生用一句话比较两类循环：`while` 适合“条件仍成立就继续”，`for` 适合“对范围或序列中的每一项执行”。再让学生指出本次三个提前改变流程的关键字或动作：状态更新、`continue`、`break`。
