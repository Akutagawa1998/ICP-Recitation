# Recitation 04/05 Classroom Script | 中英文课堂逐字讲稿

> **Instructor only / 仅供教师使用**  
> This script follows the canonical instructor notebook and the original order of all 11 exercises. Read the English paragraphs directly in class; use the Chinese paragraphs as a parallel explanation, reminder, or fallback.  
> 本讲稿与教师版 notebook 保持一致，并严格按照原题 11 道练习的顺序组织。英文段落可以直接对学生讲；中文段落用于同步解释、备课提示或必要时切换语言。

## How to use this script | 如何使用

- **Suggested time / 建议时长：** 85–95 minutes.
- **Recommended rhythm / 推荐节奏：** predict → trace → code → run → check a boundary.
- **English blocks / 英文段落：** classroom-ready wording that can be read aloud.
- **Chinese blocks / 中文段落：** matching explanation and the intended teaching point.
- **[Action] / [操作]：** something to write, run, point to, or ask students to do.
- **Expected answer / 预期答案：** the answer to obtain before moving on.

As the source requires, exercises that ask the user read values with `input()`. When a cell runs, Jupyter shows an input box under it; type a value and press Enter. Run the cell again to try another input.

与原题一致，需要用户输入的题目用 `input()` 读取。运行单元格时下方会出现输入框，输入后按回车；想换一个输入，就再运行一次该单元格。

---

## 0. Opening | 开场（约 5 分钟）

### Say in English | 英文直接讲

> Today we are going to study repetition in Python. A loop is not magic repetition. Every useful loop has three things: a state, a rule that changes the state, and a reason to stop.
>
> We will work with both `while` loops and `for` loops. We will also use nested loops, `break`, `continue`, string indexing, counters, and random numbers.
>
> Before we run any code, we will predict what should happen. Then we will trace the important variables, run the program, and check a boundary case.

### 中文对应讲解

> 今天我们学习 Python 中的重复执行。循环不是“自动重复”的魔法。一个正确的循环至少有三部分：当前状态、改变状态的规则，以及停止的原因。
>
> 本节同时练习 `while` 和 `for`，还会涉及嵌套循环、`break`、`continue`、字符串索引、计数器和随机数。
>
> 每道题都先预测，再追踪关键变量，然后运行，最后用边界值检查。

### [Action] Put these three questions on the board | 板书三个问题

1. **What is the state? / 当前状态是什么？**
2. **What changes in one iteration? / 每轮改变什么？**
3. **Why does the loop stop? / 循环为什么会停止？**

> We will use these three questions in almost every exercise today.
>
> 今天几乎每道题都可以用这三个问题分析。

---

## 1. Core knowledge | 核心知识点讲解（约 12–15 分钟）

### 1.1 The mental model of a loop | 循环的思维模型

#### Say in English

> A loop repeatedly executes a block of indented code. The indentation tells Python which statements belong to the loop.
>
> We should never look only at the loop header. We also need to track the variables used by the condition or by the sequence.

#### 中文对应讲解

> 循环会重复执行一段缩进代码。缩进决定哪些语句属于循环体。
>
> 不能只看循环头，还要追踪条件或序列中使用的变量如何变化。

#### [Action] Draw a four-column trace table | 画追踪表

| Iteration / 轮次 | State before / 执行前状态 | Action / 本轮操作 | State after / 执行后状态 |
|---:|---|---|---|
| 1 | initial values | run the body | updated values |
| 2 | previous result | run the body | updated values |

> A trace table turns a loop into a sequence of small, checkable steps.
>
> 追踪表把循环拆成一系列可以逐步检查的小步骤。

### 1.2 `while` loops | `while` 循环

```python
index = 0
while index < 5:
    print(index)
    index = index + 1
```

#### Say in English

> Read this as: while `index` is less than five, print it and add one to it.
>
> A `while` loop is controlled by a Boolean condition. It is useful when the number of repetitions depends on changing state.
>
> The update is essential. Without `index = index + 1`, the condition stays true and the loop does not stop.

#### 中文对应讲解

> 这段代码读作：只要 `index` 小于 5，就输出它，然后把它加 1。
>
> `while` 由布尔条件控制，适合“重复次数取决于状态变化”的问题。
>
> 更新语句非常关键。如果没有 `index = index + 1`，条件会一直为真，从而形成无限循环。

