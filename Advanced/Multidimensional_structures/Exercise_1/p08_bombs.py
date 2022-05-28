from collections import deque

matrix_range = int(input())
matrix = []

for row in range(matrix_range):
    col_values = [int(x) for x in input().split()]
    if len(col_values) == matrix_range:
        matrix.append(col_values)
    else:
        continue

bombs = deque(x.split(",") for x in input().split(" "))

for coords in range(len(bombs)):
    bombs[coords] = [int(x) for x in bombs[coords]]

while bombs:
    bomb_row, bomb_col = bombs.popleft()
    bomb_value = matrix[bomb_row][bomb_col]
    if bomb_value > 0:
        for sub_row in range(bomb_row-1, bomb_row+2):
            if 0 <= sub_row < matrix_range:
                for sub_col in range(bomb_col-1, bomb_col+2):
                    if 0 <= sub_col < matrix_range:
                        # if [sub_row, sub_col] not in bombs:
                        if matrix[sub_row][sub_col] > 0:
                            matrix[sub_row][sub_col] -= bomb_value

alive_cells = 0
alive_sum = 0

for row in matrix:

    for cell in row:
        if cell > 0:
            alive_cells += 1
            alive_sum += cell

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sum}")

for row in matrix:
    print(" ".join(str(x) for x in row))
