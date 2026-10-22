# Recitation 04/05 教案 | Lesson Plan: While and For Loops

> **仅供教师使用 | Instructor only.**
> 本教案依据 [`recitation-0405-instructor.ipynb`](../recitation-0405-instructor.ipynb) 编写，题目顺序与原题一致。文中所有程序输出都已在全新 Jupyter 内核中用相同的输入实际运行核对。
> This plan follows the instructor notebook and keeps the original exercise order. Every output shown here was checked by running the notebook from a fresh kernel with the same input.

---

## 0. 使用说明 | How to Use This Plan

| 标记 Marker | 含义 Meaning |
|---|---|
| **EN** | 可以直接对学生说的英文 / English you can read aloud |
| **中** | 对应的中文讲法 / The matching Chinese explanation |
| 🖊 **Board** | 板书或画图 / Write or draw on the board |
| ▶ **Run** | 运行 notebook 中对应的单元格 / Run the matching notebook cell |
| ❓ **Ask** | 课堂提问，后附参考答案 / Question for students, followed by the answer |
| ⚠️ **Pitfall** | 学生常见错误 / Common student mistake |

**每道题的固定节奏 | Rhythm for every exercise:** 读题 Read → 思路 Plan → 代码 Code → 运行 Run → 检查边界 Check a boundary。先让学生预测，再运行。/ Let students predict before you run anything.

**关于输入 | About input.** 与原题一致，第 1、3、4、5、6、8、10、11 题都用 `input()` 读取用户输入。运行这些单元格时，单元格下方会出现输入框，输入后按回车。本教案中的"输出"都以**交互记录**的形式给出：提示后面紧跟的值就是要输入的内容，例如 `Enter the number of rows: 5` 表示输入 `5`。

> **EN** When you run a cell that asks for input, a box appears under the cell. Type your value and press Enter. To try another input, just run the cell again.
>
> **中** 运行需要输入的单元格时，下方会出现一个输入框，输入后按回车。想换一个输入，再运行一次这个单元格就行。

**关于随机数 | About random numbers.** 第 4 题（秘密数）和第 11 题（密码）每次运行都随机，与原题一致。想在课堂上得到和本教案一样的结果，在**每次**运行题目单元格之前，先在另一个单元格里运行下面的代码（只设一次种子再连玩两局，第二局的秘密数就不同了）：

```python
import random
random.seed(405)   # Exercise 4: the secret number becomes 6
# random.seed(411) # Exercise 11: sizes 4, 9, 1 give 3053, 933763088, 1
```

第 9 题没有输入，notebook 里固定使用种子 409，每次结果相同。

### 时间安排 | Timing

| 环节 Part | 内容 Content | 建议时间 Time |
|---|---|---|
| Part 1 | 开场 + 知识点速讲 / Opening + concept review | 12–15 min |
| Ex 1–3 | 读 `while` 程序、卡路里、Fibonacci | 20 min |
| Ex 4–6 | 猜数字、子串计数、最大公约数 | 25 min |
| Ex 7 | 五个 `for` 程序的输出预测 | 15 min |
| Ex 8 | 四个图案 | 15 min |
| Ex 9–11 | 骰子、过山车、密码生成 | 20 min |
| Part 3 | 总结 / Wrap-up | 3–5 min |

合计约 110 分钟。原题是 04/05 合并题单：

- **分两次课讲（推荐）：** 在第 6 题后切开。第一次以 `while` 为主（Part 1 + 第 1–6 题），第二次以 `for`、嵌套、`break` / `continue` 为主（第 7–11 题）。第二次课开头用 3 分钟复习 1.3、1.5、1.6。
- **只有一次课：** 优先讲透第 1、4、5、7、8、10 题；其余 W/F 题只讲一种写法，另一种留作课后练习。

---

## Part 1 · 知识点速讲 | Quick Concept Review (12–15 min)

### 开场 | Opening (1 min)

> **EN** Today's topic is loops: how to make Python repeat work. We will use two kinds of loops, `while` and `for`. On the exercise sheet, **W** means you must use a `while` loop, **F** means you must use a `for` loop, and **W/F** means we will write it both ways.
>
> **中** 今天的主题是循环，也就是让 Python 重复做事。我们会用两种循环：`while` 和 `for`。题单里 **W** 表示必须用 `while`，**F** 表示必须用 `for`，**W/F** 表示两种写法我们都写一遍。

### 1.1 循环三要素 | The Three Parts of Every Loop

```python
count = 0              # (1) state: where we start           状态（起点）
while count < 3:       # (3) stop: when to stop              停止条件
    print("Hello")
    count = count + 1  # (2) update: what changes each round  更新
```

> **EN** Every loop has three parts. First, a **state**: the variables that describe where we are. Second, an **update**: something that changes in every round. Third, a **stopping condition**: the reason the loop ends. If you can answer these three questions, you understand the loop.
>
> **中** 每个循环都有三个部分：**状态**，即描述"现在走到哪儿"的变量；**更新**，即每一轮都会改变的东西；**停止条件**，即循环为什么会结束。这三个问题能答出来，这个循环就看懂了。

🖊 **Board** — 把这三个问题写在黑板一角，今天每道题都回来问。/ Keep these on the board for the whole lesson.

1. What is the state? / 状态是什么？
2. What changes each round? / 每轮改变什么？
3. Why does it stop? / 为什么会停？

### 1.2 `while` 循环 | `while` Loops

执行流程 / How it runs：检查条件 → 为真：执行循环体，再回到开头检查 → 为假：跳到循环后面的代码。

> **EN** A `while` loop checks its condition **before every round**. If the condition is true, it runs the indented body, then goes back and checks again. When the condition becomes false, Python jumps to the first line after the loop.
>
> **中** `while` 在**每一轮开始前**检查条件。条件为真，就执行缩进的循环体，然后回到开头再检查；条件变成假，就跳到循环后面的第一行。
>
> **EN** The most common bug is forgetting the update. If `count` never changes, `count < 3` stays true forever. That is an **infinite loop**. In Jupyter, press the stop button (■) to interrupt it.
>
> **中** 最常见的错误是忘了更新。`count` 不变，`count < 3` 就永远为真，这就是**死循环**。在 Jupyter 里按停止键（■）可以中断。

❓ **Ask** — How many times does `Hello` print? What if we delete the last line? / `Hello` 打印几次？删掉最后一行会怎样？
**Answer** — 3 times. Without the update, it never stops. / 3 次；删掉更新就会无限打印。

### 1.3 `for` 循环与 `range` | `for` Loops and `range`

```python
for minute in range(10, 31, 5):
    print(minute)        # 10 15 20 25 30

for i in range(20, 2, -2):
    print(i)             # 20 18 16 ... 4   (2 is NOT included)

for ch in "abc":
    print(ch)            # a  b  c
```

| 写法 Form | 产生的值 Values | 读法 Read as |
|---|---|---|
| `range(5)` | 0 1 2 3 4 | from 0 up to, but not including, 5 |
| `range(2, 6)` | 2 3 4 5 | from 2 up to, but not including, 6 |
| `range(10, 31, 5)` | 10 15 20 25 30 | from 10, step 5, stop before 31 |
| `range(5, 0, -1)` | 5 4 3 2 1 | count down, stop before 0 |

> **EN** A `for` loop takes one value at a time from a sequence. `range(start, stop, step)` makes a sequence of whole numbers. The most important rule: **the stop value is never included**. If you want 30 to appear, the stop must be bigger than 30, for example 31. With a negative step, `range` counts down, and it still stops before the stop value.
>
> **中** `for` 每次从一个序列里取出一个值。`range(start, stop, step)` 生成一串整数。最重要的规则：**stop 永远不包含**。想让 30 出现，stop 就要写比 30 大的数，比如 31。step 为负数时倒着数，同样在 stop 之前停下。
>
> **EN** A `for` loop can also walk through a string, one character at a time.
>
> **中** `for` 也可以直接遍历字符串，每次取一个字符。

❓ **Ask** — What does `range(2, 10, 3)` produce? And `range(5, 0, -1)`? / 这两个 `range` 分别产生什么？
**Answer** — `2, 5, 8`; `5, 4, 3, 2, 1`.

### 1.4 `while` 与 `for` 怎么选、怎么互换 | Choosing and Converting

| 情况 Situation | 优先 Prefer |
|---|---|
| 重复次数事先知道（遍历范围、列表、字符串）/ The number of rounds is known | `for` |
| 重复到某件事发生为止（找到答案、输入 0）/ Repeat until something happens | `while` |
| 每轮前进的步长不固定 / The step size changes from round to round | `while` |

```python
# for version
for i in range(start, stop, step):
    body
```

```python
# while version (same behavior for a positive step)
i = start
while i < stop:
    body
    i = i + step
```

> **EN** A `for` loop over `range` is just a `while` loop with its three parts packed into one line: start, stop, and step. To turn it into a `while` loop, unpack them. Put the start before the loop, put the stop in the condition, and write the step as the last line of the body.
>
> **中** `for ... in range(...)` 其实就是把 `while` 的三要素（起点、终点、步长）压缩到了一行。改写成 `while` 时把它们拆开：起点写在循环前，终点写进条件，步长写成循环体的最后一行。

### 1.5 嵌套循环 | Nested Loops

```python
for row in range(3):
    for col in range(4):
        print("*", end="")
    print()
```

```text
****
****
****
```

> **EN** When one loop is inside another, the inner loop runs **completely** for every single round of the outer loop. Here the outer loop runs 3 times, and each time the inner loop prints 4 stars, so we get 3 × 4 = 12 stars.
>
> **中** 一个循环套在另一个循环里时，外层每走一轮，内层都要**完整地**跑一遍。外层 3 轮，每轮内层打印 4 颗星，一共 3 × 4 = 12 颗。
>
> **EN** Two small tools: `print("*", end="")` prints without moving to a new line, and an empty `print()` only moves to the next line. A good habit: before writing nested loops, say in one sentence what each loop is responsible for. Usually the outer loop handles rows, and the inner loop handles what goes inside one row.
>
> **中** 两个小工具：`print("*", end="")` 打印后不换行；空的 `print()` 只负责换行。好习惯：写嵌套循环前，先用一句话说出每层循环负责什么。通常外层管"行"，内层管"一行里的内容"。

### 1.6 `break` 与 `continue`

```python
for i in range(1, 8):
    if i == 3:
        continue     # skip the rest of this round
    if i == 6:
        break        # leave the loop completely
    print(i)
```

输出 / Output：`1`, `2`, `4`, `5`（每个一行 / one per line）

> **EN** `continue` means "skip the rest of **this** round and go to the next round". `break` means "stop the **whole** loop right now". Here 3 is skipped, and when `i` reaches 6 the loop ends, so 6 and 7 are never printed.
>
> **中** `continue` 的意思是"这一轮剩下的不做了，直接进入下一轮"；`break` 的意思是"整个循环立刻结束"。所以 3 被跳过；`i` 到 6 时循环结束，6 和 7 都不会打印。
>
> **EN** Two warnings. First, `break` only leaves the **innermost** loop that contains it. Second, in a `while` loop, make sure the update happens **before** `continue`. Otherwise `continue` skips the update and you get an infinite loop. We will see this in Exercise 10.
>
> **中** 两个提醒：第一，`break` 只跳出**最近的那一层**循环。第二，在 `while` 里，更新语句要放在 `continue` **之前**，否则 `continue` 会跳过更新，造成死循环。第 10 题会遇到这个问题。

### 1.7 常见循环套路 | Common Loop Patterns

| 套路 Pattern | 代码形状 Shape | 本次用在 Used in |
|---|---|---|
| 计数器 Counter | `count = count + 1` | Ex 5, 9, 10 |
| 累加器 Accumulator | `total = total + x` / `text = text + ch` | Ex 1, 7, 11 |
| 索引 / 指针 Index | `text[i]`, `i = j` | Ex 1, 5, 7 |
| 递推 Recurrence | `next_value = a + b` | Ex 3 |
| 逐个搜索 Search | `d = d - 1` until found | Ex 6 |
| 上下界 Bounds | `low`, `high` shrink | Ex 4 |
| 提前结束 Early exit | `break` / `return` | Ex 4, 10, 11 |
| 终止值 Sentinel | stop when the input is 0 | Ex 11 |

