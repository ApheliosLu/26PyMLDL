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


def scan_dir(current_path, width):
    """
    目录深度优先遍历
    :return:
    """
    file_list = os.listdir(current_path)  # 得到当前文件夹下的所有文件
    for file in file_list:
        print(" " * width, file)  # 打印文件名;width表示打印多少空格以控制目录树缩进
        new_path = (
            current_path + "/" + file
        )  # 路径拼接，防止多级目录无法识别（如：dir3若不拼接则仅仅是一个文件名，无法被识别成目录。即dir3非目录，而dir2/dir3系目录）
        if os.path.isdir(new_path):  # 如果file是目录
            scan_dir(new_path, width + 4)  # 递归遍历


def use_stat(file_path):
    """
    获取文件大小等信息
    :return:
    """
    file_info = os.stat(file_path)  # 获取文件信息
    print(
        f"size{{{file_info.st_size}}},uid{{{file_info.st_uid}}},mode{{{file_info.st_mode:x}}},mtime{{{file_info.st_mtime}}}"
    )  # 文件大小 文件所有者用户id 文件类型与权限模式 文件创建时间 双花括号{{转译花括号{

    # 把秒数转换为字符串时间
    from time import strftime
    from time import gmtime

    # 使用gmtime()把文件的创建时间戳转换为UTC时间，并用strftime()格式化为可读的时间字符串
    print(
        strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime))
    )  # 2026-06-23 08:16:32


if __name__ == "__main__":
    # use_rename()
    # use_dir_func()
    # change_dir()
    # scan_dir(".", 0)  # 相对路径/绝对路径均可
    use_stat("file1")
