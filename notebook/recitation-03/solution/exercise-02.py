# 第 2 题：String indexing & slicing
# Exercise 2: String indexing & slicing

# 覆盖索引、负索引、切片、步长与越界；目的：区分单字符索引与半开区间切片。按原表逐行先左后右，共 15 项；repr 保留可见的引号和转义符。
# Coverage: indexing, negative indices, slices, steps, and bounds. Purpose: distinguish one-character indexing from stop-exclusive slicing. Follow the source table row by row, left then right; repr exposes quotes and escapes.

# 子题 01：s[-1]。从字符串末尾向前数，确认负索引对应哪个字符。
# Part 01: s[-1]. Count backward from the end to locate the character at this negative index.

# 逐字保存原题字符串；\n 在内存中是一个换行字符，不是两个字符。
# Store the exact source string; the escape sequence represents one newline character in memory.
s = 'HellO WorlD\n'
# 负索引 -1 指向最后一个字符，即换行符；repr 显示为带引号的 \n。
# Index -1 selects the last character, a newline; repr displays its escape sequence.
print(repr(s[-1]))

# 子题 02：s[5:6]。先圈出起点、终点和步长。
# Part 02: s[5:6]. Identify the start, stop, and step before evaluating.

# 切片包含索引 5，不包含 6，得到一个空格；用 repr 可看见引号之间的空格。
# The slice includes index 5 and excludes 6, giving one space, visible between the repr quotes.
print(repr(s[5:6]))

# 子题 03：s[-2]。找出倒数第二个字符，注意末尾换行也占一个位置。
# Part 03: s[-2]. Locate the second-to-last character, counting the final newline as one position.

# 负索引 -2 指向倒数第二个字符大写 D，注意保持原题大小写。
# Index -2 selects the second-to-last character, uppercase D; preserve the original case.
print(repr(s[-2]))

# 子题 04：s[6:5]。先圈出起点、终点和步长。
# Part 04: s[6:5]. Identify the start, stop, and step before evaluating.

# 默认步长为正 1，从 6 无法向前到达更小的停止位置 5，得到空字符串。
# The default step is positive 1; starting at 6 cannot move forward toward stop 5, so the string is empty.
print(repr(s[6:5]))

# 子题 05：len(s)。数出所有字符，包括空格和换行；这不是切片。
# Part 05: len(s). Count every character, including the space and newline; this is not a slice.

# 计算字符数 12；空格和最后的换行符各占一个字符。
# Count 12 characters; the space and final newline each count as one character.
print(repr(len(s)))

# 子题 06：s[-6:-1]。先圈出起点、终点和步长。
# Part 06: s[-6:-1]. Identify the start, stop, and step before evaluating.

# 负索引 -6 到 -1（不含）对应 WorlD，不包含最后的换行符。
# The slice from -6 up to but not including -1 is WorlD, excluding the newline.
print(repr(s[-6:-1]))

# 子题 07：s[-len(s)]。先求长度，再取负号，最后定位这个索引。
# Part 07: s[-len(s)]. Find the length, negate it, then locate that index.

# len(s) 为 12，因此索引 -12 指向第一个字符 H。
# len(s) is 12, so index -12 selects the first character H.
print(repr(s[-len(s)]))

# 子题 08：s[:5:2]。先圈出起点、终点和步长。
# Part 08: s[:5:2]. Identify the start, stop, and step before evaluating.

# 默认从 0 开始，到 5 之前每次跳 2 位，选索引 0、2、4，得到 HlO。
# Start at 0, stop before 5, and step by 2; indices 0, 2, 4 give HlO.
print(repr(s[:5:2]))

# 子题 09：s[-13]。先判断这个单个索引是否在有效范围内。
# Part 09: s[-13]. First check whether this single index is within the valid range.

# 为预期的越界索引开启错误保护，使后续切片题继续执行。
# Protect the expected out-of-range index so the later slice exercises still run.
try:
    # 长度为 12，最小有效负索引是 -12；-13 会抛出 IndexError。
    # The length is 12 and the lowest valid negative index is -12; -13 raises IndexError.
    print(repr(s[-13]))
# 捕获单字符索引越界错误，区别于允许端点越界的切片。
# Catch the indexing error and distinguish it from slices, which allow oversized endpoints.
except IndexError:
    # 显示英语错误说明，不把错误说成空字符串。
    # Display the English error explanation; an error is not an empty string.
    print("IndexError: string index out of range.")

# 子题 10：s[5::-1]。先圈出起点、终点和步长。
# Part 10: s[5::-1]. Identify the start, stop, and step before evaluating.

# 从索引 5 的空格开始每次向左一位；省略终点可一直包含索引 0，得到空格加 OlleH。
# Start at the space at index 5 and move left; the omitted stop includes index 0, giving a leading space followed by OlleH.
print(repr(s[5::-1]))

# 子题 11：s[:5]。先圈出起点、终点和步长。
# Part 11: s[:5]. Identify the start, stop, and step before evaluating.

# 默认从索引 0 开始，到索引 5 之前停止，得到 HellO。
# Start at index 0 and stop before 5, giving HellO.
print(repr(s[:5]))

# 子题 12：s[-2:-7:-1]。先圈出起点、终点和步长。
# Part 12: s[-2:-7:-1]. Identify the start, stop, and step before evaluating.

# 从 D 向左取索引 -2、-3、-4、-5、-6，不取 -7 的空格，得到 DlroW。
# Move left from D through indices -2 to -6, excluding the space at -7, giving DlroW.
print(repr(s[-2:-7:-1]))

# 子题 13：s[6:500]。先圈出起点、终点和步长。
# Part 13: s[6:500]. Identify the start, stop, and step before evaluating.

# 切片停止位置超出长度时会截到末尾，不会报错；结果是 WorlD 加换行符。
# An oversized slice stop is clipped to the end without an error, giving WorlD followed by the newline.
print(repr(s[6:500]))

# 子题 14：s[:7] + s[7:]。先圈出起点、终点和步长。
# Part 14: s[:7] + s[7:]. Identify the start, stop, and step before evaluating.

# 在索引 7 切分，再用加号连接两个字符串片段，恢复原字符串，包括换行符。
# Split at index 7 and concatenate the two slices to reconstruct the original string, including its newline.
print(repr(s[:7] + s[7:]))

# 子题 15：s[7:]。先圈出起点、终点和步长。
# Part 15: s[7:]. Identify the start, stop, and step before evaluating.

# 从索引 7 的小写 o 取到末尾，结果是 orlD 加换行符。
# Take the suffix from lowercase o at index 7 through the end, giving orlD and a newline.
print(repr(s[7:]))
