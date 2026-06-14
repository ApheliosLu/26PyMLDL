# Author: ApheliosLu
# 2026-06-09 10:31:11
# https://github.com/ApheliosLu


"""
3.设计一个类，实例化1个对象，会实现下面两种行为
需求：
•一只 黄颜色 的 狗狗 叫 大黄
•具有  汪汪叫 行为
•具有  摇尾巴 行为
"""


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self) -> None:
        print(f"{self.name}汪汪叫")

    @staticmethod  # 静态方法
    def wag_tail():
        print(f"摇尾巴")


my_dog = Dog("大黄", "黄")
print(f"这是一只{my_dog.color}颜色的狗，叫{my_dog.name}")
my_dog.bark()
my_dog.wag_tail()

print(my_dog.__dict__)  # 展示对象的属性 {'name': '大黄', 'color': '黄'}
print(dir(my_dog))  # dir展示对象的所有属性和方法（包括内置）

a = 123
print("%d" % a)
print("%x" % a)
print(f"{a:d}")
print(f"{a:x}")
