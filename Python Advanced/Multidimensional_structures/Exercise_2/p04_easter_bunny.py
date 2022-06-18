size = int(input())
board = []
bunny_row, bunny_col = "No bunny", "No bunny"

for i in range(size):
    if size == 0:
        break
    current_row = list(input().split(" "))
    board.append(current_row)
    # Where is the bunny?
    if "B" in current_row:
        bunny_row = i
        for j in range(len(current_row)):
            if current_row[j] == "B":
                bunny_col = j
                break  # Bunny is found!

if bunny_row == "No bunny" or bunny_col == "No bunny":
    bunny = False
else:
    bunny = [bunny_row, bunny_col]

best_dir = ""
best_eggs = 0

data = {
    "up": {"step": (0, -1), "eggs": 0, "moves": []},
    "down": {"step": (0, 1), "eggs": 0, "moves": []},
    "left": {"step": (-1, 0), "eggs": 0, "moves": []},
    "right": {"step": (1, 0), "eggs": 0, "moves": []},
}

for path in data.keys():
    if not bunny:
        break
    current_bunny_row = bunny_row
    current_bunny_col = bunny_col
    col_step, row_step = data[path]["step"]

    while True:
        current_bunny_row += row_step
        current_bunny_col += col_step
        if not (0 <= current_bunny_row < size) or not (0 <= current_bunny_col < size):
            break
        if board[current_bunny_row][current_bunny_col] == "X":
            break
        data[path]["eggs"] += int(board[current_bunny_row][current_bunny_col])
        data[path]["moves"].append([current_bunny_row, current_bunny_col])
    # print(data[path]["eggs"])
    # print(data[path]["moves"])
    if data[path]["eggs"] > best_eggs:
        best_dir = path
        best_eggs = data[path]["eggs"]

if best_eggs > 0 and bunny:
    print(best_dir)
    for move in data[best_dir]["moves"]:
        print(move)
    print(data[best_dir]["eggs"])
