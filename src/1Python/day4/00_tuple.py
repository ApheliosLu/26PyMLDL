# Author: ApheliosLu
# 2026-05-29 17:32:43
# https://github.com/ApheliosLu

# 元组基本使用
info_tuple = ("zhangsan", 18, 1.75, "zhangsan")  # 可重复不可改
print(info_tuple)
print(id(info_tuple))

# 1.取值和取索引
print(info_tuple[0])
print(info_tuple.index("zhangsan"))

# 2.统计计数
print(info_tuple.count("zhangsan"))
print(len(info_tuple))

# 3.迭代遍历元组
for item in info_tuple:
    print(item)

# 4.元组与格式化字符串
info_tuple = ("zhangsan", 18, 1.75)  # id变了
print(id(info_tuple))

print("%s 年龄是 %d 身高是 %.2f米" % info_tuple)  # 格式化字符串后面的()本质为元组
print("%s 年龄是 %d 身高是 %.2f米" % (info_tuple[0], info_tuple[1], info_tuple[2]))
info_str = "%s 年龄是 %d 身高是 %.2f米" % info_tuple  # 解包
print(info_str)
print(f"{info_str}")
print(f"{info_tuple[0]} 年龄是 {info_tuple[1]} 身高是 {info_tuple[2]}米")

# 5.其他
a = ()  # 空元组
print(type(a))
b = (1,)  # 一个元素的元组
print(type(b))
print(list(b))
