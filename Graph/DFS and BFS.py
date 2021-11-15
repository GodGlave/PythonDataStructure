def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = []
    seen.append(s)
    while stack:
        vertex = stack.pop()  # 栈，取出最后一个并删掉 先进后出
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.append(w)
        print(vertex)


def BFS(graph, s):
    queue = []  # 建立队列
    queue.append(s)
    seen = []  # 记录已经遍历过的点
    seen.append(s)
    while queue:
        vertex = queue.pop(0)  # 队列，先进先出
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.append(w)
        print(vertex)


if __name__ == '__main__':
    # 图节点
    graph = {

        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    BFS(graph, 'A')
    DFS(graph, 'A')