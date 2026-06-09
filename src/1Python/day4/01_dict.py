# Author: ApheliosLu
# 2026-05-29 21:12:01
# https://github.com/ApheliosLu


def use_dict_base():
    """
    字典基础操作
    :return:
    """
    xiaoming_dict = {"name": "小明", "age": 18}
    print(xiaoming_dict)
    print(hex(id(xiaoming_dict)))

    # 1.取值
    print(xiaoming_dict["name"])  # 取不存在的key会报错
    print(xiaoming_dict.get("name1"))  # None 取不存在的key不会报错

    # 2.增加/修改
    # type：ignore
    xiaoming_dict["height"] = 190  # 增加
    xiaoming_dict["name"] = "小小明"  # 修改
    print(xiaoming_dict)

    ret=xiaoming_dict.setdefault("age", 20)  # setdefault若key本就存在，不会修改原值 ret=18
    print(f"ret={ret}")
    print(xiaoming_dict)

    # 3.删除
    print(xiaoming_dict.pop("name"))  # pop会返回删除的key对应的value
    print(xiaoming_dict)
    xiaoming_dict["gender"] = "male"
    print(xiaoming_dict)
    xiaoming_dict.popitem()  # popitem删除最后一个键值对
    print(xiaoming_dict)
    del xiaoming_dict["age"]
    print(xiaoming_dict)

    # 4.统计键值对数量
    print(len(xiaoming_dict))

    # 5.合并字典
    temp_dict = xiaoming_dict.copy()
    print(temp_dict)
    temp_dict["height"] = 191
    xiaoming_dict.update(temp_dict)  # 已存在的key-value会被覆盖
    print(xiaoming_dict)

    temp_dict.setdefault("name", "小明")
    temp_dict["age"] = 18
    print(temp_dict)
    xiaoming_dict.update(temp_dict)
    print(xiaoming_dict)

    # 6.清空、删除
    xiaoming_dict.clear()
    print(xiaoming_dict)
    print(hex(id(xiaoming_dict)))
    del xiaoming_dict


def use_dict_iteration():
    """
    字典遍历
    :return:
    """
    xiaoming_dict = {"name": "xiaoming", "qq": "123456", "phone": "10000"}

    # 直接遍历字典（for key in dict）时，每次循环拿到的是单个键（字符串），而不是 (key, value) 这样的元组。
    for key in xiaoming_dict:
        print(f"{key}:{xiaoming_dict[key]}")
    print("-" * 50)

    # 想要同时拿到kv需要用.items()
    for key, value in xiaoming_dict.items():
        print(f"key:{key:^5},value:{value:>9}")  # < > ^ 左 右 居中
    print("-" * 50)

    # 或 for kv in items，直接输出kv不拆包
    for kv in xiaoming_dict.items():
        print(f"{kv[0]}:{kv[1]}")
    print("-" * 50)

    for key in xiaoming_dict.keys():
        print(f"key:{key:>5}")
    print("-" * 50)

    for value in xiaoming_dict.values():
        print(f"value:{value:<9}")


def use_dict_list():
    """
    字典列表
    :return:
    """
    card_list = [
        {"name": "张三", "qq": "12345", "phone": "110"},
        {"name": "李四", "qq": "54321", "phone": "10000"},
    ]
    i = 0
    for card in card_list:
        print(f"card{i+1}:{card}")
        i += 1


def use_unpack_package():
    k, v, _, w = (1, 2, 3, 4)
    print(k, v, w)


if __name__ == "__main__":
    # use_dict_base()
    use_dict_iteration()
    # use_dict_list()
    # use_unpack_package()
