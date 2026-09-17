# 第 5 题：Roman Numerals
# Exercise 5: Roman Numerals

# 覆盖离散值匹配与错误分支；目的：按整数 1 到 10 的完整对照表逐项匹配，尤其注意 IV 和 IX。假设输入是整数，不额外处理非数字文本。
# Coverage: matching discrete values and an error branch. Purpose: implement all integers 1 through 10 from the table, especially IV and IX. Assume integer input; parsing nonnumeric text is outside this exercise.

# 保存整数样例 7；交互版使用 int(input("Enter a number from 1 to 10: "))。
# Store integer sample 7; an interactive version uses int(input("Enter a number from 1 to 10: ")).
number = 7
# 检查输入是否等于 1；== 比较数值，不是赋值。
# Test whether the input equals 1; == compares values rather than assigning.
if number == 1:
    # 匹配成功时输出对应罗马数字 I，然后跳过同一链的其他分支。
    # If matched, display Roman numeral I and skip the other branches in the chain.
    print("I")
# 检查输入是否等于 2；== 比较数值，不是赋值。
# Test whether the input equals 2; == compares values rather than assigning.
elif number == 2:
    # 匹配成功时输出对应罗马数字 II，然后跳过同一链的其他分支。
    # If matched, display Roman numeral II and skip the other branches in the chain.
    print("II")
# 检查输入是否等于 3；== 比较数值，不是赋值。
# Test whether the input equals 3; == compares values rather than assigning.
elif number == 3:
    # 匹配成功时输出对应罗马数字 III，然后跳过同一链的其他分支。
    # If matched, display Roman numeral III and skip the other branches in the chain.
    print("III")
# 检查输入是否等于 4；== 比较数值，不是赋值。
# Test whether the input equals 4; == compares values rather than assigning.
elif number == 4:
    # 匹配成功时输出对应罗马数字 IV，然后跳过同一链的其他分支。
    # If matched, display Roman numeral IV and skip the other branches in the chain.
    print("IV")
# 检查输入是否等于 5；== 比较数值，不是赋值。
# Test whether the input equals 5; == compares values rather than assigning.
elif number == 5:
    # 匹配成功时输出对应罗马数字 V，然后跳过同一链的其他分支。
    # If matched, display Roman numeral V and skip the other branches in the chain.
    print("V")
# 检查输入是否等于 6；== 比较数值，不是赋值。
# Test whether the input equals 6; == compares values rather than assigning.
elif number == 6:
    # 匹配成功时输出对应罗马数字 VI，然后跳过同一链的其他分支。
    # If matched, display Roman numeral VI and skip the other branches in the chain.
    print("VI")
# 检查输入是否等于 7；== 比较数值，不是赋值。
# Test whether the input equals 7; == compares values rather than assigning.
elif number == 7:
    # 匹配成功时输出对应罗马数字 VII，然后跳过同一链的其他分支。
    # If matched, display Roman numeral VII and skip the other branches in the chain.
    print("VII")
# 检查输入是否等于 8；== 比较数值，不是赋值。
# Test whether the input equals 8; == compares values rather than assigning.
elif number == 8:
    # 匹配成功时输出对应罗马数字 VIII，然后跳过同一链的其他分支。
    # If matched, display Roman numeral VIII and skip the other branches in the chain.
    print("VIII")
# 检查输入是否等于 9；== 比较数值，不是赋值。
# Test whether the input equals 9; == compares values rather than assigning.
elif number == 9:
    # 匹配成功时输出对应罗马数字 IX，然后跳过同一链的其他分支。
    # If matched, display Roman numeral IX and skip the other branches in the chain.
    print("IX")
# 检查输入是否等于 10；== 比较数值，不是赋值。
# Test whether the input equals 10; == compares values rather than assigning.
elif number == 10:
    # 匹配成功时输出对应罗马数字 X，然后跳过同一链的其他分支。
    # If matched, display Roman numeral X and skip the other branches in the chain.
    print("X")
# 所有 1 到 10 的匹配都失败时进入错误分支。
# Enter the error branch when no integer from 1 through 10 matched.
else:
    # 提示允许范围；0、11 等范围外整数会触发此消息。
    # State the allowed range; integers such as 0 and 11 trigger this message.
    print("Error: enter an integer from 1 to 10.")

