# Author: ApheliosLu
# 2026-06-10 10:02:04
# https://github.com/ApheliosLu


import card_tools

while True:
    card_tools.clear_screen()  # 清屏

    # TODO(ApheliosLu): 显示系统菜单
    card_tools.show_menu()

    action = input(f"请选择菜单功能：")
    print(f"您选择的操作是:{str(action)}")
    # 根据用户输入决定后续的此操作
    if action in ["1", "2", "3"]:
        if action == "1":
            card_tools.new_card()
        elif action == "2":
            card_tools.show_all()
        elif action == "3":
            card_tools.seach_card()
    elif action == "0":
        print(f"欢迎再次使用【名片管理系统】！")
        break
    else:
        print(f"输入有误，请重新输入！")
        input(f"按任意键返回菜单！")
