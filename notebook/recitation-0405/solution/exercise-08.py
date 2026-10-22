# 第 8 题：使用嵌套 for 循环绘制四种图案。
# 教学目的：先为每一层循环分配一个职责，再控制字符数、空格和字母状态。
# 解题方法：四个子题分别封装为函数，按原题顺序排列，并像原题样例一样让用户输入大小。
# 常见错误：用字符串乘法绕过 nested loops 要求，或在每一行重置字母索引。

# 子题 1：定义逐行减少星号数量的函数。
def draw_decreasing_stars(rows):
    # number_of_stars 从 rows 递减到 1。
    for number_of_stars in range(rows, 0, -1):
        # 内层循环负责打印本行指定数量的星号。
        for _ in range(number_of_stars):
            # 使用空 end，让同一行的星号相邻。
            print("*", end="")
        # 本行星号完成后换行。
        print()

# 按原题提示读取行数，并用 int 转成整数；原题样例输入 5。
rows = int(input("Enter the number of rows: "))
# 使用用户输入的行数绘制第一个图案。
draw_decreasing_stars(rows)

# 子题 2：定义两个 # 之间空格逐行增加的函数。
def draw_widening_hashes(rows):
    # row_index 从 0 开始，因此正好等于本行内部空格数。
    for row_index in range(rows):
        # 先显示每行左侧的 #，并留在当前行。
        print("#", end="")
        # 内层循环显示 row_index 个空格。
        for _ in range(row_index):
            # 每次打印一个空格，使右侧 # 逐行右移。
            print(" ", end="")
        # 显示右侧 # 并自动换行；第 0 行因此得到 ##。
        print("#")

# 读取第二个图案的行数；原题样例输入 6。
rows = int(input("Enter the number of rows: "))
# 使用用户输入的行数绘制第二个图案。
draw_widening_hashes(rows)

# 子题 3：定义字母持续递增并在 Z 后回到 A 的三角形函数。
def draw_letter_triangle(rows):
    # 全局字母索引在不同行之间持续，不在每行重置。
    letter_index = 0
    # row_number 从 1 到 rows，表示本行字母数量。
    for row_number in range(1, rows + 1):
        # 先打印 rows-row_number 个领先空格，使图形向右对齐。
        for _ in range(rows - row_number):
            # 每次输出一个领先空格且不换行。
            print(" ", end="")
        # 再按本行需要的字母数量逐个输出。
        for column_index in range(row_number):
            # 除第一个字母外，在相邻字母之间加入一个空格。
            if column_index > 0:
                # 打印字母间隔并留在当前行。
                print(" ", end="")
            # 用模 26 把任意索引映射回 A 到 Z。
            letter = chr(ord("A") + letter_index % 26)
            # 显示当前字母且暂不换行。
            print(letter, end="")
            # 全局索引加一，下一位置使用下一个字母。
            letter_index = letter_index + 1
        # 本行所有字母完成后换行。
        print()

# 读取字母三角形的行数；原题样例输入 8。
rows = int(input("Enter the number of rows: "))
# 使用用户输入的行数绘制字母三角形。
draw_letter_triangle(rows)

# 子题 4：定义连续绘制 N 个、每个大小为 M 的三角形函数。
def draw_triangles(number_of_triangles, triangle_size):
    # 最外层循环控制一共绘制多少个三角形。
    for _ in range(number_of_triangles):
        # 中层循环控制当前三角形的行号 1 到 M。
        for row_number in range(1, triangle_size + 1):
            # 最内层循环在本行打印 row_number 个星号。
            for _ in range(row_number):
                # 星号连续输出，不自动换行。
                print("*", end="")
            # 每一行完成后换行；三角形之间不额外输出空行。
            print()

# 按原题提示读取三角形个数 N；原题样例输入 3。
number_of_triangles = int(input("Enter the number of triangles: "))
# 按原题提示读取每个三角形的大小 M；原题样例输入 3。
triangle_size = int(input("Enter the size of one triangle: "))
# 使用用户输入的 N 和 M 绘制最后一个图案。
draw_triangles(number_of_triangles, triangle_size)
