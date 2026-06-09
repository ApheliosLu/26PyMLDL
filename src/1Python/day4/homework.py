# Author: ApheliosLu
# 2026-05-31 14:41:21
# https://github.com/ApheliosLu

import copy
import typing


# 2、求两个有序数字列表的公共元素
def find_common_elements(list_a, list_b):
    # & 运算符不能直接用于列表，转化为集合并求交集
    return list(set(list_a) & set(list_b))


list1 = [1, 3, 4, 5, 6]
list2 = [2, 3, 5, 7]
result = find_common_elements(list1, list2)
print(result)
print("-----第2道题-----")


# 3、给定一个n个整型元素的列表a，其中有一个元素出现次数超过n / 2，求这个元素
def majority_element(list_3):  # 参照了摩尔投票算法原理
    # 投票阶段
    candidate = None
    count = 0

    for num in list_3:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1  # 三元表达式

    # 验证阶段
    count = list_3.count(candidate)
    if count > len(list_3) // 2:
        return candidate
    else:
        return None  # 如果没有元素出现超过n/2次，返回None


a = [3, 3, 4, 2, 4, 4, 2, 4, 4]
result = majority_element(a)
print(result)
print("-----第3道题-----")

# 4、列表、元组，字典的相同点，不同点有哪些，请罗列
"""
相同点： 
1.支持迭代，使用for来遍历其中元素 2.支持成员操作，使用in判断元素是否在其中 
3.支持索引访问，列表和元组支持下标索引，字典支持按键索引 4.都可以存储不同类型的元素包括整型和字符串等
不同点：
1.列表和字典可变，元组不可变 2.列表和元组元素可重复，字典键不可重复
3.元组不支持插入删除，属于不可变类型长度不可变
"""
print("-----第4道题-----")

# 5、将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表。
tuple_data = (1, 2, 3)
set_data = {4, 5, 6}

merged_list = list(tuple_data) + list(set_data)  # 使用加法运算符合并

print(merged_list)
print(type(merged_list))  # <class 'list'>
print("-----第5道题-----")

# 6、在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 0和 7。
my_list = [1, 2, 3, 4, 5, 6]

my_list.insert(0, 0)

my_list.append(7)

print(my_list)
print("-----第6道题-----")

# 7、反转列表 [0,1,2,3,4,5,6,7] 。
list_7 = [0, 1, 2, 3, 4, 5, 6, 7]
list_7_1 = list_7[::-1]
print(list_7_1)
print("-----第7道题-----")

# 8、反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号。
list_8 = [0, 1, 2, 3, 4, 5, 6, 7]
list_8_1 = list_8[::-1]
print(list_8_1)
print(list_8_1.index(5))
print("-----第8道题-----")

# 9、分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
list_9 = [True, False, 0, 1, 2]
print(list_9.count(True))
print(list_9.count(False))
print(list_9.count(0))
print(list_9.count(1))
print(list_9.count(2))  # 结果 2 2 2 2 1 ，即True等价于1、False等价于0
print("-----第9道题-----")

# 10、从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。
list_10 = [True, 1, 0, "x", None, "x", False, 2, True]
list_10 = [item for item in list_10 if item != "x"]
# 或者 while 'x' in list_10:      list_10.remove('x')
print(list_10)
print("-----第10道题-----")

# 11、从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素。
list_11 = [True, 1, 0, "x", None, "x", False, 2, True]
list_11.pop(4)
print(list_11)
print("-----第11道题-----")

# 12、删除列表中索引号为奇数（或偶数）的元素。
list_12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_even_index = list_12[::2]  # 删除奇数
print(list_even_index)
list_odd_index = list_12[1::2]
print(list_odd_index)
print("-----第12道题-----")

# 13、清空列表中的所有元素。
list_13 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_13.clear()
print(list_13)
print("-----第13道题-----")

# 14、对列表 [3,0,8,5,7] 分别做升序和降序排列。    # sort方法返回值是none
list_14 = [3, 0, 8, 5, 7]
list_14.sort()
print(list_14)
list_14.sort(reverse=True)
print(list_14)
print("-----第14道题-----")

# 15、将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0。
list_15 = [3, 0, 8, 5, 7]  # 必须用索引来修改
for index, value in enumerate(
    list_15
):  # enumerate() 函数返回每个元素的索引和值，这样就可以直接根据 index 修改 list_15 中对应位置的元素。
    if value > 5:
        list_15[index] = 1
    else:
        list_15[index] = 0
# list_15 = [1 if x > 5 else 0 for x in list_15]
print(list_15)
print("-----第15道题-----")

