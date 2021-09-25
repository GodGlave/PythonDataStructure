'''
from timeit import timeit
def test():
    #import random
    #gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
    # array= list(gen)
    array = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
    quick_sort(array, 0, len(array)-1)
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
    print('Quick sort function run 1000 times, cost: ', timeit('test()', 'from __main__ import test', number=1000), 'seconds.')
# Output:
# Quick sort function run 1000 times, cost:  0.0901155 seconds.
'''

'''
from timeit import timeit
def test():
    # import random
    # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
    # L = list(gen)
    L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
    quick_sort(L, 0, len(L)-1)
def quick_sort(L, left, right):
    temp_stack = []
    temp_stack.append((left, right))
    while temp_stack:
        left, right = temp_stack.pop()
        pivot_index = partition(L, left, right)
        if pivot_index - 1 > left:
            temp_stack.append((left, pivot_index-1))
        if pivot_index + 1 < right:
            temp_stack.append((pivot_index+1, right))
def partition(L, first, last):
    smaller_index = first - 1
    pivot_value = L[last]
    for i in range(first, last):
        if L[i] <= pivot_value:
            smaller_index += 1
            L[smaller_index], L[i] = L[i], L[smaller_index]
    L[smaller_index + 1], L[last] = L[last], L[smaller_index + 1]
    return smaller_index + 1
print('Quick sort function run 1000 times, cost: ', timeit('test()', 'from __main__ import test', number=1000), 'seconds.')
# Quick sort function run 1000 times, cost:  0.083452 seconds.
'''

'''
from timeit import timeit
def test():
    # import random
    # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
    # L = list(gen)
    L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
    quick_sort(L)
def quick_sort(L):
    n = len(L)
    if n <= 1:
        return L
    pivot_value = L[0]
    lesser = [item for item in L[1:] if item <= pivot_value]
    greater = [item for item in L[1:] if item > pivot_value]
    return quick_sort(lesser) + [pivot_value] + quick_sort(greater)
print('Quick sort function run 1000 times, cost: ', timeit('test()', 'from __main__ import test', number=1000), 'seconds.')
# Output:
#Quick sort function run 1000 times, cost:  0.1047325 seconds.
'''