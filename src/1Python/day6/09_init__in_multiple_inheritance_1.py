# Author: ApheliosLu
# 2026-06-19 10:28:16
# https://github.com/ApheliosLu


class Parent:
    def __init__(self, height):
        self.height = height


class Son1(Parent):
    def __init__(self, age, *args):
        self.age = age
        super().__init__(*args)


class Son2(Parent):
    def __init__(self, score, *args):
        self.score = score
        super().__init__(*args)


class Grandson(Son1, Son2):
    def __init__(self, name, *args):
        self.name = name
        super().__init__(*args)


if __name__ == "__main__":
    xiaoming = Grandson("小明", 18, 98.5, 175)  # 姓名 年龄 成绩 身高
    print(Grandson.__mro__)  # 关键就在于mro即方法搜索顺序
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)
    print(xiaoming.height)
