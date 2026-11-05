# Recitation 08 中英文逐句授课教纲 Bilingual Teaching Guide

EN: Today we will use lists and tuples to collect data, trace changes, and build small programs.

中：今天我们用列表和元组收集数据、追踪变化，并完成几个小程序。

EN: Read each English sentence aloud and use the Chinese sentence immediately below it as your teaching reference.

中：每句英文都可以直接读给学生听，紧接其后的中文句子供你对照讲解。

EN: Open `recitation-08-student.ipynb` for the class and keep `solution/recitation-08-teaching.ipynb` open for your own reference.

中：课堂展示 `recitation-08-student.ipynb`，自己同时打开 `solution/recitation-08-teaching.ipynb` 作为参考。

EN: The notebook includes complete answers, so ask students to predict a result before revealing or running its solution cell.

中：notebook 已包含完整答案，所以展示或运行解答单元格之前，先请学生预测结果。

## 授课安排 Lesson timing

EN: Allow about 110 minutes for the complete lesson, including short student discussions.

中：完整授课建议预留约 110 分钟，其中包含简短的学生讨论。

| Section / 环节 | Minutes / 分钟 | Main question / 核心问题 |
| --- | ---: | --- |
| Opening and core concepts / 开场与基础概念 | 10 | What can change? / 什么可以改变？ |
| Exercise 1 / 第 1 题 | 20 | What actually happens to the object? / 对象实际发生了什么变化？ |
| Exercise 2 / 第 2 题 | 6 | How do we accumulate seven values? / 如何累加七个数值？ |
| Exercise 3 / 第 3 题 | 5 | How do we keep seven digit positions? / 如何保留七位数字？ |
| Exercise 4 / 第 4 题 | 7 | How do we summarize one list? / 如何概括同一个列表？ |
| Exercise 5 / 第 5 题 | 6 | Which values pass the condition? / 哪些数满足条件？ |
| Exercise 6 / 第 6 题 | 14 | Have we checked every rule? / 是否检查了全部规则？ |
| Exercise 7 / 第 7 题 | 14 | Which values need numeric conversion? / 哪些值需要转成数字？ |
| Exercise 8 / 第 8 题 | 22 | How do records persist between menu choices? / 菜单操作之间如何保存记录？ |
| Recap / 回顾 | 3 | Can we explain the data and the update? / 能否解释数据与更新方式？ |

EN: If the class period is shorter, complete Exercises 1 through 7 together and use Exercise 8 as a guided follow-up lab.

中：如果课时较短，可以先共同完成第 1 至 7 题，再把第 8 题作为带指导的后续实验。

## 开场与基础概念 Opening and core concepts

EN: Before running code, we will ask what the data looks like, what changes, and what the program returns or displays.

中：运行代码前，我们先判断数据的结构、哪些内容会改变，以及程序会返回或显示什么。

EN: A list stores an ordered sequence of items and allows us to change its items.

中：列表保存有顺序的一组元素，并允许我们修改其中的元素。

EN: A tuple also stores an ordered sequence, but we cannot assign a new value to one of its positions.

中：元组也保存有顺序的一组元素，但不允许我们给其中某个位置重新赋值。

```python
numbers = [10, 20, 30]
record = ("Alice", 0)
numbers[0] = 99
```

EN: Python indexes start at zero, so `numbers[0]` means the first item.

中：Python 的索引从零开始，所以 `numbers[0]` 表示第一个元素。

EN: Changing a list and returning a value are separate actions.

中：修改列表和返回一个值是两种不同的行为。

EN: For example, `append` changes the list but returns `None`.

中：例如，`append` 会修改列表，但它的返回值是 `None`。

EN: Two variable names can refer to the same list, so a change through one name can be visible through the other.

中：两个变量名可以指向同一个列表，所以通过一个名字进行的修改，也可以通过另一个名字看到。

EN: A nested list lets us represent rows, columns, or records containing several fields.

中：嵌套列表可以表示行列组成的表格，也可以表示包含多个字段的记录。

Action: Write `data[row][column]` on the board.

操作：在黑板上写出 `data[row][column]`。

