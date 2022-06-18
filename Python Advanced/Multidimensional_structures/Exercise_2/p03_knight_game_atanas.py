def knight_moves(matrix, r, c):
    possible_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    attacks = 0
    for move in possible_moves:
        x, y = move
        if 0 <= r+x < len(matrix) and 0 <= c+y < len(matrix):
            if matrix[r+x][c+y] == "K":
                attacks += 1
    return attacks


size = int(input())
board = []

for _ in range(size):
    board.append(list(input()))

knight_counter = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(size):
        for col in range(size):
            if board[row][col] == "0":
                continue
            count = knight_moves(board, row, col)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col

    if best_count == 0:
        break

    board[knight_row][knight_col] = "0"
    knight_counter += 1

    """
    Visualise turn per turn:
    """
    # for rr in board:
    #     print("  ".join(map(str, rr)))
    # print(knight_counter)
    # print("end turn")
    """"""

print(knight_counter)
