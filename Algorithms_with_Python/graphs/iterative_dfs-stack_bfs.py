from collections import deque


def bfs(node, visited, graph):
    stack = list()  #stack instead of queue -> dfs
    visited.add(node)
    stack.append(node)
    while stack:
        v = stack.pop()
        print(v, end= " ")
        for child in graph[v]:
            if child not in visited:
                stack.append(child)
                visited.add(child)


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    21: [14],
    14: [6, 23],
    1: [7],
    12: [],
    31: [21],
    23: [21],
    6: []
}

visited = set()
first_node = 7
bfs(first_node, visited, graph)