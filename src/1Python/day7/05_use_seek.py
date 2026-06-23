# Author: ApheliosLu
# 2026-06-23 15:22:39
# https://github.com/ApheliosLu

import os


def seek_start():
    """
    相对于文件起始位置进行偏移
    :return:
    """
    file = open("file1", mode="r+", encoding="utf-8")
    file.seek(6, os.SEEK_SET)  # 相对于开头偏移6个字节（汉字偏移是3的整数倍）
    text = file.read(5)  # 读5个字符（二进制下是5个字节）
    print(text)
    file.close()


def seek_end():
    """
    相对于文件尾部进行偏移
    :return:
    """
    file = open("file1", mode="r+", encoding="utf-8")
    file.seek(0, os.SEEK_END)  # 文本文件相对于CUR/END只能偏移0
    text = file.read(5)
    print(text)  # 读不到内容，是空字符串
    file.close()


def seek_cur():
    """
    相对于文件当前位置不动
    :return:
    """
    file = open("file1", mode="r+", encoding="utf-8")
    file.seek(0, os.SEEK_CUR)  # 文本文件相对于CUR/END只能偏移0
    text = file.read(5)
    print(text)
    file.close()


def seek_b_cur():
    """
    二进制b模式下，读取到的是字节流，用于读取图片、音视频、不同编程语言间通信等等
    :return:
    """
    file = open("file1", mode="rb+")
    file.seek(5, os.SEEK_CUR)  # 二进制下相对于CUR/END偏移可正可负
    file.seek(-2, os.SEEK_CUR)
    file.seek(-3, os.SEEK_END)
    bytes_stream = file.read()  # 字节流 b'rld'
    print(bytes_stream)
    print(type(bytes_stream))  # <class 'bytes'>
    file.close()


def copy_file():
    """
    复制二进制文件
    :return:
    """
    file_from = open("韩立.png", "rb+")
    file_to = open("韩立第二元婴.png", "wb")
    bytes_stream = file_from.read()
    file_to.write(bytes_stream)
    file_to.close()
    file_from.close()


def modify_movie():
    """
    修改文件，改变哈希值，避免检测
    :return:
    """
    file_from = open("韩立.png", "rb+")
    file_from.seek(10, os.SEEK_SET)

    b = file_from.read(1)  # 读一个字节
    inverted_b = bytes([~b[0] & 0xFF])  # 按位取反后限制在0~255范围内
    print(f"b = {b}")
    print(f"inverted_b = {inverted_b}")

    file_from.seek(10, os.SEEK_SET)
    # 写回取反后的字节
    file_from.write(inverted_b)

    file_from.close()


if __name__ == "__main__":
    # seek_start()
    # seek_end()
    # seek_cur()
    seek_b_cur()
    # copy_file()
    # modify_movie()
