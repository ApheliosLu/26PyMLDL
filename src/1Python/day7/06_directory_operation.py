# Author: ApheliosLu
# 2026-06-23 17:39:35
# https://github.com/ApheliosLu

import os


def use_rename():
    """
    rename & remove
    :return:
    """
    # os.rename("file3", "file4")  # 相对路径
    # os.rename(
    #     "D:\\1\\CCC\\Python\\26PyMLDL\\src\\1Python\\day7\\file4",
    #     "D:\\1\\CCC\\Python\\26PyMLDL\\src\\1Python\\day7\\file3",
    # )  # 绝对路径 将单反斜杠换为双反斜杠

    # os.rename("./dir1/file1", "./dir1/file2")  # 或用单斜杠
    os.remove("./dir1/file2")


def use_dir_func():
    """
    目录操作
    :return:
    """
    file_list = os.listdir(".")  # 查看目录下内容，返回一个列表
    print(file_list)

    # os.mkdir("dir2")
    # os.rmdir("dir1")  # 需要删除文件夹下所有内容再删除文件夹

    print(os.getcwd())
    os.chdir("dir2")
    file = open("file1", "w", encoding="utf-8")
    file.close()


def change_dir():
    """
    改变路径
    :return:
    """
    print(os.getcwd())
    os.chdir("dir2")  # cd
    print(os.getcwd())


def scan_dir():
    """
    目录深度优先遍历
    :return:
    """


if __name__ == "__main__":
    # use_rename()
    # use_dir_func()
    # change_dir()
    scan_dir()
