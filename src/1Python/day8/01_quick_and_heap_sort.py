# Author: ApheliosLu
# 2026-07-04 11:47:28
# https://github.com/ApheliosLu

import random
import time
import sys

sys.setrecursionlimit(1 << 25)


class Sort:
    def __init__(self, n):
        """
        :param n: 排序的数的数量
        """
        self.size = n
        self.arr = [0] * n  # 初始化长度为n的列表
        self.random_data()

    def random_data(self):
        for i in range(self.size):
            self.arr[i] = random.randint(0, 99)  # 随机列表元素

    def reset_random(self):
        """重置随机数组，用于多次独立测试"""
        self.random_data()

    def partition(self, left, right):
        arr = self.arr
        # 随机基准交换到左端点,坑位天然在left（挖坑法）
        random_pos = random.randint(left, right)
        arr[left], arr[random_pos] = arr[random_pos], arr[left]
        pivot = arr[left]  # 暂存pivot值

        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        return left  # pivot最终坐标

    def quick_sort(self, left, right):  # logn层递归，每一层工作量O(n)
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_max_heap(self, pos, arr_len):
        arr = self.arr
        dad = pos
        son = 2 * dad + 1  # 通过dad计算son位置
        while son < arr_len:
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 右孩子存在且大于左孩子
                son += 1
            if arr[son] > arr[dad]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son  # 继续往下调整
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):  # 建堆O(n)，调整堆O(logn)
        arr = self.arr
        # 1.构建完整大根堆
        for parent in range(self.size // 2 - 1, -1, -1):  # 建堆循环，遍历所有非叶子节点
            self.adjust_max_heap(parent, self.size)  # 每次从parent开始调整
        # 2.逐步取出堆顶最大值放到数组末尾，最终完成排序
        for end in range(
            self.size - 1, 0, -1
        ):  # 当堆只剩 0 号元素时已天然有序，无需再处理 end=0
            arr[0], arr[end] = arr[end], arr[0]
            self.adjust_max_heap(0, end)  # 每次从0开始调整

    def test_use_time(self, sort_func, *args, **kwargs):
        """
        实例方法，测试排序用时，自动备份恢复数组
        sort_func是回调函数
        """
        bak_arr = self.arr.copy()
        start = time.time()
        sort_func(*args, **kwargs)  # 解包可变位置参数；sort_func的真正调用时刻
        end = time.time()
        func_name = sort_func.__name__
        print(f"{self.size}个元素 | {func_name} 耗时：{end - start:.6f} 秒")
        # 恢复原数组，保证多次测试独立
        self.arr = bak_arr


if __name__ == "__main__":
    count = 10
    my_sort = Sort(count)
    print("原始数组：", my_sort.arr)

    # 测试快速排序
    my_sort.test_use_time(my_sort.quick_sort, 0, count - 1)
    my_sort.quick_sort(0, count - 1)
    print("快排结果：", my_sort.arr)

    # 重置随机数组，再测试堆排序
    my_sort.reset_random()
    print("\n重置后数组：", my_sort.arr)
    my_sort.test_use_time(my_sort.heap_sort)
    my_sort.heap_sort()
    print("堆排结果：", my_sort.arr)
