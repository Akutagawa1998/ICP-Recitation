# 第 11 题：Password Generator，内层使用 for 循环，遇到 0 终止。
# 教学目的：外层处理多次长度请求，内层用 for 循环精确生成 X 个随机数字字符。
# 解题方法：外层 while True 反复询问长度，输入 0 时用 break 停止；内层 for 循环逐位拼接密码。
# 关于 F 标签：原题标注 F，但请求次数事先未知，所以外层由终止值 0 控制；题目要求的 for 循环用于生成每个密码的 X 位数字。
# 常见错误：把密码保存为整数而丢失前导 0，或把随机范围写成 1 到 9。
# 说明：密码每次运行都随机产生；课堂演示若需要固定结果，可在调用函数前执行 random.seed(411)。

# 导入标准库 random，以生成 0 到 9 的随机数字。
import random

# 定义函数，所有长度都由用户在循环中输入。
def generate_passwords():
    # while True 表示“一直重复”，真正的停止条件写在循环体里的 break。
    while True:
        # 按原题提示读取密码长度，并用 int 转成整数。
        password_size = int(input("Password size? > "))
        # 长度为 0 时按原题终止，不生成新密码。
        if password_size == 0:
            # break 立即结束外层 while 循环，程序随之结束。
            break
        # 使用字符串累积，确保随机数字 0 可以保留在开头。
        password = ""
        # 内层 for 循环精确执行 password_size 次，每次生成一位。
        for _ in range(password_size):
            # randint(0, 9) 包含 0 和 9 两端。
            digit = random.randint(0, 9)
            # 将数字转成字符并追加到密码末尾；字符串的 + 是拼接而不是相加。
            password = password + str(digit)
        # 显示本次生成的完整密码。
        print(password)

# 运行密码生成器；例如依次输入 4、9、1、0。
generate_passwords()
