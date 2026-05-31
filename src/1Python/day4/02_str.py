# Author: ApheliosLu
# 2026-05-30 11:09:31
# https://github.com/ApheliosLu


def str_iter():
    """
    字符串遍历
    :return:
    """
    str1 = "hello python"
    for char in str1:
        print(char, end=",")


def check_type():
    """
    判断字符串类型
    :return:
    """
    s1 = "abc"
    print(s1.isalnum())
    print(s1.isdigit())
    s2 = "123"
    print(s2.isdecimal())


def str_find():
    """
    字符串查找与替换
    :return:
    """
    s1 = "abcdefgcdef"
    print(s1.find("cd"))
    print(s1.find("cd", 4))
    print(s1.find("ce"))

    s2 = s1.replace("cd", "CD", 1)
    print(s2)


def str_split_join():
    """
    分割与连接
    :return:
    """
    s1 = "abc bcd 我很帅"
    print(s1.split())  # 将一个字符串分成三个元素的列表,默认按照空格分割
    s2 = "abc,bcd,我很帅"
    print(s2.split(","))  # 按照逗号分割

    s3 = "abc\nbcd\nefg"
    print(s3.splitlines())  # 换行分割
    s4 = "abc\r\nbcd\nefg"
    print(s4.splitlines(True))  # 将换行符包括在分割的每一个部分里

    # 列表转字符串
    s5 = ["a", "b", "c", "d"]
    print(type(s5))
    s6 = "".join(s5)
    print(s6)
    print(type(s6))


def study_rn():
    """
    \r和\n的区别
    :return:
    """
    s1 = "abc\rd"
    print(s1)  # 理应输出dbc,因PyCharm的控制台渲染机制导致输出d
    print(repr(s1))  # repr不处理转义，原封不动展示真实内容
    print("-" * 50)
    s2 = "abc\nd"
    print(s2)
    print("-" * 50)
    s3 = "abc\r\nd"
    print(s3)


def str_slice():
    """
    字符串切片
    :return:
    """
    num_str = "0123456789"
    # 1. 截取从 2 ~ 5 位置 的字符串
    print(num_str[2:6])

    # 2. 截取从 2 ~ `末尾` 的字符串
    print(num_str[2:])

    # 3. 截取从 `开始` ~ 5 位置 的字符串
    print(num_str[:6])

    # 4. 截取完整的字符串
    print(num_str[:])

    # 5. 从开始位置，每隔一个字符截取字符串
    print(num_str[::2])

    # 6. 从索引 1 开始，每隔一个取一个
    print(num_str[1::2])

    # 倒序切片
    # -1 表示倒数第一个字符
    print(num_str[-1])

    # 7. 截取从 2 ~ `末尾 - 1` 的字符串
    print(num_str[2:-1])

    # 8. 截取字符串末尾两个字符
    print(num_str[-2:])

    # 9. 字符串的逆序（面试题）
    print(num_str[::-1])


def list_slice():
    """
    列表切片
    :return:
    """
    my_list = list("0123456789")  # 字符串转列表
    print(my_list)
    print([int(x) for x in my_list])  # 列表元素转整型
    print(my_list[2:6])


def index_count():
    hello_str = "heallo hello"

    # 1.统计字符串长度
    print(len(hello_str))

    # 2.统计子串出现的次数
    print(hello_str.count("llo"))
    print(hello_str.count("abc"))

    # 3.获取子串出现的位置
    print(hello_str.index("llo"))  # 子串不存在会报错
    print(hello_str.find("111"))  # 子串不存在输出-1


if __name__ == "__main__":
    # str_iter()
    # check_type()
    # str_find()
    # str_split_join()
    # study_rn()
    # str_slice()
    # list_slice()
    index_count()
