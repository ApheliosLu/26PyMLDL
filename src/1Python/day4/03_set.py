# Author: ApheliosLu
# 2026-05-30 20:23:05
# https://github.com/ApheliosLu


def use_hash():
    print(hash("aphelios"))
    print(hash("alune"))
    print(len("6140877460544229483"))
    print(len("900558781683425841"))


def use_set():
    """
    集合基本操作
    :return:
    """
    # 1.初始化
    set1 = set()  # 初始化空集合
    print(set1)
    set2 = {1, 2, "a", "b", "b"}  # 集合，无序、不可重复
    print(set2)
    # print(set2[0]) # 不支持随机访问

    # 增加元素 add
    fruits = {"apple", "banana", "orange", "grape", "mango"}
    fruits.add("cherry")
    print(fruits)

    # 复制集合 copy
    fruits_copy = fruits.copy()
    print(fruits_copy)
    print(id(fruits))
    print(id(fruits_copy))  # copy的id不同，直接=赋值的id会相同（改变一个影响另一个）

    # 返回两个集合的差集
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.difference(y)
    print(f"x和y的差集z：{z}")

    # 移出相同的元素
    x.difference_update(y)
    print(f"x中移出与y中相同的元素后，x:{x}")

    # 删除元素 discard
    y.discard("apple")
    print(y)

    # 返回集合的交集
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    result = x.intersection(y, z)  # x和y、z都有的元素
    print(result)

    # 不重复的元素结合
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y)
    print(z)
    print(x ^ y)
    print("-" * 50)

    # 并集
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.union(y)
    print(z)
    x.update(y)
    print(x)

    print("apple" in z)  # in判断元素是否在集合内

    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    print(x - y)  # 差集
    print(x & y)  # 交集
    print(x | y)  # 并集
    print(x ^ y)  # 只在一个集合中的元素
    print(x.symmetric_difference(y))  # 同上 异或

    x.clear()
    print(x)


def use_set_generator():
    """
    使用生成式
    :return:
    """
    # 元组生成式
    generator = (x for x in range(10))
    # 并非元组，而是一个生成式<generator object use_set_generator.<locals>.<genexpr> at 0x0000024E99D08E10>
    print(generator)  # 生成器不会立刻计算所有值，节省内存
    print(next(generator))  # 用next()或循环获取生成器的值
    print(next(generator))

    my_tuple = tuple(generator)  # 生成器转元组
    print(my_tuple)
    print(my_tuple + my_tuple)
    print(my_tuple * 2)

    # 集合生成式
    my_set = {x for x in "abracadabra" if x not in "abc"}
    print(my_set)
    print(len(my_set))
    print(max(my_set))

    # 字典生成式
    my_dict = {x: x**2 for x in range(10)}
    print(my_dict)


if __name__ == "__main__":
    # use_hash()
    # use_set()
    use_set_generator()
