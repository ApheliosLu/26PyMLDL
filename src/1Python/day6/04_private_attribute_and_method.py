# Author: ApheliosLu
# 2026-06-14 14:55:49
# https://github.com/ApheliosLu


class Women:
    """
    私有属性和私有方法只能在类内部访问
    """

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print(f"{self.name}的年龄是{self.__age}")

    def boyfriend(self):  # 使用类内的方法访问私有属性和私有方法
        self.__secret()


if __name__ == "__main__":
    xiaohong = Women("小红", 18)

    print(xiaohong.name)
    # print(xiaohong.__age)  # AttributeError: 'Women' object has no attribute '__age'
    # xiaohong.__secret()  # AttributeError: 'Women' object has no attribute '__secret'

    xiaohong.boyfriend()  # 正确的访问私有属性和私有方法的方法

    # print(xiaohong._Women__age)  # 能运行，但不建议  访问类的 protected 成员 _Women__age
    # xiaohong._Women__secret()
