# Author: ApheliosLu
# 2026-07-04 20:48:32
# https://github.com/ApheliosLu


def binary_search(nums: list[int], target: int) -> int:
    """
    二分查找，返回目标值下标，不存在返回 -1
    :param nums: 升序有序数组
    :param target: 要查找的数字
    :return: 找到返回索引，没找到返回 -1
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        # 等价于 (left + right) // 2，防止大数溢出
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # 目标在右区间，左边界右移
            left = mid + 1
        else:
            # 目标在左区间，右边界左移
            right = mid - 1
    # 循环结束仍未找到
    return -1


# 测试示例
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(binary_search(arr, 7))  # 输出 3
    print(binary_search(arr, 4))  # 输出 -1
