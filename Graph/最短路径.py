def BFS(graph, s):
    queue = []  # 建立队列
    queue.append(s)
    seen=set()
    seen.add(s)
    parent ={s:None}
    while queue:
        vertex = queue.pop(0)  # 队列，先进先出
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent


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
    parent = BFS(graph, 'E')
    # for key in parent:
    #     print(key,parent[key])
    v ='B'
    while v is not None:
        print(v)
        v=parent[v]
