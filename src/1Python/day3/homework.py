# Author: ApheliosLu
# 2026-05-29 09:42:52
# https://github.com/ApheliosLu

import homework_module as homo
from homework_module import main


# 1.有7个整数，其中有3个数出现了两次，1个数出现了一次，找出出现了一次的那个数。
def find_unique_number(list_numbers):
    tmp = 0
    for number in list_numbers:
        tmp ^= number  # 将每个数与0异或
    return tmp


# 示例数据
test_numbers = [1, 2, 3, 2, 1, 4, 3]  # 这里3个数（1,2,3）各出现2次，4出现1次
unique_number = find_unique_number(test_numbers)
print(f"出现一次的数是：{unique_number}")


# 2.写一个简单的for循环，从1打印到20，横着打为1排
def simple_for():
    for i in range(1, 21):
        print(i, end="  ")
    print()


simple_for()


# 3.写一个say_hello函数打印多次hello并给该函数加备注（具体打印几次依靠传递的参数），
# 然后调用say_hello，同时学会快速查看函数备注，及如何跳转到函数实现快捷操作
def say_hello(times):
    """
    打印‘hello’的函数
    :param times: 指定打印次数
    :return:
    """
    for i in range(times):
        print("hello")


say_hello(3)


# 4.写一个模块（命名不要用中文），模块里写3个打印函数，然后另外一个py文件调用该模块，并调用对应模块的函数，同时用一下下面操作
if __name__ == "__main__":
    homo.print_line("#", 50)
    homo.main()
    homo.random_print(0, 500, 10)


# 5. 有8个整数，其中有3个数出现了两次，2个数出现了一次， 找出出现了一次的那2个数。
def find_two_unique_numbers(list_numbers):
    """
    算法思想：
    1.对所有数进行异或，得到一个结果，该结果是两个出现一次的数的异或值
    2.找到结果中任意一个为1的位，以此位为依据将所有数分为两组并进行再次异或，每组得到一个唯一的数
    :param list_numbers:
    :return:
    """

    # 第一步：对所有数字进行异或
    xor_result = 0
    for number in list_numbers:
        xor_result ^= number

    # 找xor_result中任意一个为1的位，这里找到最低位的1
    diff_bit = 1
    while (xor_result & diff_bit) == 0:
        diff_bit <<= 1  # 这一位不是1，左移
    # 找xor_result最低位的1的另一种方法：一个数和自己相反数按位与会得到最低位的1
    # diff_bit=xor_result&-xor_result

    # 第二步：分组进行异或
    num1, num2 = 0, 0
    list1=[]
    list2=[]
    for number in list_numbers:
        if number & diff_bit:   # 与diff_bit按位与为1，分到第一组
            num1 ^= number
            list1.append(number)
        else:
            num2 ^= number  # 第二组
            list2.append(number)
    print(list1, list2)
    return num1, num2
    # 在 Python 里，用逗号隔开多个值一起 return，就会自动变成元组。
    # 等价于 return (num1,num2)


# 示例数据
two_numbers_list = [1, 5, 1, 2, 4, 4, 5, 3]  # 3 和 2 出现一次
unique_two_numbers = find_two_unique_numbers(two_numbers_list)
print(f"两个出现一次的数为：{unique_two_numbers}")  # 两个出现一次的数为：(3, 2)
print(type(unique_two_numbers))  # <class 'tuple'>
