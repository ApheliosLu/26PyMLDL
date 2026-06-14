# Author: ApheliosLu
# 2026-06-10 10:02:34
# https://github.com/ApheliosLu


import platform
import subprocess

# card_tools.py保存名片管理系统的所有功能函数

# 保存名片数据的结构 全局变量 列表套字典
gl_card_list = []


def clear_screen():
    """
    清屏函数，兼容 Windows/macOS/Linux
    :return:
    """
    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"], shell=True)


def show_menu():
    """
    显示菜单
    :return:
    """
    print("*" * 50)
    print("欢迎使用【菜单管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """
    新建名片
    :return:
    """
    print("-" * 50)
    print("功能：新建名片")

    # 1.提示用户输入名片信息
    name = input(f"请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入qq号码：")
    email = input("请输入邮箱：")

    # 2.将用户信息保存到一个字典
    card_dict = {"name": name, "phone": phone, "qq": qq, "email": email}

    # 3.将用户信息字典添加到名片列表
    gl_card_list.append(card_dict)
    print(gl_card_list)

    # 4.提示添加成功信息，用input读取用户输入避免立刻清屏
    input(f"成功添加{card_dict['name']}的名片！按任意键返回菜单！")


def show_all():
    """
    显示全部名片
    :return:
    """
    print("-" * 50)
    print("功能：显示全部名片")

    # 判断是否有名片记录
    if len(gl_card_list) == 0:
        input(f"提示：没有任何名片记录,按任意键返回菜单！")
        return

    # 打印表头
    for category in ["姓名", "电话", "QQ", "邮箱"]:
        print(category, end="\t\t")
    print()

    # 输出名片列表
    print("=" * 50)
    for card_dict in gl_card_list:
        print(
            f"{card_dict['name']}\t\t{card_dict['phone']}\t\t{card_dict['qq']}\t\t{card_dict['email']}"
        )
    input("按任意键继续！")


def seach_card():
    """
    搜索名片
    :return:
    """
    print("-" * 50)
    print("功能：搜索名片")

    # 1.提示要搜索的姓名
    find_name = input(f"请输入要搜索的姓名：")

    # 2.遍历名片列表
    for card_dict in gl_card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-" * 40)
            print(
                f"{card_dict['name']}\t\t{card_dict['phone']}\t\t{card_dict['qq']}\t\t{card_dict['email']}"
            )
            print("-" * 40)
            # TODO(ApheliosLu): 针对找到的字典进行后续操作：修改/删除
            deal_card(card_dict)
            break
    else:
        input(f"没有找到{find_name}的名片，按任意键返回！")


def deal_card(find_dict):
    """
    操作搜索到的名片字典
    :param find_dict: 找到的名片字典
    :return: None
    """
    print(find_dict)
    action_str = input(f"请选择要执行的操作：\n[1] 修改\n[2] 删除\n[0] 返回上级菜单\n")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入邮件：")
        input(f"{find_dict['name']}的名片修改成功！按任意键后继续！")
    elif action_str == "2":
        gl_card_list.remove(find_dict)
        input("删除成功！按任意键后继续！")


def input_card_info(dict_value, tip_message):
    """
    对系统的input函数进行拓展
    :param dict_value: 字典原有值
    :param tip_message: 输入提示信息
    :return: 如果输入则返回输入内容，否则返回字典原有值
    """

    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value
