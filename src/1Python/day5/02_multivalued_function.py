# Author: ApheliosLu
# 2026-06-09 10:30:38
# https://github.com/ApheliosLu


# 多值参数，就是参数个数不确定，必须是下面的写法
# *args接位置positional参数 **kwargs接键值对keyword参数
# *接收元组 **接收字典
def demo2(*args, **kwargs):
    print(f"demo2-args:{args}")  # demo2-args:(2, 3, 4)
    print(
        f"demo2-kwargs:{kwargs}"
    )  # demo2-kwargs:{'name': '小明', 'age': 10, 'gender': True}


def demo(num, *args, **kwargs):
    print(num)  # 1
    print(args)  # (2, 3, 4)
    print(kwargs)  # {'name': '小明', 'age': 10, 'gender': True}
    print(*args)  # 2 3 4 解包

    # print(**kwargs)
    # TypeError: print() got an unexpected keyword argument 'name'
    # print函数只支持可变位置参数，没有对应的kwargs

    demo2(*args, **kwargs)  # 元组和字典的传参


def sum_numbers(*args):
    """
    接收传入的任意多个参数并求和
    :param args:
    :return:
    """
    num = 0
    for arg in args:
        num += arg
    return num


if __name__ == "__main__":
    # demo(1, 2, 3, 4, name="小明", age=10, gender=True)  # 元组和字典的拆包

    # 在 元组变量前，增加 一个 *，代表元组拆包
    # 在 字典变量前，增加 两个 *，代表字典拆包
    gl_nums = (2, 3, 4)
    gl_xiaoming = {"name": "小明", "age": 10, "gender": True}
    demo(1, *gl_nums, **gl_xiaoming)  # 等价于上面对demo的调用

    # print(f"sum_numbers:{sum_numbers(1,2,3)}")
