# Author: ApheliosLu
# 2026-07-04 20:51:48
# https://github.com/ApheliosLu


def insertion_sort(nums: list[int]) -> list[int]:
    arr = nums.copy()
    n = len(arr)
    # 从第2个元素开始（下标1，第一个元素默认有序）
    for i in range(1, n):
        current = arr[i]  # 当前待插入元素
        j = i - 1
        # 向前遍历有序区，比current大的元素后移
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        # 空位放入当前元素
        arr[j + 1] = current
    return arr


# 测试
if __name__ == "__main__":
    test = [5, 2, 9, 3, 1, 7, 4]
    print(insertion_sort(test))  # [1, 2, 3, 4, 5, 7, 9]
