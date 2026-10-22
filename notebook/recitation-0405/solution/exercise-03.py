# 第 3 题：Fibonacci，分别使用 while 和 for 循环。
# 教学目的：把 F_n = F_(n-1) + F_(n-2) 的递推关系转成可更新的程序状态。
# 本材料约定：输出 F_0 到 F_n，因此用户输入 8 时会得到 9 个值。
# 常见错误：只输出 n 个值，或计算新值时使用错误的前两个索引。

# 定义 while 版本，参数 n 是最后一个 Fibonacci 下标。
def fibonacci_through_while(n):
    # 先保存递推定义直接给出的 F_0 和 F_1。
    sequence = [0, 1]
    # 下标 2 是第一个需要用递推关系计算的位置。
    index = 2
    # 只要 index 不超过 n，就继续补充序列。
    while index <= n:
        # 用前两个已经保存的值计算当前 Fibonacci 值。
        next_value = sequence[index - 1] + sequence[index - 2]
        # 将新值追加到列表末尾，供下一轮继续使用。
        sequence.append(next_value)
        # 下标加一，准备计算下一项并保证循环结束。
        index = index + 1
    # 截取到 n+1，兼容题目要求的正整数 n，并明确包含 F_n。
    return sequence[:n + 1]

# 按原题要求让用户输入严格正整数 n；input 返回字符串，所以用 int 转成整数。
n = int(input("Enter a strictly positive integer n: "))
# 显示 while 版本从 F_0 到 F_n 的结果；输入 8 时显示 [0, 1, 1, 2, 3, 5, 8, 13, 21]。
print(fibonacci_through_while(n))

# 定义 for 版本，参数 n 同样表示最后一个下标。
def fibonacci_through_for(n):
    # 保存 F_0 和 F_1，作为递推起点。
    sequence = [0, 1]
    # range 从 2 到 n（包含 n），逐项计算后续值。
    for index in range(2, n + 1):
        # 使用当前下标之前的两个列表元素计算新值。
        next_value = sequence[index - 1] + sequence[index - 2]
        # 把新值保存到序列末尾。
        sequence.append(next_value)
    # 返回包含 F_0 和 F_n 的完整片段。
    return sequence[:n + 1]

# for 版本同样读取用户输入的 n；输入相同的数即可直接比较两个实现。
n = int(input("Enter a strictly positive integer n: "))
# 显示 for 版本的 Fibonacci 值，应与 while 版本完全一致。
print(fibonacci_through_for(n))
