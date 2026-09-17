# 符号与代码朗读 / Reading symbols and code aloud

中文：先说符号的名称，再说它在当前表达式中的含义。讲整行代码时，通常读“含义”更自然；逐字符听写代码时，再读符号名称。

English: Name a symbol first, then explain its meaning in the current expression. When explaining a line, reading its meaning usually sounds more natural. Use symbol names when dictating exact code.

## 本节最重要的区别 / The most important distinctions

| 写法 / Form | 符号名称 / Symbol name | 课堂读法 / What to say | 中文含义 / Chinese meaning |
|---|---|---|---|
| `!` | exclamation mark; also exclamation point | “exclamation mark” | 感叹号；程序员也可能叫它 “bang”。Python 不用单独的 `!` 表示逻辑非。 / Python does not use a standalone `!` for logical negation. |
| `!=` | exclamation mark followed by an equals sign | “is not equal to” | 不等于；把两个字符作为一个运算符理解。 / Treat the two characters as one comparison operator. |
| `not` | the keyword “not” | “not” | Python 的逻辑非。 / Python's logical negation keyword. |
| `=` | equals sign | “assign … to …” 或 / or “set … to …” | 赋值，不是判断是否相等。 / Assignment, not an equality test. |
| `==` | double equals | “is equal to” 或 / or “equals” | 比较两个值是否相等。 / Compare two values for equality. |

中文：感叹号 `!` 的常用读法是 **exclamation mark**，发音约为 /ˌek.skləˈmeɪ.ʃən mɑːrk/。但 `a != b` 整句要读 **“a is not equal to b”**，不用读成 “a exclamation mark equals b”，后者只适合逐字符听写。

English: The usual name for `!` is **exclamation mark**, pronounced approximately /ˌek.skləˈmeɪ.ʃən mɑːrk/. Read `a != b` as **“a is not equal to b.”** “A, exclamation mark, equals, b” is useful only when dictating the characters.

## 比较与逻辑 / Comparisons and logic

| 代码 / Code | 自然英文读法 / Natural English reading | 中文解释 / Chinese explanation |
|---|---|---|
| `a < b` | “a is less than b” | a 小于 b。 |
| `a > b` | “a is greater than b” | a 大于 b。 |
| `a <= b` | “a is less than or equal to b” | a 小于或等于 b，包含边界。 |
| `a >= b` | “a is greater than or equal to b” | a 大于或等于 b，包含边界。 |
| `a == b` | “a is equal to b” | a 与 b 的值相等。 |
| `a != b` | “a is not equal to b” | a 与 b 的值不相等。 |
| `A and B` | “A and B” | 两个条件都为真才为真（本节针对布尔条件）。 |
| `A or B` | “A or B” | 至少一个条件为真就为真，两个都真也为真。 |
| `not A` | “not A” | 对条件 A 取反。 |
| `True`, `False` | “true”, “false” | 布尔值；Python 中首字母大写。 |

English: `and` requires both Boolean conditions to be true. `or` requires at least one, including the case where both are true. `not` reverses a condition's truth value. Python spells its Boolean values `True` and `False` with capital initials. The descriptions here concern Boolean conditions; they are not a general claim that `and` and `or` always return Boolean values for arbitrary operands.

## 算术符号 / Arithmetic symbols

| 符号 / Symbol | 名称 / Name | 表达式读法 / Expression reading | 含义 / Meaning |
|---|---|---|---|
| `+` | plus sign | `a + b`: “a plus b” | 加法 / addition |
| `-` | minus sign | `a - b`: “a minus b”; `-3`: “negative three” | 减法或负号 / subtraction or unary minus |
| `*` | asterisk | `a * b`: “a times b” 或 / or “a multiplied by b” | 乘法 / multiplication |
| `/` | slash; forward slash | `a / b`: “a divided by b” | 普通除法 / true division |
| `//` | double slash | `a // b`: “a floor-divided by b” | 向下取整除法 / floor division |
| `%` | percent sign | `a % b`: “a modulo b” 或 / or “the remainder when a is divided by b” | 取余，不是自动计算百分比 / remainder, not automatic percentage calculation |
| `**` | double asterisk | `a ** b`: “a to the power of b” | 乘方 / exponentiation |

中文：折扣表中的 `20%` 读作 “twenty percent”，计算时写成 `0.20`。代码中的 `quantity % 2` 则表示取余；不要把这两个场景混淆。`//` 向负无穷方向取整，不能泛称为“删除小数部分”。

English: Read a discount of `20%` as “twenty percent” and represent it as `0.20` in a calculation. In code, `quantity % 2` means a remainder operation. Do not confuse the two uses of the percent symbol. Floor division rounds toward negative infinity; it is not generally the same as dropping the decimal part.

## 结构、标点与关键字 / Structure, punctuation, and keywords

