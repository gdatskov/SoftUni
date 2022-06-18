from collections import deque


def knight_moves(r, c):
    possible_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    removed_knights = 0
    attack = False
    for move in possible_moves:
        x, y = move
        if 0 <= r+x < board_size and 0 <= c+y < board_size:
            if board[r+x][c+y] == "K":
                board[r][c] = 0
                attack = True
    if attack:
        removed_knights += 1

    return removed_knights


def more_odd_knights(matrix):
    more_knights_on_odd = False
    odd_diagonal_knight_count = 0
    even_diagonal_knight_count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] == "K":
                if x % 2 == 1 and y % 2 == 0:   #odd diagonals
                    odd_diagonal_knight_count += 1
                else:
                    even_diagonal_knight_count += 1

    if odd_diagonal_knight_count >= even_diagonal_knight_count:
        more_knights_on_odd = True

    return more_knights_on_odd


board_size = int(input())
knights = deque()
board = []


for entry in range(board_size):
    info_row = list(input())
    board.append(info_row)
    for ch in range(len(info_row)):
        if info_row[ch] == "K":
            knights.append((entry, ch))

count = 0
min_count = len(knights)

if more_odd_knights(board):
    start_col = 1
else:
    start_col = 0

for row in range(board_size):
    for col in range(start_col, board_size, 2):
        if board[row][col] == "K":
            count += knight_moves(row, col)
    start_col = abs(start_col - 1)

    for rr in board:
        print(" ".join(map(str, rr)))
    print(count)
    print("end turn")


print(count)