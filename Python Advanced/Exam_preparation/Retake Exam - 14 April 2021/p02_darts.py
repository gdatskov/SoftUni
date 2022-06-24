players = input().split(", ")
size = 7
max_index = size - 1
board = [input().split(" ") for _ in range(size)]
score = dict((player, 501) for player in players)
throws = dict((player, 0) for player in players)
winner = None

turn = 1

while all(x > 0 for x in score.values()):
    player_index = turn % len(players) - 1
    player = players[player_index]

    target = eval(input())
    throws[player] += 1
    turn += 1

    if not all(0 <= x <= max_index for x in target):
        continue

    target_row, target_col = target
    target_value = board[target_row][target_col]

    if target_value == "B":
        score[player] = 0
        break

    if target_value.isdigit():
        score[player] -= int(target_value)
    else:
        points = sum(
            [int(x) for x in [
                board[0][target_col],
                board[max_index][target_col],
                board[target_row][0],
                board[target_row][max_index],
            ]])
        if target_value == "D":
            score[player] -= points * 2
        if target_value == "T":
            score[player] -= points * 3


for player, total_points in score.items():
    if total_points <= 0:
        winner = player

print(f"{winner} won the game with {throws[winner]} throws!")