> **EN** Most loop problems are built from a few small patterns. When you read a new problem, ask yourself: am I counting something, adding things up, searching, or waiting for a stop signal?
>
> **中** 大多数循环题都是由几个小套路组合起来的。读新题时问自己：我是在计数、累加、搜索，还是在等一个"停止信号"？

### 1.8 今天会用到的小工具 | Small Tools Used Today

| 工具 Tool | 例子 Example | 注意 Note |
|---|---|---|
| `input()` | `text = input("Enter a string: ")` | 显示提示并等待输入；**返回值永远是字符串** / always returns a string |
| `int(input())` | `n = int(input("Enter n: "))` | 需要数字时先转换 / convert before doing math |
| 取余 `%` | `84 % 30` → `24` | 余数为 0 ⇔ 整除 / remainder 0 means "divides evenly" |
| 整除 `//` | `1 // 3` → `0` | 向下取整 / rounds down |
| 索引 Index | `"abc"[0]` → `'a'` | 从 0 开始 / starts at 0 |
| 切片 Slice | `"abcde"[1:3]` → `'bc'` | 含头不含尾 / start included, stop excluded |
| `len()` | `len("abc")` → `3` | 字符个数 / number of characters |
| `str()` / `int()` | `str(9)` → `'9'`; `int("3")` → `3` | 数字与字符串互转 / number ↔ text |
| `ord()` / `chr()` | `ord("A")` → `65`; `chr(66)` → `'B'` | 字母与编号互转 / letter ↔ code |
| `random.randint(a, b)` | `randint(1, 6)` | **两端都包含**，和 `range` 不同 / both ends included, unlike `range` |
| `random.Random(seed)` | `random.Random(409)` | 第 9 题：固定种子，结果可复现 / Ex 9: same results every run |
| `random.seed(n)` | `random.seed(405)` | 课堂演示时固定第 4、11 题的随机结果 / fix Ex 4 and 11 for a demo |
| f-string | `f"{x:.1f}"` | 保留 1 位小数 / one decimal place |

> **EN** Today most exercises read input from the user. Remember: `input()` always gives you a **string**. Even if the user types `8`, you get the text `"8"`. To do math or comparisons with numbers, convert it first: `n = int(input("Enter n: "))`.
>
> **中** 今天大部分题都要读取用户输入。记住：`input()` 返回的永远是**字符串**。用户输入 `8`，得到的是文本 `"8"`。要做数学运算或比较大小，先转换：`n = int(input("Enter n: "))`。

❓ **Ask** — What does `"3" + "5"` give? And `int("3") + int("5")`? / 这两个分别得到什么？
**Answer** — `"35"` (strings are joined); `8` (numbers are added). / 字符串是拼接，整数是相加。

### 1.9 知识点与题目对照 | Concept Map

| # | 题目 Title | 循环 Loop | 核心知识点 Key ideas |
|---|---|---|---|
| 1 | Predict the output | W | 嵌套 `while`、双指针、连续段 / nested `while`, two indices, runs |
| 2 | Calories Burned | W/F | 固定步长序列、`range` 的 stop / fixed-step sequence |
| 3 | Fibonacci | W/F | 递推、列表追加、差一错误 / recurrence, `append`, off-by-one |
| 4 | Guessing Competition | W/F | 随机数、次数上限、上下界、提前结束 / random, limit, bounds, early exit |
| 5 | Repetition of a substring | W | 滑动窗口、变步长、不重叠匹配 / sliding window, variable step |
| 6 | Greatest Common Divisor | W | 递减搜索、`%`、`or` 条件 / countdown search, `%`, `or` |
| 7 | Predict the output | F | 负步长、内层依赖外层、`continue`/`break`、`//` |
| 8 | Patterns | F | 嵌套 `for`、行列公式、`chr`/`ord`、`%` 回绕 / row formulas, wrap-around |
| 9 | Dice statics | F | 列表计数器、`face - 1` 映射 / list of counters |
| 10 | Theme Park Ride Admission | W/F | 两种计数、`continue`、满员停止 / two counts, capacity |
| 11 | Password Generator | F | 终止值 0、内层循环拼字符串 / sentinel, building a string |

---

## Part 2 · 逐题讲解 | Exercise-by-Exercise Walkthrough

---

### Exercise 1 | Predict the Output (W) — ⏱ 7 min

**考点 Focus:** 嵌套 `while`、两个索引 `i` / `j`、"连续相同字符段"、`end=''`。/ Nested `while`, two indices, runs of equal adjacent characters.

#### 题目 | The Task

```python
N = input('Enter a string: ')
i, j = 0, 0
while i < len(N):
    j = i + 1
    while j < len(N) and N[j] == N[i]:
        j = j + 1
    print(N[i], end='')
    i = j
```

> **EN** In this exercise we don't write code. We read it. We need to predict the output for three inputs. Please don't run it yet.
>
> **中** 这题不写代码，而是读代码：预测三个输入对应的输出。先不要运行。

#### 解题思路 | How to Think About It

**Step 1 — 给每个变量一个"角色" / Give every variable a job.**

> **EN** Before tracing letter by letter, let's ask what each variable is for. `i` marks the **start of a group** of equal letters. `j` is a **scout**. It starts right after `i` and keeps walking right as long as it sees the same letter as `N[i]`.
>
> **中** 先别急着一个字母一个字母地追，先问每个变量是干什么的。`i` 标记一组相同字母的**开头**；`j` 是**探路的**，它从 `i` 的下一位出发，只要看到的字母和 `N[i]` 相同就继续往右走。

**Step 2 — 内层循环在找什么 / What does the inner loop find?**

> **EN** The inner loop stops when `j` reaches a **different** letter, or the **end** of the string. So when it stops, `j` is exactly the start of the next group.
>
> **中** 内层循环在 `j` 碰到**不同的字母**或走到**字符串末尾**时停下。所以它停下时，`j` 正好指向下一组的开头。

**Step 3 — 外层循环每轮做什么 / What does one outer round do?**

> **EN** Each outer round prints `N[i]` once, which is one letter for the whole group. Then `i = j` jumps straight to the next group.
>
> **中** 外层每一轮只打印一次 `N[i]`，也就是整组只输出一个字母。然后 `i = j` 直接跳到下一组。

**Step 4 — 一句话总结 / One-sentence summary.**

> **EN** So the program **squeezes each run of adjacent equal letters into one letter**. Only *adjacent* repeats are merged. If a letter comes back later, it is printed again.
>
> **中** 所以这个程序会把**每一段"连续相同"的字母压缩成一个**。只合并*相邻*的重复；同一个字母隔开后再出现，会被再次打印。

#### 追踪 | Trace on the Board

🖊 **Board** — 先用短串 `aabbcc` 演示，再用竖线给第三个输入分组。/ Demo with `aabbcc` first.

| 外层轮次 Round | `i` | `N[i]` | 内层结束时 `j` / `j` after inner loop | 这一组 Group | 打印 Printed |
|---:|---:|---|---:|---|---|
| 1 | 0 | `a` | 2 | `aa` | `a` |
| 2 | 2 | `b` | 4 | `bb` | `b` |
| 3 | 4 | `c` | 6 | `cc` | `c` |

```text
abcaabbccaaabbbcccddd
a | b | c | aa | bb | cc | aaa | bbb | ccc | ddd   →   abcabcabcd
```

#### 答案 | Answers

| Input | Output |
|---|---|
| `abcdeabcdeabcde` | `abcdeabcdeabcde`（没有相邻重复，原样输出 / no adjacent repeats, unchanged） |
| `aabbccddeeff` | `abcdef` |
| `abcaabbccaaabbbcccddd` | `abcabcabcd` |

> **EN** Because of `end=''`, all letters are printed on one line with nothing between them.
>
> **中** 因为 `end=''`，所有字母连在同一行输出，中间什么都没有。

#### Notebook 代码说明 | About the Notebook Code

```python
def keep_one_character_per_run(text):
    result = ""
    i = 0
    while i < len(text):
        j = i + 1
        while j < len(text) and text[j] == text[i]:
            j = j + 1
        result = result + text[i]   # keep one letter for this run
        i = j
    return result

text = input("Enter a string: ")
print(keep_one_character_per_run(text))
```

▶ **Run** the solution cell **three times**, typing one input from the table each time. / 运行三次，每次输入表格里的一个字符串。

```text
Enter a string: aabbccddeeff
abcdef
```

> **EN** The notebook puts the same logic in a function called `keep_one_character_per_run`. Instead of printing letters one by one, it adds each kept letter to a string called `result` and returns it. Like the source program, it reads the string with `input`. `input` already returns a string, so no conversion is needed here.
>
> **中** Notebook 把同样的逻辑封装成函数 `keep_one_character_per_run`：不是逐个 `print`，而是把保留的字母拼接到字符串 `result` 里，最后返回。和原题程序一样用 `input` 读取字符串；`input` 返回的本来就是字符串，所以这里不需要转换。

#### 课堂提问 | Questions

❓ **Ask 1** — What is the output for `ababa`? / 输入 `ababa` 输出什么？
**Answer** — `ababa`. No two equal letters are next to each other. / 没有相邻的相同字母。

❓ **Ask 2** — What if we swap the inner condition to `N[j] == N[i] and j < len(N)`? / 把内层条件的两部分换个顺序会怎样？
**Answer** — At the end of the string, `j == len(N)`, so `N[j]` raises `IndexError: string index out of range`. In the original order, when `j < len(N)` is false, Python **does not check** the second part. This is called short-circuit evaluation. / 原顺序下，`j < len(N)` 为假时 Python 不再计算后半部分（短路求值），所以不会越界；顺序反过来就会先访问 `N[j]`，从而报错。

#### ⚠️ 易错点 | Pitfalls

- 以为程序会"删除所有重复字母"，把第三个答案写成 `abcd`。/ Thinking it removes *every* duplicate letter.
- 在字母之间加空格或换行，但代码并不会打印这些内容。/ Adding spaces or newlines that the code never prints.

---

### Exercise 2 | Calories Burned (W/F) — ⏱ 5 min

**考点 Focus:** 生成固定步长的序列；`range` 不包含 stop；`while` ↔ `for` 互换。/ Fixed-step sequence, excluded stop, loop conversion.

#### 题目 | The Task

> **EN** On a treadmill you burn 4.2 calories per minute. Use a loop to display the calories burned after 10, 15, 20, 25, and 30 minutes.
>
> **中** 在跑步机上每分钟消耗 4.2 卡路里。用循环输出第 10、15、20、25、30 分钟时消耗的卡路里。

#### 解题思路 | How to Think About It

> **EN** Let's use our three questions. What repeats? "Compute one value and print one line." What changes? The minute: 10, 15, 20, 25, 30. It goes up by 5 each time. When do we stop? After 30.
>
> **中** 用三个问题分析：重复做什么？"算一个值，打印一行"。什么在变？分钟数：10、15、20、25、30，每次加 5。什么时候停？30 之后。
>
> **EN** Do we need to remember the previous result? No. Each line can be computed directly: calories = minutes × 4.2. So the loop only needs to produce the minutes, and one multiplication does the rest.
>
> **中** 需要记住上一次的结果吗？不需要。每一行都能直接算：卡路里 = 分钟 × 4.2。所以循环只负责产生分钟数，乘法负责计算。

#### 代码讲解 | Code Walkthrough

```python
# while version
calories_per_minute = 4.2
minute = 10                         # start
while minute <= 30:                 # stop condition (30 is included)
    calories = minute * calories_per_minute
    print(f"After {minute} minutes: {calories:.1f} calories")
    minute = minute + 5             # update
```

