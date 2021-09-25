def quick_sort(L):
    '''使用 '列表生成式(List Comprehensions)' 查找比 '基准(pivot)' 小或大的元素序列'''
    n = len(L)
    if n <= 1:
        return L

    pivot_value = L[0]
    lesser = [item for item in L[1:] if item <= pivot_value]
    greater = [item for item in L[1:] if item > pivot_value]

    return quick_sort(lesser) + [pivot_value] + quick_sort(greater)


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    sorted = quick_sort(L1)
    print('After: ', sorted)

# Output:
Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]