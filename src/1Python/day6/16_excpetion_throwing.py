# Author: ApheliosLu
# 2026-06-21 14:37:04
# https://github.com/ApheliosLu

# 异常抛出


def input_password():
    # 1.提示用户输入密码
    pwd = input("请输入密码：")
    # 2.判断密码长度>=8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    raise Exception(
        "密码长度必须大于等于8位啊啊啊啊啊！！！！！"
    )  # 主动raise异常，本质是创建了一个Exception类的对象；传递给e


def use_exception_throwing():
    try:
        print(input_password())
    except Exception as e:
        print(e)


def use_assert_exception():
    try:
        assert 1 == 0, "你的程序在这里发生了什么xxx异常"
        # 等价于：
        # if not (1 == 0):
        #     raise AssertionError("你的程序在这里发生了什么xxx异常")
    except Exception as e:
        print(e)


def check_palindrome():
    my_exception = Exception("非回文数!")

    while True:
        try:
            s = int(input("请输入一个数："))
        except ValueError:
            print("非整型数！")
        else:
            try:
                if str(s) != str(s)[::-1]:
                    raise my_exception  # 抛出异常
                print("该数是一个回文数！")
            except Exception as e:
                print(e)


if __name__ == "__main__":
    # input_password()
    # use_exception_throwing()
    # use_assert_exception()
    check_palindrome()
