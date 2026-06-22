# Author: ApheliosLu
# 2026-06-22 19:02:52
# https://github.com/ApheliosLu


class A:
    def __init__(self):
        self.__age = 10

    def base_age(self):
        print(self.__age)  # 公共方法访问私有属性


class B(A):
    def get_age(self):
        self.base_age()  # 调用父类方法


def main():
    zhangsan = B()
    zhangsan.get_age()  # 子类对象通过调用父类方法访问父类私有属性
    # print(zhangsan._A__age)  # 不规范
    print(dir(zhangsan))
    print(dir(B))


if __name__ == "__main__":
    main()
