# 第 6 题：Color Mixer
# Exercise 6: Color Mixer

# 覆盖验证输入、and/or 和两种输入顺序；目的：把颜色配对写成布尔条件。原题未说明同色混合，补充规则是报错要求两个不同原色；只接受精确的小写名称。
# Coverage: input validation, and/or, and both input orders. Purpose: express color pairs as Boolean conditions. The source omits duplicate colors, so report an error asking for two different primary colors; accept exact lowercase names only.

# 保存第一个原色字符串 red；这里不自动改大小写。
# Store first primary color red; case is not changed automatically.
color1 = "red"
# 保存第二个原色 blue；调换两个样例值也应得到同一结果。
# Store second primary color blue; reversing the two samples should give the same result.
color2 = "blue"
# 第一个颜色与三个允许值都不相等时才无效，因此三个比较用 and。
# The first color is invalid only if it differs from all three allowed values, so join the tests with and.
if color1 != "red" and color1 != "blue" and color1 != "yellow":
    # 第一个名称无效，输出允许的原色名称。
    # If the first name is invalid, display the permitted primary colors.
    print("Error: use red, blue, or yellow.")
# 第一个颜色有效后，再用同样规则检查第二个颜色。
# After validating the first color, check the second with the same rule.
elif color2 != "red" and color2 != "blue" and color2 != "yellow":
    # 第二个名称无效时也显示相同错误消息。
    # Display the same error if the second name is invalid.
    print("Error: use red, blue, or yellow.")
# 两个名称都有效但相同时，采用已明确说明的补充规则。
# When both names are valid but equal, apply the explicitly stated added rule.
elif color1 == color2:
    # 提示选择不同原色，因为题目没有给同色混合的次生色。
    # Ask for different primaries because the question provides no secondary color for duplicates.
    print("Error: choose two different primary colors.")
# 分别检查红蓝和蓝红，任一顺序成立都匹配；括号把每个完整配对分组。
# Check red-blue and blue-red; either complete pair matches, with parentheses grouping each pair.
elif (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    # 红蓝组合输出紫色；当前样例进入此分支。
    # Display purple for red and blue; the sample selects this branch.
    print("Purple")
# 检查红黄或黄红两种顺序，避免只处理一种输入顺序。
# Check both red-yellow and yellow-red so neither input order is omitted.
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    # 红黄组合输出橙色。
    # Display orange for red and yellow.
    print("Orange")
# 有效、不同且排除前两种组合后，只剩蓝黄组合的两个顺序。
# After validating distinct colors and excluding the first two pairs, only blue-yellow in either order remains.
else:
    # 蓝黄组合输出绿色。
    # Display green for blue and yellow.
    print("Green")

