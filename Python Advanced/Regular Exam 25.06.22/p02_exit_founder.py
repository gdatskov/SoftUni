players = input().split(", ")
size = 6
max_index = size - 1
maze = [input().split(" ") for _ in range(size)]

next_player, current_player = players
rest_counter = dict((player, 0) for player in players)

while True:
    current_player, next_player = next_player, current_player

    target = eval(input())

    if rest_counter[current_player]:
        rest_counter[current_player] -= 1
        continue

    target_row, target_col = target
    symbol = maze[target_row][target_col]

    if symbol == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif symbol == "T":
        print(f"{current_player} is out of the game! The winner is {next_player}.")
        break
    elif symbol == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        rest_counter[current_player] = 1