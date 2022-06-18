import copy
from collections import deque


def knight_moves(r, c): # 1, 4
    direct_hit = False #  V         NV       NV       NV       NV      NV      V       V
                    #   0, 2     -1, 3     -1, 5    0, 6     2, 6    3, 5,   3,  3,   2, 2
    possible_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    for move in possible_moves:
        x, y = move # -2, -1
        #  0 <= 1-2 < 5         and  0 <= 4-1 < 5
        if 0 <= r+x < board_size and 0 <= c+y < board_size:
            #  board_copy [0]  [2]
            if board_copy[r+x][c+y] == "K":
                direct_hit = True
                return [direct_hit, r+x, c+y]
    return [direct_hit, r, c]


board_size = int(input())
knights = []
board = []


for entry in range(board_size):
    info_row = list(input())
    board.append(info_row)
    for ch in range(len(info_row)):
        if info_row[ch] == "K":
            knights.append((entry, ch))

count = 0
min_count = len(knights)

for knight in knights:
    print(knight)
    board_copy = copy.deepcopy(board)
    row, col = knight
    while True:
        valid_move, current_row, current_col = knight_moves(row, col)
        if not valid_move:
            break
        count += 1
        board_copy[row][col] = 0
        row, col = current_row, current_col
        for rr in board_copy:
            print(" ".join(map(str, rr)))
        print("end turn")
    print("end iteration")
    print()
    if count < min_count:
        min_count = count
    count = 0


print(min_count)