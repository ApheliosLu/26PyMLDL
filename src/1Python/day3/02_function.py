# Author: ApheliosLu
# 2026-04-27 14:49:36
# https://github.com/ApheliosLu


def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")


# print("before say_hello()")
# say_hello()
# print("after say_hello()")


def sum_2_elem(elem1, elem2):
    result = elem1 + elem2
    print(f"{elem1}+{elem2}={result}")
    return result


ret = sum_2_elem("abc", "def")
# print(ret)


def test1():
    print("*" * 50)
    print("here is test1")
    print("*" * 50)


def test2():
    print("-" * 50)
    print("here is test2")
    test1()
    print("-" * 50)


test2()  # 嵌套函数调用
