# #栈--深度优先搜索（回溯法）
#
from collections import deque
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
    lambda x,y:(x+1,y),
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1),
]
# def maze_path(x1,y1,x2,y2):
#     stack = []
#     stack.append((x1,y1))
#     while(len(stack)>0):
#         curNode = stack[-1] #当前的节点
#         if curNode[0] == x2 and curNode[1] == y2:
#             for p in stack:
#                 print(p)
#             return True
#         # x，y四个方向 x-1,y;x+1,y;x,y-1;x,y+1
#         for dir in dirs:
#             nextNode = dir(curNode[0],curNode[1])
#             #如果下一个节点能走
#             if maze[nextNode[0]][nextNode[1]] == 0:
#                 stack.append(nextNode)
#                 maze[nextNode[0]][nextNode[1]]=2 #2表示已经走过
#                 break
#         else:
#             maze[nextNode[0]][nextNode[1]]=2
#             stack.pop()
#     else:
#         print("没有路")
#         return  False
#
# maze_path(1,1,8,8)



#队列--广度优先搜索
def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        #realpath.append(curNode[0],curNode[1])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2])  # 起点
    realpath.reverse()
    for node in realpath:
        print(node)
    # print(realpath)

def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 终点
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))  # 后续节点进队，记录哪个节点带它来的
                maze[nextNode[0]][nextNode[1]] = 2  # 标记为已走过
    else:
        print("没有路")
        return False


maze_path_queue(1, 1, 8, 8)
