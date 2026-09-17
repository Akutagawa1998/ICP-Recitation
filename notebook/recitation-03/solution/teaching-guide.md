# Recitation 03 备课讲义 / Teaching guide

## 如何使用这份讲义 / How to use this guide

中文：这是一份教师用中英文对照讲义，按原题的 10 道练习顺序组织。每题先说明“为什么练”，再给出你可以直接说的英语、讲解步骤、答案和检查问题。投屏使用全英文 instructor notebook；课前用本讲义和逐行注释的 Python 文件备课。所有参考答案仅供教师使用。

English: This instructor-only bilingual guide follows the original ten exercises. Each section explains the purpose, gives classroom-ready English, and supplies teaching steps, answers, and checking questions. Project the English instructor notebook; prepare with this guide and the line-commented Python files. All solutions are for instructors only.

中文：建议采用同一个节奏：①先让学生预测；②把表达式拆开或画表；③逐步实现；④运行并解释结果；⑤用边界值检查。不要在学生预测前一次性运行整个教师 notebook。以下时间是可调整的教学建议，并非原题要求：开场 3 分钟，题 1–2 约 20 分钟，题 3–5 约 12 分钟，题 6–8 约 15 分钟，题 9–10 约 12 分钟，收尾 3 分钟，总计约 65 分钟。课时较短时可让学生先完成其中几题，余题作为延伸练习，保持原题顺序。

English: Use a consistent rhythm: predict, break down or tabulate, implement, run and explain, then check boundaries. Do not run the whole instructor notebook before students make predictions. Suggested, adjustable pacing is 3 minutes for the opening, 20 for Exercises 1–2, 12 for 3–5, 15 for 6–8, 12 for 9–10, and 3 for the wrap-up: about 65 minutes. For a shorter session, assign remaining exercises as follow-up while retaining the original order.

### 开场可以这样说 / Suggested opening

> “Today we will turn descriptions into precise conditions. Before we run a program, we will predict what it should do and explain why.”
>
> “今天我们要把文字描述变成精确的条件。运行之前，先预测程序应该做什么，并说明原因。”

中文：学生应能理解变量、数字与字符串、基本算术和 `print`。布尔运算、字符串索引/切片与分支是本次练习要巩固的内容。不要因本讲义出现了测试表，就要求初学者先学习测试框架。

English: Students should recognize variables, numbers, strings, basic arithmetic, and `print`. This session reinforces Boolean expressions, string indexing/slicing, and branching. The checking tables do not require students to learn a testing framework.

## 原题缺漏与本次约定 / Source gaps and teaching conventions

| 项目 / Item | 中文说明 | English explanation |
|---|---|---|
| 原题 / Source | 使用 `recitation/Recitaion 03.pdf`；保留题序和样例。原文件标题 `Recitaion`、表头 `Roman numer` 有拼写/缩写问题，不修改源文件。 | The original prompt, order, and sample data come from `Recitaion 03.pdf`. Source spelling is preserved; the source file is not edited. |
| 题 1 / E1 | “总是”按普通实数/整数理解，不讨论 NaN 或任意自定义对象。 | “Always” is evaluated over ordinary real/integer values, excluding NaN and arbitrary custom objects. |
| 题 2 / E2 | 原题只有赋值和两列表格。本次补充“求值并注明错误”，按每行先左后右讲解；编号是教学辅助。 | The source gives an assignment and a two-column table. We add “evaluate and note errors” and read each row left to right. Item numbering is editorial. |
| 输入 / Input | 自动执行时用可编辑变量模拟输入；原题要求的 `input` 写法见下文。 | Editable variables simulate input for automatic execution; the original interactive input form is explained below. |
| 数据范围 / Domain | 年龄、质量、尺寸默认是有效的非负数；罗马数字和轮盘编号按整数处理。 | Ages, masses, and dimensions are assumed valid and nonnegative; Roman numeral inputs and pocket numbers are integers. |
| 题 6 / E6 | 使用精确小写颜色名。两个相同的合法颜色不产生题目要求的次生色，本次提示改选两个不同颜色。 | Use exact lowercase color names. Two identical valid colors do not produce the requested secondary color; our added policy asks for two different colors. |
| 题 7 / E7 | 100–500 N（含端点）只显示重量，无额外警告。 | From 100 through 500 N inclusive, display the weight without an additional warning. |
| 题 9 / E9 | 原题在折扣表后缺少任务说明。本次明确补充：输入非负整数数量，计算原价总额、折扣金额和应付金额；不足 10 件按无折扣处理。 | The task instruction after the discount table is missing. Our explicit completion computes subtotal, discount, and total for a nonnegative integer quantity; fewer than 10 units receive no discount. |
| 题 10 / E10 | 按每条独立要求输出所有适用单位的总量，用 `/` 得到可含小数的结果。不是只输出最大单位，也不是时分秒分解；不足 60 秒不显示换算。 | Each independent requirement displays the total in its unit, using `/` and allowing fractions. This is neither largest-unit-only output nor a remainder decomposition. Below 60 seconds, no conversion is displayed. |

