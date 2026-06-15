# Author: ApheliosLu
# 2026-06-15 15:01:56
# https://github.com/ApheliosLu


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}eat")

    def drink(self):
        print(f"{self.name}drink")

    def run(self):
        print(f"{self.name}run")

    def sleep(self):
        print(f"{self.name}sleep")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # 子类继承父类的init
        self.color = color  # 子类对父类的init进行扩展

    def bark(self):
        print(f"{self.color}的{self.name}汪汪叫")

    def run(self):
        super().run()  # 调用父类的run
        print(f"{self.name}跑得快")


class XiaoTianQuan(Dog):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age

    def bark(self):  # 覆盖父类方法
        print(f"{self.name}嗷呜嗷呜嗷呜")

    def fly(self):
        print(f"{self.age}岁的{self.color}{self.name}fly")


if __name__ == "__main__":
    wangcai = Dog("旺财", "黄色")
    wangcai.bark()
    wangcai.run()

    xiaotianquan = XiaoTianQuan("哮天犬", "黑色", "2000")
    xiaotianquan.fly()
    xiaotianquan.bark()
