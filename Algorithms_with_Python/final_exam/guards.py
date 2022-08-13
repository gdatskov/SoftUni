from collections import deque

nodes_count = int(input())
edges_count = int(input())

graph = {}

for _ in range(edges_count):
    source, destination = [int(x) for x in input().split()]
    if destination not in graph.keys():
        graph[destination] = []
    if source not in graph.keys():
        graph[source] = [destination]
    else:
        graph[source].append(destination)

start = int(input())
visited = [False] * (nodes_count+1)
queue = deque([start])
visited[start] = True
while True:
    if not queue:
        break
    node = queue.pop()
    for child in graph[node]:
        if not visited[child]:
            queue.appendleft(child)
            visited[child] = True

for node in range(1, len(visited)):
    if visited[node] == False:
        print(node, end=" ")