### 如何从演示变量恢复交互输入 / Restoring interactive input

中文：先让学生看懂“值从哪里来”，再解释类型转换。`input` 返回字符串；需要计算时用 `float` 或 `int`。下面只展示输入语句的替换方式，不在 notebook 自动执行路径中等待键盘输入。

English: Explain where a value comes from before introducing conversion. `input` returns a string; calculations may require `float` or `int`. These examples show how to replace a sample assignment without blocking the notebook's automatic execution.

```python
length1 = float(input("Length of the first rectangle: "))
age = float(input("Age in years: "))
number = int(input("Enter an integer from 1 through 10: "))
color1 = input("First primary color: ")
mass = float(input("Mass in kilograms: "))
pocket = int(input("Pocket number: "))
quantity = int(input("Number of packages: "))
seconds = float(input("Number of seconds: "))
```

> “Input gives us text. We convert that text to a number before doing arithmetic.”
>
> “输入得到的是文本。做算术之前，先把文本转换成数字。”

中文：不要说 `int(input(...))` 自动处理所有无效输入。比如输入 `hello` 或 `3.5` 会发生转换错误；本节主要练习有效类型输入之后的条件判断。年龄可以用小数；罗马数字、轮盘编号和购买数量必须为整数。

English: Do not claim that `int(input(...))` handles every invalid input. Text such as `hello` or `3.5` raises a conversion error. These exercises primarily practice decisions after input has the expected type. Age may be fractional; Roman numerals, pocket numbers, and quantities use integers.

## 1. 布尔表达式 / Boolean expressions

**目的 / Purpose.** 中文：区分布尔值、比较结果和错误；区分“这组数值下为真”与“对所有允许值都为真”。English: Distinguish Boolean values, comparison results, and errors, and separate truth for one assignment from truth for every allowed assignment.

### 第 1 小题：逐层求值 / Part 1: Evaluate in stages

1. 中文：让学生先不运行，给六个表达式写预测；允许回答“错误”，不强迫每题选 True/False。English: Ask for six predictions before running anything. Allow “error” rather than requiring every answer to be True or False.
   > “Does every comparison produce True or False, or could one of these raise an error?”
   > “每个比较都会得到 True/False 吗，还是有的会报错？”
2. 中文：先处理括号及算术/比较，再按 `not`、`and`、`or` 的优先级组合；不是简单从左到右。English: Evaluate grouping and arithmetic/comparisons, then combine using the precedence `not`, `and`, `or`, rather than blindly reading left to right.
3. 中文：先问操作数是什么类型，再判断比较是否合法。English: Identify operand types before deciding whether the comparison is valid.
4. 中文：运行后解释为什么字符串排序和数值排序不能混用。捕获异常只是为了课堂演示不中断，不是把原表达式改成了有效比较。English: After running, explain why string and numeric ordering cannot be mixed. Catching the error keeps the demonstration running; it does not make the original comparison valid.

| 原表达式 / Expression | 答案 / Answer | 中文推导 | English explanation |
|---|---|---|---|
| `False or True and False` | `False` | 先算 `True and False` 得 False，再算 `False or False`。 | `and` is evaluated before `or`, so both sides of the final `or` are False. |
| `True and not (9 < 5)` | `True` | `9 < 5` 是 False，取反后是 True。 | The comparison is False; `not` makes it True. |
| `24 / 12 >= 2 and 'hello' != 'goodbye'` | `True` | `24 / 12` 是 `2.0`，第一部分为真；两个字符串不相同，第二部分也真。 | The quotient is `2.0`, which is at least 2; the strings are unequal. |
| `55 != 'hello'` | `True` | 这两个内置类型的值不相等；不等比较合法。 | These built-in values are unequal; this inequality comparison is valid. |
| `'2' == 2` | `False` | 字符串 `'2'` 不等于整数 `2`，没有自动转成数值。 | The string is not equal to the integer; Python does not automatically convert it here. |
| `'hello' > 35` | `TypeError` | Python 3 不支持对字符串与整数这样排序。 | Python 3 does not support ordering a string against an integer this way. |

**读法 / Read aloud:** `55 != 'hello'` → “Fifty-five is not equal to the string hello.” `24 / 12 >= 2` → “Twenty-four divided by twelve is greater than or equal to two.”

中文：不要把“不同类型不能比较”作为一般结论；`2 == 2.0` 可以为真，题中的 `55 != 'hello'` 也合法。这里必须区分相等/不等比较与大小排序。

English: Avoid the blanket claim that different types cannot be compared. `2 == 2.0` can be True, and `55 != 'hello'` is valid. Equality/inequality and ordering must be distinguished.

### 第 2 小题：当前值与“总是” / Part 2: Current values versus “always”

