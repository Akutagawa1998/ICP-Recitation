# 第 4 题：数字分析，练习对同一列表计算四种统计量。
# 教学目的：理解最小值、最大值、总和与平均值回答的是不同问题。
# 总体思路：先存储恰好 20 个随机整数，再按题目规定顺序显示四个结果。
# 常见错误：randint 的上界应为 100，平均数应除以元素数量 20。

# %% R08-E04
# 任务：生成 20 个 1 到 100 的随机整数，并显示最小、最大、总和与平均值。
# 思路：使用 min、max、sum、len 直接表达统计含义。
# 易错点：本题没有要求数字互不相同；随机数据不能每算一个统计量就重新生成。
# 导入随机模块，使本文件可以独立运行。
import random

# 重新固定种子 8，保证本题不依赖第 3 题消耗了多少随机数。
random.seed(8)
# 建立保存本题 20 个整数的列表。
numbers = []
# 执行二十次生成操作。
for position in range(20):
    # 每次生成包含两个端点在内的 1 到 100 的整数，并存入同一个列表。
    numbers.append(random.randint(1, 100))
# 获取列表中的最小值，本演示为 4。
lowest = min(numbers)
# 获取列表中的最大值，本演示为 91。
highest = max(numbers)
# 计算所有二十个整数的总和，本演示为 853。
total = sum(numbers)
# 用总和除以元素个数，得到平均数 42.65。
average = total / len(numbers)
# 先显示数据，方便教师复核每个统计量来自同一个列表。
print("Numbers:", numbers)
# 按原题顺序首先显示最小值。
print("Lowest:", lowest)
# 然后显示最大值。
print("Highest:", highest)
# 然后显示总和。
print("Total:", total)
# 最后显示平均值。
print("Average:", average)
