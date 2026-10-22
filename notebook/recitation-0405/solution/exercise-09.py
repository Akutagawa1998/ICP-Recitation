# 第 9 题：Dice statics（原题标题），统计 1000 次六面骰结果。
# 教学目的：把随机类别 1–6 映射到列表索引 0–5，并累计频数。
# 解题方法：使用固定局部种子重复掷骰，再显示每个面的计数。
# 常见错误：直接使用 counts[face]，会使面 6 越界并浪费索引 0。

# 导入标准库 random，以生成 1 到 6 的随机整数。
import random

# 定义函数，参数分别是掷骰次数和可复现的随机种子。
def roll_die_counts(number_of_rolls, seed):
    # 创建局部随机数生成器，不改变其他代码的全局随机状态。
    randomizer = random.Random(seed)
    # 建立六个从 0 开始的计数槽，依次对应骰面 1 到 6。
    counts = [0, 0, 0, 0, 0, 0]
    # 精确执行 number_of_rolls 次随机试验。
    for _ in range(number_of_rolls):
        # randint 包含两端，因此每次得到 1 到 6 的一个整数。
        face = randomizer.randint(1, 6)
        # 用 face-1 转为列表索引，并把该面计数加一。
        counts[face - 1] = counts[face - 1] + 1
    # 返回六个面的最终频数列表。
    return counts

# 使用原题的 1000 次和固定种子 409 得到可复现结果。
counts = roll_die_counts(1000, 409)
# 依次显示骰面 1 到 6，保持自然顺序。
for face in range(1, 7):
    # 显示当前骰面和对应的频数。
    print(f"{face}: {counts[face - 1]}")
