# 作者: 陆离ApheliosLu
# 2026年04月05日15时30分16秒
# Leon12097@163.com


def use_hex():
    a = 123
    print(bin(a))  # 0b1111011
    print(hex(a))  # 0x7b
    print(oct(a))  # 0o173

    b = -5
    print(bin(b))  # -0b101 底层补码，输出符号加绝对值表示法
    print(hex(b))
    print(oct(b))


use_hex()

print(True + 1)  # 2
print(False - 1)  # -1


def use_float():
    f = 1.234567891234567891
    print(f)  # 1.234567891234568 精度大约17位


use_float()


def use_complex():
    c = complex(3, 4)
    print("c is %d+%dj" % (c.real, c.imag))  # python中的%格式输出
    print(c)  # (3+4j)


use_complex()

str1 = "a"
print(type(str1))  # <class 'str'>
str2 = "abc"
print(type(str2))
str3 = "abc‘defg"
print(str3)  # abc‘defg
str4 = "abc\n'\"\\defg"
print(str4)

print(ord("1"))  # 字符1的ascii码值
print("*" * 50)  # 字符串和整型相乘
print(chr(65))  # 65对应的字符A
