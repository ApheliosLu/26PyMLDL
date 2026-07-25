# Author: ApheliosLu
# 2026-07-13 09:48:55
# https://github.com/ApheliosLu

import copy


def use_list():
    a = [1, 2, 3]
    b = a
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}")  # id(b)=id(a)
    b[0] = 10
    print(f"a = {a}")  # a变了，可变数据类型，复制了引用
    print(f"b = {b}")

    c = [4, 5, 6]
    # d = c.copy()  # 浅 copy 不是直接赋值；自定义对象无法直接使用copy方法
    d = copy.copy(c)  # 等价于上一行
    print(f"id(c) = {id(c)}")
    print(f"id(d) = {id(d)}")  # 可变数据类型 id(d)≠id(c)
    d[0] = 10
    print(f"c = {c}")  # c没变
    print(f"d = {d}")


def use_copy():
    """
    浅copy:copy的是外层的容器对象，但是内层的元素没有copy
    """
    c = (1, 2, 3, 4)
    d = copy.copy(c)
    print(f"id(c) = {id(c)}")
    print(f"id(d) = {id(d)}")  # 不可变数据类型 id(d)=id(c)

    a = [1, 2]
    b = [3, 4]
    e = [a, b]  # 嵌套
    f = copy.copy(e)
    print(f"id(e) = {id(e)}")
    print(f"id(f) = {id(f)}")  # 可变数据类型 id(e)≠id(f)
    print(f"e = {e}")
    print(f"f = {f}")
    print("-" * 50)
    a[0] = 10
    print(f"e = {e}")
    print(f"f = {f}")  # e和f都变了
    print(f"id(e[0]) = {id(e[0])}, id(e[1]) = {id(e[1])}")
    print(f"id(f[0]) = {id(f[0])}, id(f[1]) = {id(f[1])}")  # 内层地址一致


def use_deepcopy():
    """
    deepycopy:递归去copy，不管有多少层，都会新做一个空间，把数据拿进来
    :return:
    """
    a = [1, 2]
    b = [3, 4]
    e = [a, b]  # 嵌套
    f = copy.deepcopy(e)
    print(f"id(e) = {id(e)}")
    print(f"id(f) = {id(f)}")  # 可变数据类型 id(e)≠id(f)
    print(f"e = {e}")
    print(f"f = {f}")
    print("-" * 50)
    a[0] = 10
    print(f"e = {e}")
    print(f"f = {f}")  # e变了,f没变
    print(f"id(e[0]) = {id(e[0])}, id(e[1]) = {id(e[1])}")
    print(f"id(f[0]) = {id(f[0])}, id(f[1]) = {id(f[1])}")  # 内层地址也不一致


class Hero:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood
        self.equipment = [
            "鞋子",
            "耳环",
        ]  # 嵌套可变数据类型，如果浅拷贝会影响原本的对象


def use_copy_own_object():
    """对自定义对象的copy"""
    old_hero = Hero("蚂蚁", 90)
    new_hero = copy.deepcopy(old_hero)
    # 若是浅拷贝，则修改new的可变数据类型的属性会影响old
    # 若是深拷贝，则修改new不影响old
    new_hero.blood = 80
    new_hero.equipment.append("药水")
    print(f"old_hero.blood = {old_hero.blood}")
    print(f"old_hero.equipment = {old_hero.equipment}")
    print(f"new_hero.blood = {new_hero.blood}")
    print(f"new_hero.equipment = {new_hero.equipment}")


if __name__ == "__main__":
    # use_list()
    # use_copy()
    # use_deepcopy()
    use_copy_own_object()
