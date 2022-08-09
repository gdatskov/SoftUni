from collections import deque


def dfs(node, visited, graph):
    queue = deque()
    visited.add(node)
    queue.appendleft(node)
    while queue:
        v = queue.pop()
        print(v, end= " ")
        for child in graph[v]:
            if child not in visited:
                queue.appendleft(child)
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
dfs(first_node, visited, graph)