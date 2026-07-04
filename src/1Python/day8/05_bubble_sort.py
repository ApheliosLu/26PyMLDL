# Author: ApheliosLu
# 2026-07-04 20:51:33
# https://github.com/ApheliosLu


def bubble_sort(nums: list[int]) -> list[int]:
    arr = nums.copy()  # 不修改原数组
    n = len(arr)
    # 外层控制排序轮次
    for i in range(n):
        swapped = False  # 优化标记：本轮无交换说明已有序，直接退出
        # 内层每轮比较到未排序边界
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# 测试
if __name__ == "__main__":
    test = [5, 2, 9, 3, 1, 7, 4]
    print(bubble_sort(test))  # [1, 2, 3, 4, 5, 7, 9]
