# Author: ApheliosLu
# 2026-06-25 21:09:10
# https://github.com/ApheliosLu

import os
import subprocess


def read_conf():
    """
    读取配置,eval处理配置文件
    :return:
    """
    file = open("file6", "r", encoding="utf-8")
    text_info = file.read()

    print(type(text_info))  # <class 'str'>
    print(text_info)

    # print(text_info["ip"])  # TypeError: string indices must be integers, not 'str'
    # print(dict(text_info))  # ValueError: dictionary update sequence element #0 has length 1; 2 is required
    print("-" * 50)
    my_dict = eval(text_info)
    print(type(my_dict))  # <class 'dict'>
    print(my_dict)

    file.close()


def eval_calculator():
    """
    使用eval编写一个简易计算器
    :return:
    """
    input_str = input("请输入一个算术题：")
    print(eval(input_str))


def eval_os():
    # os.system("ls")
    os.system("rm -r file5")

    eval("__import__('os').system('ls')")  # 不要用eval执行前端发过来的任何子串
    # 上一行等价于
    # import os
    # os.system('ls')


def eval_process():
    subprocess.run(["ls"], check=True)
    subprocess.run(["rm", "-r", "file5"], check=True)

    # eval("__import__('subprocess').run('ls')")


if __name__ == "__main__":
    read_conf()
    # eval_calculator()
    # eval_os()
    # eval_process()