# 16、遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号。
list_16 = ["x", "y", "z"]
for index, value in enumerate(list_16):
    print(f"索引{index},元素{value}")
print("-----第16道题-----")

# 17、将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表。
original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_list = [x for x in original_list if x % 2 == 0]  # 偶数
odd_list = [x for x in original_list if x % 2 != 0]  # 奇数

print("偶数组:", even_list)
print("奇数组:", odd_list)
print("-----第17道题-----")

# 18、分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序。相当于按6,3,2进行排序，除非第一个元素相等，按第二个元素排序。
matrix = [[6, 5], [3, 7], [2, 8]]

# 使用 sorted() 和自定义的排序键
sorted_matrix = sorted(matrix, key=lambda x: (x[0], x[1]))
# lambda x: (x[0], x[1]) 是一个排序键，表示先按每个子列表的第一个元素（x[0]）排序，如果第一个元素相等，再按第二个元素（x[1]）排序。

print(sorted_matrix)
print("-----第18道题-----")

# 19、从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素。
list_19: list[typing.Union[int | str]] = [1, 4, 7, 2, 5, 8]
list_19[3:3] = ["x", "y", "z"]
print(list_19)
print("-----第19道题-----")

# 20、快速生成由 [5,50) 区间内的整数组成的列表。
list_20 = [x for x in range(5, 50)]
print(list_20)
print("-----第20道题-----")

# 21、若 a = [1,2,3]，令 b = a，执行 b[0] = 9， a[0]亦被改变。为何？如何避免？----讲了深COPY和浅COPY再做
a_21 = [1, 2, 3]
# b_21 = a_21  # 执行 b = a 时，b 和 a 其实指向了同一个内存中的列表对象。修改b的值会影响a的值
b_21 = copy.copy(a_21)  # 浅拷贝，修改b的值不会影响a的值
b_21[0] = 9
print(b_21)
print(a_21)
print("-----第21道题-----")

# 22、将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式。
list_22_1 = ["x", "y", "z"]
lis_22_2 = [1, 2, 3]
list_22_3 = list(zip(list_22_1, lis_22_2))  # zip() 返回的是一个迭代器，而不是一个列表
print(list_22_3)
print("-----第22道题-----")

# 23、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键。
dict_23 = {"Alice": 20, "Beth": 18, "Cecil": 21}
print(dict_23)
print(list(dict_23.keys()))
print("-----第23道题-----")

# 24、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值。
print(list(dict_23.values()))
print("-----第24道题-----")

# 25、以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组。
print(list(dict_23.items()))
print("-----第25道题-----")

# 26、向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17。
dict_23["David"] = 19
dict_23["Cecil"] = 17
print(dict_23)
print("-----第26道题-----")

# 27、删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典。
dict_23.pop("Beth")
print(dict_23)
dict_23.clear()
print(dict_23)
print("-----第27道题-----")

# 28、判断 David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中。
dict_28 = {"Alice": 20, "Beth": 18, "Cecil": 21}
print("David" in dict_28)
print("Alice" in dict_28)
print("-----第28道题-----")

# 29、遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对。
for key in dict_28:
    # print("%s - %s" % (key, dict_28[key]))
    print(f"key:{key} value:{dict_28[key]}")
print("-----第29道题-----")

# 30、若 a = dict()，令 b = a，执行 b.update({‘x’:1})， a亦被改变。为何？如何避免？----讲了深COPY和浅COPY再做
a_30 = {"Alice": 20, "Beth": 18, "Cecil": 21}
# b_30 = a_30
b_30 = copy.copy(a_30)
b_30.update({"Alice": 19})
print(b_30)
print(a_30)
print("-----第30道题-----")

# 31、以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典。
letters_31 = ["A", "B", "C", "D", "E", "F", "G", "H"]

# 字典推导式，遍历列表 letters 中的每个元素，将每个元素作为字典的键，并将每个键的值设置为 0。
dict_31 = {letter: 0 for letter in letters_31}

print(dict_31)
print("-----第31道题-----")

# 32、将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典。
list_32: list[list] = [["a", 1], ["b", 2]]
tuple_32 = (("x", 3), ("y", 4))

dict_32_1 = dict(list_32)
print(dict_32_1)
dict_32_2 = dict(tuple_32)
print(dict_32_2)

dict_32_3 = {}
dict_32_3.update(dict_32_1)
dict_32_3.update(dict_32_2)
print(dict_32_3)
print("-----第32道题-----")

# 33、将元组 (1,2) 和 (3,4) 合并成一个元组。
tuple_33_1 = (1, 2)
tuple_33_2 = (3, 4)
tuple_33_3 = tuple_33_1 + tuple_33_2
print(tuple_33_3)
print("-----第33道题-----")

