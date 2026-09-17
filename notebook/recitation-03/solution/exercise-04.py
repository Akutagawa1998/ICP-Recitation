# 第 4 题：Age Classifier
# Exercise 4: Age Classifier

# 覆盖有序区间分类；目的：用 if/elif/else 保证只输出一个类别。重点检查 1、13、20 三个边界；假设年龄非负，样例使用整数岁。
# Coverage: ordered interval classification. Purpose: use if/elif/else to select exactly one category. Check boundaries 1, 13, and 20; assume a nonnegative age and use whole years in the sample.

# 保存样例年龄 20，恰好测试成人下界。
# Store sample age 20 to test the lower boundary of adulthood.
age = 20
# 小于或等于 1 的年龄属于婴儿；等号决定 1 的归属。
# Ages at most 1 are infants; the equality includes age 1.
if age <= 1:
    # 进入此分支时显示婴儿类别。
    # Display the infant category when this branch is selected.
    print("Infant")
# 前一个条件失败已说明年龄大于 1，所以这里只需检查是否小于 13。
# The previous False condition already means age is above 1, so only the upper bound needs testing.
elif age < 13:
    # 为大于 1 且小于 13 的年龄显示儿童类别。
    # Display child for an age above 1 and below 13.
    print("Child")
# 前面已排除小于 13 的年龄，此分支覆盖 13 到小于 20。
# Earlier conditions exclude ages below 13, so this branch covers 13 up to but not including 20.
elif age < 20:
    # 显示青少年类别，包含 13，不包含 20。
    # Display teenager, including 13 and excluding 20.
    print("Teenager")
# 剩余年龄至少为 20，属于成人。
# All remaining ages are at least 20 and belong to the adult category.
else:
    # 样例年龄为 20，因此显示 Adult。
    # The sample is 20, so display Adult.
    print("Adult")

