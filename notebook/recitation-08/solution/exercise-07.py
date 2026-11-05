# 第 7 题：学生成绩，练习嵌套记录、类型转换和最高值搜索。
# 教学目的：区分编号等身份字符串、参与计算的数值，以及题目要求返回的平均分字符串。
# 总体思路：第一问生成新的平均成绩记录，第二问在平均记录中按数值比较并返回身份字段。
# 常见错误：直接加成绩字符串、把编号转换成整数，或用字符串大小比较数值。
# 原题修正：John 最后一项 79 与 Joe 最后一项 92 前的弯引号改成 ASCII 引号，数值不变。
# 补充约定：最高平均分并列时保留原顺序第一人；空列表时 highestAverage 返回 []。

# %% R08-E07-P01
# 任务：实现 computeAverage(studentList)，返回每人的三个身份字段和字符串形式的平均分。
# 思路：仅把四个成绩转换成 float 计算；计算结果再用 str 转回题目指定的字符串类型。
# 易错点：题目例子为 '74.0' 而不是 '74.00'，因此不要强制统一两位小数。
# 完整保留原题五名学生和四次成绩；此多行赋值保存列表记录。
student_grades = [
    # John 的四次成绩为 79、89、49、79。
    ['2345243', 'John', 'Doe', '79', '89', '49', '79'],
    # Bob 的四次成绩为 90、90、80、90。
    ['5634423', 'Bob', 'Smith', '90', '90', '80', '90'],
    # Jane 的四次成绩为 61、71、81、81。
    ['1433145', 'Jane', 'Roe', '61', '71', '81', '81'],
    # Joe 的四次成绩为 82、93、92、92。
    ['8754543', 'Joe', 'Public', '82', '93', '92', '92'],
    # Jean 的四次成绩为 95、37、39、98。
    ['3142354', 'Jean', 'Martin', '95', '37', '39', '98']
]

# 保留原题规定的函数名与参数名。
def computeAverage(studentList):
    # 创建返回列表，不修改传入的原始成绩记录。
    average_records = []
    # 依照原学生顺序逐条处理记录。
    for student in studentList:
        # 为当前学生重新初始化总分，避免混入前一个人的成绩。
        grade_total = 0.0
        # 前三项是身份字段，从索引 3 到末尾才是四个成绩字符串。
        for grade in student[3:]:
            # 先将成绩变为数值，再累加到当前学生总分。
            grade_total = grade_total + float(grade)
        # 原题每人恰好四次测试，因此除以 4 得到算术平均分。
        average = grade_total / 4
        # 切片复制三个身份字段，另加字符串形式的平均分作为第四项。
        average_record = student[:3] + [str(average)]
        # 将当前人的新记录追加到结果中。
        average_records.append(average_record)
    # 全部学生处理完毕后返回新生成的嵌套列表。
    return average_records

# 保存原题样例的函数返回值，便于按行展示全部五名学生。
average_records = computeAverage(student_grades)
# 逐条读取结果，显示顺序与原题一致。
for record in average_records:
    # 显示身份字段与平均分字符串，结果依次为 74.0、87.5、73.5、89.75、67.25。
    print(record)

# %% R08-E07-P02
# 任务：实现 highestAverage(studentList)，仅返回最高平均分学生的编号、名与姓。
# 思路：复用第一问的结果，从第一名学生开始保存当前最优记录，再逐一比较。
# 易错点：比较前将平均分字符串转换为 float；用严格大于保留并列第一人的约定。
# 保留原题规定的第二个函数名与参数名。
def highestAverage(studentList):
    # 使用第一问函数生成每人的平均分，避免重复计算逻辑。
    averages = computeAverage(studentList)
    # 原题未规定空列表行为，这里明确返回空列表。
    if len(averages) == 0:
        # 没有学生时无法选择最高者。
        return []
    # 初始时把第一条记录作为当前最高者。
    best_student = averages[0]
    # 已选过第一人，只需遍历其后的学生。
    for student in averages[1:]:
        # 用数值比较平均分；相等时不替换，保留最先出现的学生。
        if float(student[3]) > float(best_student[3]):
            # 发现更高平均分时更新当前最高者。
            best_student = student
    # 返回前三项身份信息，不把平均分放进第二问的返回值。
    return best_student[:3]

# 样例最高平均分为 Joe 的 89.75，输出与原题给出的身份列表一致。
print(highestAverage(student_grades))
# 验证补充的空列表约定，预期显示 []。
print("Empty input:", highestAverage([]))
