# 循环与代码读法 / Loop and code reading

中文：先读符号或关键字的自然含义，再解释它怎样改变循环状态。逐字符听写时才强调括号、冒号和逗号。

English: Read the natural meaning first, then explain how it changes loop state. Name punctuation explicitly only when dictating code.

| 写法 | 自然英文读法 | 中文含义与教学提示 |
|---|---|---|
| `while condition:` | “while condition is true” | 条件为真时重复；冒号后换行并缩进。 |
| `for item in sequence:` | “for each item in sequence” | 依次取序列中的元素。 |
| `range(10, 31, 5)` | “range from ten up to, but not including, thirty-one, by fives” | 从 10 开始，每次加 5，stop 31 不包含。 |
| `range(20, 2, -2)` | “range from twenty down toward two, by negative two” | 20、18…4；2 不包含。 |
| `break` | “break out of the loop” | 立即结束最近一层循环。 |
| `continue` | “continue with the next iteration” | 跳过本轮剩余语句，进入下一轮。 |
| `i += 1` | “add one to i” | 等价于 `i = i + 1`；常用于更新循环状态。 |
| `result //= value` | “floor-divide result by value and assign it back” | 向下取整除法后写回变量。 |
| `number % divisor` | “number modulo divisor” | 余数；余数 0 表示整除。 |
| `text[start:stop]` | “text sliced from start up to stop” | start 包含，stop 不包含。 |
| `text[index]` | “the character at index” | 字符串索引从 0 开始。 |
| `len(text)` | “the length of text” | 字符数；可作为循环边界。 |
| `print(value, end="")` | “print value with an empty ending” | 不自动换行，便于同一行画图案。 |
| `print()` | “print a blank line break” | 不给参数时只换行。 |
| `input("Enter n: ")` | “input with the prompt Enter n” | 显示提示并等待用户输入；返回值永远是字符串。 |
| `int(input(...))` | “convert the input to an integer” | 先读取字符串，再用 `int` 转成整数，才能比较大小或做算术。 |
| `random.Random(409)` | “create a local random generator with seed four-oh-nine” | 固定种子让演示可复现，不影响全局随机状态。 |
| `randint(1, 6)` | “a random integer from one through six” | 两端都包含。 |
| `counts[face - 1]` | “the count at index face minus one” | 将骰面 1–6 映射到列表索引 0–5。 |
| `return value` | “return value” | 结束函数并把结果交给调用处。 |
| `def name(...):` | “define the function name” | 定义可重复调用的步骤；函数体缩进。 |
| `f"{value}"` | “an f-string containing value” | 花括号中的表达式先计算再插入。 |
| `min(a, b)` / `max(a, b)` | “the minimum/maximum of a and b” | 选择较小/较大值；猜数题用来收紧范围。 |

## 嵌套循环 / Nested loops

```python
for row in range(3):
    for column in range(2):
        print(row, column)
```

自然读法：**“For each row, go through each column and print the pair.”** 中文：每一个外层 row 都会完整执行一次内层 column 循环，因此总共执行 `3 * 2 = 6` 次打印。

## 条件循环的三问 / Three questions for a while loop

1. **Initial state:** “What is true before the first check?” / 第一次检查前状态是什么？
2. **Update:** “What changes during one iteration?” / 每轮什么值发生变化？
3. **Stop:** “Why must the condition eventually become false?” / 为什么条件最终会变假？

## 完整句子练习 / Complete readings

1. `while index < len(text):` — “While index is less than the length of text, colon.”
2. `for minute in range(10, 31, 5):` — “For each minute from ten through thirty by fives, colon.”
3. `if password_size == 0: break` — “If password size equals zero, break out of the loop.”
4. `counts[face - 1] += 1` — “Add one to the count for this die face.”
5. `letter_index % 26` — “Letter index modulo twenty-six,” used to wrap after `Z`.

中文：纠正读法时同时确认含义。学生能读出 `range` 的 stop 不包含、`randint` 两端包含、`break` 只结束最近一层循环，才算真正理解。
