# 作者: 陆离ApheliosLu
# 2026年04月06日17时06分05秒
# Leon12097@163.com

"""
运算符优先级：算术>关系>逻辑>赋值
括号 → 幂次 → 正负 → 乘除模 → 加减 → 移位 → 位运算 → 比较 → not → and → or → 赋值
"""


def use_arithmetic():
    """
    学习使用算术运算符
    :return:
    """
    a = 5 / 2
    print(a)
    a = 5 // 2
    print(a)
    a = 0.99**365
    print(f"a= {a:8.5f}")
    print(3 > 5)


# use_arithmetic()


def use_logic():
    print(3 and 5)  # 遇假则假，都真返回后一个即5
    print(0 or 0)  # 遇真则真，都假返回前一个0
    print(not 0)  # 返回True
    # and 需要两边都真，所以（前面为真时）必须执行后面
    3 and print("hello")  # 3为真，短路运算会输出hello；省去书写if
    0 and print("world")  # 0为假，短路运算不会输出world
    # or 只要前面假，就必须看后面
    0 or print("你可以看到or")  # 会输出“你可以看到or”


use_logic()


def use_bit():
    print(-5 >> 1)  # 减一除二
    print(5 ^ 0)  # 与零异或得自身
    print(5 ^ 5)  # 与己异或得零


# use_bit()
