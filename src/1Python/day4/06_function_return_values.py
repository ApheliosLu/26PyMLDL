# Author: ApheliosLu
# 2026-05-31 14:40:10
# https://github.com/ApheliosLu

import builtins
import keyword

print(len(dir(builtins)))  #  3.14版本 160个内置函数
print(len(keyword.kwlist))  # 3.14版本 35个关键字


def measure():
    """
    掌握返回多个值时，如何去处理
    :return:
    """

    print("开始测量...")
    temp = 39
    wetness = 10
    print("测量结束...")

    return temp, wetness


ret1 = measure()
print(ret1)  # return的两个返回值以元组形式返回
print(ret1[0])

a = 10
b = 5
a, b = b, a
print(a, b)