| 写法 / Form | 英文名称或读法 / English name or reading | 教学提示 / Teaching note |
|---|---|---|
| `(`, `)` | open parenthesis, close parenthesis; together: parentheses | 小括号：函数调用或表达式分组。 / Used for calls or grouping. |
| `[`, `]` | open square bracket, close square bracket; together: square brackets | 方括号：本题用于字符串索引与切片。 / Used for string indexing and slicing here. |
| `\` | backslash | 反斜杠；与除法用的 `/`（forward slash）不同。 / Different from the forward slash used in division. |
| `\n` | “backslash n”; when explaining the value: “newline” | 代码中可读“backslash n”，含义是一个换行字符。 / The escape sequence represents one newline character. |
| `s[start:stop:step]` | “s sliced from start to stop, with step …” | 起点包含，终点不包含；步长决定方向。 / Start included, stop excluded; step sets direction. |
| `:` | colon | 冒号；在 `if`、`elif`、`else` 后引出代码块。 / Introduces a block after a branch header. |
| `,` | comma | 逗号；分隔函数实参，如 `print("Total:", total)`。 / Separates arguments. |
| `.` | dot; decimal point in a number | `0.20` 读 “zero point two zero”。 / Read `0.20` as “zero point two zero.” |
| `'` | single quote | 单引号，用来包住字符串。 / Delimits a string. |
| `"` | double quote | 双引号，也可包住字符串。 / Also delimits a string. |
| `#` | hash sign; number sign | 井号；开始一段注释。 / Starts a comment. |
| `_` | underscore | 下划线；`discount_rate` 可逐词读 “discount rate”，听写时说 “discount underscore rate”。 / Say “underscore” when dictating. |
| 缩进 / indentation | “indent by four spaces” | 缩进四个空格，标明哪些语句属于该分支。 / Shows which statements belong to the branch. |
| `if` | “if” | 如果；检查第一个条件。 / Tests the first condition. |
| `elif` | “else if” | 否则如果；代码实际拼写是 `elif`。 / Written as the single keyword `elif`. |
| `else` | “else”; “otherwise” | 否则；前面的条件都不满足时执行。 / Runs when earlier conditions do not match. |
| `int` | “int”; “integer” when describing the type | 整数类型。 / Integer type. |
| `float` | “float” | 浮点数类型。 / Floating-point type. |
| `str` | “string” when describing the type | 字符串类型。 / String type. |
| `input(...)` | “call input” | 读取用户输入，返回字符串。 / Reads input and returns a string. |
| `print(...)` | “print …” | 显示括号中的值。 / Displays the supplied values. |
| `len(s)` | “the length of s” | 返回字符串字符数，包括空格与换行。 / Counts characters, including spaces and newlines. |
| `repr(s)` | “the representation of s” | 让空格、换行与空字符串的结果更容易区分。 / Makes string results easier to distinguish. |
| `try`, `except` | “try”, “except” | 本次用于安全展示预期错误，不是初学分支题的核心知识。 / Used to demonstrate expected errors safely; not the main branching topic. |
| `TypeError` | “type error” | 类型不支持这个操作，如字符串与整数之间的大小比较。 / An operation is unsupported for the operand types. |
| `IndexError` | “index error” | 单个索引超出有效范围。 / A single index is out of range. |
| `$99` | “ninety-nine dollars” | 价格符号；不是 Python 变量语法。 / A currency label, not Python variable syntax. |
| `×` | multiplication sign; “times” | 原题数学公式的乘号；Python 代码中写 `*`。 / Mathematical multiplication; write `*` in Python. |
| `{`, `}` | open brace, close brace; curly braces | 在 f-string 中包住需要计算并插入文本的表达式。 / Enclose an expression to insert into an f-string. |
| `f"..."` | “f-string”; “formatted string” | 字符串前面的 f 启用格式化，不是需要输出的字母。 / The prefix enables formatting; it is not printed. |
| `{total:.2f}` | “total formatted to two decimal places” | 冒号引出格式说明，`.2f` 表示固定小数格式的两位小数；不是切片。 / The colon introduces a format specifier; this is not slicing. |

中文：金额格式也可以写成 `format(total, '.2f')`，读 “format total to two decimal places”。两种写法都是显示格式，不改变“原价减去折扣”的算法。

English: Monetary formatting can also use `format(total, '.2f')`, read as “format total to two decimal places.” Both forms control presentation without changing the subtotal-minus-discount calculation.

## 可直接跟读的完整句子 / Complete sentences to rehearse

1. `x = 5`: **“Assign five to x.”** 中文：把 5 赋给 x。
2. `x == 5`: **“Check whether x is equal to five.”** 中文：检查 x 是否等于 5。
3. `x != 5`: **“Check whether x is not equal to five.”** 中文：检查 x 是否不等于 5。
4. `x >= 10 and x <= 20`: **“x is greater than or equal to ten, and x is less than or equal to twenty.”** 中文：x 大于等于 10，并且小于等于 20。
5. `not (x < 10)`: **“Not, open parenthesis, x is less than ten, close parenthesis.”** 解释含义时说 / To explain its meaning: **“It is not true that x is less than ten.”** 中文：x 小于 10 这件事不成立。
6. `if quantity >= 10:`: **“If quantity is greater than or equal to ten, …”** 听写时补上 / When dictating, add: **“colon, new line, indent.”** 中文：如果数量大于等于 10，就执行下面的缩进代码。
7. `discount = subtotal * discount_rate`: **“Multiply subtotal by discount rate, and assign the result to discount.”** 中文：用原价总额乘以折扣率，把结果存入 discount。
8. `seconds / 60`: **“Seconds divided by sixty.”** 中文：秒数除以 60。

中文：上课时可以先让学生只读出判断结果，再请一位学生把条件用英语完整读出来。纠正读法时同时确认含义，尤其注意 `=`/`==`、`!`/`!=`/`not` 和百分号的两个用途。

English: First ask students for the truth value, then invite one student to read the condition aloud in a complete sentence. When correcting pronunciation, also check meaning, especially for `=`/`==`, `!`/`!=`/`not`, and the two uses of the percent sign.
