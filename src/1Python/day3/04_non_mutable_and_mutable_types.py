# Author: ApheliosLu
# 2026-05-27 16:22:16
# https://github.com/ApheliosLu

a = 1
b = a
a = 2
print(f"b={b}, a={a}")


def no_change(num):
    """
    函数的参数和返回值的传递；
    不可变类型：不能改原值，只能建新值
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


def change(new_list):
    """
    想要在函数中改变外界变量的值，必须用可变数据类型 list/dict/set
    :return:
    """
    # new_list = [4, 5, 6]  # 通过赋值操作无法改变函数外的数据，相当于重新绑定对象，地址变了
    # print(f"change函数中{new_list},地址{id(new_list)}")

    new_list[0] = 10  # 修改对象内部则可改变数据，地址不变
    print(f"change函数中{new_list},地址{id(new_list)}")


my_list = [1, 2, 3]
print(f"调用change之前{my_list},地址{id(my_list)}")
change(my_list)
print(f"调用change之后{my_list},地址{id(my_list)}")
