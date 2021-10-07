#时间复杂度：O(nlogn)

def quick_sort(li, left, right):
    if left < right:    #至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)

def partition(li, left, right):    #O(n)
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 找比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写到左边空位上
        #print(li,'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边空位上
        #print(li, 'left')
        #print(li)
    li[left] = tmp  # 把tmp归位
    return left


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print(li)
# partition(li, 0, len(li) - 1)
quick_sort(li,0,len(li)-1)
print(li)

# #最坏情况O(n^2)
#import sys
#sys.setrecursionlimit(1000) #设置递归最大深度
#li=list(range(10000,0,-1))
# li=[9,8,7,6,5,4,3,2,1]
# partition(li, 0, len(li) - 1)
# print(li)