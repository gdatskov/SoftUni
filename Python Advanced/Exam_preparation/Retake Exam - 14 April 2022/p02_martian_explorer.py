rover_row, rover_col = 0, 0
terrain = []
size = 6

for i in range(size):
    row = input().split(" ")
    terrain.append(row)
    for j in range(len(row)):
        if row[j] == "E":
            rover_row, rover_col = i, j

commands = list(input().split(", "))

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

deposits = {
    "W": [],
    "M": [],
    "C": [],
}

decipher = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete",
}

for order in commands:
    terrain[rover_row][rover_col] = "-"
    move_row, move_col = movement[order]
    rover_row += move_row
    rover_col += move_col
    if not 0 <= rover_row < size:
        rover_row = (size + rover_row) % size
    if not 0 <= rover_col < size:
        rover_col = (size + rover_col) % size
    if terrain[rover_row][rover_col] == "R":
        print(f"Rover got broken at {rover_row, rover_col}")
        break
    if terrain[rover_row][rover_col] != "-":
        deposits[terrain[rover_row][rover_col]].append((rover_row, rover_col))
        print(f"{decipher[terrain[rover_row][rover_col]]} deposit found at {rover_row, rover_col}")

suitable = True
for typ, deposit in deposits.items():
    if len(deposit) < 1:
        suitable = False

if suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

# [print(" ".join(x)) for x in terrain]