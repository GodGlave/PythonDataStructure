import random
from cal_time import *

@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟
        #print(i)
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:           #降序改"<"
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return
li=list(range(10000))
random.shuffle(li)
bubble_sort(li)