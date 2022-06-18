from collections import deque

def knight_moves(r, c):
    possible_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    attacks = 0
    for move in possible_moves:
        x, y = move
        if 0 <= r+x < board_size and 0 <= c+y < board_size:
            if board[r+x][c+y] == "K":
                attacks += 1
    return attacks


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
current_best = 8

while knights and current_best:
    for _ in range(len(knights)):
        current_knight = knights.popleft()
        current_row, current_col = current_knight
        check = knight_moves(current_row, current_col)
        if knight_moves(current_row, current_col) == current_best:
            count += 1
            board[current_row][current_col] = f"{count}"
        else:
            knights.append(current_knight)
    current_best -= 1

    """
    Visualise turn per turn:
    """
    # for rr in board:
    #     print("  ".join(map(str, rr)))
    # print(count)
    # print("end turn")
    """"""

print(count)
