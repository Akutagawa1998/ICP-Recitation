# 练习 12：Chinese ID number check
# 教学目的：将验证顺序、字符处理、切片、加权累积和提前返回组织成完整的小程序。
# 解题思路：与教师 notebook 的对应答案保持相同计算逻辑。
# 常见错误：先转成整数丢失前导零；先提取后验格式；仅用 isdigit 放宽原题字符范围；返回整数校验位与字符串比较；把切片右端点当成包含；悄悄替换课堂公式。
# 子项顺序：R06-E12-P01、R06-E12-P02、R06-E12-P03、R06-E12-P04、R06-E12-P05

# 检查长度以及题目允许的 ASCII 字符范围。
def has_valid_format(id_number):
    # 长度必须先检查，避免后续索引越界。
    if len(id_number) != 18:
        # 长度错误时立即报告格式不通过。
        return False
    # 依次检查前十七个字符。
    for character in id_number[:17]:
        # 明确限定零至九，排除其他 Unicode 数字。
        if character not in "0123456789":
            # 发现一个非法字符就无需继续检查。
            return False
    # 最后一位允许数字字符或大写 X。
    return id_number[-1] in "0123456789X"

# 假设已收到十七个有效数字字符，计算课堂校验位。
def calculate_check_digit(first17):
    # 加权乘积总和从零开始。
    total = 0
    # 依次使用索引零到十六，共十七个位置。
    for i in range(17):
        # 严格按原题给定的幂和取余公式计算权重。
        weight = (2 ** (17 - i)) % 11
        # 将当前位置数字乘权重，再加入总和。
        total += int(first17[i]) * weight
    # 所有位置累加完成后才计算最终余数。
    remainder = total % 11
    # 十不能用单个数字字符表示，题目规定改用 X。
    if remainder == 10:
        # 返回大写字符串字符，方便之后逐字符比较。
        return "X"
    # 其他余数也必须转成字符串，而不是返回整数。
    return str(remainder)

# 主程序在格式通过后才调用此函数。
def has_valid_checksum(id_number):
    # 取前十七位计算预期校验字符。
    expected = calculate_check_digit(id_number[:17])
    # 与实际末位比较并返回布尔结果。
    return expected == id_number[-1]

# 按题目给出的固定位置提取出生日期字符串。
def get_birth_date(id_number):
    # 索引六至九共四位表示年份。
    year = id_number[6:10]
    # 索引十至十一共两位表示月份。
    month = id_number[10:12]
    # 索引十二至十三共两位表示日期。
    day = id_number[12:14]
    # 使用连字符把三段组合成指定格式。
    return f"{year}-{month}-{day}"

# 使用索引十六的数字奇偶性返回英文性别码。
def get_sex(id_number):
    # 把指定字符转成整数，才能进行奇偶判断。
    sex_code = int(id_number[16])
    # 除二余一说明该位是奇数。
    if sex_code % 2 == 1:
        # 按题目规则，奇数对应 Male。
        return "Male"
    # 格式已保证是数字，剩余偶数对应 Female。
    return "Female"

# 用可编辑字符串参数代替阻塞输入，同时保留主程序职责。
def main(raw_id):
    # 先删除外围空格，并把末位小写 x 规范为大写。
    id_number = raw_id.strip().upper()
    # 必须先验证格式，之后才能安全地校验和提取。
    if not has_valid_format(id_number):
        # 格式不通过时显示英文错误信息。
        print("Invalid format.")
        # 提前结束，避免进入后续校验函数。
        return
    # 仅在格式通过后比较校验位。
    if not has_valid_checksum(id_number):
        # 校验位不符时显示第二类错误。
        print("Invalid checksum.")
        # 提前结束，不输出出生日期和性别码。
        return
    # 只有两个检查都通过才显示成功信息。
    print("Format and checksum passed.")
    # 调用提取函数并显示出生日期。
    print("Date of birth:", get_birth_date(id_number))
    # 调用奇偶判断函数并显示性别码。
    print("Sex:", get_sex(id_number))

# 保留原题给出的完整示例，字符串保存前导零。
raw_id = "00000020000101038X"
# 标明原 PDF 给出的例子，保留原样并如实检查。
print("Source example:")
# 按原题公式运行，原例应显示 Invalid checksum.。
main(raw_id)
# 只把末位改为公式计算出的二，明确另列修正样例。
corrected_id = "000000200001010382"
# 清楚区分修正样例与原题不一致的例子。
print("Corrected classroom-rule example:")
# 修正样例通过后显示成功、出生日期和 Female。
main(corrected_id)
