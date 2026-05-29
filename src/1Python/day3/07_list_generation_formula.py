# Author: ApheliosLu
# 2026-05-28 20:38:59
# https://github.com/ApheliosLu

# 列表生成式
# 用法1、[变量 for 变量 in 迭代对象 if（判断）]，如[item for item in name_list if item != "alune"]
# 用法2、[元素表达式 if(条件) else for 变量 in 迭代对象 ]，如[x if x % 2 == 0 else x ** 2 for x in range(10)]

# 基础列表生成式
nums = [x**2 for x in range(5)]
print(nums)  # [0, 1, 4, 9, 16]

# 使用列表生成式与不适用对比
a = [x for x in range(10)]
print(a)
b = []
for i in range(10):
    b.append(i)
print(b)

# 2个for循环 先看前，再看后
a = [j for i in range(10) for j in range(i)]
print(f"2个for循环生成的a = {a}")

# 二维列表 先看后，再看前
a = [[col * row for col in range(5)] for row in range(5)]
print(f"二维列表a = {a}")
# 二维转一维
b = [j for x in a for j in x]
print(f"二维转一维：b = {b}")

# 使用if
c = [x for x in range(10) if x % 2 == 0]
print(c)
# 使用if else
d = [x if x % 2 == 0 else x**2 for x in range(10)]
print(f"偶数不变奇数取幂，d = {d}")

# 字典生成式
d = {k: k * 2 for k in range(3)}
print(d)  # {0: 0, 1: 2, 2: 4}

# 集合生成式
s = {x % 2 for x in range(5)}
print(s)  # {0, 1}

# 元组不能直接生成，写出来的是生成器，再用tuple()转成元组
gen = (x**2 for x in range(5))
print(gen)  # <generator object <genexpr> at 0x000001B7D7828E10>
t = tuple(gen)
print(t)  # (0, 1, 4, 9, 16)

# 字符串没有专门的生成式，用join+列表生成式
s = "".join([str(x) for x in range(3)])
print(s)  # 012
print(type(s))  # <class 'str'>

# lambda表达式：匿名、一次性函数
add = lambda a, b: a + b
print(add(1, 2))
list_tuple = [(1, 3), (2, 1)]
list_tuple.sort(key=lambda x: x[1])
print(list_tuple)
print(list(map(lambda x: x * 2, list_tuple)))  # [(2, 1, 2, 1), (1, 3, 1, 3)] * 重复
print(list(map(lambda x: (x[0] * 2, x[1] * 2), list_tuple)))  # [(4, 2), (2, 6)]
