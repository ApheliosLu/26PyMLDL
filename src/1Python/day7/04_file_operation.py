# Author: ApheliosLu
# 2026-06-23 09:02:26
# https://github.com/ApheliosLu


def open_r():
    """r:读文件"""
    file = open("file2.txt", mode="r", encoding="utf-8")
    text = file.read()  # 读出来都是字符串
    print(text)
    file.close()


def oper_rw():
    """r+:读写文件"""
    file = open("file2.txt", mode="r+", encoding="utf-8")
    text = file.read()
    print(text)
    file.write("world!")  # r+模式写，打开后指针在开头，会覆盖相应部分的内容
    file.close()


def open_w():
    """w：不存在就创建；存在就清空"""
    file = open("file3", mode="w", encoding="utf-8")  #
    file.write("正是修行时！！!")
    file.close()


def open_a():
    """a：每次写的时候写到文件末尾"""
    file = open("file1", mode="a", encoding="utf-8")
    file.write("あなた")
    file.close()


def use_readline():
    file = open("file2.txt", encoding="utf-8")

    while True:
        text = file.readline()
        if not text:  # 读到文件末尾会拿到空字符串
            break
        print(text, end="")  # 文件每行末尾自带一个换行

    file.close()


def duplicate_large_file():
    """复制大文件"""
    file_read = open("file2.txt")
    file_write = open("file2_copy.txt", "w")

    while True:
        text = file_read.readline()
        if not text:
            break
        file_write.write(text)

    file_read.close()
    file_write.close()


def main():
    # open_r()
    # oper_rw()
    # open_w()
    # open_a()
    # use_readline()
    duplicate_large_file()


if __name__ == "__main__":
    main()
