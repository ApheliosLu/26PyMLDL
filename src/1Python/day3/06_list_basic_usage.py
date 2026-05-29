# Author: ApheliosLu
# 2026-05-28 10:14:58
# https://github.com/ApheliosLu

import keyword

# keywordlist长度
print(len(keyword.kwlist))

# 列表生成式
a = [x for x in range(10)]
print(a)
print(len(a))

# 切片
c = "123456789"
print(c[::-2])  # 97531

# 列表常用操作
# 列表初始化
name_list = ["zhangsan", "lisi", "wangwu"]
my_list = ["1", "2", "3", "4", "5"]
print(my_list)
print([int(x) for x in my_list])  # 将列表中的元素转为int，注意：字符串"a"无法转为int
print(ord("a"))
print(chr(97))

# 1 取值和取索引
print(name_list[0])
print(
    name_list.index("zhangsan")
)  # 使用 index 方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_list.count("zhangsan"))

# 2 修改
name_list[1] = "李四"
print(name_list)
print(name_list.sort(reverse=True))  # 无法排序 None

# 3 添加
name_list.append("王五")
print(name_list)
name_list.insert(1, "王小美")
print(name_list)
temp_list = ["孙悟空", "猪八戒", "沙和尚"]
name_list.extend(temp_list)
print(name_list)

# 4 删除
name_list.remove("wangwu")
print(name_list)
name_list.pop()
print(name_list)
name_list.pop(3)
print(name_list)
del name_list[0]
print(name_list)
# del name_list
# print(name_list)    # del 之后 name 'name_list' is not defined.
name_list.clear()
print(name_list)
name_list.append("aphelios")
print(name_list)

# 5 数据统计
for i in range(3):
    name_list.append("alune")
print(name_list)
print(f"name_list的元素个数为：{len(name_list)}")
print(f"name_list中alune出现了{name_list.count('alune')}次")
name_list = [item for item in name_list if item != "alune"]
print(name_list)

# 6 列表排序
name_list1 = ["zhangsan", "lisi", "wangwu"]
name_list.extend(name_list1)
print(name_list)
name_list.sort()  # 升序
print(name_list)
name_list.sort(reverse=True)  # 降序
print(name_list)
name_list.reverse()  # 逆序（翻转）
print(name_list)
name_list.sort(key=len, reverse=True)  # 按照长度降序排序
print(name_list)

# 7 列表遍历
for name in name_list:
    print(f"我的名字叫 {name}!")
# 如果删除或修改元素，better use while rather than for
print("-" * 50 + "分割线" + "-" * 50)
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

# 8 列表简写
a = [1, 2, 3, 4, 5]
b = a[1:4]  # 切片 左闭右开
print(f"a = {a},id(a) = {id(a)}")
print(b)
print(a * 2)  # * 重复
a += b  # + 链接，等价于a.extend(b)，不会改变地址
# a = a + b  # 赋值运算效果等价于上一行，但会改变地址
print(f"链接后，a = {a},id(a) = {id(a)}")
print(a[2:6:2])
