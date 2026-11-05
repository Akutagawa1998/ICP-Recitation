# 第 6 题：洛书幻方，练习二维列表与多条件验证。
# 教学目的：把尺寸、取值唯一性、行列与两条对角线规则逐一转化为检查。
# 总体思路：遇到任意违反规则的情况就返回 False，所有检查都通过才返回 True。
# 常见错误：只检查行，漏掉列或第二条对角线；全是 5 的表格虽然和相同却不符合数字规则。

# %% R08-E06
# 任务：判断二维数字列表是否为 3 行 3 列且恰好含 1 至 9 的洛书幻方。
# 思路：1 至 9 的总和为 45，三行的公共和必为 15；之后逐行、逐列和逐对角线验证。
# 易错点：输入按题目假定为二维数字列表；尺寸错误、重复值、越界值都应判为 False。
# 定义返回布尔结果的检查函数，grid 保存待判断的二维列表。
def is_lo_shu(grid):
    # 洛书必须恰好有三行；行数不符可以立即排除。
    if len(grid) != 3:
        # 返回 False 表示至少一项规则失败。
        return False
    # 逐行检查，确保每一行都具有三个元素。
    for row in grid:
        # 任何一行长度不为 3，整个表格就不是 3 乘 3。
        if len(row) != 3:
            # 在访问固定位置前先排除尺寸问题，避免索引越界。
            return False
    # 建立临时一维列表，用于一次检查九个数字是否恰好各出现一次。
    values = []
    # 先逐行读取二维列表。
    for row in grid:
        # 再逐个读取该行的数字。
        for number in row:
            # 保存每个元素，以便排序后与 1 至 9 比较。
            values.append(number)
    # 排序后的列表必须严格对应 1、2、3、4、5、6、7、8、9。
    if sorted(values) != list(range(1, 10)):
        # 重复、缺失或越界都会使这一条件成立。
        return False
    # 每一行的数字之和都必须为 15。
    for row in grid:
        # 使用 sum 得到当前行的三个数字之和。
        if sum(row) != 15:
            # 只要一行不符合，就无需继续检查。
            return False
    # 用列索引 0、1、2 依次检查三列。
    for column in range(3):
        # 从三行中取同一列的元素并相加。
        column_total = grid[0][column] + grid[1][column] + grid[2][column]
        # 每一列也必须达到同一个和 15。
        if column_total != 15:
            # 列和不符即判定失败。
            return False
    # 第一条对角线从左上到右下，索引为 00、11、22。
    if grid[0][0] + grid[1][1] + grid[2][2] != 15:
        # 第一条对角线不符合即判定失败。
        return False
    # 第二条对角线从右上到左下，索引为 02、11、20。
    if grid[0][2] + grid[1][1] + grid[2][0] != 15:
        # 第二条对角线同样不能漏检。
        return False
    # 到这里说明全部规则都满足，返回 True。
    return True

# 使用原 PDF 图中的三行数字作为正例。
magic_square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
# 原图九个数字恰好各出现一次，所有规定的和均为 15，因此显示 True。
print("Source square:", is_lo_shu(magic_square))
# 九个 5 的行列与对角线和都为 15，但数字重复，因此显示 False。
print("Repeated values:", is_lo_shu([[5, 5, 5], [5, 5, 5], [5, 5, 5]]))
# 此表格含 1 至 9 且行列和为 15，但对角线不符，因此显示 False。
print("Wrong diagonals:", is_lo_shu([[1, 5, 9], [6, 7, 2], [8, 3, 4]]))
# 只有两行，不满足 3 乘 3 尺寸，因此显示 False。
print("Wrong size:", is_lo_shu([[4, 9, 2], [3, 5, 7]]))
# 把最后一个 6 改成 10，会违反范围和唯一性条件，因此显示 False。
print("Out of range:", is_lo_shu([[4, 9, 2], [3, 5, 7], [8, 1, 10]]))
