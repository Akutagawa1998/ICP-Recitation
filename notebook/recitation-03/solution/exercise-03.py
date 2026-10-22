# 第 3 题：Areas of Rectangles
# Exercise 3: Areas of Rectangles

# 覆盖乘法、变量与互斥分支；目的：先计算两块面积，再比较结果，不能只比较边长。可输入 5、4、4、5，练习容易遗漏的相等情况。
# Coverage: multiplication, variables, and mutually exclusive branches. Purpose: compute both areas before comparing them; comparing only side lengths is insufficient. Try inputs 5, 4, 4, 5 to test equal areas.

# 读取第一个长方形的长度文本，用 float 转成可含小数的数值，保存到 length1。
# Read the user input, convert it when needed, and store it for the following code.
length1 = float(input("Length of the first rectangle: "))
# 读取第一个长方形的宽度并转为浮点数；各边长使用相同单位。
# Read the user input, convert it when needed, and store it for the following code.
width1 = float(input("Width of the first rectangle: "))
# 读取第二个长方形的长度并转为浮点数，供后续面积计算使用。
# Read the user input, convert it when needed, and store it for the following code.
length2 = float(input("Length of the second rectangle: "))
# 读取第二个长方形的宽度并转为浮点数，保存到 width2。
# Read the user input, convert it when needed, and store it for the following code.
width2 = float(input("Width of the second rectangle: "))
# 长度乘宽度得到第一个面积；例如输入 5 和 4 时为 20.0；星号表示乘法。
# Multiply length by width to get the first area (20.0 for inputs 5 and 4); the asterisk means multiplication.
area1 = length1 * width1
# 同样计算第二个面积；例如输入 4 和 5 时为 20.0；先计算再判断。
# Compute the second area (20.0 for inputs 4 and 5), before making the decision.
area2 = length2 * width2
# 如果第一块面积更大，执行第一个缩进块。
# If the first area is greater, run the first indented block.
if area1 > area2:
    # 当第一个面积更大时，输出第一块更大。
    # Report that rectangle 1 is larger when its area is greater.
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
    # 两个面积相等时输出相等，例如输入 5、4、4、5。
    # Report equal areas, for example with inputs 5, 4, 4, 5.
    print("Both rectangles have the same area.")

