# 练习 1：预测输出；先直接打印答案，再展示独立的修正程序。
# 教学目的：区分打印与返回，跟踪全局变量，理解局部变量读取前必须赋值。
# 程序 2：原题 calc 按笔误统一改为 cal，不把该拼写差异作为答案。
# 程序 3：直接打印首个 UnboundLocalError，随后独立展示参数化修正版。
# 子项顺序：程序 1；程序 2 答案与修正代码；程序 3 答案与修正代码。

# Program 1: the original program.
# 程序 1：原题程序。
# Define a function with no parameters; its body runs only when called.
# 定义无参数函数；函数体直到调用时才执行。
def f():
    # Use the global variable s inside this function.
    # 指明函数中的 s 使用全局变量。
    global s
    # The global value is less at this point, so print less first.
    # 此时全局 s 为 less，因此先显示 less。
    print(s)
    # Change the global value to more; the change is also visible outside.
    # 把全局变量改为 more，函数外也能看到变化。
    s = "more"
    # Return more and end this function call immediately.
    # 返回 more 并立即结束这次函数调用。
    return s
    # This statement follows return and can never run.
    # 这一行在 return 后面，永远无法执行。
    s = "less"
# Create the global string variable before calling the function.
# 调用之前先创建全局字符串变量。
s = "less"
# Run the inner print first, then print the returned value more.
# 先执行函数内部打印，再打印函数返回的 more。
print(f())
# Display the updated global value more.
# 显示修改后的全局值 more。
print(s)

# Print the result of adding 2 and 3.
# 打印二加三得到的结果。
print(5)
# Print the message produced by div when its denominator is zero.
# 打印 div 遇到零分母时显示的提示。
print("Denominator was 0.")
# Print the implicit return value of that zero-denominator call.
# 打印这次零分母调用的隐式返回值。
print(None)

# Receive a function and two values; use the corrected name cal.
# 接收一个函数和两个值；函数名按笔误修正为 cal。
def cal(op, x, y):
    # Call the supplied function and return its result.
    # 调用传入的函数并返回其结果。
    return op(x, y)

# Define the addition operation.
# 定义加法运算。
def add(a, b):
    # Return the sum of the two arguments.
    # 返回两个实参的和。
    return a + b

# Define the division operation.
# 定义除法运算。
def div(a, b):
    # Divide only when the denominator is not zero.
    # 仅在分母非零时执行除法。
    if b != 0:
        # Return the quotient on the nonzero path.
        # 在分母非零的路径返回商。
        return a / b
    # Print the message; this path then implicitly returns None.
    # 打印提示；这条路径随后隐式返回 None。
    print("Denominator was 0.")

# Run add through cal and print 5.
# 通过 cal 调用 add，并打印 5。
print(cal(add, 2, 3))
# Run div through cal; its message appears before the outer print displays None.
# 通过 cal 调用 div；内部提示先显示，随后外层打印 None。
print(cal(div, 2, 0))

# Print the first error reached by the original program.
# 直接打印原程序首先遇到的报错信息。
print("UnboundLocalError: local variable 'a' referenced before assignment")

# Receive the initial value as a local parameter.
# 用局部形参接收初始值。
def foo_fixed(a):
    # The parameter already has a value, so increase it safely.
    # 形参已经有值，因此可以安全地加一。
    a += 1
    # Save the updated value 3.
    # 保存更新后的值 3。
    x = a
    # Calculate its square, 9.
    # 计算它的平方 9。
    y = a ** 2
    # Return both results to the caller.
    # 把两个结果返回调用处。
    return x, y

# Keep the caller's initial value 2.
# 保存调用者的初始值 2。
a = 2
# Receive the returned values 3 and 9.
# 接收返回的两个值 3 和 9。
x, y = foo_fixed(a)
# Print only defined names; the caller's a remains 2.
# 只打印已经定义的名字；调用者的 a 仍为 2。
print(a, x, y)
