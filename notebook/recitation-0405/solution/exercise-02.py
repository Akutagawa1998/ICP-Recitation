# 第 2 题：Calories Burned，分别使用 while 和 for 循环。
# 教学目的：把固定步长的时间序列与每分钟 4.2 calories 的计算结合起来。
# 解题方法：依次生成 10、15、20、25、30 分钟，再用分钟数乘以速率。
# 常见错误：遗漏 30 分钟，或在 while 版本中忘记更新 minute 而形成无限循环。

# 保存每分钟消耗的 calories，两个版本使用同一个常量。
calories_per_minute = 4.2
# while 版本从 10 分钟开始。
minute = 10
# 当 minute 不超过 30 时，继续计算并显示。
while minute <= 30:
    # 用分钟数乘以每分钟速率，得到累计消耗。
    calories = minute * calories_per_minute
    # 以一位小数显示当前分钟对应的 calories。
    print(f"After {minute} minutes: {calories:.1f} calories")
    # 每轮增加 5 分钟，生成原题要求的下一项。
    minute = minute + 5

# 再次保存同一个速率，使 for 版本与 notebook 单元逻辑一致。
calories_per_minute = 4.2
# range 的 stop 31 不包含，因此会包含 30 并按 5 递增。
for minute in range(10, 31, 5):
    # 计算当前分钟数对应的累计消耗。
    calories = minute * calories_per_minute
    # 使用与 while 版本相同的英文格式显示结果。
    print(f"After {minute} minutes: {calories:.1f} calories")
