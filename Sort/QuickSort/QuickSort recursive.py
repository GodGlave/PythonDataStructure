"""
一、介绍
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
二、步骤
    递归实现
"""


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = array[start]  # 基准值
    low = start  # 左指针
    high = end  # 右指针
    while low < high:
        while low < high and array[high] >= pivot:
            high -= 1
        array[low] = array[high]

        while low < high and array[low] < pivot:
            low += 1
        array[high] = array[low]
    array[low] = pivot
    quick_sort(array, start, low - 1)
    quick_sort(array, low + 1, end)


if __name__ == '__main__':
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(array, 0, len(array) - 1)
    print(array)