#### Ask / 提问

> What are the three parts here: initial state, condition, and update?
>
> 这里的初始状态、循环条件和更新语句分别是什么？

**Expected answer / 预期答案：** `index = 0`; `index < 5`; `index = index + 1`.

### 1.3 `for` loops and `range` | `for` 与 `range`

```python
for minute in range(10, 31, 5):
    print(minute)
```

#### Say in English

> A `for` loop takes one value at a time from a sequence. Here the sequence comes from `range`.
>
> `range(10, 31, 5)` starts at 10, stops before 31, and changes by 5. It produces 10, 15, 20, 25, and 30.
>
> The stop value is not included. That is why we use 31 when we want to include 30.

#### 中文对应讲解

> `for` 每次从一个序列中取出一个值。本例中的序列由 `range` 产生。
>
> `range(10, 31, 5)` 从 10 开始，在到达 31 之前停止，每次增加 5，所以得到 10、15、20、25、30。
>
> stop 不包含在结果中。因此想包含 30 时，stop 要写成 31。

#### Read aloud | 代码读法

> “For each minute from ten through thirty by fives.”
>
> “minute 从 10 到 30，每次增加 5。”

### 1.4 Choosing `while` or `for` | 如何选择循环

| Question / 问题 | Better starting choice / 优先考虑 |
|---|---|
| Repeat while a condition remains true / 条件成立时继续 | `while` |
| Visit each value in a known range / 遍历已知范围 | `for` |
| Search until a target is found / 搜索直到找到目标 | usually `while` / 通常 `while` |
| Process each item in a list or string / 处理序列每一项 | usually `for` / 通常 `for` |

#### Say in English

> These are guidelines, not laws. Some problems can be solved both ways. When the source says W/F, we will compare both versions.

#### 中文对应讲解

> 这是选择思路，不是绝对规则。同一个问题可能有两种写法。原题标记 W/F 时，我们会比较两个版本。

### 1.5 Nested loops | 嵌套循环

```python
for row in range(3):
    for column in range(2):
        print(row, column)
```

#### Say in English

> For every one outer-loop iteration, the inner loop runs completely. Three rows times two columns gives six printed pairs.
>
> Before writing a nested loop, give each loop one clear job.

#### 中文对应讲解

> 外层循环每执行一次，内层循环都会完整执行一遍。3 个 row 乘 2 个 column，一共输出 6 对值。
>
> 写嵌套循环前，先明确每一层循环各自负责什么。

### 1.6 `break` and `continue` | `break` 与 `continue`

#### Say in English

> `continue` skips the rest of the current iteration and moves to the next iteration.
>
> `break` ends the nearest loop completely.
>
> Continue means “skip this one.” Break means “stop the loop.”

#### 中文对应讲解

> `continue` 跳过本轮剩余语句，进入下一轮。
>
> `break` 直接结束最近的一层循环。
>
> 可以记成：`continue` 是“这一个不做完”，`break` 是“整个循环到此结束”。

### 1.7 Common loop state | 常见循环状态

#### Counter / 计数器

```python
count = count + 1
```

> A counter answers “how many?”
>
> 计数器回答“有多少个？”

#### Accumulator / 累加器

```python
total = total + value
```

> An accumulator answers “what is the running total?”
>
> 累加器保存“到目前为止的总量”。

#### Index / 索引

```python
character = text[index]
```

> An index answers “where are we in the sequence?”
>
> 索引表示“当前处理到序列的哪个位置”。

#### Bounds / 边界

```python
lowest_possible = 1
highest_possible = 100
```

> Bounds describe the values that are still possible.
>
> 上下界描述“目前仍然可能的范围”。

### 1.8 Strings and random numbers | 字符串与随机数

#### Say in English

> Strings are sequences, so we can index them, slice them, and loop over them.
>
> `input()` always returns a string. When we need a number, we convert it with `int(...)`, for example `n = int(input("Enter n: "))`.
>
> Random programs are difficult to demonstrate if every run changes. In Exercise 9, a fixed local seed gives us the same demonstration again, while the program still uses a random-number generator.

#### 中文对应讲解

> 字符串也是序列，因此可以索引、切片和循环遍历。
>
> `input()` 返回的永远是字符串；需要数字时用 `int(...)` 转换，例如 `n = int(input("Enter n: "))`。
>
> 如果每次运行随机结果都不同，课堂讲解会很难复现。第 9 题用固定的局部 seed 让演示重复得到同样结果，同时程序仍然在使用随机数生成器。