中文：先写 `x = 10, y = 20, z = 30`。第一遍只代入；第二遍才判断是否与赋值无关。要求学生用“反例”推翻错误的 Always 判断。

English: Write `x = 10, y = 20, z = 30`. First substitute; only then ask whether the result is independent of the assignment. Use counterexamples to disprove incorrect “Always” claims.

| 表达式 / Expression | 当前答案 / Current answer | 中文理由及 Always 判断 | English explanation and Always status |
|---|---|---|---|
| `(x == 10) and (y > 10)` | `True` | 两边都真；但若 x=9 就为假，因此不是 Always True。 | Both sides are True, but x=9 makes it False, so it is not always True. |
| `x < 10 and x > 10` | `Always False` | 同一个普通实数不可能同时小于和大于 10。 | One ordinary real number cannot be both below and above 10. |
| `(x < 10) or (x > 10)` | `False` | x 恰好等于 10；若 x=9 则为真，所以也不是 Always False。 | x equals 10. For x=9 it becomes True, so it is not always False. |
| `not (x < (y + z)) or not ((x + 10) <= 20)` | `False` | `not (10 < 50)` 为假，`not (20 <= 20)` 为假。若 x=30,y=0,z=0，可变为真。 | Both negated comparisons are False. Changing to x=30,y=0,z=0 makes the result True. |
| `not (x == y) and (x != y) and (x < y or y < x)` | `True` | 当前三部分都真；若 x=y=10，前两部分为假，因此不是 Always True。 | All three components are True here. If x=y=10, the expression becomes False. |

> “One successful example cannot prove that a statement is always true. Can you find a counterexample?”
>
> “一个为真的例子不能证明总是为真。你能找一个反例吗？”

**检查问题 / Check:** 中文：`x < 10 or x > 10` 为什么不包含所有数？答案：漏掉 x=10。English: Why does the expression not cover every number? It excludes x=10.

## 2. 字符串索引与切片 / String indexing and slicing

**目的 / Purpose.** 中文：精确跟踪字符、空格、换行、索引和切片边界。English: Track characters, spaces, the newline, indices, and slice boundaries precisely.

原字符串 / Original string: `s = 'HellO WorlD\n'`。中文：大写 O、大写 W、大写 D 必须保留。English: Preserve the capital O, W, and D.

| 正索引 / Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 字符 / Character | H | e | l | l | O | 空格 / space | W | o | r | l | D | `\n` |
| 负索引 / Negative index | -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

1. 中文：先让学生数长度；提醒 `\n` 在字符串值中是一个换行字符，而不是两个字符。外面的引号不属于字符串内容。English: Count the length first. `\n` represents one newline character in the value, not two characters, and the delimiters are not part of the content.
2. 中文：先只做单个索引，解释负索引从末尾数。有效范围是 -12 到 11。English: Start with single indexing and count negative indices from the end. Valid indices run from -12 through 11.
3. 中文：切片读成 `start:stop:step`；起点可包含，终点不包含。先检查步长方向，再列实际访问的索引。English: Read a slice as start, stop, step. Include the start and exclude the stop. Check the step direction, then list the visited indices.
4. 中文：用 `repr` 显示结果，区分空字符串 `''`、空格 `' '` 和换行 `'\n'`。English: Use `repr` to distinguish an empty string, one space, and a newline.

> “The stop index is excluded. Tell me which indices are visited before you tell me the characters.”
>
> “结束索引不包含在内。先告诉我访问哪些索引，再告诉我取到哪些字符。”

下表按原表逐行从左到右排列。/ This table follows the original table row by row, left to right.

| # | 表达式 / Expression | 结果 / Result shown with `repr` for strings | 中文解释 | English explanation |
|---|---|---|---|---|
| 1 | `s[-1]` | `'\n'` | 最后一个字符是换行。 | The last character is a newline. |
| 2 | `s[5:6]` | `' '` | 只取索引 5 的空格。 | Only index 5 is selected. |
| 3 | `s[-2]` | `'D'` | 倒数第二个字符。 | The second-to-last character. |
| 4 | `s[6:5]` | `''` | 默认向前，无法从 6 走到 5 之前。 | With a positive step, the slice selects no indices. |
| 5 | `len(s)` | `12` | 包含空格和换行。 | Counts the space and newline. |
| 6 | `s[-6:-1]` | `'WorlD'` | 取索引 6–10，不取最后的换行。 | Selects indices 6 through 10, excluding the newline. |
| 7 | `s[-len(s)]` | `'H'` | `-len(s)` 是 -12，对应索引 0。 | -12 identifies the first character. |
| 8 | `s[:5:2]` | `'HlO'` | 依次取 0、2、4。 | Visits indices 0, 2, and 4. |
| 9 | `s[-13]` | `IndexError` | 比最小合法负索引 -12 更小。 | -13 is outside the valid index range. |
| 10 | `s[5::-1]` | `' OlleH'` | 从空格开始，依次取 5、4、3、2、1、0；开头空格要保留。 | Visits 5 down through 0; retain the leading space. |
| 11 | `s[:5]` | `'HellO'` | 取 0–4。 | Selects indices 0 through 4. |
| 12 | `s[-2:-7:-1]` | `'DlroW'` | 依次取 10、9、8、7、6；不取 -7 对应的空格。 | Visits 10 down through 6; the space at -7 is excluded. |
| 13 | `s[6:500]` | `'WorlD\n'` | 切片终点过大时在字符串末尾截断，不报错。 | An oversized slice stop is clipped to the end. |
| 14 | `s[:7] + s[7:]` | `'HellO WorlD\n'` | 两段在索引 7 处衔接，没有重复或漏字。 | The two slices meet at 7 and reconstruct the string. |
| 15 | `s[7:]` | `'orlD\n'` | 从小写 o 开始到末尾。 | Starts at the lowercase o and continues to the end. |

