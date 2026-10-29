# 练习 4：Maximum of Two Values
# 教学目的：把条件选择封装为有返回值的函数，理解函数结果与打印结果的区别。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：只处理大于而漏掉相等；函数只打印没有返回；使用字符串比较而没有转成整数。

# 接收两个整数，返回其中较大的值。
def max_of_two_numbers(first, second):
    # 第一项更大或两项相等时，选择第一项。
    if first >= second:
        # 直接把第一项交回调用处。
        return first
    # 其余情况说明第二项严格更大。
    else:
        # 返回第二项，保证所有分支都有返回值。
        return second

# 用题目给出的第一个整数作为可编辑输入。
first_number = 7
# 用题目给出的第二个整数作为可编辑输入。
second_number = 12
# 调用函数并保存较大值。
result = max_of_two_numbers(first_number, second_number)
# 在调用处显示结果十二。
print("Greater value:", result)
