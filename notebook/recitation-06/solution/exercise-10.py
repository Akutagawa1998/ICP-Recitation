# 练习 10：Most Frequent Character
# 教学目的：同时完成频率最大值搜索与条件计数，理解平局规则如何由比较符号决定。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：使用 >= 使平局答案变成最后一个；忽略空串索引错误；元音判断漏掉大写；未经声明忽略空格。
# 子项顺序：R06-E10-P01、R06-E10-P02

# 返回最频繁字符，平局时保留最早出现者。
def most_frequent_character(text):
    # 空字符串没有字符，必须先单独处理。
    if text == "":
        # 用 None 表示不存在最频繁字符。
        return None
    # 非空时可以安全地把首字符作为暂时答案。
    best_character = text[0]
    # 暂时最大次数从零开始。
    best_count = 0
    # 按原字符串顺序考察字符，保留平局优先顺序。
    for character in text:
        # 使用题目提示的方法统计该字符总次数。
        current_count = text.count(character)
        # 仅严格更多时更新，相等时不覆盖较早字符。
        if current_count > best_count:
            # 保存新的最高频字符。
            best_character = character
            # 同时保存它的出现次数。
            best_count = current_count
    # 遍历结束后返回字符本身。
    return best_character

# 统计英文元音，大小写都包括在内。
def count_vowels(text):
    # 元音计数从零开始。
    total = 0
    # 先统一小写，便于使用一组元音字符判断。
    for character in text.lower():
        # 只有五个约定的英文元音才计数。
        if character in "aeiou":
            # 每遇到一个元音就把计数增加一。
            total += 1
    # 返回元音总数，而不是在函数内打印。
    return total

# 可编辑示例包含大小写字母和一个空格。
text = "Hello World"
# 调用频率函数取得答案或 None。
character = most_frequent_character(text)
# 先判断空字符串对应的特殊返回值。
if character is None:
    # 为空输入显示明确的英文提示。
    print("No most frequent character.")
# 非空输入时可以显示得到的字符。
else:
    # repr 让空格等字符也能清楚显示。
    print("Most frequent character:", repr(character))
# 调用元音函数并显示计数。
print("Vowels:", count_vowels(text))
