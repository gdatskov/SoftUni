from collections import deque

nodes_number = int(input())
edges_number = int(input())

graph = [[] for _ in range(nodes_number + 1)]

for _ in range(edges_number):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes_number + 1)
parent = [None] * (nodes_number + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == destination_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque([])
node = destination_node
while node is not None:
    path.appendleft(node)
    node = parent[node]

print(" ".join(str(x) for x in path))
