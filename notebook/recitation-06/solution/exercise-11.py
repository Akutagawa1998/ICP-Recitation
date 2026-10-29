# 练习 11：Armstrong Numbers
# 教学目的：把取位数、取数字、谓词判断和汇总统计拆成可复用的函数，完整处理零与空结果。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：把 0 当作零位数；先破坏 n 再求 k；把末位提取写成 /；漏掉 end；只打印数字却漏报数量和总和；没有结果时除零。
# 子项顺序：R06-E11-P01、R06-E11-P02、R06-E11-P03、R06-E11-P04、R06-E11-P05

# 用整数循环计算非负整数的十进制位数。
def count_digits(n):
    # 零需要单独处理，否则下面的循环一次也不执行。
    if n == 0:
        # 题目明确规定零是一位数。
        return 1
    # 对非零整数，已经统计的位数从零开始。
    count = 0
    # 只要还有未去掉的数字，就继续统计。
    while n > 0:
        # 每次循环对应当前的一位。
        count += 1
        # 整除十去掉末位，逐步让整数变成零。
        n //= 10
    # 返回完成循环后得到的位数。
    return count

# 计算各位数字的 k 次方之和。
def digit_power_sum(n):
    # 先确定原整数位数，不能等去位后再计算。
    k = count_digits(n)
    # 各位幂的求和从零开始。
    total = 0
    # 每轮处理当前整数的末位数字。
    while n > 0:
        # 除十余数就是当前末位。
        digit = n % 10
        # 将末位的 k 次方加入总和。
        total += digit ** k
        # 去掉处理过的末位，准备下一轮。
        n //= 10
    # 零不进入循环而返回零，也等于零的一次方。
    return total

# 用一个布尔比较表达 Armstrong 数的定义。
def is_armstrong(n):
    # 原数等于各位幂之和时返回 True，否则 False。
    return n == digit_power_sum(n)

# 在包含两端的非负区间中寻找并汇总结果。
def report_armstrong(start, end):
    # 匹配数量从零开始。
    count = 0
    # 匹配整数总和从零开始。
    total = 0
    # 打印结果标题，使后面的逐行数字含义明确。
    print("Armstrong numbers:")
    # 结束位置加一，确保把 end 本身也检查。
    for number in range(start, end + 1):
        # 调用判断函数，仅处理满足定义的整数。
        if is_armstrong(number):
            # 按从小到大的顺序显示当前匹配数。
            print(number)
            # 每发现一个匹配就增加数量。
            count += 1
            # 同时将这个数加入统计总和。
            total += number
    # 即使没有匹配也显示数量零。
    print("Count:", count)
    # 显示匹配数总和，无匹配时保持零。
    print("Sum:", total)
    # 只有数量非零时平均数才有定义。
    if count > 0:
        # 用总和除以匹配数量计算平均数。
        mean = total / count
        # 按题目要求保留两位小数。
        print(f"Mean: {mean:.2f}")
    # 没有匹配时不能执行除以零。
    else:
        # 用清楚的英文标记表示平均数不存在。
        print("Mean: N/A")

# 保留原框架的主程序结构，组织输入和报告调用。
def main():
    # 可编辑下界；交互演示时可换成 int(input("Enter start: "))。
    start = 0
    # 可编辑上界；交互演示时可换成 int(input("Enter end: "))。
    end = 500
    # 使用真正的函数调用替换框架中的英文说明。
    report_armstrong(start, end)

# 调用主程序，使整段示例可以直接运行。
main()
