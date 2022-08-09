graph = {}

while True:
    entry = input()
    if entry == "End":
        break
    node, edge = entry.split("-")
    for item in [node, edge]:
        if item not in graph.keys():
            graph[item] = []
    graph[node].append(edge)

# print(graph, sep="\n")

acyclic = False
for edges in graph.values():
    if not edges:
        acyclic = True
        break
print(f"Acyclic: {'Yes' if acyclic else 'No'}")