```python
# for version
calories_per_minute = 4.2
for minute in range(10, 31, 5):     # start 10, stop before 31, step 5
    calories = minute * calories_per_minute
    print(f"After {minute} minutes: {calories:.1f} calories")
```

> **EN** Compare the two versions line by line. `minute = 10` matches the start of `range`. `minute <= 30` matches the stop 31, because "up to and including 30" is the same as "before 31". `minute = minute + 5` matches the step 5. Same three parts, written in different places.
>
> **中** 两个版本逐行对照：`minute = 10` 对应 `range` 的起点；`minute <= 30` 对应 stop 31，因为"不超过 30"就等于"在 31 之前停下"；`minute = minute + 5` 对应步长 5。三要素完全一样，只是写的位置不同。
>
> **EN** `{calories:.1f}` shows the number with one decimal place. The source does not fix a format. One decimal keeps the output clean, because floats sometimes print long tails. For example, `0.1 + 0.2` prints `0.30000000000000004`.
>
> **中** `{calories:.1f}` 表示保留一位小数。原题没有规定格式；保留一位小数能让输出整齐，因为浮点数有时会出现很长的尾巴，例如 `0.1 + 0.2` 会打印 `0.30000000000000004`。

#### 输出 | Output (both versions)

```text
After 10 minutes: 42.0 calories
After 15 minutes: 63.0 calories
After 20 minutes: 84.0 calories
After 25 minutes: 105.0 calories
After 30 minutes: 126.0 calories
```

#### 课堂提问 | Questions

❓ **Ask 1** — Why is the stop `31`, not `30`? / 为什么 stop 写 31 而不是 30？
**Answer** — The stop is excluded. `range(10, 30, 5)` gives only 10, 15, 20, 25. / stop 不包含，写 30 会漏掉 30。

❓ **Ask 2** — Would `range(10, 35, 5)` also work? / `range(10, 35, 5)` 行不行？
**Answer** — Yes. 35 is excluded, so it still ends at 30. Any stop from 31 to 35 works; 31 is the clearest. / 可以。35 不包含，仍然停在 30。31 到 35 都可以，31 最清楚。

#### ⚠️ 易错点 | Pitfalls

- `while` 版本忘记 `minute = minute + 5`，变成死循环。/ Forgetting the update gives an infinite loop.
- 写成 `while minute < 30`，漏掉 30 分钟。/ Using `<` misses 30.

---

### Exercise 3 | Fibonacci (W/F) — ⏱ 8 min

**考点 Focus:** 把递推公式变成循环；用列表记住前面的值；差一错误（off-by-one）。/ Turning a recurrence into a loop.

#### 题目与约定 | Task and Interpretation

> **EN** Ask for a positive integer `n` and display the Fibonacci sequence up to the n-th value. The source starts counting at zero: F₀ = 0, F₁ = 1, and every later value is the sum of the two values before it. So "up to the n-th value" means F₀ through Fₙ. That is **n + 1 numbers**.
>
> **中** 输入一个正整数 `n`，输出到第 n 项为止的 Fibonacci 数列。原题从 0 开始编号：F₀ = 0，F₁ = 1，之后每一项等于前两项之和。所以"到第 n 项"指 F₀ 到 Fₙ，一共 **n + 1 个数**。

（这是本材料对原题的解释，上课时直接告诉学生。/ This is our interpretation; state it in class.）

#### 解题思路 | How to Think About It

**Step 1 — 先手算 / Compute by hand first.**

🖊 **Board**

```text
index:  0  1  2  3  4  5  6  7   8
F:      0  1  1  2  3  5  8  13  21
```

> **EN** Before coding, let's compute a few values by hand. To get the next number, what do we look at? The **two numbers just before it**. So the program must remember earlier values. A list is a simple way to remember them.
>
> **中** 写代码前先手算几项。算下一个数要看什么？**它前面的两个数**。所以程序必须记住之前的值，最简单的方法是用一个列表保存。

**Step 2 — 初始状态 / Starting state.**

> **EN** F₀ and F₁ are given, so the list starts as `[0, 1]`. The first value we actually have to calculate is at index 2.
>
> **中** F₀ 和 F₁ 是已知的，所以列表一开始就是 `[0, 1]`。第一个真正需要计算的是下标 2。

**Step 3 — 每一轮做什么 / One round.**

> **EN** In each round: add the last two stored values, append the result to the list, and move to the next index.
>
> **中** 每一轮：把最后两个已保存的值相加，把结果追加到列表末尾，然后下标加一。

**Step 4 — 何时停止 / When to stop.**

> **EN** We stop after computing index `n`. So we calculate indices 2, 3, …, n. That is `range(2, n + 1)`, or `while index <= n`.
>
> **中** 算完下标 `n` 就停。需要计算的下标是 2, 3, …, n，也就是 `range(2, n + 1)`，或 `while index <= n`。

#### 代码讲解 | Code Walkthrough

```python
def fibonacci_through_while(n):
    sequence = [0, 1]                  # F_0 and F_1 are given
    index = 2                          # first index we must compute
    while index <= n:                  # stop after F_n
        next_value = sequence[index - 1] + sequence[index - 2]
        sequence.append(next_value)
        index = index + 1
    return sequence[:n + 1]            # keep F_0 ... F_n

n = int(input("Enter a strictly positive integer n: "))   # text -> int
print(fibonacci_through_while(n))
```

```python
def fibonacci_through_for(n):
    sequence = [0, 1]
    for index in range(2, n + 1):      # index = 2, 3, ..., n
        next_value = sequence[index - 1] + sequence[index - 2]
        sequence.append(next_value)
    return sequence[:n + 1]

n = int(input("Enter a strictly positive integer n: "))
print(fibonacci_through_for(n))
```

> **EN** `sequence[index - 1]` and `sequence[index - 2]` are the two values before the one we are computing. The last line, `sequence[:n + 1]`, keeps exactly n + 1 values. For n = 1, the loop never runs and we return `[0, 1]`. The slice is also a safety net: if someone passed n = 0, it would return just `[0]`.
>
> **中** `sequence[index - 1]` 和 `sequence[index - 2]` 就是当前这一项的前两项。最后的 `sequence[:n + 1]` 保证正好返回 n + 1 个值：n = 1 时循环一次都不执行，返回 `[0, 1]`。这个切片也是一道保险：即使传入 n = 0，也只返回 `[0]`。
>
> **EN** `input` gives us text, so `int(...)` turns it into a number. Without `int`, `index <= n` would compare a number with a string and raise a `TypeError`.
>
> **中** `input` 得到的是文本，所以要用 `int(...)` 转成数字。不转换的话，`index <= n` 会拿数字和字符串比较，抛出 `TypeError`。
>
> **EN** Again, the body is identical in both versions. Only the loop frame changes: `while` manages `index` by hand, and `for` lets `range` manage it.
>
> **中** 两个版本的循环体完全一样，只有"循环外壳"不同：`while` 手动管理 `index`，`for` 交给 `range` 管理。

#### 追踪 | Trace (input `8`)

| `index` | `sequence[index-2]` | `sequence[index-1]` | `next_value` |
|---:|---:|---:|---:|
| 2 | 0 | 1 | 1 |
| 3 | 1 | 1 | 2 |
| 4 | 1 | 2 | 3 |
| 5 | 2 | 3 | 5 |
| 6 | 3 | 5 | 8 |
| 7 | 5 | 8 | 13 |
| 8 | 8 | 13 | 21 |

```text
Enter a strictly positive integer n: 8
[0, 1, 1, 2, 3, 5, 8, 13, 21]
```

#### 课堂提问 | Questions

❓ **Ask 1** — If `n = 1`, how many values do we show? And `n = 2`? / `n = 1` 和 `n = 2` 分别输出什么？
**Answer** — `[0, 1]` and `[0, 1, 1]`.

❓ **Ask 2** — Why does the range start at 2 and stop at `n + 1`? / 为什么是 `range(2, n + 1)`？
**Answer** — Indices 0 and 1 are already in the list, so we start at 2. We need index `n` itself, and the stop is excluded, so the stop is `n + 1`. / 下标 0 和 1 已经有了，所以从 2 开始；要包含下标 `n`，而 stop 不包含，所以写 `n + 1`。

#### 拓展（可选）| Optional Extension

如果学生已经会了，可以展示只用两个变量的写法（不必存整个列表）。/ If time allows, show the two-variable version.

```python
a, b = 0, 1
for _ in range(n + 1):
    print(a, end=" ")
    a, b = b, a + b
```

> **EN** `a, b = b, a + b` updates both values at the same time. `a` always holds the current value, and `b` holds the next one.
>
> **中** `a, b = b, a + b` 同时更新两个变量：`a` 永远是当前项，`b` 是下一项。

#### ⚠️ 易错点 | Pitfalls

- 只输出 n 个数（把"第 n 项"理解成"共 n 项"）。/ Showing n values instead of n + 1.
- 写成 `range(2, n)`，漏掉 Fₙ。/ `range(2, n)` misses Fₙ.
- 列表从空列表开始，导致 `sequence[index - 1]` 越界。/ Starting from an empty list.

---

### Exercise 4 | Guessing Competition (W/F) — ⏱ 10 min

**考点 Focus:** 随机数、次数上限、不断缩小的范围、猜中提前结束。/ Random numbers, an attempt limit, shrinking bounds, early exit.

#### 题目 | The Task

> **EN** The computer picks a secret number from 1 to 100. The player has at most 7 guesses. After each guess we print "Too high!", "Too low!", or "Correct!" with the number of guesses used. After every wrong guess we also print the range where the secret number can still be. If the 7th guess is also wrong, we show the range, then "Game over!", and reveal the number.
>
> **中** 电脑从 1 到 100 中随机选一个秘密数，玩家最多猜 7 次。每次猜完输出 "Too high!"、"Too low!"，或者 "Correct!" 加上已用次数。每次猜错后，还要输出秘密数目前可能的范围。如果第 7 次仍然猜错，先显示范围，再输出 "Game over!" 并公布答案。

#### 解题思路 | How to Think About It

**Step 1 — 列出游戏要记住的东西 / List the state.**

> **EN** A game is a loop with memory. Before writing code, let's list everything the game must remember.
>
> **中** 游戏就是"带记忆的循环"。写代码前，先列出游戏需要记住的所有东西。

🖊 **Board**

| 变量 Variable | 含义 Meaning | 初始值 Start |
|---|---|---|
| `secret_number` | 秘密数 / the secret | random, 1–100 |
| `attempt_number` | 已经猜了几次 / guesses used | 0 |
| `lowest_possible` | 可能范围的下界 / lower bound | 1 |
| `highest_possible` | 可能范围的上界 / upper bound | 100 |

**Step 2 — 循环有两个出口 / Two ways out.**

> **EN** This loop can end in two ways. Way one: the player guesses correctly. Then we stop immediately, even if guesses are left. Way two: all 7 guesses are used. Then it's game over. So the loop runs **at most** 7 times, but it can end early.
>
> **中** 这个循环有两种结束方式。第一种：玩家猜中，立刻结束，即使还有剩余次数。第二种：7 次用完，游戏失败。所以循环**最多**执行 7 次，但可能提前结束。

**Step 3 — 一轮里做什么 / What happens in one round.**

1. 次数加一，读一个猜测 / Count the attempt and read a guess.
2. 猜中：输出 `Correct!` 和次数，结束游戏 / If correct, print and end the game.
3. 猜大：输出 `Too high!`，上界变为 `guess - 1` / If too high, lower the upper bound.
4. 猜小：输出 `Too low!`，下界变为 `guess + 1` / If too low, raise the lower bound.
5. 输出当前范围 / Print the current range.

**Step 4 — 范围怎么更新 / How to update the range.**

