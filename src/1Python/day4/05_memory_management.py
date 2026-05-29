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
