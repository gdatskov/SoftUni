legendary = False
inventory = {"shards" : 0, "fragments" : 0, "motes" : 0}
# valid_list = ["shards", "fragments", "motes"]
rewards = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

while not legendary:

    entry = input().lower()

    entry_list = list(entry.split(" "))

    for stuff in range(0, len(entry_list), 2):

        quantity_index = stuff
        item_index = stuff+1
        quantity = int(entry_list[quantity_index])
        item = entry_list[item_index]

        if item not in inventory.keys():
            inventory[item] = quantity
        else:
            inventory[item] += quantity

        if inventory[item] >= 250 and item in rewards:
            legendary = True
            inventory[item] -= 250
        #     if item == "shards":
        #         print("Shadowmourne obtained!")
        #     if item == "fragments":
        #         print("Valanyr obtained!")
        #     if item == "motes":
        #         print("Dragonwrath obtained!")
            print(f"{rewards[item]} obtained!")

            break


for item in inventory.keys():
    print(f"{item}: {inventory[item]}")