```python
randomizer = random.Random(409)
face = randomizer.randint(1, 6)
```

> `randint(1, 6)` includes both 1 and 6.
>
> `randint(1, 6)` 的两个端点都包含。

---

## 2. Exercise 1 — Predict the output (W) | 第 1 题（约 6 分钟）

### Transition | 过渡话术

> Let us begin by tracing an existing `while` loop. Do not run it yet. Our goal is to understand what one complete outer iteration does.
>
> 第一题先追踪已有的 `while` 程序。先不要运行，我们要先看清外层循环每一轮到底完成什么工作。

### Explain the variables | 讲变量

> `i` points to the first character of the current run. `j` starts one position later and moves right while the characters stay equal.
>
> `i` 指向当前连续字符段的第一个字符；`j` 从下一位开始，只要字符仍相等就继续右移。

> When the inner loop stops, `j` is either at the first different character or at the end of the string. We print `N[i]` once, and then set `i = j` to jump to the next run.
>
> 内层循环停止时，`j` 要么指向第一个不同字符，要么已经到达字符串末尾。程序只输出一次 `N[i]`，然后用 `i = j` 跳到下一段。

### [Action] Trace `aabbcc` on the board | 板书追踪 `aabbcc`

| Outer iteration | `i` | `N[i]` | final `j` | printed |
|---:|---:|---|---:|---|
| 1 | 0 | `a` | 2 | `a` |
| 2 | 2 | `b` | 4 | `b` |
| 3 | 4 | `c` | 6 | `c` |

### Ask / 提问

> Is this removing every repeated character from the whole string?
>
> 这个程序是不是会删除整个字符串中所有重复字符？

**Expected answer / 预期答案：** No. It compresses only adjacent runs. / 不是，它只压缩相邻连续重复段。

### Reveal the three outputs | 公布三个结果

| Input / 输入 | Output / 输出 |
|---|---|
| `abcdeabcdeabcde` | `abcdeabcdeabcde` |
| `aabbccddeeff` | `abcdef` |
| `abcaabbccaaabbbcccddd` | `abcabcabcd` |

### Closing line | 收束话术

> The inner loop finds a boundary. The outer loop prints one representative and jumps to that boundary.
>
> 内层循环负责找边界，外层循环每段输出一个代表字符，然后跳到这个边界。

---

## 3. Exercise 2 — Calories Burned (W/F) | 第 2 题（约 5 分钟）

### Say in English

> Separate the problem into two jobs. The loop generates the minutes. Multiplication calculates the calories.
>
> We need the minutes 10, 15, 20, 25, and 30. In the `while` version, we start at 10 and add 5. In the `for` version, `range(10, 31, 5)` generates the same values.

### 中文对应讲解

> 把题目拆成两个任务：循环负责生成分钟数，乘法负责计算 calories。
>
> 需要的分钟数是 10、15、20、25、30。`while` 版本从 10 开始每次加 5；`for` 版本用 `range(10, 31, 5)` 产生相同序列。

### [Action] Ask before running | 运行前提问

> Why is the stop value 31 instead of 30?
>
> 为什么 stop 写 31，而不是 30？

**Expected answer / 预期答案：** The stop value of `range` is excluded. / `range` 不包含 stop。

### Expected results | 结果

| Minutes | Calories |
|---:|---:|
| 10 | 42.0 |
| 15 | 63.0 |
| 20 | 84.0 |
| 25 | 105.0 |
| 30 | 126.0 |

### Common mistake | 常见误区

> In a `while` loop, forgetting `minute = minute + 5` creates an infinite loop. In a `for` loop, `range(10, 30, 5)` incorrectly leaves out 30.
>
> `while` 中忘记更新会形成无限循环；`for` 中写 `range(10, 30, 5)` 会漏掉 30。

---

## 4. Exercise 3 — Fibonacci (W/F) | 第 3 题（约 7 分钟）

### Resolve the interpretation | 先说明题意约定

> The source indexes Fibonacci numbers from zero. Therefore, “through the n-th value” means `F_0` through `F_n`, inclusive. For `n = 8`, we display nine values.
>
> 原题从 0 开始编号，因此本材料把“直到第 n 项”解释为包含 `F_0` 到 `F_n`。所以 `n = 8` 时一共输出 9 个值。

