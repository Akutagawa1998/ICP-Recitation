# Mock Midterm 原题 Question 6：Digit Counter。
# 概念：% 取末位、// 去末位、循环条件、条件计数。
# 教学目的：不转成列表或调用字符串方法，也能逐位处理一个正整数。
# 易错点：把 >= 写成 >；只在符合条件时删除一位会造成死循环；/ 不等于 //。
# 原题 n 为正整数，因此不扩展到 n=0 或负数；k 在 0 到 9 之间。
# 不使用列表、字符串方法、字典、集合或自定义函数。

# 按原题提示读取正整数 n；input 返回文本，int 将其转换为可以取余和整除的整数。
number = int(input("Enter a positive integer: "))
# 按原题提示读取阈值 k 并转成整数；题目假设用户输入 0 到 9。
threshold = int(input("Enter a threshold (0-9): "))
# 复制待处理数字，逐位删除时仍保留原始 number 以便讲解。
remaining = number
# 用整数 0 初始化满足条件的数字个数。
count = 0
# 只要剩余数字为正，就还有一位需要检查。
while remaining > 0:
    # 对 10 取余，得到最右侧的一位数字。
    digit = remaining % 10
    # “大于等于”必须使用 >=，等于阈值也要计数。
    if digit >= threshold:
        # 当前位符合条件，把计数增加 1。
        count += 1
    # 整除 10 去掉最右侧一位；放在 if 外保证每轮都会前进。
    remaining //= 10
# 按样例标签显示本次输入的计数；输入原题数字且阈值为 3 时应得到 9。
print("Count:", count)
