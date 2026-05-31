# Author: ApheliosLu
# 2026-05-31 14:40:49
# https://github.com/ApheliosLu


def demo(num: int, num_list: list):
    """
    函数内操作可变数据类型
    :param num:
    :param num_list:
    :return:
    """

    print("函数内部代码")

    # num = num + num
    num += num

    # 使用赋值语句，不会改变传递的实参变量
    # num_list = [4, 5, 6]

    # 使用方法修改数据内容，会改变传递的实参变量
    num_list.extend(num_list)  # 由于是调用方法，所以不会修改变量的引用
    num_list += ["a", "b", "c"]

    print(num)
    print(num_list)
    print("函数代码完成")


gl_num = 9  # 不可变数据类型：函数内的修改不会改变外部（除非函数内用global声明）
gl_list = [1, 2, 3]  # 可变数据类型：函数内的修改会改变外部
demo(gl_num, gl_list)

print(gl_num)
print(gl_list)
