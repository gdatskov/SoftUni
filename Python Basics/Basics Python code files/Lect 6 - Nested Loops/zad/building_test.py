floors = int(input())
units_per_floor = int(input())
current_floor = floors
unit_index = ""
while current_floor > 0:
    current_unit = 0
    print()
    if current_floor == floors:
        unit_index = "L"
    elif current_floor % 2 == 0:
        unit_index = "O"
    else:
        unit_index = "A"
    while current_unit < units_per_floor:
        print(f"{unit_index}{current_floor}{current_unit}", end=" ")
        current_unit += 1
    current_floor -= 1