# Author: ApheliosLu
# 2026-06-25 20:49:00
# https://github.com/ApheliosLu

import sys


def pass_parameters_to_python():
    """
    1.命令行运行传参
    python .\07_pass_parameters_to_python.py 123 abc
    ['.\\07_pass_parameters_to_python.py', '123', 'abc']

    2.pycharm运行传参
    选择需要传参运行的文件，修改运行配置，传入脚本形参

    3.若要传入大量参数，则将配置导入一个文件中并传给python文件
    """
    print(type(sys.argv))  # <class 'list'>

    # 参数列表 默认只有只有自身 ['D:\\1\\CCC\\Python\\26PyMLDL\\src\\1Python\\day7\\07_pass_parameters_to_python.py']
    print(
        sys.argv
    )  # ['D:\\1\\CCC\\Python\\26PyMLDL\\src\\1Python\\day7\\07_pass_parameters_to_python.py', 'abc', '123']


def write_hello(file_path):
    """
    python文件传参执行示例
    :param file_path:
    :return:
    """
    file = open(file_path, "w+", encoding="utf-8")
    file.write("hello")
    file.close()


if __name__ == "__main__":
    # pass_parameters_to_python()

    write_hello(sys.argv[1])  # argv[0]是执行的python文件本身 argv[1]是传入的第一个参数
    # 使用命令行运行上一行的函数 python .\07_pass_parameters_to_python.py file4
    # 或用pycharm传参运行，脚本参数为file6。执行后增加file6文件、内部写入hello
