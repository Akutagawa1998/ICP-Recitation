# 第 1 题：预测嵌套 while 循环的输出。
# 教学目的：理解外层索引 i 如何跳到下一段，以及内层索引 j 如何找到连续相同字符的末尾。
# 解题方法：每一段只保留第一个字符，再把 i 更新为 j。
# 常见错误：误以为程序会删除字符串中所有重复字符；它只压缩相邻的连续重复段。

# 定义函数，把每一段连续相同字符压缩成一个字符。
def keep_one_character_per_run(text):
    # 保存逐段拼接得到的最终字符串。
    result = ""
    # 让 i 指向当前连续字符段的第一个字符。
    i = 0
    # 只要 i 仍在字符串有效范围内，就继续处理下一段。
    while i < len(text):
        # 让 j 从 i 后面的字符开始寻找当前段的末尾。
        j = i + 1
        # 当 j 未越界且字符仍与当前段首字符相同时，继续向右移动。
        while j < len(text) and text[j] == text[i]:
            # 将 j 右移一位，以检查下一个字符。
            j = j + 1
        # 当前段只保留 text[i]，并追加到结果字符串。
        result = result + text[i]
        # 将 i 跳到下一段的起点，而不是只前进一位。
        i = j
    # 返回压缩连续重复段后的字符串。
    return result

# 与原题程序一样，用 input 读取用户输入的字符串；input 返回的本来就是字符串，不需要转换。
# 原题表格有三个输入，因此本文件需要运行三次，每次输入其中一个字符串。
text = input("Enter a string: ")
# 调用函数并显示压缩连续重复段后的结果，例如输入 aabbccddeeff 时显示 abcdef。
print(keep_one_character_per_run(text))
