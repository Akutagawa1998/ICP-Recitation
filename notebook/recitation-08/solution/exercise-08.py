# 第 8 题：随机考勤，练习元组记录、随机抽样、搜索和菜单循环。
# 教学目的：理解元组不可变，但外层列表可在原位置替换一整条元组记录。
# 总体思路：四个函数依序负责注册、抽查、查询和菜单调度；最后用模拟输入复现原题行为。
# 常见错误：重复抽到同一学生、只修改局部变量没有更新原列表、每轮菜单重新注册而丢失累计缺勤。
# 补充约定：每行输入一个姓名，空行结束注册；拒绝完全相同的姓名；查询区分大小写。
# 参数说明：保留原题 check_absences(student) 的名字，student 参数在这里表示完整注册列表。

# %% R08-E08-P01
# 任务：register_students() 读取姓名并返回 [(name, 0), ...] 的列表。
# 思路：循环收集姓名；空行结束；每个新学生的缺勤次数都从 0 开始。
# 易错点：一名学生的两个字段放在一个元组中，所有学生元组放在同一个列表中。
# 导入标准库随机模块，供下一问真实随机选择使用。
import random

# 定义原题要求的无参数注册函数。
def register_students():
    # 建立外层可变列表，用于保存学生元组。
    Stu_list = []
    # 反复询问姓名，直到读到空行。
    while True:
        # 去掉姓名首尾空格；只输入空格也视为结束。
        name = input("Enter a student name (blank to finish): ").strip()
        # 空字符串是本材料明确选择的注册结束标记。
        if name == "":
            # 将已经登记的全部学生记录交给调用者。
            return Stu_list
        # 先假定这个名字尚未登记。
        enrolled = False
        # 逐条读取已有记录，检查完全相同的姓名。
        for student_name, absences in Stu_list:
            # 本材料采用区分大小写的精确姓名匹配。
            if student_name == name:
                # 找到同名记录后标记为已登记。
                enrolled = True
        # 重复姓名不创建第二条记录，以避免查询歧义。
        if enrolled:
            # 告诉用户当前姓名已经登记过。
            print("Student already enrolled.")
        # 只有不存在的姓名才加入列表。
        else:
            # 保存姓名与整数 0 构成的新元组。
            Stu_list.append((name, 0))

# %% R08-E08-P02
# 任务：take_attendance(Stu_list, n) 随机抽查 n 名不同学生并原地累计缺勤。
# 思路：不重复抽取列表索引；把需要更新的元组换成同一位置的新元组。
# 易错点：元组不能写 record[1] += 1；需要修改 Stu_list[index] 才能持久保存。
# 定义原题指定的两个参数，Stu_list 是要直接更新的原列表。
def take_attendance(Stu_list, n):
    # 抽查人数不能是负数，也不能多于已登记人数。
    if n < 0 or n > len(Stu_list):
        # 对不合法人数给出可执行的提示，不进行抽样。
        print("Choose a number from 0 to " + str(len(Stu_list)) + ".")
        # 提前结束本次抽查，原列表保持原样。
        return
    # sample 在索引范围内不放回抽样，保证本次没有重复学生。
    selected_indices = random.sample(range(len(Stu_list)), n)
    # 按本次抽中索引的顺序逐个询问出勤情况。
    for index in selected_indices:
        # 把当前不可变元组拆成姓名与当前缺勤次数两个局部变量。
        name, absences = Stu_list[index]
        # 提示中显示被抽中的姓名；统一大小写以接受 p 或 a。
        status = input("Is " + name + " present? (P/A): ").strip().upper()
        # 原题假定 P 或 A；此循环只是避免误输入被悄悄当作出勤。
        while status not in ("P", "A"):
            # 对同一名学生重新询问，直到得到合法回答。
            status = input("Please enter P or A: ").strip().upper()
        # 只有 A 才代表本轮缺勤。
        if status == "A":
            # 构造新元组并替换原列表对应位置，保存累计加一后的值。
            Stu_list[index] = (name, absences + 1)

# %% R08-E08-P03
# 任务：check_absences(student) 询问姓名并显示缺勤次数，未登记时显示指定消息。
# 思路：student 接收整个学生列表；找到匹配姓名后显示次数并立即结束搜索。
# 易错点：Student not enrolled. 只能在全部记录都未匹配后显示，不能在循环内部每遇到一条不匹配记录就显示。
# 保留原题签名；参数名 student 在这里指完整注册记录列表。
def check_absences(student):
    # 读取要查询的姓名，采用与注册时一致的首尾空格处理。
    name = input("Enter the student's name: ").strip()
    # 逐个拆出已登记学生的姓名与缺勤数。
    for student_name, absences in student:
        # 按完全相同的姓名进行匹配。
        if student_name == name:
            # 显示已累计的缺勤次数，文字格式与原题示例一致。
            print(student_name + ": " + str(absences) + " absence(s)")
            # 找到后立即结束，防止继续执行未登记提示。
            return
    # 只有遍历结束仍未返回时，才说明该姓名没有登记。
    print("Student not enrolled.")

