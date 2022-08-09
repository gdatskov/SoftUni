def find_dependencies(graph):
    # node_edges = {node: 0 for node in graph}
    # for edges in graph.values():
    #     for edge in edges:
    #         if edge in graph.keys():
    #             node_edges[edge] += 1
    # return node_edges
    node_deps = {}
    for node, children in graph.items():
        if node not in node_deps:
            node_deps[node] = 0
        for child in children:
            if child not in node_deps:
                node_deps[child] = 1
            else:
                node_deps[child] += 1
    return node_deps


def get_independent_node(dependencies):
    for node, edges in dependencies.items():
        if not edges:
            return node
    return


def remove_node(independent_node, dependencies):
    for child in graph[independent_node]:
        dependencies[child] -= 1
    dependencies.pop(independent_node)


def topology_sort(graph):
    dependencies = find_dependencies(graph)
    # print(dependencies)

    sorted_nodes_by_dependency = []

    while dependencies:
        independent_node = get_independent_node(dependencies)

        if not independent_node:
            return "Invalid topological sorting"

        sorted_nodes_by_dependency.append(independent_node)
        remove_node(independent_node, dependencies)
    return f"Topological sorting: {', '.join(sorted_nodes_by_dependency)}"


nodes = int(input())

# graph = {key: val.split(", ") for key, val in ((x.strip() for x in input().split("->")) for _ in range(nodes))}
graph = {}
for _ in range(nodes):
    node, edges = input().split("->")
    if edges:
        edges = [x.strip() for x in edges.split(", ")]
    else:
        edges = []
    graph[node.strip()] = edges
# print(*graph.items(), sep="\n")
# print()
# print(*node_edges.items(), sep="\n")


print(topology_sort(graph))
