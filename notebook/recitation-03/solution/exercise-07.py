# 第 7 题：Mass and Weight
# Exercise 7: Mass and Weight

# 覆盖公式计算和严格不等式；目的：先把千克转换成牛顿，再按重量而非质量比较。100 与 500 牛顿恰好不触发警告；中间范围只显示重量。
# Coverage: formula evaluation and strict inequalities. Purpose: convert kilograms to newtons before comparing weight, not mass. Exactly 100 and 500 newtons trigger no warning; the middle range displays only the weight.

# 保存非负样例质量 60.0 千克，可替换为 float(input(...))。
# Store nonnegative sample mass 60.0 kilograms; an interactive version can use float(input(...)).
mass = 60.0
# 按原题公式乘以 9.8，得到重量 588.0 牛顿。
# Multiply by the source constant 9.8 to obtain weight 588.0 newtons.
weight = mass * 9.8
# 先显示计算得到的重量及单位，便于核对换算。
# Display the computed weight and its unit so the conversion can be checked.
print("Weight:", weight, "newtons")
# 严格大于 500 才过重，不能改成大于或等于。
# Only a weight strictly above 500 is too heavy; do not include equality.
if weight > 500:
    # 当前重量 588.0 满足条件，显示过重警告。
    # The sample weight 588.0 satisfies the condition, so display the heavy warning.
    print("Too heavy.")
# 独立检查是否严格小于 100；这里比较的是重量。
# Independently check whether weight is strictly below 100.
if weight < 100:
    # 小于 100 才显示过轻警告；当前样例不输出此行。
    # Display the light warning only below 100; the current sample does not print it.
    print("Too light.")

