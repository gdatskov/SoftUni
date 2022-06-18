from collections import deque

matrix_size = int(input())
matrix = []
for row in range(matrix_size):
    matrix.append(list(int(x) for x in input().split()))

while True:
    command = input()

    if command == "END":
        break

    command = deque(command.split(" "))
    action = command.popleft()
    row_index = int(command.popleft())
    col_index = int(command.popleft())
    value = int(command.popleft())

    if not 0 <= row_index < matrix_size or not 0 <= col_index < matrix_size:
        print("Invalid coordinates")
        continue

    if action == "Add":
        matrix[row_index][col_index] += value
    if action == "Subtract":
        matrix[row_index][col_index] -= value

for row in matrix:
    print(" ".join(map(str, row)))
