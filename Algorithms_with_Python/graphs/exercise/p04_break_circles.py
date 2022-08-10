import random
from collections import deque


def path_exists(source, destination, graph):
    visited = set()

    bfs(source, graph, visited)

    return destination in visited



def bfs(node, graph, visited):
    queue = deque()
    visited.add(node)
    queue.appendleft(node)
    while queue:
        current_node = queue.pop()
        for child in graph[current_node]:
            if child not in visited:
                queue.appendleft(child)
                visited.add(child)

# Part 1: Create graph from input
nodes = int(input())
graph = {}
edges = []
for _ in range(nodes):
    node, children = input().split("->")
    node = node.strip()
    children = children.strip()
    if children:
        children = [x for x in children.split(" ")]
    else:
        children = []
    graph[node] = children
    for child in children:
        edges.append((node, child))
# print(*graph.items(), sep="\n")
# print(*edges, sep="\n")

removed_edges = []

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination in graph[source] and source in graph[destination]:
        graph[source].remove(destination)
        graph[destination].remove(source)

        if path_exists(source, destination, graph):
            removed_edges.append((source, destination))
        else:
            graph[source].append(destination)
            graph[destination].append(source)

print(f"Edges to remove: {len(removed_edges)}")
for s, d in removed_edges:
    print(f"{s} - {d}")
