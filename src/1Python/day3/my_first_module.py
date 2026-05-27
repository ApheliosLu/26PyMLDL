# Author: ApheliosLu
# 2026-05-21 11:56:38
# https://github.com/ApheliosLu
PI = 3.1415926  # global constant


def print_line(char, times):
    print(char * times)


def main():
    a = "&"
    times = 100
    num = 1000000
    print_line(a, times)


if __name__ == "__main__":
    main()
    print(f"{__name__}")  # __name__ 为 __main__