EN: The first index chooses a row, and the second index chooses an item inside that row.

中：第一个索引选择一行，第二个索引选择这一行中的一个元素。

## 第 1 题 输出预测 Predict the output

EN: Treat the seven snippets as seven independent programs.

中：把这七段代码看作七个互相独立的程序。

EN: For each snippet, predict the printed result or the exception before running its answer cell.

中：每一小题都先预测打印结果或异常，再运行对应的解答单元格。

### 小题 1 元组赋值

```python
T = (1, 2, 3)
T[0] = 3
```

EN: The second line tries to replace the first item of a tuple.

中：第二行试图替换元组的第一个元素。

EN: That operation raises a `TypeError` because tuples do not support item assignment.

中：这个操作会引发 `TypeError`，因为元组不支持对元素位置进行赋值。

EN: The original program stops with an exception instead of producing a normal printed result.

中：原程序会因为异常而停止，而不是产生正常的打印结果。

EN: Our answer cell catches this expected error so the rest of the notebook can still run.

中：解答单元格会捕获这个预期错误，让 notebook 后面的内容仍然能够继续执行。

Expected result / 预期结果：

```text
TypeError: 'tuple' object does not support item assignment
```

Ask: Would replacing `T` with a list make this assignment valid?

提问：如果把 `T` 换成列表，这个赋值操作是否就合法了？

EN: Yes, because a list allows item assignment.

中：是的，因为列表允许对某个位置的元素重新赋值。

### 小题 2 append 的返回值

```python
L = [1, 2, 3]
print(L.append([4, 5]))
```

EN: Evaluate the call inside `print` first.

中：先计算 `print` 内部的函数调用。

EN: The call appends the whole list `[4, 5]` as one new item.

中：这个调用把整个列表 `[4, 5]` 作为一个新元素追加到末尾。

EN: The return value is `None`, so the displayed result is `None`.

中：返回值是 `None`，所以显示结果也是 `None`。

EN: After the call, the list itself is `[1, 2, 3, [4, 5]]`.

中：调用结束后，列表本身变成 `[1, 2, 3, [4, 5]]`。

EN: The original snippet does not print that changed list.

中：原题这段代码没有打印修改后的列表。

### 小题 3 原地排序

```python
L = [4, 2, 1, 3]
L.sort()
print(L)
```

EN: `sort` rearranges the existing list in ascending order.

中：`sort` 会把已有列表中的元素按升序重新排列。

EN: We then print the changed list, which is `[1, 2, 3, 4]`.

中：随后打印修改后的列表，得到 `[1, 2, 3, 4]`。

Ask: Why should we avoid writing `L = L.sort()` here?

提问：这里为什么应该避免写成 `L = L.sort()`？

EN: Because `sort` returns `None`, that assignment would replace the variable's reference with `None`.

中：因为 `sort` 返回 `None`，这样赋值会让变量改为指向 `None`。

### 小题 4 extend 与字符串

```python
L = ['a', 'b', 'c']
L.extend(['d', 'e'])
L.extend('fg')
print(L)
```

EN: `extend` takes items from an iterable and adds them one at a time.

中：`extend` 从一个可迭代对象中取出元素，并逐个添加到列表末尾。

EN: The first call adds `d` and `e`, and the second call adds the characters `f` and `g`.

中：第一次调用添加 `d` 和 `e`，第二次调用添加字符 `f` 和 `g`。

EN: The result is `['a', 'b', 'c', 'd', 'e', 'f', 'g']`.

中：结果是 `['a', 'b', 'c', 'd', 'e', 'f', 'g']`。

Ask: What would `append('fg')` add instead?

提问：如果改成 `append('fg')`，会添加什么？

EN: It would add one string item containing both characters.

中：它会添加一个包含这两个字符的字符串元素。

### 小题 5 列表推导式

```python
L = ["apple", "cat", "banana", "dog"]
L1 = [len(x) for x in L]
L2 = [x for x in L if len(x) > 4]
print(L1)
print(L2)
```

EN: In the first comprehension, each word becomes its length.