> **EN** If 50 is too high, is 50 still possible? No. So the new upper bound is 49, which is `guess - 1`. In the same way, if 3 is too low, the new lower bound is 4, which is `guess + 1`.
>
> **中** 如果 50 猜大了，50 还可能是答案吗？不可能。所以新的上界是 49，也就是 `guess - 1`。同理，3 猜小了，新的下界就是 4，也就是 `guess + 1`。
>
> **EN** Why do we use `min` and `max`? Suppose the range is already 1–24, and the player guesses 40. It is too high, but the upper bound must stay 24. It must not grow to 39. `min(24, 39)` keeps 24. So `min` and `max` protect us from guesses outside the current range.
>
> **中** 为什么要用 `min` 和 `max`？假设范围已经是 1–24，玩家却猜了 40。这确实猜大了，但上界应该保持 24，不能变成 39。`min(24, 39)` 会保留 24。所以 `min`/`max` 能防止范围外的猜测把范围"撑大"。

**Step 5 — 循环结束之后 / After the loop.**

> **EN** If the program reaches the code after the loop, the player never guessed correctly, because a correct guess would already have left the function with `return`. So "Game over!" belongs after the loop.
>
> **中** 程序如果走到了循环后面，说明玩家一直没猜中，因为猜中时已经用 `return` 离开了函数。所以 "Game over!" 写在循环之后。

#### 代码讲解 | Code Walkthrough

```python
import random

def play_guessing_game_while():
    secret_number = random.randint(1, 100)       # 1 and 100 are both possible
    lowest_possible = 1
    highest_possible = 100
    attempt_number = 0
    while attempt_number < 7:                    # at most 7 guesses
        attempt_number = attempt_number + 1      # update first: 1, 2, ..., 7
        guess = int(input(f"Guess {attempt_number}: "))
        if guess == secret_number:
            print("Correct!")
            print("Guesses used:", attempt_number)
            return                               # early exit: leave loop and function
        if guess > secret_number:
            print("Too high!")
            highest_possible = min(highest_possible, guess - 1)
        else:
            print("Too low!")
            lowest_possible = max(lowest_possible, guess + 1)
        print(f"Possible range: {lowest_possible}-{highest_possible}")
    print("Game over!")
    print("Secret number:", secret_number)

play_guessing_game_while()
```

> **EN** `random.randint(1, 100)` picks the secret, and it includes both 1 and 100. Every time we run the cell, we get a new secret, just like the source says.
>
> **中** `random.randint(1, 100)` 选出秘密数，1 和 100 都可能取到。每次运行单元格都会得到新的秘密数，和原题要求一致。
>
> **EN** Look at the loop. The counter is updated **first**, at the top of the body, so the prompt shows "Guess 1", "Guess 2", and so on, and we can never forget the update. Then `int(input(...))` reads the guess and turns the text into a number.
>
> **中** 看循环：计数器在循环体**一开头**就更新，所以提示依次显示 "Guess 1"、"Guess 2"……也不可能忘记更新。然后 `int(input(...))` 读入猜测，把文本转成数字。
>
> **EN** `return` is the early exit. It leaves the loop and the whole function at once. That's why "Game over!" never appears after a correct guess.
>
> **中** `return` 就是提前结束：它一次性跳出循环和整个函数，所以猜中之后不会再出现 "Game over!"。

`for` 版本只改了"循环外壳"：/ The `for` version only changes the loop frame:

```python
def play_guessing_game_for():
    secret_number = random.randint(1, 100)
    lowest_possible = 1
    highest_possible = 100
    for attempt_number in range(1, 8):           # 1, 2, ..., 7
        guess = int(input(f"Guess {attempt_number}: "))
        # ... same body as the while version ...
    print("Game over!")
    print("Secret number:", secret_number)
```

> **EN** `range(1, 8)` gives the attempt numbers 1 to 7 directly, so the `for` version needs no counter of its own. The body is identical. The `while` version manages the counter itself, and the `for` version lets `range` manage it.
>
> **中** `range(1, 8)` 直接产生尝试编号 1 到 7，所以 `for` 版本不需要自己维护计数器，循环体完全一样。`while` 版本自己管理计数器，`for` 版本交给 `range` 管理。

#### 交互演示 | Live Demo

秘密数每次都随机。想得到下面和教案一致的结果，每局开始前紧接着运行 `random.seed(405)`，秘密数就是 **6**。/ Run `random.seed(405)` right before each game to make the secret **6**.

**成功路径 | Success path** — 依次输入 / type `50, 25, 12, 6` ▶ **Run**

```text
Guess 1: 50
Too high!
Possible range: 1-49
Guess 2: 25
Too high!
Possible range: 1-24
Guess 3: 12
Too high!
Possible range: 1-11
Guess 4: 6
Correct!
Guesses used: 4
```

**失败路径 | Failure path** — 再运行一次 `random.seed(405)`，然后依次输入 / reseed, then type `50, 25, 12, 3, 9, 4, 8`

```text
Guess 1: 50
Too high!
Possible range: 1-49
Guess 2: 25
Too high!
Possible range: 1-24
Guess 3: 12
Too high!
Possible range: 1-11
Guess 4: 3
Too low!
Possible range: 4-11
Guess 5: 9
Too high!
Possible range: 4-8
Guess 6: 4
Too low!
Possible range: 5-8
Guess 7: 8
Too high!
Possible range: 5-7
Game over!
Secret number: 6
```

> **EN** Without a seed, let a student come up and play. It's a good chance to practice the halving strategy from Ask 3 below.
>
> **中** 不设种子时，可以请一位学生上来玩一局，顺便练习下面提问 3 的"折半"策略。

#### 课堂提问 | Questions

❓ **Ask 1** — Why `guess - 1` and not `guess`? / 为什么上界是 `guess - 1` 而不是 `guess`？
**Answer** — The guess itself was wrong, so it can't be the secret. / 猜过的数已经确定不是答案。

❓ **Ask 2** — What happens if the player is correct on the 7th guess? / 第 7 次才猜中会怎样？
**Answer** — `Correct!` and `Guesses used: 7`. No "Game over!", because `return` leaves the function before reaching it. / 输出猜中信息，不会输出 Game over，因为 `return` 已经离开了函数。

❓ **Ask 3（趣味 / fun）** — What is the best strategy? / 最好的策略是什么？
**Answer** — Always guess the middle of the current range. Each guess cuts the range in half, and 2⁷ = 128 > 100, so 7 guesses are always enough. / 每次猜当前范围的中间值，范围每次减半；2⁷ = 128 > 100，所以 7 次一定够用。

#### ⚠️ 易错点 | Pitfalls

- 猜中后没有提前结束，最后仍然打印 "Game over!"。/ No early exit, so "Game over!" appears after a win.
- 把猜测值本身当作新边界。/ Using the guess itself as the new bound.
- 以为 `randint(1, 100)` 像 `range` 一样不包含 100。/ Thinking `randint` excludes the end like `range`.
- 输出次数从 0 开始。/ Printing guess numbers starting from 0.

---

### Exercise 5 | Repetition of a Substring (W) — ⏱ 8 min

**考点 Focus:** 切片做"滑动窗口"、可变步长、不重叠匹配、最后一个合法起点。/ Sliding window, variable step, non-overlapping matches.

#### 题目 | The Task

> **EN** Count how many times one string appears in another. For example, `abc` appears 3 times in `abcdeabcdeabcde`, and `aa` appears 2 times in `aaabcaa`. We must use a `while` loop.
>
> **中** 统计一个字符串在另一个字符串中出现的次数。例如 `abc` 在 `abcdeabcdeabcde` 中出现 3 次，`aa` 在 `aaabcaa` 中出现 2 次。必须用 `while` 循环。

（原题写 "appears into another"，应为 "appears in another"。/ The source wording "appears into" likely means "appears in".）

#### 解题思路 | How to Think About It

**Step 1 — 用例子确定规则 / Let the example decide the rule.**

> **EN** How many times does `aa` appear in `aaabcaa`? Let's list every starting position: 0, 1, and 5. That's 3. But the source says 2! So the matches must **not overlap**. Once we use the letters at positions 0 and 1, position 1 cannot be used again.
>
> **中** `aa` 在 `aaabcaa` 里出现几次？列出所有起点：0、1、5，一共 3 个。但原题说是 2！所以匹配**不能重叠**：位置 0 和 1 的字母已经用过了，位置 1 就不能再用。

🖊 **Board**

```text
index:    0 1 2 3 4 5 6
text:     a a a b c a a
match 1:  a a              start 0 → jump to 2
match 2:            a a    start 5 → jump to 7
```

**Step 2 — 滑动窗口 / A sliding window.**

> **EN** Imagine a window exactly as wide as the substring. Put it at position `index`, and compare `text[index:index + len(substring)]` with the substring.
>
> **中** 想象一个和子串一样宽的"窗口"，放在位置 `index`，比较 `text[index:index + len(substring)]` 和子串是否相同。

**Step 3 — 窗口怎么移动 / How the window moves.**

> **EN** If it matches, count it, and jump past the whole match: move by `len(substring)`. If it doesn't match, move by one.
>
> **中** 匹配成功：计数加一，并跳过整个匹配，前进 `len(substring)`；匹配失败：只前进一位。
>
> **EN** This is why the source asks for `while`. The step is sometimes 1 and sometimes `len(substring)`. A `for` loop over `range` has a fixed step, but a `while` loop lets us choose the step in every round.
>
> **中** 这就是原题要求用 `while` 的原因：步长有时是 1，有时是 `len(substring)`。`for ... in range` 的步长是固定的，而 `while` 可以每一轮自己决定前进多少。

**Step 4 — 最后一个起点 / The last start position.**

> **EN** The window must fit inside the text. The last start where a full window fits is `len(text) - len(substring)`. For `aaabcaa` (length 7) and `aa` (length 2), the last start is 5. We must include it, so the condition is `index <= last_start`.
>
> **中** 窗口必须完整地落在文本里。最后一个能放下完整窗口的起点是 `len(text) - len(substring)`。`aaabcaa` 长 7，`aa` 长 2，最后起点是 5。这个位置也要检查，所以条件写 `index <= last_start`。

#### 代码讲解 | Code Walkthrough

```python
def count_non_overlapping(text, substring):
    count = 0
    index = 0                                    # where the window starts
    last_start = len(text) - len(substring)      # last place a full window fits
    while index <= last_start:
        if text[index:index + len(substring)] == substring:
            count = count + 1
            index = index + len(substring)       # match: jump past it
        else:
            index = index + 1                    # miss: move one step
    return count

text = input("Write a string: ")
substring = input("Write another string: ")
number_of_matches = count_non_overlapping(text, substring)
print(f"String '{substring}' appears {number_of_matches} times.")
```

> **EN** Both inputs are strings already, so we don't need `int` here. We use the same prompts as the source: "Write a string" and "Write another string".
>
> **中** 两个输入本来就是字符串，所以这里不需要 `int`。提示语和原题一样："Write a string" 和 "Write another string"。

#### 追踪 | Trace (`aaabcaa`, `aa`, last_start = 5)

| `index` | 窗口 Window | 匹配? Match? | `count` | 下一个 `index` / Next |
|---:|---|---|---:|---:|
| 0 | `aa` | ✔ | 1 | 2 |
| 2 | `ab` | ✘ | 1 | 3 |
| 3 | `bc` | ✘ | 1 | 4 |
| 4 | `ca` | ✘ | 1 | 5 |
| 5 | `aa` | ✔ | 2 | 7 |
| 7 | — | 7 > 5，停止 / stop | 2 | — |

第一个样例的匹配起点是 0、5、10，共 3 次。/ In the first example, matches start at 0, 5, and 10.

#### 输出 | Output (run twice, with the two source examples)

```text
Write a string: abcdeabcdeabcde
Write another string: abc
String 'abc' appears 3 times.
```

```text
Write a string: aaabcaa
Write another string: aa
String 'aa' appears 2 times.
```

#### 课堂提问 | Questions

