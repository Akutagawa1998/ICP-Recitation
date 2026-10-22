# 第 4 题：Guessing Competition，分别使用 while 和 for 循环。
# 教学目的：同时维护尝试次数、秘密数和仍可能的闭区间，并在猜中时提前结束。
# 解题方法：每次尝试读取用户的一个猜测；高猜只收紧上界，低猜只收紧下界；最多处理 7 次猜测。
# 常见错误：把高猜值本身留在范围内，或在第 7 次错误后忘记显示更新后的范围。
# 说明：秘密数每次运行都随机产生；课堂演示若需要固定结果，可在每次调用游戏函数前紧接着执行 random.seed(405)，此时秘密数为 6。

# 导入标准库 random，以生成题目要求的随机秘密数；notebook 两个单元格各自导入，本脚本在顶部导入一次即可供两个版本使用。
import random

# 定义 while 版本；猜测由用户在循环中逐次输入。
def play_guessing_game_while():
    # randint 两端都包含，因此秘密数范围是 1 到 100。
    secret_number = random.randint(1, 100)
    # 初始化仍可能的最小值为 1。
    lowest_possible = 1
    # 初始化仍可能的最大值为 100。
    highest_possible = 100
    # 记录已经使用了几次猜测，开始时为 0。
    attempt_number = 0
    # 最多允许 7 次猜测；attempt_number 达到 7 时条件变假，循环结束。
    while attempt_number < 7:
        # 先把尝试次数加一，使提示编号从 1 开始，同时保证循环最终结束。
        attempt_number = attempt_number + 1
        # 显示本次是第几次猜测，读取用户输入并用 int 转成整数。
        guess = int(input(f"Guess {attempt_number}: "))
        # 如果猜测等于秘密数，就成功结束函数。
        if guess == secret_number:
            # 按原题显示成功信息。
            print("Correct!")
            # 显示实际使用的猜测次数。
            print("Guesses used:", attempt_number)
            # return 立即结束函数，因此循环也随之结束，不会显示 Game over!。
            return
        # 如果猜测过高，就收紧可能范围的上界。
        if guess > secret_number:
            # 按原题显示过高信息。
            print("Too high!")
            # 新上界必须排除已经确定错误的 guess；min 防止范围外的猜测把上界变大。
            highest_possible = min(highest_possible, guess - 1)
        # 否则该错误猜测一定过低。
        else:
            # 按原题显示过低信息。
            print("Too low!")
            # 新下界必须排除已经确定错误的 guess；max 防止范围外的猜测把下界变小。
            lowest_possible = max(lowest_possible, guess + 1)
        # 每次错误猜测后显示更新后的闭区间。
        print(f"Possible range: {lowest_possible}-{highest_possible}")
    # 能执行到循环之后，说明 7 次都没有猜中。
    print("Game over!")
    # 按原题揭示秘密数。
    print("Secret number:", secret_number)

# 运行 while 版本，开始一局交互式游戏。
play_guessing_game_while()

# 定义 for 版本，规则与 while 版本完全相同。
def play_guessing_game_for():
    # 在 1 到 100 的闭区间内随机生成秘密数。
    secret_number = random.randint(1, 100)
    # 初始化闭区间下界。
    lowest_possible = 1
    # 初始化闭区间上界。
    highest_possible = 100
    # range(1, 8) 依次产生 1 到 7，正好对应最多 7 次尝试的编号。
    for attempt_number in range(1, 8):
        # 显示尝试编号并读取用户的整数猜测。
        guess = int(input(f"Guess {attempt_number}: "))
        # 猜中时显示结果并立即返回。
        if guess == secret_number:
            # 显示原题指定的成功文字。
            print("Correct!")
            # 显示使用的猜测次数。
            print("Guesses used:", attempt_number)
            # return 结束函数，也就提前结束了 for 循环。
            return
        # 猜测大于秘密数时更新上界。
        if guess > secret_number:
            # 显示过高提示。
            print("Too high!")
            # 排除本次猜测并保留更小的已有上界。
            highest_possible = min(highest_possible, guess - 1)
        # 其余错误猜测属于过低。
        else:
            # 显示过低提示。
            print("Too low!")
            # 排除本次猜测并保留更大的已有下界。
            lowest_possible = max(lowest_possible, guess + 1)
        # 显示本次错误后的可能范围。
        print(f"Possible range: {lowest_possible}-{highest_possible}")
    # 用尽 7 次猜测后显示失败信息。
    print("Game over!")
    # 揭示本局秘密数。
    print("Secret number:", secret_number)

# 运行 for 版本，再玩一局；两局的秘密数通常不同。
play_guessing_game_for()
