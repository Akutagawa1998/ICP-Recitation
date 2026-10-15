# Recitation 06 中文教学说明

本次材料按原题顺序覆盖 Assignment 04 的 Exercise 2，以及 Mock Midterm 的 Question 5–8。期中考试为纸笔形式，因此 Question 1 布尔表达式、Question 2 二进制/十六进制、Question 3–4 预测输出不收入 notebook；这些题仍属于纸笔复习范围。

两份 notebook 均使用简短英文。教师版是唯一答案源，学生版由官方脚本派生，课堂发放学生材料时请只发学生版。本目录保存详细中文备课说明和独立运行的程序。

## 先修内容与学习目标

需要变量、整数与字符串、下标、类型转换、比较与布尔运算、if/elif/else、while、for 和 random.randint。通过逐题练习，把文字条件转换为有顺序的判断，追踪循环状态，检查边界，并保持输出格式。不要用过度抽象替代初学者应能手写的步骤。

Mock Question 5–8 禁用列表、字符串方法（例如 .split()、.count()）、字典、集合、自定义函数；所有答案遵守此限制。字符串遍历、下标、len、str、int 和 f-string 不属于字符串方法。

## 文件顺序与每题目的

1. `exercise-01.py`：Assignment 04 Exercise 2，Blackjack。P01 对应读取手牌，P02 对应输出行动，P02A 为 Hit，P02B 为 Stay，P02C 为 Bust。原题分项的描述顺序保留，但实际判断必须优先处理 Bust。教学重点是辨认两字符牌 10、先将所有 A 计为 1，再安全升值一张 A，最后应用庄家 17 点停牌规则。它是一道完整程序题，不应拆成互不相关的小程序。原题要求命名 exercise2.py，本资料为统一练习编号使用 exercise-01.py。
2. `exercise-02.py`：Mock Question 5，Triangle Classifier。先用三角形不等式排除无效情况，再判等边、等腰、不等边。重点讨论相加等于第三边也无效，以及等边判断必须先于“任意两边相等”。
3. `exercise-03.py`：Mock Question 6，Digit Counter。用 % 10 取末位、// 10 去末位，统计大于或等于阈值的位数。目标是理解算术式逐位处理和每轮前进，不依赖字符串方法。样例计数为 9。
4. `exercise-04.py`：Mock Question 7，Message Compressor。跟踪当前字符和连续次数，在字符变化时保存前一组，循环结束后补上最后一组。重点区分连续次数与全串总次数，保留次数 1，区分大小写。两个原样例都保留在 notebook。
5. `exercise-05.py`：Mock Question 8，Dice Duel。外层循环负责计分回合，内层循环处理平局重掷；直到某人 3 分停止。重点是平局不计分、不增加回合数，两人都重掷，且每次掷骰都要输出。

每个脚本与对应教师 notebook 的输入提示、变量、算法和输出保持一致。脚本每条可执行行上方都有中文解释，便于上课逐行讲解；程序标识符和输出保持英文。

## 输入与演示

所有要求输入的题目均使用真实的 `input()`：Blackjack 读取手牌，Triangle Classifier 分别读取三条边，Digit Counter 读取正整数和阈值，Message Compressor 读取消息。字符串直接使用 `input(...)`，整数使用 `int(input(...))`；输入提示与原题一致。教师版、学生版和独立脚本均会等待用户输入，不使用预设的静态输入值，也不增加原题未要求的输入校验。

在 notebook 中逐题运行单元并在输入框中键入数据；运行全部单元时，也需要依次回答每个输入提示。在终端运行独立脚本时，根据提示键入数据并回车。可先输入原题样例：A39；三角形的 5、5、3；正整数 431663334231 和阈值 3；消息 aaabbcaaaa，再尝试其他合法输入。

Dice Duel 原题是计算机自动模拟，不要求用户输入；保留 `random.seed(7)` 使课堂演示可复现，并会遇到平局。随机演示不保证与原题展示的 4 回合骰子序列一致，题目要求输出格式而非指定随机数。

在仓库根目录依次运行：

```bash
python notebook/recitation-06/solution/exercise-01.py
python notebook/recitation-06/solution/exercise-02.py
python notebook/recitation-06/solution/exercise-03.py
python notebook/recitation-06/solution/exercise-04.py
python notebook/recitation-06/solution/exercise-05.py
```

使用装有 nbformat、nbclient、ipykernel 和 python3 kernel 的 Python 环境进行 notebook 验证。脚本不依赖第三方库。

## 原文歧义、假设与教学提醒

- Blackjack 原文说 12 点时“只有 J、Q、K”会使总点数超过 21，但 10 也会；notebook 保留该原句并明确指出遗漏。无需改动原始 PDF。
- Blackjack 原文对“A 作为 11 后仍低于 17”的情形没有完全说明。本答案使用不超过 21 的最高点数；若最低点数已超 21 则 Bust。这与全部六个样例一致，且歧义情形无论把 A 记为 1 还是 11，行动均为 Hit。多张 A 至多一张能升到 11，因为两张 11 已经超过 21。
- Blackjack 假设输入是合法、连写、大写的手牌，10 为一个两字符牌；不额外实现洗牌、发牌、玩家策略或非法输入处理。
- Triangle Classifier 假设三条边为正整数。Digit Counter 假设 n 为正整数、k 为 0–9；不扩展到负数或 n=0。所有三角形分支及等号边界应在手写追踪时检查。
- Message Compressor 对大小写敏感，每组即使只出现一次也要写 1；后面再次出现相同字符时不与之前不相邻的组混合。题目没有限定非空输入，本算法自然把空串压缩为空串，不要求输出一定更短或实现解压。
- Dice Duel 原答案在平局后的重掷输出中遗漏逗号，首次掷骰输出有逗号。本资料按题目样例统一为 `Alice rolls x, Bob rolls y`，每回合结算后留空行。

## 验证方式

学生版使用官方派生脚本生成，并通过官方校验器的结构与派生一致性检查。原校验器的执行模式不提供标准输入，不能直接验证交互题；本次在临时目录启动全新 Jupyter 内核，逐单元运行原始代码，通过 Jupyter 标准输入通道回复真实的输入请求；独立脚本通过标准输入接收测试数据。交付代码保留真实 `input()`，不覆盖输入函数。

交互版本验证完成：教师版与学生版均在全新内核中完成运行，各自准确请求并读取 7 次输入；16 项脚本标准输入测试与 3602 项答案、边界及禁用语法检查通过。独立审阅另外通过 19 项标准输入及模拟测试，确认无静态输入残留、学生版无答案泄漏、中文逐行注释完整，五个脚本与教师版代码的抽象语法树一致，无阻塞问题。交付 notebook 不保存测试代码、测试输入或运行输出；原始 PDF 未改动。