中：第一个推导式把每个单词转换成它的长度。

EN: In the second comprehension, we keep a word only when its length is greater than four.

中：第二个推导式只保留长度大于四的单词。

EN: The expression before `for` tells us what goes into the new list.

中：`for` 前面的表达式决定新列表中放入什么内容。

EN: The optional `if` condition tells us which original items are included.

中：可选的 `if` 条件决定原列表中的哪些元素会被包含进来。

```text
[5, 3, 6, 3]
['apple', 'banana']
```

### 小题 6 遍历时删除元素

```python
t = [1, 3, 5, 7, 9]
for i in t:
    if i % 2:
        t.remove(i)
print(t)
```

EN: Every original item is odd, but this loop does not visit every original item.

中：原列表中的元素都是奇数，但这个循环不会访问原来的每一个元素。

EN: Removing an item shifts the later items to the left while the iterator moves on to its next position.

中：删除元素会让后面的元素左移，而迭代器仍然继续访问下一个位置。

| Iteration / 轮次 | Value visited / 访问值 | List after removal / 删除后的列表 | Next position / 下次位置 |
| --- | ---: | --- | --- |
| 1 | 1 | `[3, 5, 7, 9]` | index 1 contains 5 / 索引 1 对应 5 |
| 2 | 5 | `[3, 7, 9]` | index 2 contains 9 / 索引 2 对应 9 |
| 3 | 9 | `[3, 7]` | index 3 is past the end / 索引 3 已超出末尾 |

EN: The loop visits `1`, `5`, and `9`, so the final list is `[3, 7]`.

中：循环访问了 `1`、`5` 和 `9`，所以最终列表是 `[3, 7]`。

EN: Here an odd number has a remainder of one, and that nonzero value is treated as true.

中：这里奇数除以二的余数是一，这个非零值在条件中被当作真。

EN: If we actually wanted to filter a list, we could build a new list instead of deleting items from the list being traversed.

中：如果真正想实现筛选，可以建立一个新列表，避免直接删除正在遍历的列表中的元素。

EN: That safer approach is a follow-up discussion, while the answer to the original snippet remains `[3, 7]`.

中：这种更安全的写法属于后续讨论，原题代码的答案仍然是 `[3, 7]`。

### 小题 7 两个名字指向同一个列表

```python
def myappend(L):
    L.append(3)
    return L

x = [1, 2]
y = myappend(x)
y.append(4)
print(x)
```

EN: The parameter `L` refers to the same list that `x` refers to.

中：形参 `L` 和变量 `x` 指向同一个列表。

EN: Appending `3` changes that list to `[1, 2, 3]`.

中：追加 `3` 后，这个列表变为 `[1, 2, 3]`。

EN: Returning `L` gives `y` a reference to that same list rather than a new copy.

中：返回 `L` 后，`y` 得到的是同一个列表的引用，而不是一个新副本。

EN: Appending `4` through `y` changes the list that `x` also sees.

中：通过 `y` 追加 `4`，也会改变 `x` 所能看到的那个列表。

EN: The final output is `[1, 2, 3, 4]`.

中：最终输出是 `[1, 2, 3, 4]`。

Action: Draw two arrows labeled `x` and `y` pointing to one list.

操作：画出分别标为 `x` 和 `y` 的两个箭头，让它们指向同一个列表。

## 第 2 题 一周销售额 Total sales

EN: We need seven daily sales amounts, a list that stores them, and a loop that computes their total.

中：我们需要七天的销售额、一个保存它们的列表，以及一个计算总额的循环。

EN: First collect the input values and convert the text from `input` to numbers.

中：先收集输入值，并把 `input` 得到的文本转换成数字。

EN: We use `float` because a sales amount can include cents.

中：销售额可能包含小数，因此使用 `float`。

EN: Then start the total at zero and add one stored amount on each iteration.

中：随后把总额初始化为零，并在每一轮加入一个已保存的销售额。

```python
total = 0
for amount in sales:
    total = total + amount
```

EN: This loop is required by the question, even though Python also provides a built-in `sum` function.

