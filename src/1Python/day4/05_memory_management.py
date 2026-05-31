# Author: ApheliosLu
# 2026-05-29 17:35:39
# https://github.com/ApheliosLu

a = 2
b = 2
print(a is b)  # True 不可变类型id相同

c = "hello"
d = "hello"
print(c is d)  # True

e = []
f = []
print(e is f)  # False 可变类型id不同
print(e == f)  # True

g = 122344566671827398591738
h = 122344566671827398591738
print(g is h)  # True

i = 122344566671827398591738.1
j = 122344566671827398591738.1
print(i is j)  # True

k = (1, 2, 3)
l = (1, 2, 3)
print(k is l)  # True 短元组
