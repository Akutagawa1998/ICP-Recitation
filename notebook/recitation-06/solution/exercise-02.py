# Mock Midterm 原题 Question 5：Triangle Classifier。
# 概念：三角形不等式、or/and、按优先级组织 if/elif/else。
# 教学目的：先排除无效输入几何情况，再按“全相等、两边相等、全不同”分类。
# 题目假设输入是正整数；这里不额外加入输入校验，保持答题范围。
# 易错点：两边和等于第三边也无效；若先查两边相等，会误分等边三角形。
# 不使用列表、字符串方法、字典、集合或自定义函数。

# 显示第一条边的提示，读取用户输入，再用 int 将数字文本转换为整数边长。
side1 = int(input("Enter side 1: "))
# 按原题提示读取第二条边，并将输入的文本转换为整数。
side2 = int(input("Enter side 2: "))
# 按原题提示读取第三条边，并将输入的文本转换为整数。
side3 = int(input("Enter side 3: "))
# 三组两边之和中，只要有一组小于或等于第三边，就无法组成三角形；等号也必须排除。
if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    # 记录无效三角形的英文结果。
    result = "Invalid triangle"
# 通过有效性检查后，先检查三边全部相等。
elif side1 == side2 and side2 == side3:
    # 三边相等时记录等边三角形结果。
    result = "Equilateral triangle"
# 等边情况已排除，所以此时任意一对相等就表示恰有两边相等。
elif side1 == side2 or side1 == side3 or side2 == side3:
    # 记录等腰三角形结果。
    result = "Isosceles triangle"
# 有效且没有任何两边相等，只能是三边各异。
else:
    # 记录不等边三角形结果。
    result = "Scalene triangle"
# 按原样例在用户输入和分类结果之间留一空行。
print()
# 显示唯一的分类结果。
print(result)
