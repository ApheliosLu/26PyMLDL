# 作者: 陆离ApheliosLu
# 2026年04月06日11时03分18秒
# Leon12097@163.com

# print("start")
# while True:
#     pass


def change_alphabet():
    a = input("请输入您的英雄：\n")
    print(a)
    print(type(a))  # <class 'str'>
    print(type(ord(a)))  # <class 'int'> ord函数将字符转为ASCII码
    print(chr(ord(a) - 32))  # 单个字符小写转大写


# change_alphabet()


def change_type():
    num = input("请输入数字：")  # input函数接收的输入默认是字符串类型
    print(num + "b")  # 字符+字符
    print(ord(num) + 5)  # 字符转为ASCII码后加5
    print(int(num) + 5)  # 字符转为整数后加5


# change_type()


def format_print():
    score = 98.2
    name = "小明"
    student_no = 1
    price = 9
    weight = 5
    money = price * weight
    scale = 0.1
    print(score)
    print("成绩是%.2f" % score)
    print("名字是%s,年龄是%-3d,学号是%06d" % (name, 19, student_no))
    print("苹果单价是%.2f元/斤,购买%.02f斤,需要支付%.02f元" % (price, weight, money))
    print("数据比例是%.05f%%" % (scale * 100))


# format_print()


def grocery_apple():
    weight_str = input("请输入苹果重量：")
    price = float(input("请输入苹果价格："))
    weight = float(weight_str)
    money = price * weight
    print("%.2f" % money)


# grocery_apple()


def use_end():
    print("end测试1")  # 测试1独占一行
    print("end测试2", end="   ")  # 和测试3在同一行，测试2后有三个空格
    print("end测试3", end="")  # 和测试4在同一行，测试3后无任何字符
    print("end测试4")


# use_end()

# 科学计数输出
print("%e", 1)  # %e 1
print("%e" % 1)  # 1.000000e+00     %e输出6位小数的科学计数
print("%.3e" % 1)  # 1.000e+00
print("%E" % 1)  # 1.000000E+00
print("%g" % 1111.1111)  # 1111.11   %g输出6位有效数字
print("%g" % 123000000)  # 1.23e+08  %g自动选择小数形式 / 科学计数法，哪个短用哪个
print("%G" % 123000000)  # 1.23E+08

# 取整接口round
print(round(1.2345))  # 1   取整
print(round(1.2356, 3))  # 1.236    保留三位小数

# 现代格式化输出
name = "李华"
age = 22
print(f"我叫{name},今年{age}岁")  # 占位符内写变量

pi = 3.14159
print(f"π = {pi:.2f}")  # 保留两位小数
print(f"π = {pi:.0f}")  # 保留整数
print(f"π = {pi:.2e}")  # 3.14e+00 科学计数带两位小数
print(f"π = {pi:.4g}")  # 3.142 自动精简
print(f"π = {pi:8.2f}")  # 占8个字符宽度，右对齐
print(f"π = {pi:<8.2f}")  # 占8个字符宽度，左对齐

a = 10
b = 3
print(f"{a} + {b} = {a + b}")

print(f"小写转大写：{'abc'.upper()}")