中：题目明确要求使用循环，因此这里保留累加循环，尽管 Python 也提供内置的 `sum` 函数。

EN: Our demonstration supplies `120`, `135.5`, `98`, `150`, `210`, `300`, and `175` as the seven input amounts.

中：演示为七次输入依次提供 `120`、`135.5`、`98`、`150`、`210`、`300` 和 `175`。

EN: These are teaching sample values, and their weekly total is `1188.50`.

中：这些是教学示例值，对应的一周总额为 `1188.50`。

EN: The actual input-based function remains available, while the demonstration supplies responses automatically so Run All does not pause.

中：实际读取输入的函数仍然保留，演示只是自动提供输入，使“全部运行”不会暂停等待。

Ask: What happens if the total is reset to zero inside the accumulation loop?

提问：如果在累加循环内部把总额重新设为零，会发生什么？

EN: Earlier amounts are lost, so only the current amount remains in the total.

中：之前累积的金额会丢失，总额中只剩当前这一笔金额。

## 第 3 题 彩票号码 Lottery number generator

EN: The question asks for seven random digits stored in seven list positions.

中：题目要求生成七个随机数字，并把它们保存到列表的七个位置中。

EN: Each call to `randint(0, 9)` can produce any integer from zero through nine, including both endpoints.

中：每次调用 `randint(0, 9)` 都可能产生零到九之间的任意整数，包括两个端点。

EN: Use one loop to append seven digits and another loop to display them.

中：使用第一个循环追加七个数字，再用另一个循环显示它们。

EN: The digits may repeat because the question does not require different digit values.

中：数字可以重复，因为题目没有要求各位数字互不相同。

EN: A leading zero is also allowed by the stated range, so keep the result as seven displayed positions.

中：按照给定范围，首位也允许为零，因此应当保留七个显示位置。

EN: Converting the whole result to an integer could remove a leading zero.

中：如果把整个结果转换为整数，开头的零就可能丢失。

EN: We fix the random seed at eight only to make the classroom demonstration repeatable.

中：我们把随机种子固定为八，只是为了让课堂演示能够复现。

EN: The demonstration list is `[3, 5, 6, 2, 3, 0, 1]`, and its displayed lottery number is `3562301`.

中：演示列表是 `[3, 5, 6, 2, 3, 0, 1]`，显示的彩票号码是 `3562301`。

Ask: Does setting a seed mean every generated digit must be different?

提问：设置随机种子是否意味着每个生成的数字都必须不同？

EN: No, the seed makes the sequence repeatable and does not add a uniqueness rule.

中：不是，随机种子只是让序列能够复现，并没有增加数字唯一性的要求。

## 第 4 题 数字分析 Number analysis

EN: Generate twenty integers from one through one hundred and store all of them in one list.

中：生成二十个一到一百之间的整数，并把它们全部存入同一个列表。

EN: All four statistics must describe that same list.

中：四个统计量都必须来自这同一个列表。

EN: The lowest and highest values can be found with `min` and `max`.

中：可以分别使用 `min` 和 `max` 找到最小值和最大值。

EN: The average is the total divided by the number of items, so use ordinary division.

中：平均值等于总和除以元素数量，因此应使用普通除法。

EN: Integer division would discard a fractional part and could give the wrong average.

中：整数除法会丢掉小数部分，可能得到错误的平均值。

EN: With a fresh seed of eight, our demonstration produces the following list.

中：重新设置随机种子为八后，演示会得到以下列表。

```text
[30, 48, 49, 17, 25, 91, 6, 11, 18, 32,
 65, 27, 52, 83, 4, 59, 63, 59, 50, 64]
```

| Requested statistic / 题目要求 | Result / 结果 |
| --- | ---: |
| Lowest / 最小值 | 4 |
| Highest / 最大值 | 91 |
| Total / 总和 | 853 |
| Average / 平均值 | 42.65 |

Ask: Why should we avoid generating a new list before computing each statistic?

提问：为什么不应该在计算每个统计量之前都重新生成一个列表？

EN: We would be describing different datasets instead of summarizing the same twenty numbers.

中：那样得到的统计量会对应不同的数据集，而不是概括同样的二十个数。