❓ **Ask 1** — Why `<=` and not `<`? / 为什么是 `<=` 而不是 `<`？
**Answer** — With `<`, the last start is never checked. `aaabcaa` would give 1, and `abcabc` with `abc` would give 1 instead of 2. / 用 `<` 会漏掉最后一个起点：`aaabcaa` 得到 1，`abcabc` 中的 `abc` 也只数到 1。

❓ **Ask 2** — `aaaa` with `aa`? `abc` with `z`? / 这两组分别是多少？
**Answer** — 2 (non-overlapping); 0.

❓ **Ask 3** — How can we double-check our answer? / 怎么验证答案？
**Answer** — Python's `text.count(substring)` also counts non-overlapping matches: `"aaabcaa".count("aa")` gives 2. It is good for checking, but today we practice writing the loop ourselves. / Python 自带的 `count` 也是不重叠计数，可以用来核对，但本题目的是自己写循环。

#### ⚠️ 易错点 | Pitfalls

- 匹配后也只前进 1，得到重叠计数（`aaabcaa` 会得到 3）。/ Always moving by 1 counts overlaps.
- 条件写成 `<`，漏掉末尾的匹配。/ `<` misses a match at the very end.
- 空子串：`len(substring)` 为 0，匹配后 `index` 不前进，造成死循环。所以本题假设子串非空。/ An empty substring never advances `index`; we assume it is not empty.

---

### Exercise 6 | Greatest Common Divisor (W) — ⏱ 7 min

**考点 Focus:** 把英文算法逐句翻译成代码、`%`、循环条件中的 `or`、为什么一定会停。/ Translating an algorithm, `%`, `or`, termination.

#### 题目 | The Task

> **EN** The GCD of two positive integers is the largest number that divides both of them evenly. The source gives us the algorithm: start `d` at the smaller number; while `d` does not divide `m` or does not divide `n`, decrease `d` by 1; then report `d`. We must follow this exact algorithm.
>
> **中** 两个正整数的最大公约数，是能同时整除它们的最大整数。原题直接给出了算法：`d` 从较小的数开始；只要 `d` 不能整除 `m` **或** 不能整除 `n`，就把 `d` 减 1；最后报告 `d`。我们要严格按这个算法写。

（PDF 的项目符号没有清楚缩进；本材料把"`d` 减 1"当作循环体，"报告 `d`"放在循环之后。/ The PDF bullets are not clearly indented; we treat "decrease d" as the loop body.）

#### 解题思路 | How to Think About It

**Step 1 — 逐句翻译 / Translate sentence by sentence.**

| 原文 Source wording | Python |
|---|---|
| Initialize d to the smaller of m and n | `divisor = min(first_number, second_number)` |
| d does not evenly divide m | `first_number % divisor != 0` |
| … **or** d does not evenly divide n | `or second_number % divisor != 0` |
| Decrease d by 1 | `divisor = divisor - 1` |
| Report d | `return divisor`（循环之后 / after the loop） |

> **EN** "Evenly divides" means the remainder is zero. In Python, "`a` divided by `d` leaves no remainder" is `a % d == 0`. So "does not evenly divide" is `a % d != 0`.
>
> **中** "整除"就是余数为 0。在 Python 里，"`a` 除以 `d` 没有余数"写作 `a % d == 0`；所以"不能整除"就是 `a % d != 0`。

**Step 2 — 为什么从较小的数开始往下数 / Why start at the smaller number and count down?**

> **EN** A common divisor can't be bigger than the smaller number. For example, 31 can't divide 30. And because we count **down**, the first common divisor we meet is automatically the **greatest** one.
>
> **中** 公约数不可能比较小的那个数还大，比如 31 不可能整除 30。而且我们是**往下**数的，所以遇到的第一个公约数自然就是**最大**的。

**Step 3 — 为什么用 `or` / Why `or`?**

> **EN** The loop condition says when to **keep going**. We keep going if `d` fails for `m`, **or** fails for `n`. Failing either one is enough to reject `d`. We stop only when `d` works for both.
>
> **中** 循环条件描述的是"什么时候**继续找**"。只要 `d` 对 `m` 不行，**或者**对 `n` 不行，就要继续：任何一个不整除，`d` 就不合格。只有两个都整除时才停。

**Step 4 — 一定会停吗 / Will it always stop?**

> **EN** Yes. In the worst case, `d` reaches 1, and 1 divides every number. So the loop always stops at 1 or earlier.
>
> **中** 一定会。最坏情况下 `d` 减到 1，而 1 能整除任何数，所以循环最晚在 1 停下。

#### 代码讲解 | Code Walkthrough

```python
def greatest_common_divisor(first_number, second_number):
    divisor = min(first_number, second_number)
    while first_number % divisor != 0 or second_number % divisor != 0:
        divisor = divisor - 1
    return divisor

first_number = int(input("Enter the first positive integer: "))
second_number = int(input("Enter the second positive integer: "))
print("Greatest common divisor:", greatest_common_divisor(first_number, second_number))
```

> **EN** The source says "reads two positive integers from the user", so we ask twice and convert each answer with `int`.
>
> **中** 原题说"从用户处读取两个正整数"，所以询问两次，每次都用 `int` 转换。

#### 追踪 | Trace (84, 30) — 只列关键行 / key rows only

| `d` | `84 % d` | `30 % d` | 继续? Keep going? |
|---:|---:|---:|---|
| 30 | 24 | 0 | yes — fails 84 |
| 28 | 0 | 2 | yes — fails 30 |
| 21 | 0 | 9 | yes — fails 30 |
| 15 | 9 | 0 | yes — fails 84 |
| 14 | 0 | 2 | yes — fails 30 |
| 12 | 0 | 6 | yes — fails 30 |
| 10 | 4 | 0 | yes — fails 84 |
| 7 | 0 | 2 | yes — fails 30 |
| **6** | **0** | **0** | **no → answer 6** |

> **EN** Look at 28, 21, 14, and 7: they divide 84 but not 30. And 15 and 10 divide 30 but not 84. That is exactly why we need `or`: working for one number is not enough. In total, `d` goes from 30 down to 6, which is 24 decrements.
>
> **中** 看 28、21、14、7：它们整除 84，但不整除 30；15 和 10 整除 30，但不整除 84。这正是需要 `or` 的原因：只整除其中一个不算数。`d` 从 30 一路减到 6，一共减了 24 次。

```text
Enter the first positive integer: 84
Enter the second positive integer: 30
Greatest common divisor: 6
```

#### 课堂提问 | Questions

❓ **Ask 1** — What if we wrote `and` instead of `or`? / 把 `or` 写成 `and` 会怎样？
**Answer** — At `d = 30`: `84 % 30 != 0` is True, `30 % 30 != 0` is False. True **and** False is False, so the loop stops immediately and reports **30**, which is wrong. / 第一步就停在 30，得到错误答案。

❓ **Ask 2** — GCD of (17, 17)? (35, 64)? (12, 18)? / 这几组的答案？
**Answer** — 17 (the loop runs 0 times); 1; 6.

#### ⚠️ 易错点 | Pitfalls

- `or` 写成 `and`。/ Using `and`.
- 从较大的数开始：答案仍正确，但不是原题算法，而且多做很多步（84、30 要减 78 次）。/ Starting from the larger number still works but is not the given algorithm and takes 78 steps.
- 在循环里面 `print`，输出了很多行。/ Printing inside the loop.

---

### Exercise 7 | Predict the Output (F) — ⏱ 15 min

**考点 Focus:** 负步长、内层范围依赖外层变量、`continue` 与 `break`、`//`、反向索引、`print` 的缩进位置。

#### 通用方法 | General Method

> **EN** For every program, use the same three steps. One: write out the values the `range` produces. Two: trace the variables in a table. Three: check where `print` is. A `print` inside the loop prints many times; a `print` after the loop prints once.
>
> **中** 每个程序都用同样的三步：第一，写出 `range` 产生的所有值；第二，用表格追踪变量；第三，看 `print` 在哪里：在循环里面会打印很多次，在循环后面只打印一次。
>
> **EN** One more note: these programs use `sum` as a variable name. That hides Python's built-in `sum` function. It works here, but please don't do it in your own code.
>
> **中** 另外，这些程序把 `sum` 当变量名，会遮住 Python 自带的 `sum` 函数。这里能运行，但自己写代码时不要这样命名。

#### Program 1 — 负步长累加 / Counting Down and Adding

```python
sum = 0
for i in range(20, 2, -2):
    sum += i
print(sum)
```

> **EN** `range(20, 2, -2)` gives 20, 18, 16, 14, 12, 10, 8, 6, 4. It stops **before** 2. That's 9 numbers. Their average is 12, so the total is 9 × 12 = 108. `print` is after the loop, so we see one line.
>
> **中** `range(20, 2, -2)` 产生 20、18、16、14、12、10、8、6、4，在 2 **之前**停下，共 9 个数。平均值是 12，所以总和是 9 × 12 = 108。`print` 在循环之后，只输出一行。

```text
108
```

#### Program 2 — 内层范围依赖外层变量 / The Inner Range Depends on `i`

```python
for i in range(0, 3):
    print(i + 1, end=" ")
    for j in range(3, i, -1):
        print(j + 1, end=" ")
    print()
```

| `i` | 先打印 `i+1` | `range(3, i, -1)` | 再打印 `j+1` | 这一行 Line |
|---:|---:|---|---|---|
| 0 | 1 | 3, 2, 1 | 4 3 2 | `1 4 3 2 ` |
| 1 | 2 | 3, 2 | 4 3 | `2 4 3 ` |
| 2 | 3 | 3 | 4 | `3 4 ` |

> **EN** The inner range stops before `i`, and `i` grows, so the inner loop gets shorter every row. Every number is followed by a space because of `end=" "`, so each line ends with an invisible space. The empty `print()` ends the line.
>
> **中** 内层 `range` 在 `i` 之前停下，而 `i` 越来越大，所以内层循环每一行都变短。由于 `end=" "`，每个数字后面都跟一个空格，所以每行末尾有一个看不见的空格。空的 `print()` 负责换行。

```text
1 4 3 2 
2 4 3 
3 4 
```

（每行末尾都有一个空格。/ Each line ends with a space.）

#### Program 3 — `continue` 与 `break`

```python
sum = 0
for i in range(1, 15):
    if '4' in str(i):
        continue
    if '9' in str(i):
        break
    sum += i
    print(i, sum)
```

| `i` | 含 '4'? | 含 '9'? | 动作 Action | `sum` | 打印 Printed |
|---:|---|---|---|---:|---|
| 1 | no | no | add | 1 | `1 1` |
| 2 | no | no | add | 3 | `2 3` |
| 3 | no | no | add | 6 | `3 6` |
| 4 | **yes** | — | `continue` | 6 | — |
| 5 | no | no | add | 11 | `5 11` |
| 6 | no | no | add | 17 | `6 17` |
| 7 | no | no | add | 24 | `7 24` |
| 8 | no | no | add | 32 | `8 32` |
| 9 | no | **yes** | `break` | 32 | — |

> **EN** The `'4'` check comes first, then the `'9'` check. At 4, `continue` skips both the addition and the print. At 9, `break` ends the loop, so 10 to 14 are never checked. Note that 14 also contains a 4, but we never reach it.
>
> **中** 先检查 `'4'`，再检查 `'9'`。到 4 时 `continue` 跳过了累加和打印；到 9 时 `break` 结束整个循环，10 到 14 根本没机会检查。14 虽然也含 4，但循环走不到那里。

```text
1 1
2 3
3 6
5 11
6 17
7 24
8 32
```

❓ **Ask** — Why `'4' in str(i)` and not `i == 4`? / 为什么写 `'4' in str(i)` 而不是 `i == 4`？
**Answer** — `str(i)` turns the number into text, so we can ask whether the **digit** 4 appears anywhere, as in 14 or 24. / 转成字符串后，可以检查"数字 4 这个字符"是否出现，例如 14、24。

#### Program 4 — 整除让结果归零 / Floor Division Collapses to 0

