# 第 5 题：使用 while 循环统计不重叠子串出现次数。
# 教学目的：根据原题第二个样例判断“匹配后应跳过整个子串”。
# 解题方法：匹配成功前进 len(substring)，失败只前进 1。
# 常见错误：每次都只前进 1，从而把 aaabcaa 中 aa 的重叠匹配算成 3 次。

# 定义函数，参数 text 是完整字符串，substring 是非空目标子串。
def count_non_overlapping(text, substring):
    # 从 0 开始累计成功匹配次数。
    count = 0
    # 从完整字符串的第一个位置开始尝试。
    index = 0
    # 计算仍能容纳完整子串的最后一个起始位置。
    last_start = len(text) - len(substring)
    # 只在子串还能完整放入 text 时继续比较。
    while index <= last_start:
        # 切片与目标相等时，找到一次大小写敏感的匹配。
        if text[index:index + len(substring)] == substring:
            # 匹配计数加一。
            count = count + 1
            # 跳过整个已匹配子串，保证结果不重叠。
            index = index + len(substring)
        # 当前起点没有匹配时，只移动一个字符继续搜索。
        else:
            # 将起点右移一位。
            index = index + 1
    # 返回不重叠匹配总数。
    return count

# 按原题提示读取完整字符串，例如 abcdeabcdeabcde 或 aaabcaa。
text = input("Write a string: ")
# 按原题提示读取要统计的子串，例如 abc 或 aa；本题假设它不是空字符串。
substring = input("Write another string: ")
# 调用函数计算不重叠匹配次数，并保存在描述性变量中。
number_of_matches = count_non_overlapping(text, substring)
# 使用原题英文句式显示结果；两组原题样例分别应得到 3 和 2。
print(f"String '{substring}' appears {number_of_matches} times.")
