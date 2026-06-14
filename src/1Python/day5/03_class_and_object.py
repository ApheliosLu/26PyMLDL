# Author: ApheliosLu
# 2026-06-09 10:30:57
# https://github.com/ApheliosLu


# 定义一个类
class Person(object):  # 继承基类object
    def __init__(self, name, age, height):  # 初始化属性的方法__init__
        self.name = name  # 属性 = 形参
        self.age = age
        self.height = height

    def run(self):  # 类内的函数叫方法
        print(f"{self.name}正在奔跑")

    def eat(self):
        print(self.name + "正在吃东西")


# 类的实例化/实例化一个对象
elephant = Person("大象", 18, 1.75)
print(
    elephant
)  # <__main__.Person object at 0x000002202CA48AD0> elephant的地址和self的地址一样
print(elephant.name, elephant.age, elephant.height)
elephant.run()
elephant.eat()

tiger = Person("老虎", 17, 1.65)
print(tiger.name, tiger.age, tiger.height)
tiger.eat()

print("#" * 50)
print(dir(Person))  # 只有类方法
print("#" * 50)
print(dir(elephant))  # 多了属性

print("-" * 50)
print(id(elephant))
elephant.name = "大黄蜂"  # 地址未改变，对象是可变数据类型
print(id(elephant))
print(elephant.name, elephant.age, elephant.height)
