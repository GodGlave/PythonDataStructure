import heapq  #q-->queue 优先队列 小/大先出
import random

li = list(range(100))
random.shuffle(li)

print(li)

heapq.heapify(li) #建堆
print(li)
heapq.heappop(li)

n=len(li)
for i in range(n):
    print(heapq.heappop(li),end=',')
