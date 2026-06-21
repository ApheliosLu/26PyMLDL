# Author: ApheliosLu
# 2026-06-21 14:36:42
# https://github.com/ApheliosLu

# 异常传递


def demo1():
    num = int(input("Enter a number: "))
    print("I am demo1.")
    return num


def demo2():
    print("I am demo2.")
    return demo1()


if __name__ == "__main__":
    try:
        print(f"结果：{demo2()}")
    except Exception as e:
        print(f"未知错误：{e}")
