from collections import deque

matrix_rows, matrix_columns = [int(x) for x in input().split(" ")]
matrix = list()

for rows in range(matrix_rows):
    row_entry = input().split()
    matrix.append(row_entry)


while True:

    valid = True

    command = deque(input().split())
    action = command.popleft()
    if action == "END":
        break
    if action != "swap" or len(command) != 4:
        valid = False
        print("Invalid input!")
        continue
    for char in range(len(command)):
        if not command[char].isdigit():
            valid = False
            break
    for char in range(len(command)):
        check = command[char]
        if int(command[char]) % 2 != 0 and not 0 <= int(command[char]) < matrix_columns:
            valid = False
            break
        if int(command[char]) % 2 == 0 and not 0 <= int(command[char]) < matrix_rows:
            valid = False
            break
    if not valid:
        print("Invalid input!")
        continue
    command = [int(x) for x in command]
    row1, col1 = (command[0], command[1])
    row2, col2 = (command[2], command[3])

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(" ".join(row))
