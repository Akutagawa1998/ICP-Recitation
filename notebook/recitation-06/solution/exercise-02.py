# 练习 2：Property Tax
# 教学目的：把题目中的百分比和单位关系写成表达式，并用参数把数据传给函数。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：混淆美分与美元；忘记每 100 美元中的除以 100；把显示两位小数误认为修改了计算规则。

# 接收实际价值，用题目指定的函数名完成计算和显示。
def computePropertyTax(actual_value):
    # 实际价值的百分之六十是评估值。
    assessment_value = actual_value * 0.60
    # 每一百美元收零点七二美元税。
    property_tax = assessment_value / 100 * 0.72
    # 按两位小数显示评估值。
    print(f"Assessment value: ${assessment_value:.2f}")
    # 按两位小数显示税额。
    print(f"Property tax: ${property_tax:.2f}")

# 用可编辑示例代替阻塞式输入；课堂可改为 float(input(...))。
actual_value = 10000.0
# 把实际价值传入函数并显示两项结果。
computePropertyTax(actual_value)
