# Author: ApheliosLu
# 2026-05-28 20:38:59
# https://github.com/ApheliosLu

# 列表生成式
# 用法1、[元素表达式 if(条件) else for 变量 in 迭代对象 ]，如[x if x % 2 == 0 else x ** 2 for x in range(10)]
# 用法2、[变量 for 变量 in 迭代对象 if（判断）]，如[item for item in name_list if item != "alune"]

# 基础列表生成式
nums = [x**2 for x in range(5)]
print(nums)  # [0, 1, 4, 9, 16]

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
