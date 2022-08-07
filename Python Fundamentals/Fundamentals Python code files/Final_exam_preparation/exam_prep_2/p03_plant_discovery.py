info_rarity = {}
info_rating = {}
entry_lines = int(input())
for num in range(entry_lines):
    plant = input()
    name, rarity = plant.split("<->")
    info_rarity[name] = rarity
    info_rating[name] = []

while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.split(": ")
    plant_command_info = command[1].split(" - ")
    plant_name = plant_command_info[0]
    if plant_name not in info_rating:
        print("error")
        continue
    if command[0] == "Rate":
        rating = int(plant_command_info[1])
        info_rating[plant_name].append(rating)
    if command[0] == "Update":
        new_rarity = int(plant_command_info[1])
        info_rarity[plant_name] = new_rarity
    if command[0] == "Reset":
        info_rating[plant_name].clear()

print("Plants for the exhibition:")
for plant_name in info_rarity.keys():
    rarity = info_rarity[plant_name]
    rating = info_rating[plant_name]
    average_rating = sum(rating)/len(rating) if rating else 0
    print(f"- {plant_name}; Rarity: {rarity}; Rating: {average_rating:.2f}")