```python
result = 1
for c in "123":
    for d in "321":
        result *= int(c)
        result //= int(d)
print(result)
```

| `c` | `d` | `result *= int(c)` | `result //= int(d)` |
|---|---|---|---|
| '1' | '3' | 1 × 1 = 1 | 1 // 3 = **0** |
| '1' | '2' | 0 × 1 = 0 | 0 // 2 = 0 |
| '1' | '1' | 0 | 0 |
| '2', '3' | … | 0 | 0 |

> **EN** `c` and `d` are characters, so `int()` turns them into numbers. The very first step already gives `1 // 3 = 0`, because `//` rounds down. Once the result is 0, multiplying keeps it 0, and 0 floor-divided by anything is 0. The inner body runs 3 × 3 = 9 times, but the answer is decided in the first step.
>
> **中** `c` 和 `d` 是字符，所以要用 `int()` 转成数字。第一步就得到 `1 // 3 = 0`，因为 `//` 向下取整。结果一旦变成 0，乘法仍是 0，0 整除任何数也是 0。内层循环体一共执行 3 × 3 = 9 次，但答案在第一步就决定了。

```text
0
```

> **EN** Fun fact: with normal division `/`, the answer would be `1.0`, because each digit is multiplied three times and divided three times. The `//` makes all the difference.
>
> **中** 小知识：如果用普通除法 `/`，结果会是 `1.0`，因为每个数字都被乘了三次、也被除了三次。差别完全来自 `//`。

#### Program 5 — 从右往左取数字 / Reading Digits from the Right

```python
s, t = "12345", 0
for i in range(1, 6):
    t += int(s[len(s) - i])
    print(t)
```

| `i` | `len(s) - i` | `s[len(s) - i]` | `t` |
|---:|---:|---|---:|
| 1 | 4 | '5' | 5 |
| 2 | 3 | '4' | 9 |
| 3 | 2 | '3' | 12 |
| 4 | 1 | '2' | 14 |
| 5 | 0 | '1' | 15 |

> **EN** `len(s) - i` walks from the last index, 4, down to the first index, 0. So we read the digits from right to left. `print(t)` is inside the loop, so we see every running total.
>
> **中** `len(s) - i` 从最后一个下标 4 走到第一个下标 0，也就是从右往左读数字。`print(t)` 在循环里面，所以每一次的累计值都会打印。

```text
5
9
12
14
15
```

❓ **Ask** — If `print(t)` is moved out of the loop, how many lines do we see? / 把 `print(t)` 移到循环外，会输出几行？
**Answer** — One line: `15`.

#### ⚠️ 易错点 | Pitfalls

- P1 把 2 也加进去，得到 110。/ Including the stop value 2.
- P2 把每行都写成 `1 2 3 4` 一类，没注意内层 `range` 的 stop 是 `i`。/ Ignoring that the inner stop is `i`.
- P3 把 `continue` 当成 `break`，或以为 9 也会被打印。/ Mixing up `continue` and `break`.
- P4 把 `//` 当成普通除法。/ Treating `//` like `/`.
- P5 以为只打印最后一个值。/ Missing that `print` is inside the loop.

---

### Exercise 8 | Patterns (F) — ⏱ 15 min

**考点 Focus:** 嵌套 `for`、找出"每行几个空格、几个符号"的公式、`chr`/`ord`、`%` 回绕、把大问题拆成小问题。

#### 通用方法 | General Method

> **EN** Each part first asks the user for the size, exactly like the source examples, for example "Enter the number of rows: 5". The drawing function then receives that number as its parameter.
>
> **中** 每个子题都先像原题样例那样让用户输入大小，例如 "Enter the number of rows: 5"，再把这个数作为参数传给画图函数。
>
> **EN** For every pattern, use three steps. One: the outer loop goes through the rows. Two: make a small table. For each row, how many spaces, and how many symbols? Find the formula. Three: the inner loops print exactly that with `end=""`, and `print()` finishes the row.
>
> **中** 画图案都用三步：第一，外层循环负责一行一行地走；第二，列一个小表格，写出每行有几个空格、几个符号，找出公式；第三，内层循环用 `end=""` 打印这些内容，最后用 `print()` 换行。

#### Part 1 — 递减星号 / Decreasing Stars (input 5)

| 行 Row | 星号数 Stars |
|---:|---:|
| 1 | 5 |
| 2 | 4 |
| 3 | 3 |
| 4 | 2 |
| 5 | 1 |

> **EN** The number of stars goes 5, 4, 3, 2, 1. Instead of computing it from the row number, the outer loop can count down the number of stars directly with `range(rows, 0, -1)`.
>
> **中** 星号数是 5、4、3、2、1。不必从行号去算，外层循环可以直接用 `range(rows, 0, -1)` 倒数星号个数。

```python
def draw_decreasing_stars(rows):
    for number_of_stars in range(rows, 0, -1):   # 5, 4, 3, 2, 1
        for _ in range(number_of_stars):         # print that many stars
            print("*", end="")
        print()                                  # end the row

rows = int(input("Enter the number of rows: "))
draw_decreasing_stars(rows)
```

> **EN** The underscore `_` is a variable name that means "I need to repeat, but I don't need the counter's value."
>
> **中** 下划线 `_` 也是变量名，意思是"我只需要重复这么多次，用不到计数器的值"。

```text
Enter the number of rows: 5
*****
****
***
**
*
```

#### Part 2 — 逐渐变宽的井号 / Widening Hashes (input 6)

| `row_index` | 中间空格数 Spaces between |
|---:|---:|
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| … | … |
| 5 | 5 |

> **EN** Every row is: one `#`, then some spaces, then one `#`. The number of spaces equals the row index, counting from 0.
>
> **中** 每一行都是：一个 `#`，若干空格，再一个 `#`。空格数等于从 0 开始的行号。

```python
def draw_widening_hashes(rows):
    for row_index in range(rows):
        print("#", end="")              # left hash, stay on this line
        for _ in range(row_index):
            print(" ", end="")          # row_index spaces
        print("#")                      # right hash, then a new line

rows = int(input("Enter the number of rows: "))
draw_widening_hashes(rows)
```

> **EN** Notice the last `print("#")` has no `end=""`. It prints the right `#` and moves to a new line in one step.
>
> **中** 注意最后的 `print("#")` 没有 `end=""`：它一步完成"打印右边的 `#`"和"换行"两件事。

```text
Enter the number of rows: 6
##
# #
#  #
#   #
#    #
#     #
```

#### Part 3 — 字母三角形 / Letter Triangle (input 8)

🖊 **Board** — 先让学生一起填表。/ Fill in this table together.

| `row_number` | 前导空格 Leading spaces = 8 − row | 字母个数 Letters = row | 字母 Letters | 字母编号 Letter indices |
|---:|---:|---:|---|---|
| 1 | 7 | 1 | A | 0 |
| 2 | 6 | 2 | B C | 1–2 |
| 3 | 5 | 3 | D E F | 3–5 |
| 4 | 4 | 4 | G H I J | 6–9 |
| 5 | 3 | 5 | K L M N O | 10–14 |
| 6 | 2 | 6 | P Q R S T U | 15–20 |
| 7 | 1 | 7 | V W X Y Z A B | 21–27 |
| 8 | 0 | 8 | C D E F G H I J | 28–35 |

> **EN** This pattern has four ideas. First, the leading spaces: `rows - row_number`. Second, row number `r` has `r` letters.
>
> **中** 这个图案有四个要点。第一，前导空格数是 `rows - row_number`；第二，第 `r` 行有 `r` 个字母。
>
> **EN** Third, and most important: the letters **continue** from one row to the next. Row 2 does not start again at A. So we need one counter, `letter_index`, created **before** the outer loop, increased after every letter, and never reset.
>
> **中** 第三点最关键：字母是**跨行连续**的，第 2 行不会从 A 重新开始。所以需要一个计数器 `letter_index`，在外层循环**之前**创建，每打印一个字母加一，永远不重置。
>
> **EN** Fourth: how do we turn a number into a letter? `ord("A")` is 65, and `chr(65)` is `"A"`. So `chr(ord("A") + k)` is the k-th letter after A. After Z, the index is 26, and we want A again. `k % 26` wraps 26 back to 0, 27 to 1, and so on.
>
> **中** 第四，怎么把编号变成字母？`ord("A")` 是 65，`chr(65)` 是 `"A"`，所以 `chr(ord("A") + k)` 就是 A 后面第 k 个字母。Z 之后编号到了 26，我们想要回到 A：`k % 26` 会把 26 变回 0、27 变回 1，依此类推。

```python
def draw_letter_triangle(rows):
    letter_index = 0                                  # shared by all rows: never reset
    for row_number in range(1, rows + 1):
        for _ in range(rows - row_number):            # leading spaces
            print(" ", end="")
        for column_index in range(row_number):        # row_number letters
            if column_index > 0:
                print(" ", end="")                    # a space BEFORE every letter except the first
            letter = chr(ord("A") + letter_index % 26)
            print(letter, end="")
            letter_index = letter_index + 1
        print()

rows = int(input("Enter the number of rows: "))
draw_letter_triangle(rows)
```

> **EN** Why print the space **before** each letter, except the first? Because then the line never ends with an extra space. The letters are separated, and the right edge stays clean.
>
> **中** 为什么空格打印在字母**前面**（第一个字母除外）？这样每行末尾不会多出空格：字母之间有分隔，右边也干净。

```text
Enter the number of rows: 8
       A
      B C
     D E F
    G H I J
   K L M N O
  P Q R S T U
 V W X Y Z A B
C D E F G H I J
```

❓ **Ask** — Where must `letter_index = 0` go? What if we put it inside the outer loop? / `letter_index = 0` 应该写在哪里？放进外层循环会怎样？
**Answer** — Before the outer loop. Inside, every row would restart at A: `A`, `A B`, `A B C`, … / 必须在外层循环之前；放进去的话每行都从 A 开始。

#### Part 4 — 重复的三角形 / Repeated Triangles (input N = 3, M = 3)

> **EN** Solve a smaller problem first: draw **one** triangle of size M. That needs two loops: one for rows and one for stars. Then repeat that whole thing N times by wrapping it in one more loop. Three loops, three jobs: triangles, rows, stars.
>
> **中** 先解决小问题：画**一个**大小为 M 的三角形，需要两层循环（行、星号）。然后把整个过程重复 N 次，再在外面套一层循环。三层循环，三个职责：三角形、行、星号。

```python
def draw_triangles(number_of_triangles, triangle_size):
    for _ in range(number_of_triangles):               # job 1: which triangle
        for row_number in range(1, triangle_size + 1): # job 2: which row
            for _ in range(row_number):                # job 3: stars in this row
                print("*", end="")
            print()

number_of_triangles = int(input("Enter the number of triangles: "))
triangle_size = int(input("Enter the size of one triangle: "))
draw_triangles(number_of_triangles, triangle_size)
```

```text
Enter the number of triangles: 3
Enter the size of one triangle: 3
*
**
***
*
**
***
*
**
***
```

（三角形之间没有空行。/ No blank line between triangles.）

#### ⚠️ 易错点 | Pitfalls

- `letter_index` 每行重置，导致每行都从 A 开始。/ Resetting the letter index every row.
- 三角形之间多打印了空行。/ Extra blank lines between triangles.
- 用 `"*" * n` 字符串乘法：实际中可以用，但本题要求用嵌套循环练习结构。/ String multiplication works in real code, but this exercise requires nested loops.
- 前导空格公式差一（写成 `rows - row_number + 1`），整个三角形向右偏一格。/ An off-by-one in the leading spaces shifts the triangle.

---

### Exercise 9 | Dice Statics (F) — ⏱ 5 min

**考点 Focus:** 用列表代替六个变量做计数器、骰面到下标的映射 `face - 1`、用总和检查结果。

（原题标题 "Dice statics" 应为 "Dice statistics"。/ The title is likely a typo for "Dice statistics".）

#### 题目 | The Task