### Build the recurrence | 讲递推

> We already know `F_0 = 0` and `F_1 = 1`. Index 2 is the first position that needs calculation. Each new value is the sum of the previous two stored values.
>
> 已知 `F_0 = 0`、`F_1 = 1`。下标 2 是第一项需要计算的值。每个新值等于前两个已保存值之和。

### [Action] Build the list together | 一起板书

```text
index:     0  1  2  3  4  5  6  7   8
F_index:   0  1  1  2  3  5  8  13  21
```

### Ask / 提问

> If `n = 1`, how many values should we display?
>
> 如果 `n = 1`，应该输出几个值？

**Expected answer / 预期答案：** Two values: `0, 1`. / 两个值：`0, 1`。

### Compare the two versions | 比较两种循环

> The `while` version explicitly updates `index`. The `for` version receives each index from `range(2, n + 1)`. The recurrence itself is the same.
>
> `while` 版本手动更新 `index`；`for` 版本由 `range(2, n + 1)` 依次提供下标。两者的递推计算完全相同。

### Expected output for `n = 8`

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21]
```

---

## 5. Exercise 4 — Guessing Competition (W/F) | 第 4 题（约 9 分钟）

### Introduce the state | 说明需要维护的状态

> This game has several pieces of state: the secret number, the attempt number, the current guess, the lowest possible value, and the highest possible value.
>
> 这个游戏同时维护多个状态：秘密数、尝试次数、当前猜测、可能范围的下界和上界。

### Explain range updates | 讲范围更新

> If a guess is too high, the guess itself is impossible, so the new upper bound is `guess - 1`.
>
> If a guess is too low, the guess itself is impossible, so the new lower bound is `guess + 1`.

> 猜高时，当前猜测已经确定不可能，所以新上界是 `guess - 1`。
>
> 猜低时，新下界是 `guess + 1`。

### [Action] Use the reproducible demonstration | 使用固定演示

The secret number is random on every run. For a fixed demonstration, run `random.seed(405)` right before each game; the secret number is then 6. Type the guesses `50, 25, 12, 6`.

秘密数每次运行都随机。需要固定演示时，每局开始前紧接着运行 `random.seed(405)`，秘密数为 6，然后依次输入 `50, 25, 12, 6`。

| Attempt | Guess | Message | New possible range |
|---:|---:|---|---|
| 1 | 50 | Too high! | 1–49 |
| 2 | 25 | Too high! | 1–24 |
| 3 | 12 | Too high! | 1–11 |
| 4 | 6 | Correct! | stop |

### Ask / 提问

> Why do we use `return` immediately after a correct guess?
>
> 猜中后为什么要立即 `return`？

**Expected answer / 预期答案：** The game is finished; processing more guesses would be incorrect. / 游戏已经结束，继续处理后续猜测不符合题意。

### Failure path | 失败路径

> The player gets at most seven guesses. After the seventh wrong guess, show the updated range, then print `Game over!` and reveal the secret number.
>
> 玩家最多猜 7 次。第 7 次猜错后，先显示更新后的范围，再显示 `Game over!` 并公布秘密数。

### Compare loops | 比较循环

> The `while` version checks the attempt condition explicitly. The `for` version takes the attempt numbers 1 through 7 from `range(1, 8)`. Both maintain the same game state.
>
> `while` 版本显式检查次数条件；`for` 版本从 `range(1, 8)` 依次取得尝试编号 1 到 7。两者维护的游戏状态相同。

---

## 6. Exercise 5 — Repetition of a substring (W) | 第 5 题（约 6 分钟）

### Use the example to determine meaning | 用样例判断语义

> The phrase “appears in another string” could mean overlapping or non-overlapping matches. The second source example answers this question.
>
> In `aaabcaa`, the substring `aa` has three overlapping starting positions, but the source reports two. Therefore, the required matches are non-overlapping.

> “子串出现次数”可能包含重叠，也可能不包含。原题第二个样例已经给出答案。
>
> `aaabcaa` 中 `aa` 若允许重叠会有 3 次，但原题结果是 2，因此这里按不重叠计算。

### Explain index movement | 讲索引移动

> On a match, count one and move forward by `len(substring)`. On a miss, move forward by one.
>
> 匹配成功时计数加一，并前进 `len(substring)`；匹配失败时只前进一位。

### [Action] Compare two traces | 比较两种移动

```text
text = "aaaa", substring = "aa"

