area = []
you_row, you_col = 0, 0

collectables = {
    "D": [0, 0],    # [collected, total]
    "G": [0, 0],
    "C": [0, 0],
}


rows, columns = [int(x) for x in input().split(", ")]

for i in range(rows):
    row = input().split(" ")
    area.append(row)
    for j in range(columns):
        if row[j] == "Y":
            you_row, you_col = i, j
        else:
            if row[j] != ".":
                collectables[row[j]][1] += 1

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
christmas = False
while not christmas:
    command = input()

    if command == "End":
        break

    direction, steps = command.split("-")
    steps = int(steps)
    move_row, move_col = movement[direction]

    for _ in range(steps):
        area[you_row][you_col] = "x"
        new_row = (you_row + move_row) % rows
        new_col = (you_col + move_col) % columns
        symbol = area[new_row][new_col]
        if symbol not in [".", "x"]:
            collectables[symbol][0] += 1
        you_row, you_col = new_row, new_col
        area[you_row][you_col] = "Y"

        christmas = True if all(a == b for a, b in collectables.values()) else False
        if christmas:
            print("Merry Christmas!")
            break


print("You've collected:")
print(f"- {collectables['D'][0]} Christmas decorations")
print(f"- {collectables['G'][0]} Gifts")
print(f"- {collectables['C'][0]} Cookies")

for z in range(len(area)):
    print(" ".join(area[z]))
