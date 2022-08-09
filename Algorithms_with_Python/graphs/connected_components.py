def dfs(node, graph, visited, components):
    if visited[node]:
        return
    visited[node] = True
    # components.append(node)   #also working, different order
    for child in graph[node]:
        dfs(child, graph, visited, components)
    components.append(node)


total_nodes = int(input())
graph = []
for node in range(total_nodes):
    edges = [int(x) for x in input().split(" ") if x]
    graph.append(edges)

# print(*graph, sep="\n")

visited = [False] * len(graph)
for node in range(total_nodes):
    if not visited[node]:
        connected = []
        dfs(node, graph, visited, connected)
        print(f"Connected component: {' '.join(str(x) for x in connected)}")