## 第 5 题 显示大于 n 的数字 Larger than n

EN: The function receives a numeric list and a threshold named `n`.

中：函数接收一个数字列表，以及一个名为 `n` 的阈值。

EN: Visit each number and print it only when `number > n` is true.

中：逐个访问数字，仅当 `number > n` 为真时才打印它。

EN: The word greater means strictly greater, so a value equal to `n` must be excluded.

中：“大于”表示严格大于，因此等于 `n` 的值必须排除。

EN: For `[4, 10, 15, 10, 23, -2]` and `n = 10`, the displayed numbers are `15` and `23`.

中：对于 `[4, 10, 15, 10, 23, -2]` 和 `n = 10`，显示的数字是 `15` 和 `23`。

EN: Displaying the matches is part of the requirement, so returning a filtered list alone would be incomplete.

中：显示符合条件的数字是题目要求的一部分，因此只返回筛选后的列表还不完整。

Ask: What should the function display for an empty list or a list with no matching values?

提问：如果列表为空，或者没有任何值满足条件，函数应该显示什么？

EN: It should display no numbers and finish normally.

中：它应该不显示任何数字，并正常结束。

## 第 6 题 洛书九宫格 Lo Shu magic square

EN: A Lo Shu square must satisfy all the rules together.

中：洛书九宫格必须同时满足全部规则。

EN: It must have three rows and three columns, use each integer from one through nine exactly once, and give the same sum for every row, column, and diagonal.

中：它必须有三行三列，恰好各使用一次一到九的整数，并且每一行、每一列和每一条对角线的和都相同。

EN: The example in the question is the following square.

中：原题给出的示例如下。

```text
4 9 2
3 5 7
8 1 6
```

EN: The numbers one through nine total forty-five, so each of the three equal row sums must be fifteen.

中：一到九的总和是四十五，所以三行相等时，每行的和必须是十五。

Action: Point to the three rows, three columns, and both diagonals.

操作：依次指出三行、三列和两条对角线。

EN: That gives us eight line sums to check.

中：这样一共需要检查八条线的和。

EN: Check the dimensions before using a fixed row or column index.

中：在使用固定的行列索引之前，先检查尺寸。

EN: Otherwise a short row could cause an indexing error before we can return `False`.

中：否则，某一行过短时，程序可能还没来得及返回 `False` 就出现索引错误。

EN: Next collect the nine values and check that they are exactly the required numbers.

中：接着收集九个值，检查它们是否恰好是题目要求的那些数字。

EN: Comparing the sorted values with `[1, 2, 3, 4, 5, 6, 7, 8, 9]` checks both the range and repeated values for our integer grids.

中：对于这里的整数网格，把排序后的值与 `[1, 2, 3, 4, 5, 6, 7, 8, 9]` 比较，可以同时检查取值范围和重复值。

EN: Then check the row sums, column sums, and both diagonal sums.

中：随后检查行和、列和，以及两条对角线的和。

EN: Return `False` as soon as a required rule fails, and return `True` only after every rule passes.

中：只要有一条必要规则不满足，就返回 `False`；只有全部规则都满足后，才返回 `True`。

Ask: Would a three-by-three grid filled with fives be a Lo Shu square?

提问：一个所有位置都是五的三行三列网格，是否属于洛书九宫格？

EN: No, because matching line sums do not satisfy the requirement to use one through nine exactly once.

中：不属于，因为线和相同并不能满足一到九各使用一次的要求。

Action: Use the following grid as a separate diagonal test.

操作：用下面这个网格单独检查对角线条件。

```text
1 5 9
6 7 2
8 3 4
```

EN: Every row and column sums to fifteen, but the diagonal sums are twelve and twenty-four.

中：每行和每列的和都是十五，但两条对角线的和分别是十二和二十四。

EN: A correct validator must reject this grid even though the row and column checks pass.

中：即使行列检查通过，正确的判断函数也必须拒绝这个网格。

EN: Wrong-size grids, repeated values, and failed line sums are teaching checks rather than extra numbered parts in the source question.

