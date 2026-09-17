# 第 8 题：Roulette Wheel Colors
# Exercise 8: Roulette Wheel Colors

# 覆盖范围验证、嵌套判断和余数；目的：先确定号码所在区间，再根据奇偶选择颜色。不要将所有奇数都判红；0 要单独处理。
# Coverage: range validation, nested decisions, and remainder. Purpose: locate the interval before using parity to choose the color. Odd does not always mean red; handle 0 separately.

# 保存整数号码 18，测试第二段的右端点及偶数规则。
# Store integer pocket 18 to test the second interval endpoint and its even-number rule.
pocket = 18
# 小于 0 或大于 36 任一条件成立就越界，先排除无效号码。
# A number below 0 or above 36 is out of range; reject it first.
if pocket < 0 or pocket > 36:
    # 显示允许范围，避免无效号码误入后面的颜色分支。
    # Display the allowed range so an invalid pocket cannot enter a later color branch.
    print("Error: enter an integer from 0 to 36.")
# 合法范围中先处理特殊号码 0。
# Within the valid range, handle the special pocket 0 first.
elif pocket == 0:
    # 号码 0 固定输出绿色，不使用奇偶规则。
    # Pocket 0 always displays green without applying parity rules.
    print("Green")
# 前面的分支已排除更小号码，这一段覆盖 1 到 10，保留原题的区间顺序。
# Earlier branches exclude smaller pockets, so this branch covers 1 through 10, preserving the source interval order.
elif pocket <= 10:
    # 用 % 计算除以 2 的余数；非负整数余数为 1 表示奇数。
    # Use % to find the remainder after division by 2; remainder 1 means an odd nonnegative integer.
    if pocket % 2 == 1:
        # 此区间的奇数输出 Red。
        # Display Red for odd pockets in this interval.
        print("Red")
    # 余数不为 1 时，该合法整数为偶数。
    # If the remainder is not 1, the valid integer pocket is even.
    else:
        # 此区间的偶数输出 Black。
        # Display Black for even pockets in this interval.
        print("Black")
# 前面的分支已排除更小号码，这一段覆盖 11 到 18，保留原题的区间顺序。
# Earlier branches exclude smaller pockets, so this branch covers 11 through 18, preserving the source interval order.
elif pocket <= 18:
    # 用 % 计算除以 2 的余数；非负整数余数为 1 表示奇数。
    # Use % to find the remainder after division by 2; remainder 1 means an odd nonnegative integer.
    if pocket % 2 == 1:
        # 此区间的奇数输出 Black。
        # Display Black for odd pockets in this interval.
        print("Black")
    # 余数不为 1 时，该合法整数为偶数。
    # If the remainder is not 1, the valid integer pocket is even.
    else:
        # 此区间的偶数输出 Red。
        # Display Red for even pockets in this interval.
        print("Red")
# 前面的分支已排除更小号码，这一段覆盖 19 到 28，保留原题的区间顺序。
# Earlier branches exclude smaller pockets, so this branch covers 19 through 28, preserving the source interval order.
elif pocket <= 28:
    # 用 % 计算除以 2 的余数；非负整数余数为 1 表示奇数。
    # Use % to find the remainder after division by 2; remainder 1 means an odd nonnegative integer.
    if pocket % 2 == 1:
        # 此区间的奇数输出 Red。
        # Display Red for odd pockets in this interval.
        print("Red")
    # 余数不为 1 时，该合法整数为偶数。
    # If the remainder is not 1, the valid integer pocket is even.
    else:
        # 此区间的偶数输出 Black。
        # Display Black for even pockets in this interval.
        print("Black")
# 前面的分支已排除更小号码，这一段覆盖 29 到 36，保留原题的区间顺序。
# Earlier branches exclude smaller pockets, so this branch covers 29 through 36, preserving the source interval order.
else:
    # 用 % 计算除以 2 的余数；非负整数余数为 1 表示奇数。
    # Use % to find the remainder after division by 2; remainder 1 means an odd nonnegative integer.
    if pocket % 2 == 1:
        # 此区间的奇数输出 Black。
        # Display Black for odd pockets in this interval.
        print("Black")
    # 余数不为 1 时，该合法整数为偶数。
    # If the remainder is not 1, the valid integer pocket is even.
    else:
        # 此区间的偶数输出 Red。
        # Display Red for even pockets in this interval.
        print("Red")

