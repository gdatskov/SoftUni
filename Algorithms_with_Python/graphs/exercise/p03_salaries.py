employees = int(input())
employee_graph = []
for employee in range(employees):
    employee_graph.append(list(input()))


def find_dependencies(graph):
    total_employees = len(graph)
    dependencies = {x: 0 for x in range(total_employees)}
    for employee in graph:
        for worker in range(len(employee)):
            if employee[worker] == "Y":
                dependencies[worker] += 1
    return dependencies


def get_independent(dependencies):
    for employee, workers in dependencies.items():
        if workers == 0:
            return employee


def remove_node(independent, dependencies, graph):
    for worker in range(len(graph)):
        if graph[independent][worker] == "Y":
            dependencies[worker] -= 1
    dependencies.pop(independent)


def topology_sort(graph):
    dependencies: dict = find_dependencies(graph)
    sorted_by_dependency = []

    while dependencies:
        independent = get_independent(dependencies)
        sorted_by_dependency.append(independent)
        remove_node(independent, dependencies, graph)

    return sorted_by_dependency


dependency_sorted_employees = topology_sort(employee_graph)
salaries = {employee: 0 for employee in dependency_sorted_employees}

while dependency_sorted_employees:
    employee = dependency_sorted_employees.pop()
    if "Y" not in employee_graph[employee]:
        salaries[employee] = 1
        continue
    for worker in range(employees):
        if employee_graph[employee][worker] == "Y":
            salaries[employee] += salaries[worker]
# print(salaries, sep="\n")
print(sum(salaries.values()))