# 34、将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z。
tuple_34 = (1, 2, 3)
x, y, z = tuple_34
print("x=%d   y=%d   z=%d    " % (x, y, z))
print(f"x = {x}, y = {y}, z = {z}")
print("-----第34道题-----")

# 35、返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号。
tuple_35 = ("Alice", "Beth", "Cecil")
print(tuple_35.index("Cecil"))
print("-----第35道题-----")

# 36、返回元组 (2,5,3,2,4) 中元素 2 的个数。
tuple_36 = (2, 5, 3, 2, 4)
print(tuple_36.count(2))
print("-----第36道题-----")

# 37、判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中。
print("Cecil" in tuple_35)
print("-----第37道题-----")

# 38、返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组。
tuple_37 = (2, 5, 3, 7)
tuple_37_1 = tuple_37[:2] + (9,) + tuple_37[2:]  # (9,)
print(tuple_37_1)
print("-----第38道题-----")

# 39、创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素。
set_39 = set()
set_39.update(["x", "y", "z"])  # update方法一次添加多个元素（一个列表）
print(set_39)
print("-----第39道题-----")

# 40、删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增加元素 ‘w’，然后清空整个集合。
set_39.discard("z")
print(set_39)
set_39.add("w")
print(set_39)
set_39.clear()
print(set_39)
print("-----第40道题-----")

# 41、返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）。
set_41a = {"A", "D", "B"}
set_41b = {"D", "E", "C"}

set_41c = set_41a.difference(set_41b)
print(set_41c)
print("-----第41道题-----")

# 42、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集。
set_41d = set_41a.union(set_41b)
print(set_41d)
print("-----第42道题-----")

# 43、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集。
set_41e = set_41a.intersection(set_41b)
print(set_41e)
print("-----第43道题-----")

# 44、返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合。
set_41f = set_41a.symmetric_difference(set_41b)
print(set_41f)
print("-----第44道题-----")

# 45、判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素。
set45_a = {"A", "D", "B"}
set45_b = {"D", "E", "C"}

# 使用 & 运算符
intersection = set45_a & set45_b

# 如果交集非空，则说明有重复元素
if intersection:
    print(f"有重复元素: {intersection}")
else:
    print("没有重复元素")
print("-----第44道题-----")

# 46、判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集。
set_46a = {"A", "C"}
set_46b = {"D", "C", "E", "A"}
print(set_46a.issubset(set_46b))
print("-----第46道题-----")

# 47、去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素。
arr = [1, 2, 5, 2, 3, 4, 5, "x", 4, "x"]
seen = set()
unique_elements = []
for item in arr:
    if item not in seen:
        unique_elements.append(item)  # 保持原序
        seen.add(item)

print(unique_elements)
print("-----第47道题-----")

# 48、返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大下写互换形式。
s = "abCdEfg"

# 全部大写
upper_case = s.upper()

# 全部小写
lower_case = s.lower()

# 大小写互换
swap_case = s.swapcase()

# 输出结果
print("全部大写:", upper_case)
print(f"全部大写：{upper_case}")
print("全部小写:", lower_case)
print("大小写互换:", swap_case)
print("-----第48道题-----")

# 49、判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写。
str_49 = "abCdEfg"
print(str_49.istitle())
print(str_49.islower())
print(str_49.isupper())
print("-----第49道题-----")

# 50、返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式。
str_50 = "this is python"
print(str_50.capitalize())
print(str_50.title())
print("-----第50道题-----")

# 51、判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾。
print(str_50.startswith("this"))
print(str_50.endswith("python"))
print("-----第51道题-----")

# 52、返回字符串 ‘this is python’ 中 ‘is’ 的出现次数。
print(f"is出现的次数：{str_50.count('is')}")  # 2

# 将字符串按空格分割成单词
words = str_50.split()
print(type(words))  # <class 'list'>
# 计算 'is' 作为独立单词出现的次数
count_is = words.count("is")
print(f"'is' 作为独立单词出现的次数：{count_is}")  # 1

print("-----第52道题-----")
# 53、返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置。
first_index = str_50.index("is")
last_index = str_50.rindex("is")

print(f"首次出现 'is' 的位置: {first_index}")
print(f"最后一次出现 'is' 的位置: {last_index}")
print("-----第53道题-----")

# 54、将字符串 ‘this is python’ 切片成3个单词。
list_54 = str_50.split()
print(list_54)
print("-----第54道题-----")

