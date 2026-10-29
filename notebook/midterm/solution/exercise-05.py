# Mock Midterm 原题 Question 8：Dice Duel。
# 概念：随机整数、外层计分回合、内层平局重掷、计分器和停止条件。
# 教学目的：明确“掷骰次数”和“回合数”不同；一回合可以包含多次平局重掷。
# 易错点：平局错误加分或增加回合数；只重掷一人；把外层 and 写成 or。
# 输出必须包含回合、每次骰子、平局提示、得分、胜者和总回合数。
# 原答案重掷输出少了逗号；本程序遵循题目样例，首次和重掷格式完全相同。
# 不使用列表、字符串方法、字典、集合或自定义函数；f-string 只负责格式化输出。

# 导入标准库 random，用于产生六面骰的随机整数。
import random
# 固定种子 7，使课堂演示可复现；它不保证重现题目示例的具体骰子序列。
random.seed(7)
# Alice 初始得分为 0。
alice_score = 0
# Bob 初始得分为 0。
bob_score = 0
# 初始已进行回合数为 0，只在开始新回合时增加。
rounds_played = 0
# 只有两人都尚未达到 3 分才继续，and 保证任意一人胜出就停止。
while alice_score < 3 and bob_score < 3:
    # 新回合开始时只增加一次计数，平局重掷不执行本行。
    rounds_played += 1
    # 按样例格式显示当前回合编号。
    print(f"Round {rounds_played}")
    # 为 Alice 掷一次骰子，randint 的两个端点 1 和 6 都可能出现。
    alice_roll = random.randint(1, 6)
    # 为 Bob 独立掷一次骰子。
    bob_roll = random.randint(1, 6)
    # 显示本次两人的骰子点数，并保留中间的逗号。
    print(f"Alice rolls {alice_roll}, Bob rolls {bob_roll}")
    # 只要两人点数相同，就在当前回合持续重掷，不加分也不增加回合数。
    while alice_roll == bob_roll:
        # 按原题精确输出平局提示。
        print("Tie! Roll again.")
        # 平局后为 Alice 重新掷骰子，而不是只给某一人重掷。
        alice_roll = random.randint(1, 6)
        # 平局后也为 Bob 重新掷骰子。
        bob_roll = random.randint(1, 6)
        # 显示重掷结果；与首次掷骰一样使用逗号分隔。
        print(f"Alice rolls {alice_roll}, Bob rolls {bob_roll}")
    # 退出内层循环时已经保证不是平局，再比较胜者。
    if alice_roll > bob_roll:
        # Alice 点数更大，为 Alice 增加 1 分。
        alice_score += 1
    # 既然不是平局且 Alice 没赢，剩余情况必定是 Bob 点数更大。
    else:
        # 为 Bob 增加 1 分。
        bob_score += 1
    # 按样例格式显示当前回合结算后的双方得分。
    print(f"Score: Alice {alice_score}, Bob {bob_score}")
    # 每个回合结束留一空行，与题目示例格式一致。
    print()
# 外层循环结束时检查是否为 Alice 先到 3 分。
if alice_score == 3:
    # Alice 达到 3 分时显示 Alice 获胜。
    print("Alice wins!")
# 否则达到 3 分的是 Bob。
else:
    # 显示 Bob 获胜。
    print("Bob wins!")
# 最后输出已完成的计分回合数，平局重掷不另计回合。
print("Rounds played:", rounds_played)
