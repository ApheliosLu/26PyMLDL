# Author: ApheliosLu
# 2026-06-15 16:23:36
# https://github.com/ApheliosLu

# 循环读取，以CR隔断
my_list = []
for i in range(7):
    num = input()
    my_list.append(num)
print(my_list)

# 循环读取，以SPACE隔断
num = input()
your_list = num.split()
print(your_list)
print([int(i) for i in your_list])
