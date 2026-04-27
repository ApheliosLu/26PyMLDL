# Author: ApheliosLu
# 2026-04-08 15:58:48
# https://github.com/ApheliosLu


def use_while():
    i = 1
    while i <= 5:
        print(f"hello,{i}")
        i += 1
    print(f"循环结束，i = {i}")


# use_while()


def use_continue():
    result = 0
    num = 0
    while num <= 100:
        if num % 2 == 1:
            num += 1
            continue  # 跳过本次循环后续的代码
        result += num
        num += 1
    print(f"0~100之间的偶数求和结果 = {result} num = {num}")


use_continue()


def use_break():
    result = 0
    i = 0
    while i <= 100:
        if result > 2000:
            break  # 结束循环
        result += i
        i += 1
    print(f"0~100之间的数字求和结果 = {result} i = {i}")


# use_break()


def nine_nine():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print(f"{col} * {row} = {col*row}", end="\t")
            col += 1
        print()
        row += 1


# nine_nine()


def use_for_else():
    item = None  # 解除 局部变量 'item' 可能在赋值前引用 的警告
    my_list = ["ab", "cd", "ef", "haha"]
    for item in my_list:
        print(item, end=" ")
    print()
    print("-" * 50)
    if item == "haha":
        print(f"遍历到了最后一个,item = {item}")  # for的游标在for循环外可以使用
    else:
        print(f"遍历失败")


# use_for_else()

for i in range(10):  # in一个可迭代对象
    if i == 15:
        print("I got 15!")
        break
else:
    print("I didn't find 15!")
