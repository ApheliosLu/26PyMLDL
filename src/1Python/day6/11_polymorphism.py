# Author: ApheliosLu
# 2026-06-19 11:32:45
# https://github.com/ApheliosLu

# 多态：同一条指令，不同的对象产生的行为是不一样的


class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print(f"{self.name} 蹦蹦跳跳地玩耍")


class XiaoTianDog(Dog):
    def game(self):
        print(f"{self.name} 飞到天上去玩耍")


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog: Dog):  # 类型注解(Type Hint)
        print(f"{self.name}在和{dog.name}快乐地玩耍……")
        dog.game()


if __name__ == "__main__":
    zhangsan = Person("张三")
    wangcai = Dog("旺财")
    zhangsan.game_with_dog(wangcai)

    xiaotianquan = XiaoTianDog("哮天犬")
    zhangsan.game_with_dog(xiaotianquan)