non-overlapping starts: 0, 2  -> 2 matches
overlapping starts:     0, 1, 2 -> 3 matches
```

### Ask / 提问

> Why does the loop stop at `len(text) - len(substring)`?
>
> 为什么最后一个起点是 `len(text) - len(substring)`？

**Expected answer / 预期答案：** After that position, there is not enough remaining text for a complete substring. / 再往后剩余字符不足以容纳完整子串。

### Source examples | 原题样例

- `abcdeabcdeabcde` with `abc` → `3`
- `aaabcaa` with `aa` → `2`

---

## 7. Exercise 6 — Greatest Common Divisor (W) | 第 6 题（约 6 分钟）

### Say in English

> We will implement the algorithm given by the source. We start with the smaller input and decrease the candidate until it divides both numbers evenly.
>
> We stop only when both remainders are zero.

### 中文对应讲解

> 本题要忠实实现原题给出的递减搜索算法：从两个数中较小者开始，不断减小候选除数，直到它能够同时整除两个数。
>
> 只有两个余数都为 0 时才能停止。

### Focus on `or` | 强调 `or`

```python
while first_number % divisor != 0 or second_number % divisor != 0:
    divisor = divisor - 1
```

> Why `or`? If either number is not divisible, the candidate is not a common divisor, so the search must continue.
>
> 为什么用 `or`？只要任意一个数不能整除，候选值就不是公约数，因此必须继续。

### [Action] Use 84 and 30 | 使用样例

> Start at 30. Many candidates fail. The first candidate found while moving downward that divides both numbers is 6. Therefore the greatest common divisor is 6.
>
> 从 30 开始向下检查。第一个能同时整除 84 和 30 的候选值是 6，因此最大公约数是 6。

### Boundary questions | 边界问题

- `gcd(17, 17)` → `17`
- `gcd(35, 64)` → `1`

### Common mistake | 常见误区

> Replacing `or` with `and` can stop when the candidate divides only one number. That result is not a common divisor.
>
> 如果把 `or` 写成 `and`，候选值只整除其中一个数时就可能错误停止。

---

## 8. Exercise 7 — Predict five outputs (F) | 第 7 题（约 14–16 分钟）

### Opening instruction | 开始话术

> For each program, first identify the range, then track the variables, and finally check the indentation of `print`.
>
> 每一小题都先看 `range`，再追踪变量，最后检查 `print` 的缩进位置。

### Program 1 — Descending accumulation | 子题 1：递减累加

> `range(20, 2, -2)` produces 20 down to 4. It does not include 2. We add those values and print once after the loop.
>
> `range(20, 2, -2)` 产生 20 到 4 的偶数，不包含 2。循环结束后只打印一次总和。

**Expected output / 预期输出：**

```text
108
```

### Program 2 — Dependent nested ranges | 子题 2：依赖外层变量的嵌套范围

> The inner stop value is `i`, so the inner loop becomes shorter on each outer iteration. `end=" "` keeps values on the same row, and the empty `print()` starts a new row.
>
> 内层循环的 stop 是外层变量 `i`，所以每一行的内层循环都会变短。`end=" "` 让数字留在同一行，空的 `print()` 负责换行。

**Expected output / 预期输出：**

```text
1 4 3 2 
2 4 3 
3 4 
```

### Program 3 — `continue` and `break` | 子题 3：`continue` 与 `break`

> When `i` contains the digit 4, `continue` skips the addition and print. When `i` contains the digit 9, `break` ends the loop. Therefore 4 is skipped, and the program stops at 9.
>
> `i` 的文本中含 4 时，`continue` 跳过累加和输出；含 9 时，`break` 结束整个循环。所以 4 被跳过，程序到 9 为止。

**Expected output / 预期输出：**

```text
1 1
2 3
3 6
5 11
6 17
7 24
8 32
```

### Program 4 — Floor division collapses the state | 子题 4：整除使状态归零

> On the first inner iteration, the result becomes `1 * 1 // 3`, which is 0. After the state becomes 0, later multiplication and floor division keep it at 0.
>
> 第一次内层循环后，结果是 `1 * 1 // 3 = 0`。状态一旦变成 0，后面的乘法和整除仍然得到 0。

