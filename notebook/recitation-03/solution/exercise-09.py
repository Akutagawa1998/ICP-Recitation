# 第 9 题：Software Sales
# Exercise 9: Software Sales

# 原题只有售价与折扣表，没有完整任务；补充教学任务是计算订单小计、折扣金额与应付总额。假设数量为非负整数、少于 10 件无折扣，所选折扣适用于整个订单。
# The source gives only the price and discount table. The added teaching task computes subtotal, discount amount, and final total. Assume a nonnegative integer quantity, no discount below 10, and one selected discount applied to the entire order.

# 目的：把文字区间转成互斥分支，区分折扣率、折扣金额与应付金额。最终格式 .2f 仅让金额显示两位小数，不改变公式。
# Purpose: translate ranges into exclusive branches and distinguish the rate, discount amount, and amount due. Formatting with .2f displays two decimal places without changing the formula.

# 保存订单数量 25，落在原表 20 到 49 这一档。
# Store order quantity 25, within the source table interval 20 through 49.
quantity = 25
# 保存原题规定的单价 99 美元，不改变样例数据。
# Store the original unit price of 99 dollars.
unit_price = 99
# 按明确补充的规则，少于 10 件没有折扣。
# Apply the explicitly added rule: quantities below 10 receive no discount.
if quantity < 10:
    # 零折扣率意味着折扣金额为 0。
    # A zero rate means the discount amount is zero.
    discount_rate = 0.0
# 前面已排除少于 10，因此这一档覆盖 10 到 19。
# The earlier branch excluded quantities below 10, so this covers 10 through 19.
elif quantity < 20:
    # 把 10% 写成小数 0.10，以便参与乘法。
    # Write 10% as decimal 0.10 for multiplication.
    discount_rate = 0.10
# 这一档覆盖 20 到 49，当前数量 25 进入此分支。
# This interval covers 20 through 49; sample quantity 25 selects it.
elif quantity < 50:
    # 保存 20% 折扣率，而不是把应付比例 80% 当作折扣率。
    # Store the 20% discount rate, not the 80% fraction still payable.
    discount_rate = 0.20
# 这一档覆盖 50 到 99，100 不属于此档。
# This interval covers 50 through 99; it does not include 100.
elif quantity < 100:
    # 保存 30% 折扣率。
    # Store the 30% discount rate.
    discount_rate = 0.30
# 剩余非负整数数量至少为 100，对应最后一档。
# All remaining allowed quantities are at least 100 and belong to the final tier.
else:
    # 保存 40% 折扣率。
    # Store the 40% discount rate.
    discount_rate = 0.40
# 数量乘单价得到折扣前金额；25 乘 99 为 2475。
# Multiply quantity by unit price for the pre-discount amount; 25 times 99 is 2475.
subtotal = quantity * unit_price
# 小计乘折扣率得到减免金额 495.0，注意这不是应付金额。
# Multiply subtotal by the rate for a discount amount of 495.0; this is not the amount due.
discount = subtotal * discount_rate
# 从小计减去折扣金额，得到应付总额 1980.0。
# Subtract the discount from the subtotal to obtain total due, 1980.0.
total = subtotal - discount
# f 字符串在花括号中填入变量，.2f 显示两位小数，输出 2475.00。
# The f-string inserts the variable; .2f displays two decimal places, giving 2475.00.
print(f"Subtotal: ${subtotal:.2f}")
# 以美元与两位小数显示本次减免金额 495.00。
# Display the dollar discount amount with two decimal places: 495.00.
print(f"Discount: ${discount:.2f}")
# 显示最终应付金额 1980.00，便于与手算核对。
# Display final amount due, 1980.00, for comparison with the hand calculation.
print(f"Total: ${total:.2f}")