中：错误尺寸、重复值和线和不满足要求的情况是教学检查，不是原题新增的编号小题。

## 第 7 题 学生成绩 Grades

EN: Each student record contains an ID, a first name, a last name, and four test grades.

中：每条学生记录包含学号、名、姓，以及四次测试成绩。

EN: All seven fields are stored as strings in the supplied data.

中：给定数据中的七个字段全部按字符串保存。

EN: Keep the student ID as text, but convert grades to numbers when calculating an average.

中：学号应保留为文本，而计算平均值时需要把成绩转为数字。

EN: The PDF has malformed opening quotes before John's last `79` and Joe's last `92`, so the runnable data uses ordinary matching quotes without changing either grade.

中：PDF 中 John 最后一个 `79` 和 Joe 最后一个 `92` 的左引号不合法，因此可运行数据改用配对的普通引号，但不改变成绩值。

### 小题 1 computeAverage

EN: Keep the required function name `computeAverage` and parameter name `studentList`.

中：保留题目指定的函数名 `computeAverage` 和参数名 `studentList`。

EN: For each record, add the four numeric grades and divide by four.

中：对于每条记录，把四次数字成绩相加，再除以四。

EN: Build a new record containing the three identity fields and the average converted back to a string.

中：建立一条新记录，包含前三个身份字段，以及重新转换为字符串的平均成绩。

EN: Append each new record to a new result list and return the list after all students have been processed.

中：把每条新记录追加到新的结果列表中，处理完全部学生后再返回这个列表。

EN: Returning inside the student loop would stop after the first student.

中：如果在遍历学生的循环内部返回，函数处理完第一名学生就会停止。

EN: John's four grades total `296`, so his average is `74.0`.

中：John 的四次成绩总和为 `296`，所以平均值是 `74.0`。

| Student / 学生 | Average string / 平均值字符串 |
| --- | --- |
| John Doe | `'74.0'` |
| Bob Smith | `'87.5'` |
| Jane Roe | `'73.5'` |
| Joe Public | `'89.75'` |
| Jean Martin | `'67.25'` |

EN: These string forms match the source examples, so we do not force every average to two decimal places.

中：这些字符串形式与原题示例一致，因此不把所有平均值强制格式化为两位小数。

### 小题 2 highestAverage

EN: The input still contains the original four test grades rather than the shorter average records.

中：输入仍然包含原来的四次测试成绩，而不是已经缩短的平均值记录。

EN: Compute or reuse each average, convert the comparison value to a number, and track the best student seen so far.

中：计算或复用每名学生的平均值，把用于比较的值转成数字，并记录目前成绩最好的学生。

EN: Comparing strings would compare their characters instead of their numeric values.

中：比较字符串时比较的是字符顺序，而不是数值大小。

EN: The required return value contains only the ID, first name, and last name.

中：要求的返回值只包含学号、名和姓。

```python
['8754543', 'Joe', 'Public']
```

EN: Joe has the highest average at `89.75`.

中：Joe 的平均成绩最高，为 `89.75`。

EN: The source does not specify ties or empty input, so our implementation keeps the first student in a tie and returns an empty list when there are no students.

中：原题没有规定并列或空输入的处理方式，因此本实现遇到并列时保留先出现的学生，遇到空输入时返回空列表。

Ask: Why must the average field in each returned record be stored as text?

提问：为什么返回记录中的平均值字段必须保存为文本？

EN: Because the required output format explicitly asks for the average grade as a string.

中：因为题目明确要求平均成绩以字符串形式返回。

## 第 8 题 随机考勤系统 Random attendance system

EN: We will now combine a mutable list, immutable tuples, random selection, and a menu loop.

中：现在把可变列表、不可变元组、随机抽选和菜单循环组合起来。

```python
Stu_list = [("Alice", 0), ("Bob", 0), ("Charlie", 0)]
```

EN: The outer list stores the roster, while each tuple stores one name and one absence count.

中：外层列表保存学生名单，每个元组保存一个姓名和一个缺勤次数。

EN: The same list must remain in use across menu choices so previous absences are remembered.

