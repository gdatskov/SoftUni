from collections import deque


def valid_move(action_, row_, col_, range_):
    valid = True
    if action_ == "left":
        if col_ == 0:
            valid = False
    if action_ == "right":
        if col_ == range_ - 1:
            valid = False
    if action_ == "up":
        if row_ == 0:
            valid = False
    if action_ == "down":
        if row_ == range_ - 1:
            valid = False
    return valid


def move_action(action_, row_, col_, field):

    def collect(row__, col__, coal_collected_=0):
        sym = field[row__][col__]
        collectable = sym
        field[row__][col__] = "*"
        if collectable == "c":
            coal_collected_ += 1
        if collectable == "e":
            coal_collected_ = "end"
        return coal_collected_

    if action_ == "left":
        col_ -= 1
        collected = collect(row_, col_)
    if action_ == "right":
        col_ += 1
        collected = collect(row_, col_)
    if action_ == "up":
        row_ -= 1
        collected = collect(row_, col_)
    if action_ == "down":
        row_ += 1
        collected = collect(row_, col_)

    new_miner_loc = (row_, col_)

    return [collected, new_miner_loc]


matrix_range = int(input())
commands = deque(input().split())

matrix = []
coal_in_field = 0
coal = 0
game_over = False

for row in range(matrix_range):
    col_values = input().split()
    matrix.append(col_values)
    for col in range(len(col_values)):
        if matrix[row][col] == "s":
            miner_loc = (row, col)
        if matrix[row][col] == "c":
            coal_in_field += 1

while commands and coal_in_field:
    action = commands.popleft()
    row_loc, col_loc = miner_loc
    if not valid_move(action, row_loc, col_loc, matrix_range):
        continue
    miner_data = move_action(action, row_loc, col_loc, matrix)
    miner_loc = miner_data[1]
    coal_collected = miner_data[0]
    if coal_collected == "end":
        game_over = True
        break
    else:
        coal += coal_collected
        coal_in_field -= coal_collected
    matrix[miner_loc[0]][miner_loc[1]] = "s"
    # for row in matrix:
    #     print(" ".join(row))
    # print()

if game_over:
    print(f"Game over!", miner_loc)
else:
    if coal_in_field:
        print(f"{coal_in_field} pieces of coal left.", miner_loc)
    else:
        print(f"You collected all coal!", miner_loc)

