# Author: ApheliosLu
# 2026-06-14 10:29:03
# https://github.com/ApheliosLu

# 封装


class Person:
    """人类"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f"{self.name}跑步了，体重减去0.5公斤，现有体重为{self.weight}公斤")

    def eat(self):
        self.weight += 1
        print(f"{self.name}吃饭了，体重增加1公斤，现有体重为{self.weight}公斤")

    def __str__(self):
        """
        因为该函数是别人调用的，必须返回str类型
        :return:
        """
        return f"我的名字叫{self.name}，体重为{self.weight}公斤"


if __name__ == "__main__":
    elephant = Person("大象", 100)
    elephant.run()
    elephant.eat()
    print(elephant)

    tiger = Person("老虎", 45)
    tiger.eat()
    tiger.run()
    print(tiger)
