# 练习 8：Date Printer
# 教学目的：练习 split、字符串转整数、列表索引和格式化输出。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：忘记月份减一；把月和日的位置反过来；把格式转换误称为完整日期校验。

# 接收有效的月日年字符串，输出英文日期。
def print_date(date_text):
    # 按一月至十二月顺序建立月份名称表。
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    # 用斜杠把输入拆成月、日、年三个字符串。
    parts = date_text.split("/")
    # 把第一部分转换成整数月份。
    month_number = int(parts[0])
    # 转成整数日数，显示时去掉前导零。
    day = int(parts[1])
    # 第三部分保留为四位年份字符串。
    year = parts[2]
    # 月份从一开始，列表索引从零开始。
    month_name = month_names[month_number - 1]
    # 按英文月份名、日和年的顺序输出。
    print(f"{month_name} {day}, {year}")

# 用与原题目标输出对应的有效示例日期。
date_text = "03/12/2014"
# 调用日期打印函数，显示 March 12, 2014。
print_date(date_text)
