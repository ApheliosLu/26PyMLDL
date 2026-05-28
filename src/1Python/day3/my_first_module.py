# Author: ApheliosLu
# 2026-05-21 11:56:38
# https://github.com/ApheliosLu
PI = 3.1415926  # global constant


def print_line(char, times):
    print(char * times)
    # print(num)  # 其他模块调用时会报未解析的引用，因为num定义在name==main下面，不合理的写法


def main():
    a = "&"
    times = 100
    # global num
    num = 1000000
    print_line(a, times)


if __name__ == "__main__":
    # if __name__ == "__main__":下面的内容仅在执行本文件时会执行，可用于测试代码用
    a = 100  # 虽然是全局变量，但是对外（对其他模块）不可见
    num = 1
    main()
    print(f"{__name__}")  # __name__ 为 __main__
    # 当在另一个文件 import my_first_module 时，Python 只会执行模块中顶层可执行代码，
    # 不会执行 if __name__ == "__main__": 块里的内容，也不会执行它后面的代码，因此别的文件看不到a=100
