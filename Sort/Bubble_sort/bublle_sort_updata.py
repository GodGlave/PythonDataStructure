# 升序排列
#时间复杂度：O（n^2）
import random

def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟
        #print(i)
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:           #降序改"<"
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return

# li = [random.randint(0, 10000) for i in range(1000)]
# print(li)
# bubble_sort(li)
# print(li)
li=[1,2,3,4,5,6,7,8,9]
print(li)
bubble_sort(li)