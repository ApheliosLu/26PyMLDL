# Author: ApheliosLu
# 2026-05-29 09:43:31
# https://github.com/ApheliosLu

import random


def print_line(char, times):
    print(char * times + "分割线" + char * times)


def main():
    a = "*"
    times = 50
    num = 100
    print_line(a, times)


def random_print(a, b, seed=None):
    if seed is not None:
        random.seed(seed)  # 设置随机数种子，则每次生成的随机数保持一致
    print(random.randint(a, b))


if __name__ == "__main__":
    """
    通过判断name变量的取值，可以确定当前的执行情况。这样可以确保测试代码只在直接执行脚本时被执行，而在导入为模块时不被执行。
    name变量在自身文件中为main，在调用文件中显示自身名字。
    该语句下面的内容（包括全局变量）在python xxx.py时会执行，而在import xxx时不会执行。
    """
    main()
    random_print(1, 100, seed=10)