# 55、返回字符串 ‘blog.csdn.net/xufive/article/details/102946961’ 按路径分隔符切片的结果。
str_55 = "blog.csdn.net/xufive/article/details/102946961"
list_55 = str_55.split("/")
print(list_55)
print("-----第55道题-----")

# 56、将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整形。
str_56 = "2.72, 5, 7, 3.14"
list_56 = str_56.split(",")
print(list_56)

# 将每个元素转换为浮点数或整数
converted_elements = [float(x) if "." in x else int(x) for x in list_56]

print(converted_elements)
print("-----第56道题-----")
# 57、判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母？
str57 = "adS12K56"
print(str57.isalnum())
print(str57.isalpha())
print(str57.isdecimal())
print("-----第57道题-----")

# 58、将字符串 ‘there is python’ 中的 ‘is’ 替换为 ‘are’。
print("there is python".replace("is", "are"))
print("-----第58道题-----")

# 59、清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符。
print("\t python \n".lstrip())
print("\t python \n".rstrip())
print("\t python \n".strip())
print("-----第59道题-----")

# 60、将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果。
str60 = ["ok", "hello", "thank you"]
# len60 = len(str60[2])
len60 = max(len(x) for x in str60)
print("左对齐")
for i in str60:
    print(i.ljust(len60))
print("*" * 10)

print("右对齐")
for i in str60:
    print(i.rjust(len60))
print("*" * 10)

print("居中对齐")
for i in str60:
    print(i.center(len60))
print("*" * 10)
print("-----第60道题-----")

# 61、将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度。
str61 = ["15", "127", "65535"]
len61 = max([len(x) for x in str61])
for x in str61:
    print(x.rjust(len61, "0"))
print("-----第61道题-----")

# 62、将列表 [‘a’,‘b’,‘c’] 中各个元素用’|'连接成一个字符串。
str62 = ["a", "b", "c"]
str62_1 = "|".join(str62)
print(str62_1)
print("|".join(str62))
print(type("|".join(str62)))
print("-----第62道题-----")

# 63、将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串。
str63 = "abc"
print(",".join(str63))
print("-----第63道题-----")

# 64、从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串。
# phone = input("输入手机号:")
# print("Mobile：" + phone)
print("-----第64道题-----")

# 65、从键盘输入年月日时分秒，输出形如 ‘2019-05-01 12:00:00’ 的字符串。
# 2019-05-01 12:00:00
# dt = input("年 月 日 时 分 秒").split()
# print("-".join(dt[:3]) + " " + ":".join(dt[3:]))
print("-----第65道题-----")

# 66、给定两个浮点数 3.1415926 和 2.7182818，格式化输出字符串 ‘pi = 3.1416, e = 2.7183’。
a66 = 3.1415926
b66 = 2.7182818
print("pi:{:.4f} e:{:.4f}".format(a66, b66))
print(f"pi:{a66:.4f} e:{b66:.4f}")
print("-----第66道题-----")

# 67、将 0.00774592 和 356800000 格式化输出为科学计数法字符串。
a67 = 0.00774592
b67 = 356800000
print("{:e} {:e}".format(a67, b67))
print(f"{a67:e} {b67:e}")
print("-----第67道题-----")

# 68、将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型。
a68 = [0, 1, 2, 3.14, "x", None, "", list(), {5}]
a68 = [bool(x) for x in a68]
print(a68)
print("-----第68道题-----")

# 69、返回字符 ‘a’ 和 ‘A’ 的ASCII编码值。
print(ord("a"))
print(ord("A"))
print("-----第69道题-----")

# 70、返回ASCII编码值为 57 和 122 的字符。
a70 = [57, 122]
# a70 = [x for x in range(57, 123)]
for i in a70:
    # print("{}在ASCII码表对应的字符为{}".format(i, chr(i)))
    print(f"{i}在ASCII码表中对应的字符为{chr(i)}")
print("-----第70道题-----")

# 71、将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0。
list71 = [3, "a", 5.2, 4, {}, 9, []]
modified_list = [1 if isinstance(x, (int, float)) and x > 3 else 0 for x in list71]
print(modified_list)
print("-----第71道题-----")

# 72、将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表。
a72 = [[1], ["a", "b"], [2.3, 4.5, 6.7]]
a72 = [j for x in a72 for j in x]  # 先看前for 再看后for
print(a72)
print("-----第72道题-----")

# 73、将等长的键列表和值列表转为字典。
a = "A B C D E".split()
b = range(len(a))
dic = dict(zip(a, b))
print(dic)
print("-----第73道题-----")

# 74、数字列表求和。
s = list(range(10))
print(sum(s))
print("-----第74道题-----")
