# Author: ApheliosLu
# 2026年04月05日12:00:23
# Email:  Leon12097@163.com

print("hello，陈师姐")


def first_func():  # 方法定义前后空两行
    print("啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊")


first_func()  # 1个用法

# 长字符串使用三引号，直接换行写。下面的print会输出5行
print("""
第一行
第二行
第三行
""")

# 多个print默认换行，不想换行的做法如下
print("hello,", end="")
print("world",end=" ")  # 字符串用双引号或者单引号，若用单引号则格式化后自动转为双引号
print("python")

print("")  # 等价于输出一个空行

"""
多行注释用一对三个双引号
print(1)
"""

print(1)