**重点 / Key point.** 中文：单个索引越界会报错，但越界切片通常会裁剪；空切片不等于异常。负步长下，省略终点和显式写 `-1` 也不是同一回事，例如 `s[5::-1]` 可以走到索引 0。English: An invalid single index raises an error, whereas slicing clips bounds. An empty slice is not an exception. With a negative step, omitting the stop is also different from explicitly using -1; `s[5::-1]` reaches index 0.

**读法 / Read aloud:** `s[-2]` → “s at index negative two”; `s[5:6]` → “s sliced from five up to, but not including, six”; `s[5::-1]` → “s from index five backward to the beginning, with a step of negative one.”

**检查问题 / Check:** 中文：`s[500]` 与 `s[6:500]` 为什么不同？答案：前者必须取到一个字符，后者只是界定一个可裁剪的范围。English: Why do these differ? A single index must identify an existing character; slice bounds define a range that can be clipped.

## 3. 比较两个长方形 / Areas of rectangles

**目的 / Purpose.** 中文：把“先计算，再比较”转成程序，并完整覆盖大于、小于、相等三种结果。English: Compute first, compare second, and cover all three outcomes.

1. 中文：问学生需要哪些输入，写出两组长和宽，并约定同一单位。English: Identify four inputs and assume consistent length units.
   > “What should we compare: the lengths, or the areas?”
   > “应该比较长度，还是面积？”
2. 中文：分别写 `area1 = length1 * width1` 和 `area2 = length2 * width2`，强调中间变量有助于检查。English: Compute each area in a named variable so the calculation is easy to inspect.
3. 中文：先判断 area1 大，再判断 area2 大，剩下就是相等。English: Test whether the first area is greater, then whether the second is greater; otherwise they are equal.
4. 中文：运行默认样例：5×4 和 4×5 都是 20；尺寸顺序不同不代表面积不同。English: Run the default example: both areas equal 20 despite the different dimensions.

**样例答案 / Sample answer:** `Both rectangles have the same area.`

| 输入 / Dimensions | 预期 / Expected outcome |
|---|---|
| (5,4), (4,5) | 面积相等 / Equal areas |
| (6,4), (4,5) | 第一个更大 / First is larger |
| (3,4), (4,5) | 第二个更大 / Second is larger |

**重点 / Focus.** 中文：不要只比较长，不要遗漏相等分支；使用 `if/elif/else` 体现三种结果互斥。English: Compare areas, retain equality, and use an exclusive branch chain.

**检查问题 / Check:** “If the first rectangle is longer, must its area be larger?” / “第一个更长，面积就一定更大吗？” 答案 / Answer: No; width also matters. / 不一定，还要看宽度。

### 完整参考代码 / Complete reference code

```python
length1 = 5.0
width1 = 4.0
length2 = 4.0
width2 = 5.0
area1 = length1 * width1
area2 = length2 * width2
if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both rectangles have the same area.")

```

逐行中英文解释 / Line-by-line bilingual explanations: [exercise-03.py](exercise-03.py)

## 4. 年龄分类 / Age classifier

**目的 / Purpose.** 中文：把中文/英文中的“至多、超过、不到、至少”转换成包含端点或不包含端点的条件。English: Translate “at most,” “older than,” “less than,” and “at least” into precise boundaries.

1. 中文：画数轴，标 1、13、20；先不要写代码。English: Draw a number line and mark 1, 13, and 20 before coding.
2. 中文：按顺序写 `age <= 1`、`age < 13`、`age < 20`、`else`。后面的分支不必重复前面已经排除的下界。English: Use ordered tests `age <= 1`, `age < 13`, `age < 20`, then `else`; earlier failures already establish lower bounds.
   > “When we reach this elif, what do we already know about the age?”
   > “执行到这个 elif 时，我们已经知道年龄满足什么条件？”
