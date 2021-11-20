# from  collections import deque  #双向队列
#
# # q = deque([1,2,3,4,5],5)
# # q.append(6) #队尾进队
# # print(q.popleft()) #队首出队
#
# #用于双向队列
# #q.appengleft(1) #队首进队
# #q.pop() #队尾出队
#
# def tail(n):
#     with open('test.txt', 'r') as f:    #原理：f相当于一个列表line，持续进队；n是队列大小。
#         q = deque(f,n)
#         return q
# #print(tail(5))
# for line in tail(5):
#     print(line,end='')



import heapq
pqueue =[]
heapq.heappush(pqueue, (1, 'A'))
heapq.heappush(pqueue, (7, 'B'))
heapq.heappush(pqueue, (2, 'E'))
heapq.heappop(pqueue)
print(pqueue)
heapq.heappop(pqueue)
print(pqueue)
heapq.heappush(pqueue, (2, 'E'))
print(pqueue)