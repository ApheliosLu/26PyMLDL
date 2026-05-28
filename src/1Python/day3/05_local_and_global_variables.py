#!/usr/bin/env python3
# shebang指示解释器路径

# Author: ApheliosLu
# 2026-05-28 09:58:01
# https://github.com/ApheliosLu

import my_first_module

# 1、执行到需要全局变量时，全局变量必须被定义了
# 2、就近原则


def demo1() -> None:
    global num  # 如果在函数中需要修改全局变量，需要使用 global 进行声明
    print(num)
    num = 2
    print(f"demo1中修改后的 num = {num},id(num) = {id(num)}")


num = 10
print(f"调用函数前 num = {num},id(num) = {id(num)}")
demo1()
# 在函数中利用global修改了num
print(f"调用函数后 num = {num},id(num) = {id(num)}")

my_first_module.print_line("&", 100)
print(my_first_module.PI)
# print(my_first_module.a)  # 看不到__name__==__main__后的代码，看不到a
print(__name__)  # __main__
print(my_first_module.__name__)  # my_first_module
