"""
Chessboard 8 x 8 = 64
Rows = numbers(ranks) from 1 to 8
Columns = letters from a to h
E.g. each cell is a1, b4, h3, etc...

Two pawns - white (w) and black (b)
Each moves trough the ranks with 1 square per move:
1-8 for white
8-1 for black
They can only attack in front of them(movement direction) diagonally

The pawns are put at random squares. First move is white. Then black, etc

The first who captures the opponent or reaches the end of board wins.

"""

chessboard = []
size = 8
white_row, white_col = 0, 0
black_row, black_col = 0, 0

for i in range(size):
    row = input().split(" ")
    chessboard.append(row)
    for j in range(size):
        if row[j] == "w":
            white_row, white_col = i, j
        if row[j] == "b":
            black_row, black_col = i, j

white_capture = False
white_queen = False
black_capture = False
black_queen = False

while True:
    # White turn
    if white_row != 0:
        if white_col < size - 1:
            if chessboard[white_row-1][white_col+1] == "b":
                white_row -= 1
                white_col += 1
                white_capture = True
                break
        if white_col > 0:
            if chessboard[white_row-1][white_col-1] == "b":
                white_row -= 1
                white_col -= 1
                white_capture = True
                break
        if not white_capture:
            chessboard[white_row][white_col] = "-"
            white_row -= 1
            chessboard[white_row][white_col] = "w"
    else:
        white_queen = True
        break
    # Black turn
    if black_row != size - 1:
        if black_col < size-1:
            if chessboard[black_row+1][black_col+1] == "w":
                black_row += 1
                black_col += 1
                black_capture = True
                break
        if black_col > 0:
            if chessboard[black_row+1][black_col-1] == "w":
                black_row += 1
                black_col -= 1
                black_capture = True
                break
        if not black_capture:
            chessboard[black_row][black_col] = "-"
            black_row += 1
            chessboard[black_row][black_col] = "b"
    else:
        black_queen = True
        break


white_row = size - white_row
black_row = size - black_row

white_col = chr(97+white_col)
black_col = chr(97+black_col)

if white_capture:
    print(f"Game over! White win, capture on {white_col+str(white_row)}.")
if white_queen:
    print(f"Game over! White pawn is promoted to a queen at {white_col+str(white_row)}.")
if black_capture:
    print(f"Game over! Black win, capture on {black_col+str(black_row)}.")
if black_queen:
    print(f"Game over! Black pawn is promoted to a queen at {black_col+str(black_row)}.")
