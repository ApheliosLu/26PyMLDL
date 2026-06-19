# Author: ApheliosLu
# 2026-06-19 14:14:44
# https://github.com/ApheliosLu


class Tool:
    count = 0  # 类属性，类似于类的全局变量

    def __init__(self, name):
        self.name = name
        Tool.count += 1  # 场景：统计一个类实例化了多少次

    def func(self):  # 对象方法
        print(f"{self.name}可以做很多事情。")

    @classmethod
    def show_tool_count(cls):
        """
        当不使用对象属性，只使用类属性、类方法
        :return:
        """
        print(f"实例化了 {cls.count} 个对象。")

    @staticmethod
    def help():
        """
        静态方法不使用对象属性，也不使用类属性
        :return:
        """
        print(f"这是一个工具类，作用是实例化各种工具对象。")

    def __del__(self):
        Tool.count -= 1  # 删除对象时减少类属性的值


if __name__ == "__main__":
    tool1 = Tool("斧头")
    print(Tool.count)

    tool2 = Tool("锤子")
    print(Tool.count)

    del tool1
    print(Tool.count)  # 如果想要变化需要重写类的del方法
    # print(tool2.count)  # 不推荐：使用对象访问类属性

    # print(dir(Tool))
    # Tool.name = "工具类"  # 不规范的写法：在类外给类增加类属性
    # print(Tool.name)
    # print(dir(Tool))

    print("-" * 50)
    Tool.show_tool_count()
    Tool.help()
