# 第 7 题：预测五段 for 循环程序的精确输出。
# 教学目的：练习 range 边界、嵌套循环、continue、break、整除和缩进。
# 解题方法：按原代码逐步更新变量并运行，程序顺序与 PDF 完全一致。
# 常见错误：把 range 的 stop 当成包含，或忽略 print 位于循环内部还是外部。

# 子题 1：把偶数 20 到 4 累加；保留原题变量名 sum。
sum = 0
# 从 20 开始每次减 2，stop 2 不包含。
for i in range(20, 2, -2):
    # 将当前偶数加入累计值。
    sum += i
# 循环后显示总和 108。
print(sum)

# 子题 2：外层循环产生三行。
for i in range(0, 3):
    # 每行先显示 i+1，并保留在当前行。
    print(i + 1, end=" ")
    # 内层 j 从 3 递减到 i+1，因为 stop i 不包含。
    for j in range(3, i, -1):
        # 显示 j+1，并继续留在当前行。
        print(j + 1, end=" ")
    # 内层结束后换行，完成本行输出。
    print()

# 子题 3：重新把累计值设为 0，仍保留原题变量名。
sum = 0
# 依次检查 1 到 14，stop 15 不包含。
for i in range(1, 15):
    # 数字文本中含 4 时跳过本轮剩余语句。
    if '4' in str(i):
        # continue 使 4 和 14 不参与累计与打印。
        continue
    # 数字文本中含 9 时终止整个循环。
    if '9' in str(i):
        # break 使 9 以及后续数字都不再处理。
        break
    # 只有没有触发 continue 或 break 的数字才加入累计值。
    sum += i
    # print 在循环内部，因此每次成功累计后都显示一行。
    print(i, sum)

# 子题 4：从整数 1 开始反复乘法和向下取整除法。
result = 1
# 外层依次把字符 1、2、3 赋给 c。
for c in "123":
    # 每个 c 都配合字符 3、2、1 完整执行内层循环。
    for d in "321":
        # 先把 result 乘以当前 c 转换得到的整数。
        result *= int(c)
        # 再把 result 对当前 d 做向下取整除法并写回。
        result //= int(d)
# 第一次 1//3 已变成 0，后续一直为 0，因此最终显示 0。
print(result)

# 子题 5：保存数字字符串和初始累计值。
s, t = "12345", 0
# i 从 1 到 5，用 len(s)-i 从右向左访问全部字符。
for i in range(1, 6):
    # 把当前字符转成整数并加入累计值。
    t += int(s[len(s) - i])
    # print 在循环内部，因此依次显示 5、9、12、14、15。
    print(t)
