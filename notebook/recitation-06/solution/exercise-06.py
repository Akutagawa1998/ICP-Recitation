# 练习 6：Combination
# 教学目的：理解乘积累积器的初始值、辅助函数复用以及整除与普通除法的区别。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：把乘积初值设成零；range 漏掉 n；用 / 返回浮点数；调用现成 math.factorial 违背练习要求。
# 子项顺序：R06-E06-P01、R06-E06-P02、R06-E06-P03、R06-E06-P04

# 计算非负整数 n 的阶乘，不使用 math 模块。
def factorial(n):
    # 乘积从一开始，也自然覆盖零的阶乘。
    product = 1
    # range 不包含右端点，所以用 n 加一来包含 n。
    for number in range(1, n + 1):
        # 把当前整数乘入累积乘积。
        product *= number
    # 循环结束后返回阶乘；n 为零时返回一。
    return product

# 在整数且零不大于 r 不大于 n 的前提下求组合数。
def combination(n, r):
    # 复用阶乘函数计算分子 n 的阶乘。
    numerator = factorial(n)
    # 分母由两个阶乘相乘构成。
    denominator = factorial(r) * factorial(n - r)
    # 有效组合公式能整除，双斜杠保证结果为整数。
    return numerator // denominator

# 原题第一个例子应得到十。
print(combination(5, 2))
# 原题第二个例子应得到二十。
print(combination(6, 3))
# 原题第三个例子应得到一，检查零的阶乘。
print(combination(4, 0))
