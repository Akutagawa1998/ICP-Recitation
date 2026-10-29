# 练习 3：Painting cost
# 教学目的：练习把大任务拆成职责清晰的小函数，并把前一个计算的结果传给下一个函数。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：在函数中打印之后忘记返回；把面积当作加仑数；在题目没有要求时自行加入整桶向上取整。
# 子项顺序：R06-E03-P01、R06-E03-P02、R06-E03-P03、R06-E03-P04、R06-E03-P05

# 第一步根据墙面面积返回所需加仑数。
def paint_volume(area):
    # 一百一十二平方英尺对应一加仑，按比例相除。
    return area / 112

# 第二步根据同一面积返回劳动小时数。
def labor_hours(area):
    # 先求面积倍数，再乘每份所需的八小时。
    return area / 112 * 8

# 第三步接收用量和单价，计算油漆费用。
def paint_cost(gallons, price_per_gallon):
    # 用量乘每加仑价格得到总油漆费。
    return gallons * price_per_gallon

# 第四步接收工时，使用题目指定的时薪。
def labor_cost(hours):
    # 每小时三十五美元，乘工时得到劳动费。
    return hours * 35.00

# 第五步把两类费用组合起来。
def total_cost(paint_charge, labor_charge):
    # 总费用等于油漆费与劳动费之和。
    return paint_charge + labor_charge

# 可编辑墙面面积，原题交互版可从 float(input(...)) 获得。
wall_area = 224.0
# 可编辑每加仑油漆价格。
price_per_gallon = 25.0
# 调用第一个函数并保存油漆用量。
gallons = paint_volume(wall_area)
# 调用第二个函数并保存工时。
hours = labor_hours(wall_area)
# 把用量与单价传给费用函数。
paint_charge = paint_cost(gallons, price_per_gallon)
# 把工时传给劳动费用函数。
labor_charge = labor_cost(hours)
# 把两项费用传给总价函数。
job_charge = total_cost(paint_charge, labor_charge)
# 显示油漆用量，示例为两加仑。
print(f"Paint required: {gallons:.2f} gallons")
# 显示工时，示例为十六小时。
print(f"Labor required: {hours:.2f} hours")
# 显示油漆费用五十美元。
print(f"Paint cost: ${paint_charge:.2f}")
# 显示劳动费用五百六十美元。
print(f"Labor cost: ${labor_charge:.2f}")
# 显示总价六百一十美元。
print(f"Total cost: ${job_charge:.2f}")
