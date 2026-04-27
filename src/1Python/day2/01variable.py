# Author: ApheliosLu
# 2026年04月05日12:30:09
# Email:  Leon12097@163.com
import keyword

print(keyword.kwlist)
print(keyword.iskeyword("你的名字"))  # 检测是否关键字 False

# 定义变量不需要声明类型
i = 10
print(i)
print(type(i))
i = 98.5
print(i)
print(type(i))
i = "abc"
print(i)
print(type(i))  # <class 'str'>

# 字符/字符串均会格式化为双引号
qq_num = "1"
print(qq_num)
qq_pwd = "123"
print(qq_pwd)

# 数据和变量分离。id（）用于显示数据地址而非变量地址，a和b都指向1，即同一个地址
a = 1
b = 1
print(a)
print(b)
print(id(a))
print(id(b))  # a和b的地址相同
a = 2  # 指向了新的数据，因此id(a)改变了，本质是数据1和数据2的地址
print(id(a))
print(type(a))  # <class 'int'>
print(ord("a"))  # 97 ord输出字符的ASCII码
print(chr(ord("a")))  # a   chr将整型转为字符

print("*" * 50)
print("超市买苹果案例")
price = 8.5
print(type(price))  # <class 'float'> 对应C/CPP的double
weight: float = 7.5
money = price * weight
print(money)
money -= 5
money = money - 5
print(money)

print("复数")
c = complex(2, 3)
print(c)  # (2+3j)
print(type(c))  # <class 'complex'>
print(c.real)  # 2.0
print(c.imag)  # 3.0

print("转义字符")
print("\\")
print("'")
print('"')

print("-" * 50)
first_name = "张"
second_name = "三"
print(first_name + second_name)  # 字符串拼接
