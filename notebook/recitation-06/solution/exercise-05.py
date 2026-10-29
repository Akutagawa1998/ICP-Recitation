# 练习 5：Test Average and Grade
# 教学目的：把平均数计算与等级判断分开，练习从高到低排列条件和检查边界。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：把缺失评分表当作已知；从低分开始写 >= 条件导致高分过早归类；只把最后一项除以五。
# 子项顺序：R06-E05-P01、R06-E05-P02

# 按要求接收五个独立的考试分数。
def calc_average(score1, score2, score3, score4, score5):
    # 先求总分，再除以五得到平均数。
    return (score1 + score2 + score3 + score4 + score5) / 5

# 根据明确声明的暂定评分规则返回字母等级。
def determine_grade(score):
    # 从最高分界开始，九十分及以上为 A。
    if score >= 90:
        # 返回后函数结束，不会再进入后面的分支。
        return "A"
    # 到此处已知低于九十，因此只需检查八十分下界。
    elif score >= 80:
        # 八十分至不足九十分返回 B。
        return "B"
    # 七十分至不足八十分使用此分支。
    elif score >= 70:
        # 返回等级 C。
        return "C"
    # 六十分至不足七十分使用此分支。
    elif score >= 60:
        # 返回等级 D。
        return "D"
    # 在约定的零至一百分范围中，剩余分数低于六十。
    else:
        # 返回等级 F。
        return "F"

# 第一项可编辑成绩，对应等级 A。
score1 = 95.0
# 第二项可编辑成绩，对应等级 B。
score2 = 82.0
# 第三项可编辑成绩，对应等级 C。
score3 = 76.0
# 第四项可编辑成绩，对应等级 D。
score4 = 64.0
# 第五项可编辑成绩，对应等级 F。
score5 = 50.0
# 按原输入顺序逐个处理五项成绩。
for score in (score1, score2, score3, score4, score5):
    # 调用等级函数并显示当前成绩和等级。
    print(f"Score {score:g}: {determine_grade(score)}")
# 把五项成绩传入平均数函数。
average = calc_average(score1, score2, score3, score4, score5)
# 以两位小数显示平均分七十三点四零。
print(f"Average score: {average:.2f}")
