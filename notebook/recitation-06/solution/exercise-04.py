# Mock Midterm 原题 Question 7：Message Compressor。
# 概念：按顺序遍历字符串、连续组状态、字符串拼接、循环结束后的收尾。
# 教学目的：理解“连续出现”与“整串总次数”不同，先保存旧组再开启新组。
# 易错点：遗漏最后一组；把不相邻的 a 合并；漏写次数 1；混淆 A 与 a。
# 空消息输出空压缩串是自然边界行为，不额外要求必须缩短字符串或解压。
# 不使用列表、字符串方法、字典、集合或自定义函数；str(count) 是类型转换。

# 按原题提示读取用户的消息，保留字符的大小写与空格；直接回车得到空字符串。
message = input("Enter a message: ")
# 从空字符串开始累加压缩结果。
compressed = ""
# 用空字符串初始化当前组字符；读取首字符时会建立第一组。
current = ""
# 初始化当前组计数为 0，表示还没有读到任何字符。
count = 0
# 从左到右逐个读取字符，不使用字符串方法。
for character in message:
    # 判断字符是否与当前组相同；大小写直接比较，因而 A 与 a 不同。
    if character == current:
        # 相同字符延续当前连续组，把计数增加 1。
        count += 1
    # 字符变化时，需要结束上一组并建立下一组。
    else:
        # 计数大于 0 才表示真的有上一组，避免在开头输出空组。
        if count > 0:
            # 把上一组的字符与次数转成文本拼接到结果；次数 1 也保留。
            compressed += current + str(count)
        # 保存新字符作为下一组的字符。
        current = character
        # 新组已经读到了当前字符，所以计数从 1 开始。
        count = 1
# 循环结束后若存在组，就必须再保存最后一组；空输入的计数仍是 0。
if count > 0:
    # 把最后一组追加到结果，避免遗漏尾部字符。
    compressed += current + str(count)
# 使用样例要求的标签输出压缩字符串。
print("Compressed:", compressed)