3. 中文：用边界值验证，不只用 8、16 这样的中间值。English: Test category boundaries, not only comfortable interior values.
4. 中文：默认 age=20，应输出 Adult，而不是 Teenager。English: With the default age of 20, the output is Adult, not Teenager.

| 年龄 / Age | 分类 / Category |
|---|---|
| 0, 1 | Infant / 婴儿 |
| 1.5, 12 | Child / 儿童 |
| 13, 19 | Teenager / 青少年 |
| 20, 21 | Adult / 成年人 |

**重点 / Focus.** 中文：四个独立 `if` 加最后一个 `else` 很容易产生多个输出或错误绑定。我们要的是一次只选一个类别。English: Separate `if` statements can produce multiple outputs or an incorrectly associated `else`. Choose exactly one category.

**检查问题 / Check:** “Why does age 13 not enter the child branch?” / “13 岁为什么不进入儿童分支？” 答案 / Answer: Because the child condition is strictly below 13. / 因为必须严格小于 13。

### 完整参考代码 / Complete reference code

```python
age = 20
if age <= 1:
    print("Infant")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

```

逐行中英文解释 / Line-by-line bilingual explanations: [exercise-04.py](exercise-04.py)

## 5. 罗马数字 / Roman numerals

**目的 / Purpose.** 中文：练习多个离散值的分支选择，以及覆盖范围外输入的错误分支。English: Practice selecting among discrete values and handling values outside the allowed range.

1. 中文：先阅读完整映射，不让学生误以为只是重复输出 I。English: Read the complete mapping; it is not simply a repeated sequence of I characters.
2. 中文：按 `number == 1` 到 `number == 10` 写分支，先掌握结构，不必引入字典查表。English: Use branches for values 1 through 10; a dictionary is unnecessary for this exercise's decision-structure goal.
3. 中文：最后用 `else` 处理不在 1–10 的整数。English: Use a final `else` for integers outside 1 through 10.
4. 中文：重点读 IV 和 IX，再运行默认 number=7，得到 VII。English: Highlight IV and IX, then run the default number 7 to obtain VII.

| 数值 / Value | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 罗马数字 / Roman numeral | I | II | III | IV | V | VI | VII | VIII | IX | X |

**读法 / Read aloud.** 中文：解释数值时，IV 可以说 “Roman numeral four”；逐字符听写时说 “capital I, capital V”。English: Say “Roman numeral four” when discussing the value of IV, and “capital I, capital V” when dictating its characters.

**边界 / Boundaries:** 0 → error；1 → I；10 → X；11 → error。

**检查问题 / Check:** “Why is `number == 4` a comparison, while `number = 4` is not?” / “为什么 `==` 是比较，而 `=` 不是？” 答案 / Answer: `=` assigns a value; `==` tests equality. / 前者赋值，后者判断相等。

### 完整参考代码 / Complete reference code

```python
number = 7
if number == 1:
    print("I")
elif number == 2:
    print("II")
elif number == 3:
    print("III")
elif number == 4:
    print("IV")
elif number == 5:
    print("V")
elif number == 6:
    print("VI")
elif number == 7:
    print("VII")
elif number == 8:
    print("VIII")
elif number == 9:
    print("IX")
elif number == 10:
    print("X")
else:
    print("Error: enter an integer from 1 to 10.")

```

逐行中英文解释 / Line-by-line bilingual explanations: [exercise-05.py](exercise-05.py)

## 6. 颜色混合 / Color mixer

**目的 / Purpose.** 中文：先验证输入，再匹配组合，并确保颜色顺序不影响结果。English: Validate inputs, match combinations, and make the result independent of input order.

1. 中文：在板上列合法值 red、blue、yellow，强调这是原题指定的颜料颜色模型。English: List red, blue, and yellow as the allowed inputs in the source's classroom color model.
2. 中文：先检查两个输入是否都合法，再处理重复颜色的新增约定。English: Check both inputs for validity, then apply the disclosed policy for duplicate colors.
3. 中文：对每种混合考虑两个顺序，例如 red/blue 与 blue/red。每个顺序内部用 `and`，两个顺序之间用 `or`。English: Include both orders for each mixture, joining each pair with `and` and the alternative orders with `or`.
   > “Mixing red with blue should give the same result as mixing blue with red. Where does our condition express that?”
   > “红加蓝与蓝加红结果应相同。我们的条件在哪里体现这一点？”
4. 中文：运行 red/blue 得 Purple，再反转次序验证，不要只测一个方向。English: Run red/blue for Purple, then reverse the order to verify symmetry.

| 输入 / Inputs | 结果 / Result |
|---|---|
| red + blue；blue + red | Purple / 紫色 |
| red + yellow；yellow + red | Orange / 橙色 |
| blue + yellow；yellow + blue | Green / 绿色 |
| red + red | 提示选择不同颜色（本次约定） / Ask for distinct colors (our convention) |
| red + green | 非法输入 / Invalid input |
| Red + blue | 本次精确小写规则下非法 / Invalid under the exact-lowercase convention |

