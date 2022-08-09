rows = int(input())
columns = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * columns)


def dfs(row, col, matrix, visited, element):
    if not 0 <= row < rows or not 0 <= col < columns:
        return
    if visited[row][col] or matrix[row][col] != element:
        return
    visited[row][col] = True
    # connected[element] += 1
    dfs(row + 1, col, matrix, visited, element)
    dfs(row, col + 1, matrix, visited, element)
    dfs(row - 1, col, matrix, visited, element)
    dfs(row, col - 1, matrix, visited, element)


found_areas = {}
for row in range(rows):
    for col in range(columns):
        if visited[row][col]:
            continue
        element = matrix[row][col]
        # connected_elements = {element: 0}
        if element not in found_areas.keys():
            found_areas[element] = 0
        dfs(row, col, matrix, visited, element)
        found_areas[element] += 1
        # if element not in found_areas.keys():
        #     found_areas[element] = [connected_elements[element]]
        # else:
        #     found_areas[element].append(connected_elements[element])

print(f"Areas: {sum(found_areas.values())}")
for letter, count in sorted(found_areas.items()):
    print(f"Letter '{letter}' -> {count}")