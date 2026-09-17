# 第 10 题：Time calculator
# Exercise 10: Time calculator

# 覆盖独立 if、含等号的阈值和单位换算；目的：区分多个条件可同时满足与只选一个分支。原题逐项提出条件，因此满足几项就输出几项，使用 / 保留小数。
# Coverage: independent if statements, inclusive thresholds, and unit conversion. Purpose: distinguish multiple matching conditions from selecting one branch. The source states each condition separately, so display every eligible conversion using / to retain fractions.

# 样例 90061 秒超过一天，因此输出总分钟、总小时、总天数。这里不做天/小时/分钟/秒的余数分解，也不只显示最大单位；少于 60 秒不显示换算。
# The sample 90061 seconds exceeds one day, so it displays total minutes, hours, and days. This is not a remainder decomposition or a largest-unit-only display; below 60 seconds there is no conversion output.

# 保存非负样例秒数 90061，特意测试三个条件全部满足且带小数的情况。
# Store nonnegative sample seconds 90061 to test all three conditions and fractional results.
seconds = 90061
# 不少于 60 秒时允许显示总分钟数，等号包括恰好 60 秒。
# At least 60 seconds permits displaying total minutes, including exactly 60 seconds.
if seconds >= 60:
    # 把全部秒数除以 60，而不是只换算不足一小时的余数。
    # Divide the entire seconds value by 60, not a leftover amount below one hour.
    minutes = seconds / 60
    # 显示总分钟数约 1501.0167；默认输出保留浮点显示精度。
    # Display total minutes, approximately 1501.0167, using the default float representation.
    print("Minutes:", minutes)
# 这是第二个独立 if，因此即使已输出分钟，仍会检查小时条件。
# This second if is independent, so the hour condition is checked even after minutes were displayed.
if seconds >= 3600:
    # 用全部秒数除以每小时 3600 秒，得到总小时数。
    # Divide all seconds by 3600 seconds per hour to obtain total hours.
    hours = seconds / 3600
    # 显示总小时数约 25.0169，而不是去掉完整一天后的小时余数。
    # Display total hours, approximately 25.0169, not the hours left after removing a whole day.
    print("Hours:", hours)
# 第三个独立条件检查是否达到一天的 86400 秒。
# The third independent condition checks the 86400-second threshold for a day.
if seconds >= 86400:
    # 把全部秒数除以 86400，保留小数天数。
    # Divide the entire seconds value by 86400, retaining fractional days.
    days = seconds / 86400
    # 显示总天数约 1.04237；当前样例共输出三行。
    # Display total days, approximately 1.04237; this sample produces three output lines.
    print("Days:", days)