**Expected output / 预期输出：**

```text
0
```

### Program 5 — Reverse indexing and indentation | 子题 5：反向索引与缩进

> `len(s) - i` visits the indices 4, 3, 2, 1, and 0. The digits are added in reverse order. Because `print(t)` is inside the loop, we see every cumulative total.
>
> `len(s) - i` 依次访问下标 4、3、2、1、0，也就是从右向左取数字。由于 `print(t)` 在循环内部，所以会看到每一次累计结果。

**Expected output / 预期输出：**

```text
5
9
12
14
15
```

### Ask / 提问

> If `print(t)` moved outside the loop, how many lines would we see?
>
> 如果把 `print(t)` 取消缩进并移到循环外，会输出几行？

**Expected answer / 预期答案：** One line, `15`. / 一行，内容是 `15`。

---

## 9. Exercise 8 — Patterns (F) | 第 8 题（约 13–15 分钟）

### Opening rule | 开始规则

> Before writing a nested loop, say one sentence for the job of each loop.
>
> 写嵌套循环前，先用一句话说明每一层循环负责什么。

### Part 1 — Decreasing stars | 子题 1：递减星号

> The outer loop chooses the number of stars in the row: 5, 4, 3, 2, 1. The inner loop prints that many stars. Then `print()` ends the row.
>
> 外层循环决定本行星号数量：5、4、3、2、1；内层循环打印对应数量；空 `print()` 负责换行。

```text
*****
****
***
**
*
```

### Part 2 — Widening hashes | 子题 2：逐渐加宽的井号

> Every row has a left hash and a right hash. The row index tells us how many spaces belong between them. Row zero has zero spaces, so it prints `##`.
>
> 每行都有左侧和右侧两个 `#`。行索引决定它们中间的空格数。第 0 行有 0 个空格，所以输出 `##`。

```text
##
# #
#  #
#   #
#    #
#     #
```

### Part 3 — Letter triangle | 子题 3：字母三角形

> This pattern needs three changing quantities: fewer leading spaces, more letters in each row, and one letter index that continues across rows.
>
> 这个图案同时维护三个变化量：领先空格逐行减少、每行字母数逐行增加、全局字母索引跨行持续。

> We use `letter_index % 26` to wrap from `Z` back to `A`. Do not reset `letter_index` at the start of each row.
>
> 使用 `letter_index % 26` 在 `Z` 后回到 `A`。不能在每一行开始时把 `letter_index` 重置。

```text
       A
      B C
     D E F
    G H I J
   K L M N O
  P Q R S T U
 V W X Y Z A B
C D E F G H I J
```

### Part 4 — Repeated triangles | 子题 4：重复三角形

> We need three loop levels. The outer loop counts triangles. The middle loop counts rows in one triangle. The inner loop prints stars in one row.
>
> 本题需要三层循环：最外层控制三角形数量，中层控制一个三角形的行，最内层控制一行中的星号。

> There is no extra blank line between triangles.
>
> 三角形之间不额外留空行。

### Ask / 提问

> Which variable should continue across rows in the letter triangle?
>
> 字母三角形中，哪个变量必须跨行持续？

**Expected answer / 预期答案：** `letter_index`.

### Common mistake | 常见误区

> String multiplication may draw the pattern, but the source explicitly asks for nested loops. Our goal is to practice loop structure, not only to produce the picture.
>
> 字符串乘法也许能画出部分图案，但原题明确要求 nested loops；本题目标是练习循环结构，而不只是得到图形。

---

## 10. Exercise 9 — Dice statics (F) | 第 9 题（约 6 分钟）

### Address the source title | 说明标题

> The source title says “Dice statics.” This is likely a typo for “Dice statistics,” but we preserve and disclose the source wording.
>
> 原题标题写的是 “Dice statics”，很可能是 “Dice statistics” 的拼写错误。本材料保留并明确说明原文。

### Explain the mapping | 讲骰面与列表下标映射

> A die face is from 1 through 6, but a six-element list uses indices 0 through 5. Therefore face 1 belongs at index 0, and face 6 belongs at index 5. The conversion is `face - 1`.
>
> 骰面是 1 到 6，但长度为 6 的列表下标是 0 到 5。所以骰面 1 对应下标 0，骰面 6 对应下标 5，转换关系是 `face - 1`。