> **EN** Roll a six-sided die 1,000 times. Count how many ones, twos, threes, fours, fives, and sixes we get, and display all six counts.
>
> **中** 掷一个六面骰子 1000 次，统计 1 到 6 各出现了多少次，并输出这六个计数。

#### 解题思路 | How to Think About It

**Step 1 — 用哪种循环 / Which loop?**

> **EN** We know the exact number of rolls, 1,000, so a `for` loop over `range(1000)` is natural.
>
> **中** 次数是确定的 1000 次，所以用 `for ... in range(1000)` 最自然。

**Step 2 — 六个计数器怎么存 / Where do six counters live?**

> **EN** The naive way is six variables and a long `if`/`elif` chain:
>
> **中** 最直接的写法是六个变量加一长串 `if`/`elif`：

```python
ones = twos = threes = fours = fives = sixes = 0
# inside the loop:
if face == 1:
    ones = ones + 1
elif face == 2:
    twos = twos + 1
# ... four more branches ...
```

> **EN** This works, but it's long and easy to get wrong. A list of six counters does the same job in one line.
>
> **中** 能用，但又长又容易出错。用一个长度为 6 的列表当计数器，一行就能完成。

**Step 3 — 骰面与下标 / Face vs. index.**

> **EN** Faces go from 1 to 6, but list indices go from 0 to 5. So face 1 goes to index 0, and face 6 goes to index 5. The rule is `face - 1`.
>
> **中** 骰面是 1 到 6，列表下标是 0 到 5。所以骰面 1 存在下标 0，骰面 6 存在下标 5，规则是 `face - 1`。

#### 代码讲解 | Code Walkthrough

```python
import random

def roll_die_counts(number_of_rolls, seed):
    randomizer = random.Random(seed)
    counts = [0, 0, 0, 0, 0, 0]                 # one counter per face, created ONCE
    for _ in range(number_of_rolls):
        face = randomizer.randint(1, 6)         # 1 and 6 are both possible
        counts[face - 1] = counts[face - 1] + 1 # face 1 -> index 0, ..., face 6 -> index 5
    return counts

counts = roll_die_counts(1000, 409)
for face in range(1, 7):                        # faces 1..6 (stop 7 is excluded)
    print(f"{face}: {counts[face - 1]}")
```

#### 输出 | Output (seed 409)

```text
1: 180
2: 145
3: 186
4: 163
5: 169
6: 157
```

> **EN** Let's check: 180 + 145 + 186 + 163 + 169 + 157 = 1,000. Whatever the seed, the six counts must always add up to 1,000. Each count is around 1,000 ÷ 6 ≈ 167, but not exactly, because the rolls are random.
>
> **中** 验证一下：180 + 145 + 186 + 163 + 169 + 157 = 1000。不管种子是多少，六个计数之和一定是 1000。每个计数大约是 1000 ÷ 6 ≈ 167，但不会正好相等，因为结果是随机的。

#### 课堂提问 | Questions

❓ **Ask 1** — Why `counts[face - 1]` and not `counts[face]`? / 为什么要减 1？
**Answer** — Face 6 would try index 6, but a 6-item list only has indices 0–5 → `IndexError`. / 骰面 6 会访问下标 6，越界。

❓ **Ask 2** — Why `range(1, 7)` when printing? / 打印时为什么是 `range(1, 7)`？
**Answer** — We want faces 1 to 6, and the stop is excluded. / 要 1 到 6，stop 不包含。

#### ⚠️ 易错点 | Pitfalls

- `counts[face]`，掷到 6 时越界。/ Off-by-one index.
- 把 `counts = [0, ...]` 写在循环里面，每次掷骰都被清零。/ Re-creating the list inside the loop resets it every roll.
- 写成 `randint(1, 7)`，以为右端不包含。/ Thinking `randint` excludes its end.

---

### Exercise 10 | Theme Park Ride Admission (W/F) — ⏱ 9 min

**考点 Focus:** 区分"检查了几人"和"上车了几人"、`continue` 跳过、满员停止、`while` 中更新语句的位置。

#### 题目 | The Task

> **EN** Ten people are waiting, but the roller coaster has only 5 seats. For each person, we ask for their height. Under 120 cm: print "Sorry, you are not tall enough." and move to the next person. Otherwise: print "Welcome aboard!" and they take a seat. When 5 people are on board, stop checking. At the end, print "The ride is full!" only if 5 people boarded, and always print the number of passengers.
>
> **中** 10 个人排队，过山车只有 5 个座位。逐个询问身高：低于 120 cm 就输出 "Sorry, you are not tall enough." 并跳到下一个人；否则输出 "Welcome aboard!" 并占一个座位。坐满 5 人就不再检查后面的人。最后，只有坐满时才输出 "The ride is full!"，乘客人数则总是输出。

#### 解题思路 | How to Think About It

**Step 1 — 两个不同的数 / Two different numbers.**

> **EN** There are two different numbers here, so don't mix them up. "How many people have we checked?" goes up for **every** person, up to 10. "How many passengers are on board?" goes up **only** for people who are tall enough, up to 5.
>
> **中** 这里有两个不同的数，千万别混：一个是"已经检查了几个人"，**每个人**都会让它加一，最多 10；另一个是"已经上车几人"，**只有**身高合格才加一，最多 5。

**Step 2 — 两个停止理由 / Two reasons to stop.**

> **EN** The loop stops when we have checked all 10 people, **or** when all 5 seats are taken, whichever happens first.
>
> **中** 循环在两种情况下停止：10 个人都检查完了，**或者** 5 个座位坐满了，以先发生的为准。

**Step 3 — 每个人做什么 / For each person.**

> **EN** "At least 120" means 120 is allowed. So we reject when `height < 120`. If rejected, print sorry and `continue`. If accepted, print welcome and add one passenger.
>
> **中** "至少 120"包含 120，所以拒绝条件是 `height < 120`。不合格：输出抱歉并 `continue`；合格：输出欢迎，乘客数加一。

**Step 4 — 循环之后 / After the loop.**

> **EN** The loop may end because the ride is full, or because we ran out of people. So we need an `if` to decide whether to print "The ride is full!". The passenger count is always printed.
>
> **中** 循环结束可能是因为坐满了，也可能是人检查完了，所以要用 `if` 判断是否输出 "The ride is full!"。乘客人数则无论如何都输出。

#### 代码讲解 | Code Walkthrough — `while` 版本

```python
def admit_passengers_while():
    passenger_count = 0
    person_number = 0
    while person_number < 10 and passenger_count < 5:
        person_number = person_number + 1        # update BEFORE any continue
        height = int(input(f"Person {person_number} - Enter height: "))
        if height < 120:
            print("Sorry, you are not tall enough.")
            continue
        print("Welcome aboard!")
        passenger_count = passenger_count + 1
    if passenger_count == 5:
        print("The ride is full!")
    print(f"{passenger_count} passengers are on board.")

admit_passengers_while()
```

> **EN** Both stop reasons are in the `while` condition: 10 people, and 5 passengers. The prompt uses the same format as the source: "Person 1 - Enter height: ". Now the key detail: `person_number` is updated at the **top** of the body, **before** the `continue`. Watch what happens if we move it to the end.
>
> **中** 两个停止理由都写在 `while` 条件里：10 个人、5 名乘客。输入提示和原题样例格式一样："Person 1 - Enter height: "。关键细节是：`person_number` 在循环体**开头**、也就是 `continue` **之前**更新。看看如果把它挪到最后会发生什么。

```python
# BUGGY: the update comes after continue
person_number = 1
while person_number <= 10 and passenger_count < 5:
    height = int(input(f"Person {person_number} - Enter height: "))
    if height < 120:
        print("Sorry, you are not tall enough.")
        continue                         # jumps straight back to the condition...
    print("Welcome aboard!")
    passenger_count = passenger_count + 1
    person_number = person_number + 1    # ...so a short person never reaches this line
```

> **EN** When a short person appears, `continue` jumps back to the condition **without** updating `person_number`. The program asks the **same** person number again and again, and short people never count toward the limit of 10. If everyone is short, the loop never ends. In a `while` loop, always update the state before any `continue`.
>
> **中** 遇到身高不够的人时，`continue` 直接跳回条件判断，`person_number` **没有更新**：程序会一遍又一遍地询问**同一个**人号，身高不够的人永远不计入 10 人的上限；如果大家都不够高，循环就永远不会结束。在 `while` 里，更新语句一定要放在 `continue` 之前。

#### 代码讲解 | Code Walkthrough — `for` 版本

```python
def admit_passengers_for():
    passenger_count = 0
    for person_number in range(1, 11):           # people 1, 2, ..., 10
        height = int(input(f"Person {person_number} - Enter height: "))
        if height < 120:
            print("Sorry, you are not tall enough.")
            continue
        print("Welcome aboard!")
        passenger_count = passenger_count + 1
        if passenger_count == 5:
            break                                # the ride is full: stop asking
    if passenger_count == 5:
        print("The ride is full!")
    print(f"{passenger_count} passengers are on board.")

admit_passengers_for()
```

> **EN** Compare the two. In the `for` version, `range(1, 11)` moves to the next person for us, so `continue` is safe. But `range` only knows about the 10 people. It doesn't know about the 5 seats, so we need an explicit `break` when the 5th passenger boards. In the `while` version, the 5-seat rule sits in the condition instead. Same rule, two ways to express it.
>
> **中** 对比一下：`for` 版本里 `range(1, 11)` 会自动走到下一个人，所以 `continue` 是安全的；但 `range` 只知道 10 个人，不知道 5 个座位，所以第 5 名乘客上车时要显式 `break`。`while` 版本则把"5 个座位"写进了循环条件。同一条规则，两种表达方式。

#### 交互演示 | Live Demo

依次输入 / Type in order: `135, 110, 121, 119, 150, 120, 140`

| 人 Person | 身高 Height | 结果 Result | 乘客数 Passengers |
|---:|---:|---|---:|
| 1 | 135 | Welcome aboard! | 1 |
| 2 | 110 | Sorry… | 1 |
| 3 | 121 | Welcome aboard! | 2 |
| 4 | 119 | Sorry… | 2 |
| 5 | 150 | Welcome aboard! | 3 |
| 6 | 120 | Welcome aboard!（恰好 120，合格 / exactly 120 boards） | 4 |
| 7 | 140 | Welcome aboard! → full, stop | 5 |
| 8–10 | — | 程序不再询问 / never asked | — |

```text
Person 1 - Enter height: 135
Welcome aboard!
Person 2 - Enter height: 110
Sorry, you are not tall enough.
Person 3 - Enter height: 121
Welcome aboard!
Person 4 - Enter height: 119
Sorry, you are not tall enough.
Person 5 - Enter height: 150
Welcome aboard!
Person 6 - Enter height: 120
Welcome aboard!
Person 7 - Enter height: 140
Welcome aboard!
The ride is full!
5 passengers are on board.
```

> **EN** Notice: after person 7, the program stops asking. That's the capacity rule in action.
>
> **中** 注意：第 7 人之后程序就不再询问了，这就是"满员停止"规则在起作用。

**边界测试 | Boundary tests** — 再运行几次，输入不同的数据。/ Run again with different input.

- 10 次都输入低于 120 的身高（如 `100`）：10 句 Sorry，最后只输出 `0 passengers are on board.`，**没有** "The ride is full!"。/ All too short: no "full" message.
- 依次输入 `100, 130, 100, 125, 100, 100, 100, 100, 100, 140`：10 人都会被询问，最后输出 `3 passengers are on board.`

#### 课堂提问 | Questions

❓ **Ask 1** — Does a person who is exactly 120 cm ride? / 恰好 120 cm 能坐吗？
**Answer** — Yes. "At least 120" includes 120, so we reject only `height < 120`. / 能。

❓ **Ask 2** — Why is "The ride is full!" inside an `if` after the loop? / 为什么满员信息要放在循环后的 `if` 里？
**Answer** — The loop can also end after checking all 10 people with fewer than 5 passengers. / 循环也可能因为 10 人都检查完而结束，此时并没有坐满。