中：不同菜单操作必须继续使用同一个列表，才能保留此前的缺勤记录。

### 小题 1 注册学生

EN: `register_students()` reads names, creates a tuple with a zero absence count for each name, and returns the completed list.

中：`register_students()` 读取姓名，为每个姓名创建缺勤次数为零的元组，并返回完整列表。

EN: The source does not define how registration ends, so we enter one name at a time and finish with a blank line.

中：原题没有规定如何结束注册，因此这里采用逐个输入姓名、输入空行结束的方式。

EN: We use unique names, reject exact duplicates, and look up names with matching letter case.

中：本实现要求姓名唯一，拒绝完全相同的重复姓名，并按大小写一致的姓名进行查询。

EN: These are implementation choices for the unspecified parts of the question.

中：这些是针对原题未明确部分作出的实现约定。

Ask: Why do we set the initial absence count to zero?

提问：为什么注册时要把缺勤次数设为零？

EN: No attendance round has recorded an absence for that student yet.

中：因为此时还没有任何一次点名记录该学生缺勤。

### 小题 2 随机点名与更新元组

EN: `take_attendance(Stu_list, n)` must select `n` different students in one attendance round.

中：`take_attendance(Stu_list, n)` 必须在一轮点名中抽选 `n` 名不同的学生。

EN: Use `random.sample` to choose different list positions without replacement.

中：使用 `random.sample` 不放回地抽取不同的列表位置。

EN: The selected count must be between zero and the number of enrolled students.

中：抽选人数必须在零到已注册学生总人数之间。

EN: Choosing randomly in a loop without tracking earlier choices could select the same student twice.

中：如果只是在循环中重复随机选择，却不记录此前的选择，就可能两次选中同一名学生。

EN: For each selected position, read the current name and absence count from the tuple.

中：对于每个被选中的位置，从元组中读取当前姓名和缺勤次数。

EN: A response of `P` leaves the count unchanged, and a response of `A` increases the count by one.

中：输入 `P` 时次数保持不变，输入 `A` 时次数增加一。

EN: We cannot assign to the count inside the tuple, but we can replace the tuple stored at that position in the list.

中：我们不能直接给元组内部的次数位置赋值，但可以替换列表在该位置保存的整个元组。

```python
name, absences = Stu_list[index]
# When the response is A:
Stu_list[index] = (name, absences + 1)
```

EN: Replacing the list item updates the original roster that `main` is using.

中：替换列表元素会更新 `main` 正在使用的原名单。

Ask: Why would changing only a temporary variable fail to save the new absence count?

提问：为什么只修改一个临时变量，不能保存新的缺勤次数？

EN: The record inside the roster would still contain the old tuple until we assign the new tuple back into the list.

中：如果不把新元组写回列表，名单中的记录仍然保存旧元组。

### 小题 3 查询缺勤次数

EN: Keep the source signature `check_absences(student)` and pass the complete roster through the parameter named `student`.

中：保留原题签名 `check_absences(student)`，并通过名为 `student` 的参数传入完整名单。

EN: The parameter name is ambiguous in the source, so this meaning is stated explicitly in our materials.

中：原题中的这个参数名容易产生歧义，因此材料明确说明它的含义。

EN: Ask for a name, search the records, and display the matched student's current absence count.

中：读取一个姓名，搜索全部记录，并显示匹配学生当前的缺勤次数。

EN: If no record matches, print exactly `Student not enrolled.`.

中：如果没有匹配记录，就准确打印 `Student not enrolled.`。

EN: A matched student with zero absences is different from an unenrolled student.

中：已经注册但缺勤次数为零的学生，与尚未注册的学生是两种不同情况。

### 小题 4 主程序与菜单

EN: `main()` registers students once and then repeatedly displays the menu.

中：`main()` 只注册一次学生，然后重复显示菜单。

```text
1. Take attendance
2. Check a student's absence count
3. Quit
```

EN: Option one asks for a selection count and calls the attendance function.

中：选项一读取抽选人数，并调用点名函数。

EN: Option two calls the lookup function with the same roster.

中：选项二把同一份名单传给查询函数。

