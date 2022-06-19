size = int(input())
board = []
alice_row, alice_col = None, None
rabbit_row, rabbit_col = None, None

for i in range(size):
    current_row = list(input().split(" "))
    board.append(current_row)
    if "A" or "R" in current_row:
        for j in range(len(current_row)):
            if current_row[j] == "A":
                alice_row = i
                alice_col = j
            if current_row[j] == "R":
                rabbit_row = i
                rabbit_col = j

data = {
    "up":    ( 0, -1),
    "down":  ( 0,  1),
    "left":  (-1,  0),
    "right": ( 1,  0),
}

tea = 0
alice = True

while alice:
    move = input()
    move_col, move_row = data[move]
    alice_next_row = alice_row + move_row
    alice_next_col = alice_col + move_col
    board[alice_row][alice_col] = "*"

    if alice_next_row not in range(size) or alice_next_col not in range(size):
        alice = False
        break

    alice_next_move_cell = board[alice_row+move_row][alice_col+move_col]

    if alice_next_move_cell == "R":
        board[alice_row+move_row][alice_col+move_col] = "*"
        alice = False
        break

    if alice_next_move_cell.isdigit():
        tea += int(alice_next_move_cell)

    alice_row = alice_row + move_row
    alice_col = alice_col + move_col
    board[alice_row][alice_col] = "*"

    if tea >= 10:
        break

if alice:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for i in board:
    print(" ".join(i))