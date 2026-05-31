# Author: ApheliosLu
# 2026-05-31 14:41:12
# https://github.com/ApheliosLu


def test(name, age: object = 6):
    print(name, age)


test(
    "xiaoming", "han"
)  # 提示：应为类型 'int'，但实际为 'str' 但可以运行;给age添加类型提示object（任意类型）以消除提示


def print_info(
    name, title="", gender=True
):  # name为positional参数，title、gender为缺省参数（或keyword参数）
    """
    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"  # 默认True是男生
    if not gender:
        gender_text = "女生"
    print("%s%s 是 %s" % (title, name, gender_text))
    print(f"{title}{name} 是 {gender_text}")


# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
print_info("老王", title="班长")
print_info("小美", gender=False)
print("-" * 50)
print_info("小美", gender=False, title="学习委员")


test_list = [x for x in range(10)]
test_list.sort(reverse=True)  # sort方法本身没有返回值，原地排序in-place
print(test_list)

test_list1 = sorted([x for x in range(10)], reverse=True)  # sorted会返回新列表
print(test_list1)