# %% R08-E08-P04
# 任务：main() 先注册，再反复显示菜单并调度抽查、查询或退出。
# 思路：学生列表只在进入菜单前创建一次，所有后续操作都共享这个列表。
# 易错点：不要在 while 菜单循环内部重新 register_students，否则缺勤计数会被清零。
# 定义入口函数；定义本身不会立即读取输入。
def main():
    # 显示注册阶段的开头提示。
    print("Enroll students...")
    # 注册一次，并保存随后各轮菜单共同使用的列表。
    Stu_list = register_students()
    # 直到用户选择退出，始终重复显示菜单。
    while True:
        # 输出第一个菜单选项。
        print("1. Take attendance")
        # 输出第二个菜单选项。
        print("2. Check a student's absence count")
        # 输出退出选项。
        print("3. Quit")
        # 菜单选择保留为字符串，便于直接与字符选项比较。
        choice = input("Choose an option: ").strip()
        # 选项 1 进入随机考勤。
        if choice == "1":
            # 捕获把非整数文本转换为 int 时可能出现的错误。
            try:
                # 将抽查人数转换为整数，再交给考勤函数检查范围。
                n = int(input("How many students should be selected? "))
            # 不是整数的输入无法用于抽样。
            except ValueError:
                # 显示清楚的纠正提示。
                print("Please enter an integer.")
                # 回到下一轮菜单，不使用尚未获得的 n。
                continue
            # 对同一个列表执行抽查，缺勤会保留到下一轮菜单。
            take_attendance(Stu_list, n)
        # 选项 2 查询当前已经累计的缺勤记录。
        elif choice == "2":
            # 将整个注册列表传给原题名为 student 的参数。
            check_absences(Stu_list)
        # 选项 3 结束菜单循环。
        elif choice == "3":
            # 返回最终记录以便课堂核对；原题只要求退出，返回值是演示辅助。
            return Stu_list
        # 其他选择不退出，也不修改学生数据。
        else:
            # 告诉用户合法的菜单数字。
            print("Choose 1, 2, or 3.")

# %% R08-E08-DEMO
# 任务：自动复现原题的两轮抽查、三次查询和退出，验证 Bob 缺勤会累计到 2。
# 思路：只在演示块内替换输入和抽中索引；四个真实交互函数不包含这些预定答案。
# 易错点：随机抽样被替换仅为复现原题演示顺序，退出 with 后真实随机抽查立即恢复。
# 导入标准库演示工具，使本文件可以独立执行而不等待键盘输入。
from unittest.mock import patch

# 按程序执行顺序预置注册、两轮考勤、查询和退出的全部字符串回答。
attendance_answers = iter([
    # 注册三个姓名，第四个空字符串结束注册。
    "Alice", "Bob", "Charlie", "",
    # 首轮选项 1，抽查 2 人；Bob 缺勤、Alice 出勤。
    "1", "2", "A", "P",
    # 查询 Bob，预期显示 1 次缺勤。
    "2", "Bob",
    # 第二轮抽查 2 人；Charlie 出勤、Bob 再次缺勤。
    "1", "2", "P", "A",
    # 再查 Bob，预期显示累计 2 次缺勤。
    "2", "Bob",
    # 查询未登记的 David，随后选择退出。
    "2", "David", "3"
])
# 定义用于显示提示与模拟回答的演示输入函数。
def attendance_demo_input(prompt):
    # 从预定回答序列读取下一条字符串。
    answer = next(attendance_answers)
    # 保留完整的交互记录，显示本次问题和对应回答。
    print(prompt + answer)
    # 返回字符串，与真正 input 的行为保持一致。
    return answer

# 第一轮索引为 Bob、Alice，第二轮为 Charlie、Bob；每轮的索引互不重复。
selected_rounds = [[1, 0], [2, 1]]
# 仅为本次演示临时替换输入函数。
with patch("builtins.input", attendance_demo_input):
    # 仅为本次演示临时固定抽样结果，真实考勤函数仍调用 random.sample。
    with patch("random.sample", side_effect=selected_rounds):
        # 执行主程序并保存退出时最终列表，整个过程不会等待键盘输入。
        final_records = main()
# 显示最终记录，Bob 的缺勤为 2，另两人仍为 0。
print("Final records:", final_records)
