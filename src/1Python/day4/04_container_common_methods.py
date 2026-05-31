# Author: ApheliosLu
# 2026-05-31 09:45:22
# https://github.com/ApheliosLu


def find_name():
    students = [
        {"name": "阿土", "age": 20, "gender": True, "height": 1.7, "weight": 75.0},
        {"name": "小美", "age": 19, "gender": False, "height": 1.6, "weight": 45.0},
    ]
    to_find_name = "阿火"
    for stu_dict in students:
        print(stu_dict)
        if stu_dict["name"] == to_find_name:
            print(f"找到了阿火！")
            break  # break结束for循环将不会执行else
    else:  # for循环结束后，会正常执行else
        print(f"没找到阿火！")
    print(f"循环结束。")


def list_set_slice():
    # 显式声明列表可以包含 int 或 str
    test_list: list[int | str | list[str]] = [1, 2, 3, 4, 5, 6]
    # test_list.insert(3, ["x", "y", "z"])  # 并非想要效果
    test_list[3:3] = ["x", "y", "z"]  # 往列表中插入一个列表
    print(test_list)
    print(test_list[3:3])  # []


def list_compare():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)
    print(a is b)  # is运算符是判断两个对象的地址是否一致的，一致是True

    c = (1, 2, 3)
    d = (1, 2, 3)
    print(c == d)
    print(c is d)  # 不可变类型，地址相等


def use_method():
    """
    容器的一些方法 zip enumerate，用于合并元组、生成序列键值对字典
    :return:
    """
    a = (1, 2, 3)
    b = ("a", "b", "c")

    print(list(zip(a, b)))  # zip将两个元组合并
    print(dict(zip(b, a)))

    # 如何使用enumerate 枚举
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    list2 = list(enumerate(seasons))  # 枚举会自动加序号
    print(f"list2:{list2}")

    my_dict = dict(list2)
    print(my_dict)

    print({v: k for k, v in my_dict.items()})
    new_dict = {v: k for k, v in my_dict.items()}
    print(new_dict)


def use_enumerate():
    a = (1, 2, 3)
    b = ("a", "b", "c")
    print(list(zip(a, b)))
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    list2 = list(enumerate(seasons))
    print(list2)

    dict1 = {}
    for i in list2:
        dict1[i[1]] = i[0]  # 另一种列表转字典
    print(dict1)


def other_methods():
    # 判断空字符串
    space_str = "     \r\t\n"
    print(space_str.isspace())  # True

    # 判断字符串是否只包含数字
    # 1> 都不能判断小数
    # num_str = "1.1"
    # 2> unicode 字符串
    # num_str = "\u00b2"
    # 3> 中文数字
    num_str = "一千零一"
    print(num_str)
    print(num_str.isdecimal())
    print(num_str.isdigit())  # 可以判断unicode
    print(num_str.isnumeric())  # 可以判断unicode、中文数字


def scrap_process():
    """
    抓取字符串后处理
    :return:
    """

    # 假设：以下内容是从网络上抓取的
    # 要求：顺序并且居中对齐输出以下内容
    poem = [
        "\t\n 登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼",
    ]
    for poem_str in poem:
        # 先使用 strip 方法去除字符串中的空白字符
        # 再使用 center 方法居中显示文本
        # print("|%s|" % poem_str.strip().center(10, " "))
        print(f"|{poem_str.strip().center(10,' '):^20}|")

    # 假设：以下内容是从网络上抓取的
    # 要求：
    # 1. 将字符串中的空白字符全部去掉
    # 2. 再使用 " " 作为分隔符，拼接成一个整齐的字符串
    print("-" * 100)
    poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\t\n更上一层楼"
    print(poem_str)
    # 1. 拆分字符串
    poem_list = poem_str.split()
    print(poem_list)
    # 2. 合并字符串
    result = " ".join(poem_list)
    print(result)


if __name__ == "__main__":
    # find_name()
    list_set_slice()
    # list_compare()
    # use_method()
    # use_enumerate()
    # other_methods()
    # scrap_process()
