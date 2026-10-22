# 第 6 题：使用原题给出的递减算法计算最大公约数。
# 教学目的：把自然语言伪代码翻译成 while 条件、状态更新和循环后结果。
# 解题方法：从两个正整数中较小者开始，直到候选数同时整除两数。
# 常见错误：把循环条件中的 or 写成 and，导致只整除一个数时就错误停止。

# 定义函数，两个参数都按原题假设为正整数。
def greatest_common_divisor(first_number, second_number):
    # 从较小的输入开始，保证候选数不会大于任一输入。
    divisor = min(first_number, second_number)
    # 只要至少有一个数不能被候选数整除，就继续向下搜索。
    while first_number % divisor != 0 or second_number % divisor != 0:
        # 将候选除数减一，检查下一个更小的正整数。
        divisor = divisor - 1
    # 循环结束时 divisor 同时整除两数，因此它是从上向下找到的最大值。
    return divisor

# 按原题要求读取第一个正整数，并用 int 把输入的字符串转成整数。
first_number = int(input("Enter the first positive integer: "))
# 读取第二个正整数，同样转成整数。
second_number = int(input("Enter the second positive integer: "))
# 显示两数的最大公约数；例如输入 84 和 30 时显示 6。
print("Greatest common divisor:", greatest_common_divisor(first_number, second_number))
