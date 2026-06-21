# Author: ApheliosLu
# 2026-06-19 16:11:54
# https://github.com/ApheliosLu

# 异常捕获

import sys
import traceback
import test_exception_module


def use_exception():
    """完整的异常捕获代码"""
    try:
        num = int(input("请输入一个整数：").strip())
        result = 8 // num
        print(f"8 // {num} = {result:.2f}")
    except ValueError:
        print("请输入正确的数字！")
    except ZeroDivisionError:
        print("division by zero")
    except Exception as e:  # e代表异常对象的别名
        print(f"未知错误:{e}")
    else:
        print("正常执行！")
    finally:
        print(f"执行完成，但不保证正确！")  # finally不受return影响，无论如何都会执行


def use_exception_file_line():
    """捕获异常发生时的文件（模块）和具体行数"""
    try:
        test_exception_module.test()
    except Exception as e:
        print(e)
        # 获取完整的traceback信息
        tb_info = traceback.extract_tb(e.__traceback__)[
            -1
        ]  # -1取最后一层（真正出错的地方）也即异常定义处；改成0则是取异常调用处
        file_name = tb_info.filename
        lineno = tb_info.lineno
        print(f"异常发生的文件（模块）：{file_name}")
        print(f"异常发生的具体行数：{lineno}")


def use_exception_traceback_detail():
    try:
        test_exception_module.test()
    except Exception as e:
        # 打印异常信息
        print(f"异常信息：{e}")

        # 1. 提取最后一层回溯
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tb_last = exc_traceback
        while tb_last.tb_next:  # 循环到最内层调用
            tb_last = tb_last.tb_next

        # 2. 获取异常位置信息
        filename = tb_last.tb_frame.f_code.co_filename
        lineno = tb_last.tb_lineno
        func_name = tb_last.tb_frame.f_code.co_name

        print(f"异常发生的文件: {filename}")
        print(f"异常发生的行号: {lineno}")
        print(f"异常发生的函数: {func_name}")

        # 3. 读取并打印异常行代码
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"发生异常的代码: {lines[lineno - 1].strip()}")


def is_palindrome(number):
    """判断一个整数是否是回文数"""
    return (
        str(number) == str(number)[::-1]
    )  # 将数字转为字符串，检查是否与其反转后的字符串相同


def check_palindrome():
    """捕获输入并判断是否为回文数"""
    try:
        user_input = input("请输入一个整数:")
        number = int(user_input)  # 如果输入不是数字，抛出ValueError异常
        if is_palindrome(number):
            print(f"{number}是回文数。")
        else:
            print(f"{number}不是回文数。")
    except ValueError:
        print(f"输入无效，请输入一个数字！")


if __name__ == "__main__":
    # use_exception()
    # use_exception_file_line()
    use_exception_traceback_detail()
    # check_palindrome()
