# 问题：
# 现在有n个数，设计算法得到前k大的数。（k<n)
#
# 解决思路：
# 排序后切片                      O(nlogn)
# 排序LowB三人组（冒泡/选择/插入）   O（kn）
#
# 堆排序思路：                    O(klogn)
# 取K个数建堆
# 构建小根堆
# 遍历列表调整堆
#
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def topk(li,k):
    heap =li[0:k]
    for i in range(k-2//2,-1,-1):
        sift(li,i,k-1)
    #1.建堆(小根堆）
    for i in range(k,len(li)):
        if li[i]>heap[0]:
            heap[0]=li[i]
            sift(heap,0,k-1)
    #2.遍历
    for i in range(k- 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    #3.出数
    return heap
li=[i for i in range(100)]
# import random
# li=list(range(1000))
# random.shuffle(li)
print(topk(li,10))
