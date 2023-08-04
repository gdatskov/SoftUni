matrix_rows, matrix_cols = map(int, input().split())

player_row, player_col = None, None
moves = 0
opponents = 3
matrix = []

for x in range(matrix_rows):
    row = input().split()
    matrix.append(row)
    if "B" in row:
        player_row = x
        player_col = row.index("B")


while opponents > 0:
    command = input()
    if command == "Finish":
        break
    next_row, next_col = player_row, player_col

    # Next move coords
    if command == "up" and player_row > 0:
        next_row = player_row - 1
    elif command == "down" and player_row < matrix_rows:
        next_row = player_row + 1
    elif command == "left" and player_col > 0:
        next_col = player_col - 1
    elif command == "right" and player_col < matrix_cols:
        next_col = player_col + 1

    # Action
    next_object = matrix[next_row][next_col]
    if next_object != "O" and next_object != "B":
        if next_object == "P":
            opponents -= 1
        matrix[player_row][player_col] = "-"
        matrix[next_row][next_col] = "B"
        player_row = next_row
        player_col = next_col
        moves += 1

print("Game over!")
print(f"Touched opponents: {3 - opponents} Moves made: {moves}")