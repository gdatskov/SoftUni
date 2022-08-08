food_limit = {}
living_area = {}

while True:
    command_line = input()
    if command_line == "EndDay":
        break
    command, info = command_line.split(": ")
    if command == "Add":
        name, needed_food, area = info.split("-")
        if name not in food_limit.keys():
            food_limit[name] = int(needed_food)
            living_area[name] = area
        else:
            food_limit[name] += int(needed_food)
            living_area[name] = area
    if command == "Feed":
        name, food = info.split("-")
        if name in food_limit.keys():
            food_limit[name] -= int(food)
            if food_limit[name] <= 0:
                del food_limit[name]
                del living_area[name]
                print(f"{name} was successfully fed")

hungry_animals_by_area = {}
for animal, area in living_area.items():
    if area not in hungry_animals_by_area.keys():
        hungry_animals_by_area[area] = [animal]
    else:
        hungry_animals_by_area[area].append(animal)

print("Animals:")
for name in food_limit.keys():
    print(f" {name} -> {food_limit[name]}g")

print("Areas with hungry animals:")
for area in hungry_animals_by_area.keys():
    print(f" {area}: {len(hungry_animals_by_area[area])}")
