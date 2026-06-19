# Author: ApheliosLu
# 2026-06-19 10:10:39
# https://github.com/ApheliosLu
from uuid import main


class Son1:
    def __init__(self, age, *args):
        # Son1 的 __init__ 方法接收到 18 和 98.5 作为参数。
        # self.age = 18，
        # 然后 super().__init__(98.5) 会调用 Son2.__init__（根据 MRO 的顺序）。

        self.age = age
        super().__init__(*args)

        # 本质：
        # super().__init__(*args) 的是把剩下的参数（*args）传递给 MRO 顺序中的下一个类 的 __init__ 方法。
        # Grandson → Son1 → Son2 → object
        # 所以 Son1 里的 super() 实际指向的是 Son2，这行代码会调用 Son2.__init__，完成 score 属性的初始化。


class Son2:
    def __init__(self, score):
        self.score = score


class Grandson(Son1, Son2):
    def __init__(self, name, *args):
        self.name = name  # 子类自己初始化name
        super().__init__(*args)  # 其余参数交予 MRO 顺序中的下一个类init


if __name__ == "__main__":
    xiaoming = Grandson("小明", 18, 98.5)  # 姓名 年龄 分数
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)
