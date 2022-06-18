import copy
from collections import deque


def valid_move(action_, row_, col_, row_range, col_range):
    valid = True
    if action_ == "L":
        if col_ == 0:
            valid = False
    if action_ == "R":
        if col_ == col_range - 1:
            valid = False
    if action_ == "U":
        if row_ == 0:
            valid = False
    if action_ == "D":
        if row_ == row_range - 1:
            valid = False
    return valid


def win_move_check(current_row=0, current_col=0):
    player_status = True
    win_status = False
    for r in range(total_rows):
        for c in range(total_columns):
            if bunny_lair[r][c] == "P":
                current_row, current_col = r, c
                if not valid_move(action, r, c, total_rows, total_columns):
                    player_status = False
                    win_status = True
                    return [player_status, win_status, current_row, current_col]
    return [player_status, win_status, current_row, current_col]


def move(action_, old_r, old_c):
    new_r, new_c = old_r, old_c
    if action_ == "U" and old_r > 0:
        new_r, new_c = old_r - 1, old_c
    if action_ == "D" and old_r < total_rows:
        new_r, new_c = old_r + 1, old_c
    if action_ == "L" and old_c > 0:
        new_r, new_c = old_r, old_c - 1
    if action_ == "R" and old_c < total_columns:
        new_r, new_c = old_r, old_c + 1
    return new_r, new_c


total_rows, total_columns = (int(x) for x in input().split())
bunny_lair = [list(input()) for rows in range(total_rows)]
commands = deque(input())

# new_row, new_col, old_row, old_col = 0, 0, 0, 0
player = True
win = False


while player:
    # if win or not commands or not bunny_lair:
    # if win:
    #     break
    # if not commands:
    #     break

    action = commands.popleft()

    player, win, old_row, old_col = win_move_check()

    new_row, new_col = move(action, old_row, old_col)

    if bunny_lair:
        if bunny_lair[new_row][new_col] == "B":
            player = False
            win = False

        if bunny_lair[new_row][new_col] != "B":
            bunny_lair[new_row][new_col] = "P"

        bunny_lair[old_row][old_col] = "."

    bunny_lair_expansion = copy.deepcopy(bunny_lair)

    for row in range(total_rows):
        for col in range(total_columns):
            if bunny_lair[row][col] == "B":
                for sub_row in range(row - 1, row + 2):
                    if sub_row < 0 or sub_row >= total_rows:
                        continue
                    for sub_col in range(col - 1, col + 2):
                        if sub_col < 0 or sub_col >= total_columns:
                            continue
                        if sub_row == row or sub_col == col:
                            if bunny_lair_expansion[sub_row][sub_col] == "P":
                                player = False
                                win = False
                            bunny_lair_expansion[sub_row][sub_col] = "B"
                            # for r in bunny_lair_expansion:
                            #     print(" ".join(r))
                            # print(f"Player", player)
                            # print(f"win", win)
                            # print(new_row, new_col)
                            # print()

    if bunny_lair_expansion:
        bunny_lair = bunny_lair_expansion

for row in bunny_lair:
    print("".join(row))
if win:
    print(f"won: {new_row} {new_col}")
else:
    print(f"dead: {new_row} {new_col}")

