# Author: ApheliosLu
# 2026-05-27 16:22:16
# https://github.com/ApheliosLu

a = 1
b = a
a = 2
print(f"b={b}, a={a}")


def no_change(num):
    """
    函数的参数和返回值的传递
    :param num:
    :return:
    """
    print("-" * 50)
    print("参数 %d 在函数内的内存地址是 %d" % (num, id(num)))

    num = 5
    # 函数内改变值后，id改变（本质改变了引用对象）
    print("参数 %d 在函数内的内存地址是 %d" % (num, id(num)))

    result = 100
    print(f"返回值 result 在函数中的地址是{hex(id(result))}")
    print("-" * 50)
    return result


a = 10  # 不可变类型
print(f"调用函数前 实参a的内存地址是{id(a)}")
r = no_change(a)

# 实参a的内存地址在调用函数前后一致，在函数中也不会改变
print(f"调用函数后 实参a的内存地址是{id(a)}")

# 返回值r的内存地址在函数中和调用函数后一致
print(f"调用函数后 返回值r内存地址是{id(r):#x}")

print("-" * 50 + "分割线" + "-" * 50)


def change():
    """
    想要在函数中改变外界变量的值，必须用可变数据类型 list/dict/set
    :return:
    """
    pass