**重点 / Focus.** 中文：不要写 `color1 == 'red' or 'blue'`；第二部分不是对 color1 的比较。也不要把两个合法的相同颜色描述为“输入了不存在的颜色”。English: Do not write `color1 == 'red' or 'blue'`; the second operand is not a comparison of color1. Do not mislabel identical valid colors as nonexistent colors.

**检查问题 / Check:** “How many ordered pairs of distinct primary colors should succeed?” / “不同原色的有序输入对有多少种应该成功？” 答案 / Answer: Six. / 六种。

### 完整参考代码 / Complete reference code

```python
color1 = "red"
color2 = "blue"
if color1 != "red" and color1 != "blue" and color1 != "yellow":
    print("Error: use red, blue, or yellow.")
elif color2 != "red" and color2 != "blue" and color2 != "yellow":
    print("Error: use red, blue, or yellow.")
elif color1 == color2:
    print("Error: choose two different primary colors.")
elif (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("Purple")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("Orange")
else:
    print("Green")

```

逐行中英文解释 / Line-by-line bilingual explanations: [exercise-06.py](exercise-06.py)

## 7. 质量与重量 / Mass and weight

**目的 / Purpose.** 中文：区分输入的质量和需要判断的重量；练习严格大于/小于阈值。English: Distinguish mass from weight and apply strict threshold comparisons.

1. 中文：先问单位：mass 是 kg，weight 是 N。English: Establish that mass is in kilograms and weight is in newtons.
2. 中文：写出 `weight = mass * 9.8`，再比较 weight，不是直接拿 mass 与 500 比较。English: Calculate weight first; compare weight, not mass, against the stated thresholds.
3. 中文：`weight > 500` 是太重，`weight < 100` 是太轻；刚好 100 或 500 都不触发警告。English: Above 500 is too heavy; below 100 is too light. Exactly 100 or 500 triggers neither warning.
4. 中文：默认 mass=60.0，重量为 588.0 N，显示 Too heavy。English: The default mass gives 588.0 N and the warning Too heavy.

```text
Weight: 588.0 newtons
Too heavy.
```

| 测试 / Test | 预期 / Expected |
|---|---|
| mass=5 → weight=49 N | Too light / 太轻 |
| mass=20 → weight=196 N | 只显示重量 / Display the weight only |
| mass=60 → weight=588 N | Too heavy / 太重 |
| 手算判断 / Direct condition check: weight=100,500 | 都无警告 / Neither boundary triggers a warning |

中文：可以把 100 和 500 直接代入“条件”讲端点，再用 5、20、60 kg 验证整个程序。不要为了构造端点而把浮点近似问题当成本题重点。

English: Substitute 100 and 500 directly into the conditions to discuss boundaries, then use masses 5, 20, and 60 to check the full program. Floating-point approximation need not become the focus of this exercise.

**检查问题 / Check:** “Does 500 newtons count as too heavy?” / “500 N 算太重吗？” 答案 / Answer: No: the requirement says more than 500. / 不算，因为原题要求超过 500。

### 完整参考代码 / Complete reference code

```python
mass = 60.0
weight = mass * 9.8
print("Weight:", weight, "newtons")
if weight > 500:
    print("Too heavy.")
if weight < 100:
    print("Too light.")

```

逐行中英文解释 / Line-by-line bilingual explanations: [exercise-07.py](exercise-07.py)

## 8. 轮盘颜色 / Roulette wheel colors

**目的 / Purpose.** 中文：把较长规则拆成“合法范围 → 特殊值 → 所在区间 → 奇偶性”。English: Decompose the rules into validity, the special case, interval selection, and parity.

1. 中文：先检查 0–36 范围。范围外先报错，避免无效编号进入颜色计算。English: Reject values outside 0 through 36 before selecting a color.
2. 中文：单独处理 0 为 Green；不是所有偶数都是 Black。English: Handle zero as Green; not every even number is Black.
3. 中文：保留四段规则，先找区间，再用 `pocket % 2` 判断奇偶。English: Identify one of the four intervals, then use the remainder after division by 2 to determine parity.
4. 中文：把区间边界放在一起测试，展示为什么“所有奇数都是红色”是错的。English: Test adjacent interval boundaries to disprove the shortcut that all odd pockets are red.

| 范围 / Range | 奇数 / Odd | 偶数 / Even |
|---|---|---|
| 1–10 | Red / 红 | Black / 黑 |
| 11–18 | Black / 黑 | Red / 红 |
| 19–28 | Red / 红 | Black / 黑 |
| 29–36 | Black / 黑 | Red / 红 |

**读法 / Read aloud:** `pocket % 2 == 0` → “The remainder when pocket is divided by two is equal to zero.” 中文：编号除以 2 的余数等于 0，所以是偶数。English: A zero remainder indicates an even number.

