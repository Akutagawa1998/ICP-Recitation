# 第 7 题：Mass and Weight
# Exercise 7: Mass and Weight

# 覆盖公式计算和严格不等式；目的：先把千克转换成牛顿，再按重量而非质量比较。100 与 500 牛顿恰好不触发警告；中间范围只显示重量。
# Coverage: formula evaluation and strict inequalities. Purpose: convert kilograms to newtons before comparing weight, not mass. Exactly 100 and 500 newtons trigger no warning; the middle range displays only the weight.

# 读取以千克为单位的质量，用 float 转成数值；只输入数字，不输入 kg。
# Read the user input, convert it when needed, and store it for the following code.
mass = float(input("Mass in kilograms: "))
# 按原题公式乘以 9.8，得到重量；例如输入 60 时为 588.0 牛顿。
# Multiply by the source constant 9.8 to obtain weight (588.0 newtons for input 60).
weight = mass * 9.8
# 先显示计算得到的重量及单位，便于核对换算。
# Display the computed weight and its unit so the conversion can be checked.
print("Weight:", weight, "newtons")
# 严格大于 500 才过重，不能改成大于或等于。
# Only a weight strictly above 500 is too heavy; do not include equality.
if weight > 500:
    # 例如输入 60 时，重量 588.0 满足条件，显示过重警告。
    # The example input weight 588.0 satisfies the condition, so display the heavy warning.
    print("Too heavy.")
# 独立检查是否严格小于 100；这里比较的是重量。
# Independently check whether weight is strictly below 100.
if weight < 100:
    # 小于 100 才显示过轻警告；例如输入质量 5 时会输出此行。
    # Display the light warning only below 100, for example for mass 5.
    print("Too light.")

