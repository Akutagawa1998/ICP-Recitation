# 第 10 题：Theme Park Ride Admission，分别使用 while 和 for 循环。
# 教学目的：把身高过滤、continue、容量计数和达到 5 人后提前停止结合起来。
# 解题方法：最多检查 10 人，每人输入一次身高；身高至少 120 才增加 passenger_count。
# 常见错误：把 120 判为不合格，或满 5 人后继续询问剩余人员；while 版本还要注意在 continue 之前更新人号。

# 定义 while 版本，每个人的身高由用户依次输入。
def admit_passengers_while():
    # 从 0 名已登车乘客开始计数。
    passenger_count = 0
    # 记录已经检查到第几个人，开始时还没有检查任何人。
    person_number = 0
    # 同时限制最多检查 10 人，并且容量未满 5 人。
    while person_number < 10 and passenger_count < 5:
        # 先把人号加一；放在 continue 之前，保证身高不足时也会前进到下一人，避免死循环。
        person_number = person_number + 1
        # 按原题样例格式提示输入当前人的身高，并转成整数。
        height = int(input(f"Person {person_number} - Enter height: "))
        # 低于 120 cm 时不占座位。
        if height < 120:
            # 显示原题指定的不合格提示。
            print("Sorry, you are not tall enough.")
            # 跳过本轮剩余语句，直接检查下一人。
            continue
        # 身高至少 120 cm 时显示欢迎信息。
        print("Welcome aboard!")
        # 合格乘客占用一个座位。
        passenger_count = passenger_count + 1
    # 只有实际达到容量 5 时才显示满员信息。
    if passenger_count == 5:
        # 显示原题样例中的满员文字。
        print("The ride is full!")
    # 无论是否满员，都显示最终乘客人数。
    print(f"{passenger_count} passengers are on board.")

# 运行 while 版本，依次输入每个人的身高。
admit_passengers_while()

# 定义 for 版本，使用相同规则和输出文字。
def admit_passengers_for():
    # 初始化已登车人数为 0。
    passenger_count = 0
    # range(1, 11) 依次产生人号 1 到 10，最多检查 10 人。
    for person_number in range(1, 11):
        # 按原题样例格式读取当前人的身高。
        height = int(input(f"Person {person_number} - Enter height: "))
        # 低于 120 cm 时拒绝登车。
        if height < 120:
            # 显示原题指定的拒绝文字。
            print("Sorry, you are not tall enough.")
            # 直接进入下一次 for 迭代；range 会自动前进到下一人，不增加乘客数。
            continue
        # 合格者得到欢迎信息。
        print("Welcome aboard!")
        # 合格乘客数加一。
        passenger_count = passenger_count + 1
        # 达到五个座位时准备提前停止。
        if passenger_count == 5:
            # break 结束最近的 for 循环，不再询问后续人员。
            break
    # 仅当五个座位全部占用时显示满员。
    if passenger_count == 5:
        # 显示满员信息。
        print("The ride is full!")
    # 始终显示最终登车人数。
    print(f"{passenger_count} passengers are on board.")

# 运行 for 版本，再输入一组身高。
admit_passengers_for()
