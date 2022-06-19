from collections import deque

size = 5
board = []
targets_left = []
targets_hit = []
ranger_row, ranger_col = "No ranger", "No ranger"
shooter = False
targets = False

for i in range(size):
    current_row = list(input().split(" "))
    board.append(current_row)
    # Where are the ranger and the targets?
    if "A" or "x" in current_row:
        for j in range(len(current_row)):
            if current_row[j] == "A":
                shooter = True
                ranger_row, ranger_col = i, j   # Remember shooter initial position
            if current_row[j] == "x":
                targets = True
                targets_left.append((i, j))     # Remember target positions

steps = {
    "up":    ( 0, -1),
    "down":  ( 0,  1),
    "left":  (-1,  0),
    "right": ( 1,  0),
}

commands = int(input())

for _ in range(commands):
    if not shooter or not targets:
        break
    # Get commands
    line = deque(input().split(" "))
    action, direction = line.popleft(), line.popleft()
    if line:
        moves = int(line.popleft())

    # Get direction steps
    step_col, step_row = steps[direction]

    if action == "move":
        # Move at once with steps given or step by step until end of moves?
        next_move_row = ranger_row + step_row * moves   # All at once
        next_move_col = ranger_col + step_col * moves

        # Movement validity check
        if next_move_col not in range(size) or next_move_row not in range(size):
            # # Show turn if invalid movement:
            # for row in board:
            #     print(" ".join(row))
            # print("invalid move")
            # print()
            continue

        # Skip movement command if field location is unavailable
        if board[next_move_row][next_move_col] != ".":
            continue

        # board[next_move_row][next_move_col] = "A" # Show turn new position visualization
        # board[ranger_row][ranger_col] = "."   # Remove old position visualization

        # Move Shooter
        ranger_row = next_move_row
        ranger_col = next_move_col

    if action == "shoot":
        # Initialize shooting direction
        new_target_row = ranger_row + step_row
        new_target_col = ranger_col + step_col

        # Now shoot
        while True:
            # Stop shooting if out of range
            if new_target_col not in range(size) or new_target_row not in range(size):
                break

            if board[new_target_row][new_target_col] == "x":    # Target found
                board[new_target_row][new_target_col] = "."     # Target removed
                # board[new_target_row][new_target_col] = "#"   # Target destroyed visualization
                targets_left.remove((new_target_row, new_target_col))   # Remove from targets list
                targets_hit.append([new_target_row, new_target_col])    # Remember destroyed target location
                break
            else:   # Continue bullet path
                # board[new_target_row][new_target_col] = "*"   # Bullet path visualization
                new_target_row += step_row
                new_target_col += step_col

    # # Show turn:
    # for row in board:
    #     print(" ".join(row))
    # print()

# # Debug targets:
# print(f"targets_left:{targets_left}")
# print(f"targets_hit:{targets_hit}")

if targets_left:
    print(f"Training not completed! {len(targets_left)} targets left.")
else:
    print(f"Training completed! All {len(targets_hit)} targets hit.")
for target in targets_hit:
    print(target)