| 编号 / Pocket | -1 | 0 | 1 | 10 | 11 | 18 | 19 | 28 | 29 | 36 | 37 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 结果 / Result | Error | Green | Red | Black | Black | Red | Red | Black | Black | Red | Error |

**默认答案 / Default answer:** pocket=18 → `Red`。

**检查问题 / Check:** “Why do both 10 and 11 have the same color even though their parity is different?” / “为什么 10 和 11 奇偶不同，却都是黑色？” 答案 / Answer: The odd/even color rule reverses at the interval boundary. / 因为跨过边界后奇偶对应颜色发生反转。

### 完整参考代码 / Complete reference code

```python
pocket = 18
if pocket < 0 or pocket > 36:
    print("Error: enter an integer from 0 to 36.")
elif pocket == 0:
    print("Green")
elif pocket <= 10:
    if pocket % 2 == 1:
        print("Red")
    else:
        print("Black")
elif pocket <= 18:
    if pocket % 2 == 1:
        print("Black")
    else:
        print("Red")
elif pocket <= 28:
    if pocket % 2 == 1:
        print("Red")
    else:
        print("Black")
else:
    if pocket % 2 == 1:
        print("Black")
    else:
        print("Red")

```

逐行中英文解释 / Line-by-line bilingual explanations: [exercise-08.py](exercise-08.py)

## 9. 软件销售 / Software sales

**目的 / Purpose.** 中文：把阶梯折扣表转成条件，并区分折扣率、折扣金额和应付金额。English: Translate discount tiers into branches and distinguish the rate, discount amount, and final amount due.

中文：先明确告诉学生：原题没有给出表格后的完整任务。本次补充为“计算原价总额、折扣金额和最终应付金额”，并把不足 10 件视为没有折扣。这里采用达到某档后全部商品应用同一折扣率的约定，不是分段累进计价。

English: State the source omission first. We complete the task by computing the subtotal, discount amount, and final total, with no discount below ten packages. The selected tier applies to the entire purchase; this is not progressive pricing across separate quantity bands.

1. 中文：把单位价格固定为 99，数量与金额分开命名。English: Set the unit price to 99 and distinguish quantity variables from monetary amounts.
2. 中文：本解答按上界从小到大判断 `< 10`、`< 20`、`< 50`、`< 100`，最后是 `else`。走到后面的分支时，较小数量已被排除。也可以改用从大到小的 `>=` 判断，但不要从 `quantity >= 10` 开始，否则 100 件会提前进入最低折扣档。English: This solution checks ascending upper bounds: `< 10`, `< 20`, `< 50`, `< 100`, then `else`. Earlier branches exclude smaller quantities. Descending `>=` tests are another valid approach, but starting with `quantity >= 10` would catch a purchase of 100 too early.
3. 中文：依次计算 `subtotal = quantity * unit_price`、`discount = subtotal * discount_rate`、`total = subtotal - discount`。English: Calculate the subtotal from quantity and unit price, multiply it by the rate for the discount, then subtract the discount for the total.
4. 中文：默认 25 件，原价 2475，20% 折扣是 495，应付 1980。English: For 25 packages, the subtotal is 2475, the 20% discount is 495, and the total is 1980.

> “A twenty-percent discount means we subtract twenty percent, not that the customer pays twenty percent.”
>
> “打掉 20% 是减去 20%，不是只支付 20%。”

| 数量 / Quantity | 折扣率 / Rate | 折扣金额 / Discount | 应付 / Total |
|---|---|---|---|
| 0 | 0% | 0.00 | 0.00 |
| 9 | 0% | 0.00 | 891.00 |
| 10 | 10% | 99.00 | 891.00 |
| 19 | 10% | 188.10 | 1692.90 |
| 20 | 20% | 396.00 | 1584.00 |
| 25 | 20% | 495.00 | 1980.00 |
| 49 | 20% | 970.20 | 3880.80 |
| 50 | 30% | 1485.00 | 3465.00 |
| 99 | 30% | 2940.30 | 6860.70 |
| 100 | 40% | 3960.00 | 5940.00 |

中文：某些跨档购买数量更多、最终价格反而更低，是这张整单折扣表的结果，不要偷偷改成其他商业规则。金额显示保留两位小数只是显示格式，并不等于解决了所有真实财务精度问题；本题重点是分支和百分比。

English: At some tier boundaries, buying more can cost less under this whole-order discount table. Do not silently replace it with another pricing rule. Two decimal places control the display; they do not solve every real-world financial precision issue. Branching and percentages are the focus here.

**检查问题 / Check:** “Why does quantity 100 reach the final else in this solution?” / “为什么数量 100 在本解答中会进入最后的 else？” 答案 / Answer: It fails all four strict upper-bound tests, including `< 100`. / 它不满足前面四个严格小于条件，包括 `< 100`。

### 完整参考代码 / Complete reference code

