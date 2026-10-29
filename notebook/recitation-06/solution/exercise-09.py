# 练习 9：Sentence Capitalizer
# 教学目的：使用布尔状态跟踪句子开头，理解字符串不可变时如何构造结果。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：使用 capitalize 把 Joe 变小写；使用 title 改动每个词；遇到句号后的空格就过早取消等待状态。

# 根据明确约定的句界规则返回新字符串。
def capitalize_sentences(text):
    # 用空字符串保存逐步构造的结果。
    result = ""
    # 文本开始时，下一个字母视为句首。
    needs_capital = True
    # 保留原顺序逐个处理字符。
    for character in text:
        # 只有等待句首且遇到字母时才大写。
        if needs_capital and character.isalpha():
            # 把当前句首字母转换为大写。
            character = character.upper()
            # 本句句首已处理，其他字母保持原样。
            needs_capital = False
        # 遇到约定的句末标点后准备处理下一句。
        if character in ".?!":
            # 空格和其他标点不会取消这个等待状态。
            needs_capital = True
        # 把当前字符加入新字符串，保留其他大小写和空白。
        result += character
    # 返回新字符串，而不修改原输入字符串。
    return result

# 保留题目给出的完整原始示例。
text = "hello my name is Joe. what is your name?"
# 显示句首大写且 Joe 保持原样的结果。
print(capitalize_sentences(text))
