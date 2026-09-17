# 第 3 题：Areas of Rectangles
# Exercise 3: Areas of Rectangles

# 覆盖乘法、变量与互斥分支；目的：先计算两块面积，再比较结果，不能只比较边长。样例采用相同面积，练习容易遗漏的相等情况。
# Coverage: multiplication, variables, and mutually exclusive branches. Purpose: compute both areas before comparing them; comparing only side lengths is insufficient. The sample deliberately tests equal areas.

# 保存第一个长方形的长度 5.0；可编辑样例代替 float(input(...))。
# Store the first length, 5.0; this editable sample replaces float(input(...)).
length1 = 5.0
# 保存第一个长方形的宽度 4.0，使用同一种长度单位。
# Store the first width, 4.0, using the same length unit.
width1 = 4.0
# 保存第二个长方形的长度 4.0。
# Store the second length, 4.0.
length2 = 4.0
# 保存第二个长方形的宽度 5.0。
# Store the second width, 5.0.
width2 = 5.0
# 长度乘宽度得到第一个面积 20.0；星号表示乘法。
# Multiply length by width to get the first area, 20.0; the asterisk means multiplication.
area1 = length1 * width1
# 同样计算第二个面积 20.0；先计算再判断。
# Compute the second area, also 20.0, before making the decision.
area2 = length2 * width2
# 如果第一块面积更大，执行第一个缩进块。
# If the first area is greater, run the first indented block.
if area1 > area2:
    # 输出第一块更大；当前样例不会进入此分支。
    # Report that rectangle 1 is larger; this branch is not selected by the sample.
    print("Rectangle 1 has the greater area.")
# 只有前一个条件为假时，才判断第二块面积是否更大。
# Only if the first condition is False, test whether the second area is greater.
elif area2 > area1:
    # 输出第二块更大。
    # Report that rectangle 2 is larger.
    print("Rectangle 2 has the greater area.")
# 两边都不更大时，对普通数值意味着面积相等。
# If neither area is greater, ordinary numeric areas must be equal.
else:
    # 当前样例两块面积都是 20.0，因此输出相等。
    # The sample areas are both 20.0, so report equal areas.
    print("Both rectangles have the same area.")

