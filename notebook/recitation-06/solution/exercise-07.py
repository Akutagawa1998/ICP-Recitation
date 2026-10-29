# 练习 7：Sum of Digits
# 教学目的：区分数字字符串与整数，练习逐字符转换与求和累积。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：直接相加字符串；对整个整数使用 for；把一次循环中的临时值当成最终总和。

# 接收数字字符串，逐位计算数字之和。
def sum_of_digits(text):
    # 求和累积器从零开始。
    total = 0
    # 每轮取得一个数字字符，而不是整个整数。
    for character in text:
        # 把当前字符转换成整数，再加入总和。
        total += int(character)
    # 所有字符处理完后返回数字和。
    return total

# 保留原题示例为字符串，便于逐字符遍历。
digit_text = "2514"
# 调用函数并显示原例结果十二。
print("Sum of digits:", sum_of_digits(digit_text))