### Code idea | 代码思路

```python
counts = [0, 0, 0, 0, 0, 0]
for _ in range(1000):
    face = randomizer.randint(1, 6)
    counts[face - 1] = counts[face - 1] + 1
```

### Invariant | 不变量检查

> No matter how the random results are distributed, the six counts must add up to 1000.
>
> 无论随机分布如何，六个计数之和必须等于 1000。

### Reproducible classroom result | 固定课堂结果

With seed 409:

| Face | Count |
|---:|---:|
| 1 | 180 |
| 2 | 145 |
| 3 | 186 |
| 4 | 163 |
| 5 | 169 |
| 6 | 157 |

**Check / 检查：** `180 + 145 + 186 + 163 + 169 + 157 = 1000`.

### Common mistake | 常见误区

> `counts[face]` is wrong. Face 6 would try to access index 6, which is outside a six-element list.
>
> `counts[face]` 是错误的。骰面 6 会尝试访问下标 6，但长度为 6 的列表最大下标是 5。

---

## 11. Exercise 10 — Theme Park Ride Admission (W/F) | 第 10 题（约 8 分钟）

### Separate two counters | 区分两个计数

> We need to distinguish the number of people checked from the number of passengers accepted. A short person has been checked but does not use a seat.
>
> 必须区分“已经检查了多少人”和“已经登车多少人”。身高不足的人已经被检查，但不占座位。

### Explain the threshold | 讲边界

> “At least 120 centimeters” includes exactly 120. The rejection condition is `height < 120`.
>
> “至少 120 cm” 包含恰好 120，因此拒绝条件是 `height < 120`。

### Explain `continue` and stopping | 讲流程控制

> If a person is too short, print the message and `continue` to the next person. If a person is tall enough, increase the passenger count. Stop as soon as the count reaches five.
>
> 身高不足时显示提示并 `continue`；身高合格时乘客数加一；一旦达到 5 人立即停止。

### [Action] Type a sample sequence | 输入一组演示身高

依次输入 / Type in order:

```text
135, 110, 121, 119, 150, 120, 140
```

| Person | Height | Result | Passenger count |
|---:|---:|---|---:|
| 1 | 135 | board | 1 |
| 2 | 110 | reject | 1 |
| 3 | 121 | board | 2 |
| 4 | 119 | reject | 2 |
| 5 | 150 | board | 3 |
| 6 | 120 | board | 4 |
| 7 | 140 | board, then stop | 5 |

### Say in English

> After person seven, the ride is full. The program does not ask the remaining people. Then we print `The ride is full!` and `5 passengers are on board.`

### 中文对应讲解

> 第 7 人之后达到 5 名乘客，因此程序不再询问后面的人员。最后显示满员信息和乘客人数。

### Boundary case | 边界情况

> If all ten people are shorter than 120, the final count is zero, and the program must not print `The ride is full!`.
>
> 如果 10 人都低于 120，最终人数是 0，而且不能显示 `The ride is full!`。

---

## 12. Exercise 11 — Password Generator (F) | 第 11 题（约 7 分钟）

### Explain the two loop jobs | 区分两层循环职责

> The outer loop handles password-size requests. The inner loop generates exactly that many digits.
>
> 外层循环处理一次次密码长度请求，内层循环精确生成对应数量的数字字符。

> The source labels this exercise F, but we don't know in advance how many requests will come. So the outer loop is `while True`, which stops with `break` when the user enters 0. The `for` loop does the required job: building each password digit by digit.
>
> 原题标注 F，但事先不知道用户会请求几次，所以外层用 `while True`，输入 0 时用 `break` 结束；题目要求的 `for` 循环负责逐位生成每个密码。

### Explain the sentinel | 讲终止标记

> A requested size of zero is a sentinel. It means “stop.” We generate no password for zero and use `break` to ignore later requests.
>
> 长度 0 是终止标记，含义是“停止”。遇到 0 时不生成密码，并用 `break` 忽略后续请求。

### Explain the data type | 讲数据类型

> A password must be a string, not an integer. If a password begins with zero, an integer representation would lose that leading zero.
>
> 密码必须保存为字符串，不能保存为整数。因为如果密码以 0 开头，整数会丢失前导 0。

### Source example versus reproducible output | 原题随机样例与固定演示

