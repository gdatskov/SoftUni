from math import floor

field = []
path = []
player_row, player_col = 0, 0
coins = 0

size = int(input())

for i in range(size):
    row = input().split(" ")
    field.append(row)
    for j in range(size):
        if row[j] == "P":
            player_row, player_col = i, j
            path.append([player_row, player_col])
            break

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

player = True
while coins < 100:
    command = input()
    field[player_row][player_col] = 0
    move_row, move_col = movement[command]
    player_row = (player_row + move_row) % size
    player_col = (player_col + move_col) % size
    path.append([player_row, player_col])
    symbol = field[player_row][player_col]
    if str(symbol).isdigit():
        coins += int(symbol)
    else:
        player = False
        coins = int(coins / 2)
        break

if player:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
for x in path:
    print(x)
