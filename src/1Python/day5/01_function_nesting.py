# Author: ApheliosLu
# 2026-06-09 10:30:10
# https://github.com/ApheliosLu


import sys

sys.setrecursionlimit(10**6)  # 设置递归的最大深度，已突破默认1000层上限


# 递归 1.找到递归公式 2.编写结束条件
def sum_numbers(num):
    print(num)
    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return
    sum_numbers(num - 1)
    print(f"完成{num}的递归")


def r_f(n):
    # 2.结束条件
    if n == 1:
        return 1
    return n + r_f(n - 1)  # 1.递归公式


def step(n):
    """
    上台阶
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return n
    return step(n - 1) + step(n - 2)


if __name__ == "__main__":
    # sum_numbers(int(input(f"请输入sum_numbers：")))

    # [Previous line repeated 996 more times] RecursionError: maximum recursion depth exceeded
    # print(r_f(100000))

    for i in range(1, 10):
        print(step(i))