```python
quantity = 25
unit_price = 99
if quantity < 10:
    discount_rate = 0.0
elif quantity < 20:
    discount_rate = 0.10
elif quantity < 50:
    discount_rate = 0.20
elif quantity < 100:
    discount_rate = 0.30
else:
    discount_rate = 0.40
subtotal = quantity * unit_price
discount = subtotal * discount_rate
total = subtotal - discount
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Total: ${total:.2f}")

```

逐行中英文解释 / Line-by-line bilingual explanations: [exercise-09.py](exercise-09.py)

## 10. 时间换算 / Time calculator

**目的 / Purpose.** 中文：识别多个要求可以同时成立的情形，正确选择独立 `if`。English: Recognize when several requirements apply at once and use independent `if` statements.

1. 中文：把三个条件并列写出：秒数至少 60、至少 3600、至少 86400。问学生 90061 满足几个。English: Write the three thresholds side by side and ask how many are satisfied by 90061.
2. 中文：解释每个结果都是“这全部秒数等于多少分钟/小时/天”。不是先减去整天，再求剩余小时。English: Each result converts the entire input into a unit; it does not subtract whole days and then convert a remainder.
3. 中文：分别用 `seconds / 60`、`seconds / 3600`、`seconds / 86400`，条件之间用独立 `if`，不要改成 `elif`。English: Divide by each unit size under its own `if`, rather than an exclusive `elif` chain.
4. 中文：运行 90061，观察三行都输出；再试 59 和 60，讲清“至少”包含边界。English: Run 90061 to see all three lines, then try 59 and 60 to establish the inclusive boundary.

> “Can more than one requirement be true at the same time? If yes, an elif chain may skip required output.”
>
> “多个要求能同时成立吗？如果能，elif 链可能跳过本来应该输出的内容。”

**默认输出 / Default output:**

```text
Minutes: 1501.0166666666667
Hours: 25.016944444444444
Days: 1.042372685185185
```

| 秒数 / Seconds | 应输出的换算 / Required conversions under our convention |
|---|---|
| 0, 59 | 无换算 / No conversion |
| 60 | Minutes: 1.0 |
| 3599 | 只输出分钟 / Minutes only |
| 3600 | Minutes: 60.0；Hours: 1.0 |
| 86399 | 分钟和小时 / Minutes and hours |
| 86400 | Minutes: 1440.0；Hours: 24.0；Days: 1.0 |
| 90061 | 三种总量，见上方 / All three totals, as above |

**重点 / Focus.** 中文：若使用 `//` 和 `%` 得到 1 天 1 小时 1 分 1 秒，那是在解决另一种“分解时间”任务；本次不采用。小数只是总量换算的结果，不是错误。English: Producing 1 day, 1 hour, 1 minute, and 1 second with `//` and `%` solves a different decomposition task. Fractional totals are expected under our chosen interpretation.

**检查问题 / Check:** “How many conversion lines should 3600 seconds produce here?” / “这里 3600 秒应该输出几行换算？” 答案 / Answer: Two: minutes and hours. / 两行：分钟和小时。

### 完整参考代码 / Complete reference code

```python
seconds = 90061
if seconds >= 60:
    minutes = seconds / 60
    print("Minutes:", minutes)
if seconds >= 3600:
    hours = seconds / 3600
    print("Hours:", hours)
if seconds >= 86400:
    days = seconds / 86400
    print("Days:", days)

```

逐行中英文解释 / Line-by-line bilingual explanations: [exercise-10.py](exercise-10.py)

## 收尾与快速诊断 / Wrap-up and quick diagnosis

| 可直接提问的英语 / Ask in English | 中文与参考答案 / Chinese and expected answer |
|---|---|
| “What is the difference between equals and double equals?” | `=` 是赋值，`==` 是相等比较。 / Assignment versus equality testing. |
| “What do we call the exclamation mark in this operator, and how do we read the whole operator?” | `!` 叫 exclamation mark，`!=` 整体读 is not equal to。 |
| “Why can an empty slice be valid?” | 指定方向没有可访问的索引时，返回空字符串，不必报错。 / The range can legitimately select no characters. |
| “When should we choose an elif chain?” | 互斥结果，只选择一个分支时。 / When outcomes are mutually exclusive. |
| “When should we use separate if statements?” | 多条要求可以同时满足且都需要执行时。 / When several applicable requirements must all run. |
| “Which values should we test near a threshold?” | 边界前、边界本身、边界后。 / Just below, at, and just above it. |

中文：若学生答案错，先问“你走到了哪一个分支？”再问“这个条件在当前输入下是什么值？”这能区分是读错了规则、算错了值，还是写错了代码。符号读法详见 [symbol-reading.md](symbol-reading.md)。

English: When a student is wrong, first ask which branch was reached, then ask for that condition's value on the current input. This distinguishes specification, calculation, and coding mistakes. See [symbol-reading.md](symbol-reading.md) for pronunciation support.