> The source shows illustrative random passwords such as `9605`. Those are examples of format, not fixed answers.
>
> Our passwords are random on every run. For a fixed demonstration, first run `random.seed(411)`; then the sizes 4, 9, and 1 produce `3053`, `933763088`, and `1`, and size 0 stops the loop.

> 原题中的 `9605` 等密码只是随机输出格式示例，并不是固定答案。
>
> 本材料的密码每次运行都随机。需要固定演示时先运行 `random.seed(411)`，再输入长度 4、9、1，分别得到 `3053`、`933763088`、`1`，随后输入 0 终止循环。

### Ask / 提问

> For a requested size of 9, what property must always be true even though the digits are random?
>
> 当请求长度为 9 时，虽然数字是随机的，但什么性质必须始终成立？

**Expected answer / 预期答案：** The password string has exactly 9 characters, and every character is a digit from 0 through 9. / 密码字符串长度必须恰好为 9，且每个字符都是 0–9 的数字。

### Common mistakes | 常见误区

- Using `randint(1, 9)` and accidentally excluding 0. / 写成 `randint(1, 9)`，错误排除数字 0。
- Continuing after size 0. / 遇到 0 后仍继续。
- Building an integer instead of a string. / 用整数而不是字符串保存密码。

---

## 13. Closing recap | 课堂总结（约 3 分钟）

### Say in English

> Let us finish with five questions.
>
> First, when is a `while` loop a natural choice? When repetition depends on a changing condition.
>
> Second, when is a `for` loop a natural choice? When we process a known range or sequence.
>
> Third, what is the difference between `continue` and `break`? Continue skips one iteration; break stops the loop.
>
> Fourth, what should we decide before writing nested loops? One clear job for each loop.
>
> Fifth, how do we check a loop? Trace its state, run it, and test a boundary.

### 中文对应讲解

> 最后用五个问题总结。
>
> 第一，什么时候适合 `while`？当重复由变化中的条件控制时。
>
> 第二，什么时候适合 `for`？当我们遍历已知范围或序列时。
>
> 第三，`continue` 与 `break` 有什么区别？前者跳过一轮，后者结束循环。
>
> 第四，写嵌套循环前要先做什么？为每层循环分配一个清楚的职责。
>
> 第五，如何检查循环？追踪状态、运行程序、测试边界。

### Exit ticket | 下课前检查题

Ask students to answer without running code:

1. What values does `range(2, 10, 3)` produce?  
   `2, 5, 8`
2. What happens if a `while` condition stays true forever?  
   An infinite loop.
3. Does `continue` end the loop?  
   No; it moves to the next iteration.
4. Why should die face 6 use list index 5?  
   Python list indices start at zero.
5. Why is a password stored as a string?  
   To preserve every digit, including a leading zero.

---

## 14. Quick answer sheet | 快速答案表

| Exercise | Key answer / 关键答案 |
|---:|---|
| 1 | `abcdeabcdeabcde`; `abcdef`; `abcabcabcd` |
| 2 | 42.0, 63.0, 84.0, 105.0, 126.0 |
| 3 | For `n=8`: `[0, 1, 1, 2, 3, 5, 8, 13, 21]` |
| 4 | Random each run; with `random.seed(405)` right before the game → secret 6, guesses 50, 25, 12, 6 succeed on attempt 4 |
| 5 | Examples → 3 and 2 non-overlapping matches |
| 6 | `gcd(84, 30) = 6` |
| 7 | P1 `108`; P2 three rows; P3 stops before 9; P4 `0`; P5 `5,9,12,14,15` |
| 8 | Four required nested-loop patterns |
| 9 | Seed 409 counts: `[180, 145, 186, 163, 169, 157]`; sum 1000 |
| 10 | Typing 135, 110, 121, 119, 150, 120, 140 → persons 1, 3, 5, 6, 7 board; final count 5 |
| 11 | Random each run; with `random.seed(411)` and sizes 4, 9, 1 → `3053`, `933763088`, `1`; then 0 stops |

## Final reminder for the instructor | 教师最后提醒

Do not reveal an output before students make a prediction. For every loop, keep returning to the same three questions: What is the state? What changes? Why does it stop?

不要在学生预测前直接公布结果。每次讲循环都回到三个问题：状态是什么？每轮改变什么？为什么会停止？
