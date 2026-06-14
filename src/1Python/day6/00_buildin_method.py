# Author: ApheliosLu
# 2026-06-13 15:28:41
# https://github.com/ApheliosLu

# 00_内置方法


class Cat(object):
    """这是一个猫类"""

    def __init__(self, name):
        # self.属性名 = 形参/属性初始值
        self.name = name

        print(f"这是一个初始化方法，初始化了:{self.name}")

    def eat(self):
        print(f"{self.name}在吃鱼")

    def drink(self):
        print("%s在喝水" % self.name)

    def __del__(self):
        print(f"{self.name}对象被销毁")

    def __str__(self):
        """
        返回对象的描述信息，print输出对象使用
        给人看的字符串描述，可读性优先
        """
        return f"Cat类的对象:{self.name}"

    def __repr__(self):
        """
        给解释器 / 开发者看的精准标识，理想状态是能直接复制代码重建对象
        :return:
        """
        return f"Cat('{self.name}')"


def main():
    tom = Cat("Tom")
    tom.drink()
    tom.eat()
    print(tom)  # 调用__str__方法
    print(str(tom))  # 同上
    print(repr(tom))  # Cat('Tom')

    lazy_cat = Cat("懒猫")
    print(tom is lazy_cat)  # is用于对比变量地址

    # tom.height = 11  # 不规范的编程，不要在类外面给对象增加属性
    # print(tom.height)
    # print(dir(tom))


if __name__ == "__main__":
    main()
    print("程序结束！")
