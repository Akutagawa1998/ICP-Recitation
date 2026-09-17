# 第 1 题：Boolean Expression
# Exercise 1: Boolean Expression

# 覆盖比较、逻辑运算、优先级与类型差异；目的：区分本次为真和对所有允许值都为真。先预测，再运行；普通实数不包括 NaN 或特殊自定义对象。
# Coverage: comparisons, Boolean logic, precedence, and types. Purpose: separate a result for given inputs from a universal claim. Predict first, then run; ordinary real values exclude NaN and special custom objects.

# 子题 1a：先解释操作符，再判断结果。
# Part 1a: explain the operators before predicting the result.

# 先算 and 得到 False，再算 or，结果为 False；and 优先于 or。
# Evaluate and before or: both stages produce False.
print(False or True and False)

# 子题 1b：先解释操作符，再判断结果。
# Part 1b: explain the operators before predicting the result.

# 9 < 5 为 False，not 将其变成 True，因此整个 and 为 True。
# 9 < 5 is False; not makes it True, so the conjunction is True.
print(True and not (9 < 5))

# 子题 1c：先解释操作符，再判断结果。
# Part 1c: explain the operators before predicting the result.

# 除法得到 2.0，2.0 >= 2 为真；两个字符串不相等也为真，因此结果 True。
# Division gives 2.0, which is at least 2; the strings differ, so both conditions are True.
print(24 / 12 >= 2 and 'hello' != 'goodbye')

# 子题 1d：先解释操作符，再判断结果。
# Part 1d: explain the operators before predicting the result.

# 整数与这个字符串不相等，结果为 True；跨类型的不等比较允许执行。
# The integer and this string are unequal, so the result is True; this inequality comparison is allowed.
print(55 != 'hello')

# 子题 1e：先解释操作符，再判断结果。
# Part 1e: explain the operators before predicting the result.

# 左边是字符串，右边是整数；== 不会自动把字符串转换为数字，结果 False。
# The left value is a string and the right is an integer; equality does not convert the string, so it is False.
print('2' == 2)

# 子题 1f：相等比较与大小排序不是同一种操作；try/except 只是为了安全展示题目中的错误。
# Part 1f: equality and ordering are different operations; try/except only lets the demonstration report the expected error safely.

# 开始受保护的代码块，避免预期错误中断后面的题目。
# Start a protected block so the expected error does not stop the remaining exercises.
try:
    # 尝试比较字符串与整数的大小；Python 3 会抛出 TypeError，print 不会成功输出布尔值。
    # Try to order a string and an integer; Python 3 raises TypeError before print can display a Boolean.
    print('hello' > 35)
# 只捕获本题预期的类型错误，不把错误当作 False。
# Catch the expected type error only; an error is not the Boolean value False.
except TypeError:
    # 显示英语错误说明，随后程序可继续运行。
    # Display the error explanation in English so execution can continue.
    print("TypeError: strings and integers cannot be ordered.")

# 子题 2a：代入原题 x=10、y=20、z=30，同时检查是否需要 Always。
# Part 2a: substitute the original x=10, y=20, z=30 and check whether Always applies.

# 保存原题给定的 x 值 10，供本组五个表达式使用。
# Store the original value 10 in x for the five expressions in part 2.
x = 10
# 保存原题给定的 y 值 20，供本组五个表达式使用。
# Store the original value 20 in y for the five expressions in part 2.
y = 20
# 保存原题给定的 z 值 30，供本组五个表达式使用。
# Store the original value 30 in z for the five expressions in part 2.
z = 30
# 两个条件在给定值下都为 True，但改成 x=9 就为 False，不标 Always。
# Both conditions are True for the given values, but x=9 makes it False, so do not label it Always.
print((x == 10) and (y > 10))

# 子题 2b：代入原题 x=10、y=20、z=30，同时检查是否需要 Always。
# Part 2b: substitute the original x=10, y=20, z=30 and check whether Always applies.

# 同一个普通实数不能同时小于和大于 10，因此这是 Always False。
# An ordinary real number cannot be both below and above 10; this is Always False.
print("Always False:", x < 10 and x > 10)

# 子题 2c：代入原题 x=10、y=20、z=30，同时检查是否需要 Always。
# Part 2c: substitute the original x=10, y=20, z=30 and check whether Always applies.

# x=10 时两边都为 False；x=9 时为 True，因此本次为 False，但不是 Always False。
# Both sides are False at x=10; x=9 makes it True, so this is False for this input only.
print((x < 10) or (x > 10))

# 子题 2d：代入原题 x=10、y=20、z=30，同时检查是否需要 Always。
# Part 2d: substitute the original x=10, y=20, z=30 and check whether Always applies.

# 给定值下 not(10<50) 与 not(20<=20) 都为 False；x=11 时右边为 True，故不是恒假。
# With the given values, not(10<50) and not(20<=20) are False; x=11 makes the right side True, so it is not always False.
print(not (x < (y + z)) or not ((x + 10) <= 20))

# 子题 2e：代入原题 x=10、y=20、z=30，同时检查是否需要 Always。
# Part 2e: substitute the original x=10, y=20, z=30 and check whether Always applies.

# 10 与 20 不相等且可以排序，结果 True；令 x=y 就为 False，因此不是恒真。
# 10 and 20 differ and are ordered, giving True; setting x=y makes it False, so it is not always True.
print(not (x == y) and (x != y) and (x < y or y < x))

