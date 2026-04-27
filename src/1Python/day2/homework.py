# Author: ApheliosLu
# 2026-04-07 15:07:47
# Leon12097@163.com
# https://github.com/ApheliosLu


def homework1():
    """
    实现1到100的奇数求和
    :return:
    """
    print(sum([x for x in range(101) if x % 2 != 0]))
    print(sum(range(1, 101, 2)))  # range是一个范围对象


def homework2():
    """
    九九乘法表
    :return:
    """
    for i in range(1, 10):  # 行
        for j in range(1, i + 1):  # 列
            print(
                f"{j}*{i}={j*i:2}",
                end=" ",  # :2表示占两格、右对齐 左对齐则是:<2  end表示以空格结束
            )
        print()  # 换行


def homework3():
    """
    统计一个整数的二进制中1的个数
    :return:
    """
    s = int(input("请输入一个整数:"))
    if s >= 0:
        num = bin(s).count("1")
    else:
        num = 64 - bin(~s).count("1")
        # Python 里 ~x 等于 -x - 1
        # 负数在计算机里是 64 位补码
    print(num)


def homework3_2():
    """
    位运算实现统计一个整数的二进制中1的个数，
    64位是为了做题做的限制
    :return:
    """
    s = int(input("请输入一个整数："))
    check_bit_flag = 1
    count = 0  # 统计数目
    while check_bit_flag < 2**64:
        if check_bit_flag & s:
            count += 1
        check_bit_flag <<= 1
    print(f"原整数{s}的二进制中1的个数为：{count}")


if __name__ == "__main__":
    # homework1()
    homework2()
    # homework3()
    # homework3_2()
