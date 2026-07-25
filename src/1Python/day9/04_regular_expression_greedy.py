# Author: ApheliosLu
# 2026-07-13 10:02:02
# https://github.com/ApheliosLu

import re
from sys import flags


def use_greedy():
    """
    贪婪非贪婪
    :return:
    """
    s = "This is a number 234-235-22-423"
    if r := re.match(r".+(\d+-\d+-\d+-\d+)", s):  # 前面的.只留了一个4给第二组
        print(r.group())
        print(r.group(1))  # 4-235-22-423
    if r := re.match(r".+?(\d+-\d+-\d+-\d+)", s):  # 把234都留给了第二组
        print(r.group())
        print(r.group(1))  # 234-235-22-423
    print("-" * 50)

    if r := re.match(r"aa(\d+)", "aa2343ddd"):
        print(r.group(1))
    if r := re.match(r"aa(\d+?)", "aa2343ddd"):
        print(r.group(1))  # 2
    if r := re.match(r"aa(\d+)ddd", "aa2343ddd"):
        print(r.group(1))
    if r := re.match(r"aa(\d+?)ddd", "aa2343ddd"):
        print(r.group(1))  # 2343


def use_r():
    """
    r的作用
    :return:
    """
    mm = "c:\\a\\b\\c"
    print(mm)

    if ret := re.match("c:\\\\", mm):
        print(ret.group())  # 不写r，匹配原生字符串两个\，要写四个\，最终输出一个\
    else:
        print(f"匹配失败！")

    if ret := re.match(r"c:\\", mm):  # 写r直接表示原生字符串，等价于不写r的四个\
        print(ret.group())


def use_option():
    """
    正则的选项
    :return:
    """
    if ret := re.match(r"\w*", "abc函", flags=re.A | re.I):  # 忽略汉字
        print(ret.group())

    if ret := re.match(r"a*", "aA", flags=re.I):  # 加上后不区分大小写
        print(ret.group())

    if ret := re.match(
        r".*", "abc\ndef", flags=re.S
    ):  # 匹配上\n 不写的话会忽略\n以及后面的
        print(ret.group())


if __name__ == "__main__":
    # use_greedy()
    # use_r()
    use_option()
