# Author: ApheliosLu
# 2026-04-08 15:26:49
# https://github.com/ApheliosLu

import random


def use_if_elif_else():
    score = int(input("Enter your score:"))
    if score < 0 or score > 100:
        print("Your score must be between 0 and 100")
    elif score >= 90:
        print("Level A:Excellent")
    elif score >= 80:
        print("Level B:Good")
    elif score >= 60:
        print("Level C:Pass")
    else:
        print("Fail!")


# use_if_elif_else()


def use_random():
    # random.seed()  # 不指定数字，Python 会用系统当前时间做种子。不写seed同理
    random.seed(10)
    player = int(input("请出拳——石头（1），剪刀（2），布（3）："))
    computer = random.randint(1, 3)
    if (
        (player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)
    ):
        print("You win!")
    elif player == computer:
        print("Draw!")
    else:
        print("You lose!")


# use_random()


def use_logic():
    age = 100
    if 0 <= age <= 100:
        print("年龄正确！")
    else:
        print("年龄不正确！")

    python_score = 50
    cpp_score = 50
    if python_score > 60 or cpp_score > 60:
        print("Pass!")
    else:
        print("Fail!")

    is_employed = True
    if not is_employed:
        print("NO ENTERING!")


use_logic()
