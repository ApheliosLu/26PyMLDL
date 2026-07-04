# Author: ApheliosLu
# 2026-07-04 11:47:28
# https://github.com/ApheliosLu

import random
import time
import sys

sys.setrecursionlimit(10**6)


class Sort:
    def __init__(self, n):
        """
        :param n: 排序的数的数量
        """
        self.len = n  # 排序的列表的长度
        # self.arr = [3, 87, 2, 93, 78, 56, 61, 38, 12, 40]
        self.arr = [0] * n  # 初始化长度为n的列表
        self.random_data()  # 调用方法

    def random_data(self):  # 生成随机列表
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):  # 划分函数，返回分割点的下标值（挖坑法）
        arr = self.arr
        random_pos = random.randint(
            left, right
        )  # 随机选择pivot，避免陷入最坏时间复杂度
        pivot = arr[random_pos]
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        return left  # left即为将列表划分为两半的pivot的位置

    def quick_sort(self, left, right):  # logn层递归，每一层工作量O(n)
        if left < right:
            pivot = self.partition(left, right)  # 获取pivot，用以划分
            self.quick_sort(left, pivot - 1)  # 递归左右划分
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, arr_len):
        """
        把某个子树调整成大根堆
        :param pos: 被调整的元素位置，是父亲
        :param arr_len: 当时列表总长度
        :return:
        """
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < arr_len:  # 左孩子小于列表长度
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 右孩子存在且大于左孩子
                son += 1
            if arr[son] > arr[dad]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):  # 建堆O(n)，调整对O(logn)
        # 1.把列表调整为大根堆
        for parent in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(parent, self.len)
        arr = self.arr
        # 2.堆顶元素与最后一个元素交换
        arr[0], arr[self.len - 1] = arr[self.len - 1], arr[0]
        # 3.把剩余的元素继续调整为大根堆，循环往复直至有序
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, self.len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]

    @staticmethod
    def test_use_time(self, sort_func, *args, **kwargs):
        """
        回调函数，测试排序算法用时
        :param sort_func:
        :param args:
        :param kwargs:
        :return:
        """
        start_time = time.time()
        sort_func(*args, **kwargs)
        end_time = time.time()
        print(f"{self.len}个元素使用{sort_func}排序总计用时：{end_time-start_time}")


if __name__ == "__main__":
    count = 10
    my_sort = Sort(count)  # 生成待排序列表
    print(my_sort.arr)

    # print("快排之后：")
    # my_sort.quick_sort(0, count - 1)
    # print(my_sort.arr)
    # my_sort.test_use_time(my_sort.quick_sort)  # 快排用时
    #
    # my_sort.heap_sort()
    # print(my_sort.arr)
    # my_sort.test_use_time(my_sort.heap_sort)  # 堆排用时