EN: Option three exits the menu loop.

中：选项三退出菜单循环。

EN: Registering a new list inside the menu loop would erase the previous absence history.

中：如果在菜单循环内部重新注册并创建列表，就会清除之前的缺勤记录。

### 对照原题样例演示

EN: The notebook demonstration supplies fixed input responses and fixed sample selections so we can replay the source example without waiting for typing.

中：notebook 演示自动提供固定输入和固定抽选结果，以便不用等待键盘输入就能重现原题示例。

EN: This temporary demonstration setup does not change the real interactive functions or the randomness used when you call them normally.

中：这一临时演示设置不会改变真实的交互函数，也不会改变正常调用时使用的随机抽选。

| Step / 步骤 | Action / 操作 | Stored state or display / 保存状态或显示 |
| --- | --- | --- |
| 1 | Register Alice, Bob, Charlie / 注册三名学生 | All counts are 0 / 次数都为 0 |
| 2 | Select Bob and Alice; enter A and P / 抽 Bob、Alice，输入 A、P | Bob becomes 1; Alice stays 0 / Bob 为 1，Alice 为 0 |
| 3 | Query Bob / 查询 Bob | `Bob: 1 absence(s)` |
| 4 | Select Charlie and Bob; enter P and A / 抽 Charlie、Bob，输入 P、A | Charlie stays 0; Bob becomes 2 / Charlie 为 0，Bob 为 2 |
| 5 | Query Bob / 查询 Bob | `Bob: 2 absence(s)` |
| 6 | Query David / 查询 David | `Student not enrolled.` |
| 7 | Choose 3 / 选择 3 | Exit / 退出 |

EN: After the first round, Bob has one absence, and the second round increases that same stored count to two.

中：第一轮后 Bob 缺勤一次，第二轮继续更新同一个已保存的次数，使它变为两次。

EN: Alice and Charlie remain at zero because the sample marks them present.

中：示例把 Alice 和 Charlie 标记为出席，所以他们的缺勤次数保持为零。

Action: Run the demonstration cell and pause at each Bob lookup to connect the output to the stored tuple.

操作：运行演示单元格，在每次查询 Bob 时暂停讲解，把输出与保存的元组联系起来。

EN: The use of `patch` belongs to the replay setup, while the exercise solution itself is the four ordinary input-based functions.

中：`patch` 用于重放演示，练习本身的解答是四个普通的输入交互函数。

EN: To try real keyboard input, run a new cell containing `main()` after the demonstration has finished.

中：如果想实际键盘输入，在演示结束后新建一个单元格运行 `main()` 即可。

## 课堂回顾与检查 Recap and checks

Ask: What is the difference between `append` and `extend`?

提问：`append` 与 `extend` 有什么区别？

EN: `append` adds its argument as one item, while `extend` adds the argument's items individually.

中：`append` 把参数整体添加为一个元素，而 `extend` 把参数中的元素逐个添加进去。

Ask: Why did the deletion loop leave `[3, 7]`?

提问：删除循环为什么留下了 `[3, 7]`？

EN: Deletion shifted the remaining items left, so the iterator skipped the values that moved into positions it had already passed.

中：删除导致剩余元素左移，迭代器因此跳过了移到已经经过的位置上的值。

Ask: What distinguishes a valid Lo Shu square from a grid whose rows merely have equal sums?

提问：合法洛书九宫格与仅仅行和相等的网格有什么区别？

EN: A valid square also has the correct dimensions, each required number exactly once, and correct column and diagonal sums.

中：合法九宫格还必须具有正确尺寸、一到九各出现一次，以及正确的列和与对角线和。

Ask: How can we update attendance when each student record is a tuple?

提问：学生记录是元组时，我们如何更新考勤？

EN: Create a new tuple with the updated count and assign it back to the student's position in the list.

中：用新次数创建一个新元组，再把它写回列表中该学生所在的位置。

EN: For your own solutions, explain the data structure, the condition, the update, and one boundary case before writing code.

中：独立解题时，先解释数据结构、判断条件、更新方式，以及一个边界情况，再开始写代码。