#### ⚠️ 易错点 | Pitfalls

- 拒绝条件写成 `height <= 120`，把 120 cm 的人拒之门外。/ Rejecting exactly 120.
- `while` 版本把 `person_number` 的更新写在 `continue` 之后，人号不前进，可能永远停不下来。/ Update after `continue`.
- 检查满 5 **人**就停，而不是上车满 5 人才停。/ Stopping after 5 *people* instead of 5 *passengers*.
- 不论是否坐满都输出 "The ride is full!"。/ Always printing "full".

---

### Exercise 11 | Password Generator (F) — ⏱ 6 min

**考点 Focus:** 终止值（sentinel）0 与 `break`、`while True`、内层 `for` 循环逐位拼接字符串、为什么密码必须是字符串。

#### 题目 | The Task

> **EN** Keep asking the user for a password length. If they enter 0, the program ends. If they enter a positive number X, create a password of exactly X random digits, each from 0 to 9.
>
> **中** 反复询问用户密码长度。输入 0 时程序结束；输入正数 X 时，生成一个由 X 个随机数字（每位 0–9）组成的密码。

#### 解题思路 | How to Think About It

**Step 1 — 两层重复 / Two levels of repetition.**

> **EN** There are two kinds of repetition. We handle **many requests**, and for each request we generate **many digits**. Two levels of repetition means nested loops: the outer loop handles requests, and the inner loop handles digits.
>
> **中** 这里有两种重复：要处理**很多次请求**，每次请求又要生成**很多位数字**。两层重复就是嵌套循环：外层处理请求，内层生成数字。

**Step 2 — 外层：遇到 0 就停 / Outer loop: stop at 0.**

> **EN** 0 is a **sentinel**: a special value that means "stop". When we see 0, we use `break`, not `continue`, because we want to stop everything, not just skip one request.
>
> **中** 0 是**终止值（sentinel）**，一个表示"停止"的特殊值。遇到 0 用 `break` 而不是 `continue`，因为我们要结束整个程序，而不是只跳过这一次。

**Step 3 — 内层：一位一位地拼 / Inner loop: build it digit by digit.**

> **EN** Start with an empty string, `""`. Repeat X times: pick a random digit with `randint(0, 9)`, turn it into text with `str()`, and add it to the end of the password.
>
> **中** 从空字符串 `""` 开始，重复 X 次：用 `randint(0, 9)` 取一个随机数字，用 `str()` 转成字符，拼接到密码末尾。

**Step 4 — 为什么必须是字符串 / Why a string?**

> **EN** Two reasons. First, a password like `0427` starts with 0. As an integer, it would become 427 and lose a digit. Second, with strings, `+` joins text: `"30" + "5"` is `"305"`. With integers, `+` adds: `30 + 5` is `35`.
>
> **中** 两个原因：第一，像 `0427` 这样以 0 开头的密码，存成整数会变成 427，丢掉一位；第二，字符串的 `+` 是拼接，`"30" + "5"` 得到 `"305"`，而整数的 `+` 是相加，`30 + 5` 得到 `35`。

**关于 F 标签 | About the F label.**

> **EN** The source labels this exercise F, but we don't know in advance how many requests will come. A `for` loop needs a known range or sequence, so the outer loop is `while True`, which stops with `break` when the user enters 0. The `for` loop does the job the label asks for: building each password digit by digit.
>
> **中** 原题标注为 F，但事先不知道用户会请求几次。`for` 需要一个已知的范围或序列，所以外层用 `while True`，输入 0 时用 `break` 结束；题目要求的 `for` 循环负责逐位生成每个密码。
>
> **EN** `while True` means "repeat forever". The real stopping rule is the `break` inside the loop.
>
> **中** `while True` 的意思是"一直重复"，真正的停止规则是循环里的 `break`。

#### 代码讲解 | Code Walkthrough

```python
import random

def generate_passwords():
    while True:                                    # outer: one request per round
        password_size = int(input("Password size? > "))
        if password_size == 0:
            break                                  # sentinel: stop everything
        password = ""                              # start empty for each password
        for _ in range(password_size):             # inner: exactly X digits
            digit = random.randint(0, 9)           # 0 is allowed
            password = password + str(digit)       # join as text
        print(password)

generate_passwords()
```

#### 交互演示 | Live Demo

按原题样例依次输入 / Type the source sizes: `4, 9, 1, 0`

密码每次都随机。想得到下面的结果，先运行 `random.seed(411)`。/ Run `random.seed(411)` first to get exactly these passwords.

```text
Password size? > 4
3053
Password size? > 9
933763088
Password size? > 1
1
Password size? > 0
```

（原题中的 `9605` 等只是随机示例，不是固定答案；重点检查长度对不对。/ The source's `9605` etc. are only random examples; check the lengths.）

#### 课堂提问 | Questions

❓ **Ask 1** — For size 9, what must always be true, even though the digits are random? / 长度 9 时，虽然数字随机，但什么一定成立？
**Answer** — The password has exactly 9 characters, and every character is a digit from 0 to 9. / 恰好 9 个字符，每个都是 0–9 的数字。

❓ **Ask 2** — What if we used `continue` instead of `break` for 0? / 遇到 0 用 `continue` 会怎样？
**Answer** — It would skip 0 and ask again. Entering 0 would no longer end the program, so `while True` would never stop. / 只会跳过这一次再接着问，0 不再能结束程序，`while True` 永远停不下来。

❓ **Ask 3** — Why `randint(0, 9)` and not `randint(1, 9)`? / 为什么是 0 到 9？
**Answer** — 0 is a valid digit. `randint(1, 9)` would never produce a 0. / 0 也是数字，`randint(1, 9)` 永远不会生成 0。

#### ⚠️ 易错点 | Pitfalls

- 用整数累积密码：前导 0 丢失，而且 `+` 变成了加法。/ Building an integer instead of a string.
- `password = ""` 写在外层循环之前，导致后面的密码接在前面的后面。/ Not resetting `password` for each request.
- 遇到 0 之后仍然继续。/ Not stopping at 0.

---

## Part 3 · 总结 | Wrap-Up (3–5 min)

> **EN** Let's finish with five questions.
>
> **中** 最后用五个问题收尾。

| # | 问题 Question | 答案 Answer |
|---|---|---|
| 1 | When is `while` a natural choice? / 什么时候适合 `while`？ | When we repeat until something changes, or the step changes. / 重复到条件改变为止，或步长不固定。 |
| 2 | When is `for` a natural choice? / 什么时候适合 `for`？ | When we go through a known range or sequence. / 遍历已知范围或序列。 |
| 3 | `continue` vs. `break`? | `continue` skips this round; `break` ends the loop. / 跳过本轮 vs. 结束循环。 |
| 4 | Before writing nested loops? / 写嵌套循环前先做什么？ | Give each loop one clear job. / 给每层循环一个明确职责。 |
| 5 | How do we check a loop? / 怎么检查循环？ | State, update, stop, then trace and test a boundary. / 三要素 + 追踪 + 边界测试。 |

> **EN** Remember the three questions from the start of class: What is the state? What changes each round? Why does it stop? If you can answer them, you can write and debug any loop we saw today.
>
> **中** 记住开头的三个问题：状态是什么？每轮改变什么？为什么会停？能回答这三个问题，今天所有的循环你都能写、也能调试。

### 下课小测 | Exit Ticket（不运行代码作答 / answer without running code）

1. `range(2, 10, 3)` 产生什么？/ What does it produce? → `2, 5, 8`
2. `while` 条件永远为真会怎样？/ What if a `while` condition never becomes false? → Infinite loop / 死循环
3. `continue` 会结束循环吗？/ Does `continue` end the loop? → No, it goes to the next round / 不会，进入下一轮
4. 骰面 6 为什么用下标 5？/ Why does face 6 use index 5? → List indices start at 0 / 下标从 0 开始
5. 密码为什么存成字符串？/ Why store a password as a string? → To keep leading zeros and join digits / 保留前导 0，并做拼接

---

## 附录 A · 答案速查 | Appendix A: Answer Sheet

| # | 关键答案 Key answer |
|---:|---|
| 1 | 运行三次 / run three times: `abcdeabcdeabcde`; `abcdef`; `abcabcabcd` |
| 2 | 42.0, 63.0, 84.0, 105.0, 126.0 calories |
| 3 | Input 8 → `[0, 1, 1, 2, 3, 5, 8, 13, 21]` |
| 4 | Random each run; with `random.seed(405)` right before the game, the secret is 6, and typing 50, 25, 12, 6 wins on guess 4 (ranges 1-49, 1-24, 1-11) |
| 5 | `abc` → 3; `aa` → 2 (non-overlapping) |
| 6 | Input 84, 30 → 6 |
| 7 | P1 `108`; P2 `1 4 3 2` / `2 4 3` / `3 4`; P3 `1 1`, `2 3`, `3 6`, `5 11`, `6 17`, `7 24`, `8 32`; P4 `0`; P5 `5, 9, 12, 14, 15` |
| 8 | Inputs 5 / 6 / 8 / (3, 3) → the four patterns shown in Part 2 |
| 9 | Seed 409 → `180, 145, 186, 163, 169, 157` (sum 1000) |
| 10 | Typing 135, 110, 121, 119, 150, 120, 140 → persons 1, 3, 5, 6, 7 board; no more questions after person 7; `5 passengers are on board.` |
| 11 | Random each run; with `random.seed(411)`, sizes 4, 9, 1 → `3053`, `933763088`, `1`; then 0 stops |

## 附录 B · 原题措辞与本材料约定 | Appendix B: Source Wording and Conventions

| 位置 Where | 原文 Source | 本材料的处理 How we handle it |
|---|---|---|
| 文件名与标题 / File name | `Recitaion` | 拼写错误，源文件保持不改 / typo, source file kept as is |
| Ex 3 | "up till the n-th value" | 解释为 F₀ 到 Fₙ（含两端），共 n + 1 项 / F₀ through Fₙ inclusive |
| Ex 5 | "appears into another" | 应为 "appears in"；按样例采用不重叠、区分大小写、子串非空 / non-overlapping, case-sensitive, non-empty |
| Ex 6 | 项目符号缩进不清 / unclear bullet indentation | "d 减 1"为循环体，"报告 d"在循环后 / decrement is the loop body |
| Ex 8 | "numbers of rows" | 视为 "number of rows"；输入提示统一写作 `Enter the number of rows: ` |
| Ex 9 | "Dice statics" | 很可能是 "Dice statistics" |
| Ex 10 | `Person 1 - Enter height: 135` | 输入提示沿用原题格式 / same prompt format as the source |
| Ex 11 | 标注 F，但"反复询问直到 0"的次数未知 / labeled F, unknown number of requests | 外层 `while True` + `break`，内层 `for` 逐位生成数字 / outer `while True`, inner `for` builds digits |
| 全部输入题 / All input exercises | `input()` | 与原题一致使用 `input()`；假设输入合法，不做校验 / real `input()`, valid input assumed |
| 随机题 / Random exercises | "randomly" | 第 4、11 题每次运行都随机（演示可手动 `random.seed`）；第 9 题固定种子 409 / Ex 4 and 11 random each run; Ex 9 seed 409 |

## 附录 C · 相关文件 | Appendix C: Related Files

- 教师 notebook / Instructor notebook：[`../recitation-0405-instructor.ipynb`](../recitation-0405-instructor.ipynb)
- 学生 notebook / Student notebook：[`../recitation-0405-student.ipynb`](../recitation-0405-student.ipynb)（题面 + `TODO` 起始代码 / prompts + TODO starter code）
- 逐题中文注释解答 / Commented solutions：[`exercise-01.py`](exercise-01.py) … [`exercise-11.py`](exercise-11.py)
- 代码读法 / How to read code aloud：[`symbol-reading.md`](symbol-reading.md)
