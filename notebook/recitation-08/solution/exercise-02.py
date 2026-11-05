# 第 2 题：一周销售额，练习输入、列表存储和累计循环。
# 教学目的：把七次输入保存为数据集合，再用独立循环计算一个合计。
# 总体思路：保留真正的 input 交互函数；下方只在演示时模拟七次输入。
# 常见错误：把数字字符串直接相加，或用 sum 代替原题明确要求的累计循环。

# %% R08-E02
# 任务：读取七天销售额，存入列表，用循环计算并显示周销售额。
# 思路：第一轮收集数据，第二轮以 total 保存已经处理过的金额之和。
# 易错点：演示数据是新增的课堂样例，不是原 PDF 提供的数值。
# 定义真正可以在终端或 notebook 中交互使用的函数。
def collect_weekly_sales():
    # 先建立空列表，随后按天追加浮点数金额。
    sales = []
    # 一周共七天，range 的结束值 8 不包含在循环中。
    for day in range(1, 8):
        # input 返回字符串，float 将合法金额转换为可计算的数值。
        amount = float(input("Sales for day " + str(day) + ": "))
        # 把当天金额保存为列表的一个元素。
        sales.append(amount)
    # 将累加器初始化为浮点数 0，表示尚未计入任何一天。
    total = 0.0
    # 逐项读取已经保存的七个金额，满足原题使用循环计算合计的要求。
    for amount in sales:
        # 把当前金额加到此前累计的金额上。
        total = total + amount
    # 以两位小数显示周总额；本演示结果为 1188.50。
    print("Weekly total: " + format(total, ".2f"))
    # 返回保存的数据，方便课堂核对列表确实存下了七天金额。
    return sales

# %% R08-E02-DEMO
# 任务：不等待键盘输入地演示上述真实交互函数。
# 思路：patch 仅在 with 块内把 input 替换成预先安排的七个回答，退出后自动恢复。
# 易错点：模拟输入属于运行演示工具，收集销售额的算法仍使用真正的 input。
# 导入标准库的临时替换工具，只有演示代码需要它。
from unittest.mock import patch

# 使用与课堂教纲一致的七个字符串回答；迭代器每次给出一个。
sales_answers = iter(["120.0", "135.5", "98.0", "150.0", "210.0", "300.0", "175.0"])
# 定义模拟输入函数，使运行输出保留提示文字和本次回答。
def sales_demo_input(prompt):
    # 按输入顺序取出下一个样例金额字符串。
    answer = next(sales_answers)
    # 将提示与回答一同显示，便于读者看到七天输入。
    print(prompt + answer)
    # 按照 input 的约定返回字符串。
    return answer

# 只在这一块中模拟输入，不影响之后手动调用交互函数。
with patch("builtins.input", sales_demo_input):
    # 执行完整程序，内部打印周总额，并取回保存的列表。
    weekly_sales = collect_weekly_sales()
# 显示保存的七天金额，作为原题列表存储要求的可见证据。
print("Stored sales:", weekly_sales)
