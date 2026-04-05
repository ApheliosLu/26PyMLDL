# 作者: 陆离ApheliosLu
# 2026年04月05日15时30分16秒
# Leon12097@163.com


def use_hex():
    a = 123
    print(bin(a))  # 0b1111011
    print(hex(a))  # 0x7b
    print(oct(a))  # 0o173

    b = -5
    print(bin(b))  # -0b101 底层补码，输出原码
    print(hex(b))
    print(oct(b))


use_hex()

print(True + 1)  # 2
print(False - 1)  # -1


def use_float():
    f = 1.234567891234567891
    print(f)  # 1.234567891234568 精度大约17位


use_float()
