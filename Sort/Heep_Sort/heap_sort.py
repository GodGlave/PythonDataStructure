#时间复杂度：nlogn


def sift(li, low, high):
    """

    :param li: 列表
    :param low: 堆的根节点位置
    :param high:堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # temp更大，把tmp放到i的位置上
            li[i] = tmp  # 把tmp放到某一级领导位置上
            break
    # li[i]=tmp
    else:
        li[i] = tmp  # 把tmp放到叶子节点上

def heap_sort(li):
    n = len(li)
    #建堆从小堆->大堆
    for i in range((n-2)//2,-1,-1):   #倒着遍历到0，步长-1，下标n-1;i代表建堆的时候调整的部分根的下标
        sift(li,i,n-1) #high判断越界可取n-1，建堆完成了
    # print(li)
    #排序，把根放尾部，调大根堆....
    for i in range(n-1,-1,-1):
        #i 指向当前堆的最后一个元素
        li[0],li[i]=li[i],li[0]
        sift(li,0,i-1) #i-1是新的high


li=[i for i in range(100)]
import random
random.shuffle(li)
print(li)

heap_sort(li)
print(li)