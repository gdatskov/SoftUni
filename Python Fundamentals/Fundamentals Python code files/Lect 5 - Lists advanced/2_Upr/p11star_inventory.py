inventory = input().split(", ")
command = input()

while command != "Craft!":

    command_list = command.split(" - ")
    action = command_list[0]
    item = command_list[1]

    if action == "Collect" and item not in inventory:
        inventory.append(item)

    if action == "Drop" and item in inventory:
        inventory.remove(item)

    if action == "Combine Items":
        swap_list = item.split(":")
        old_item = swap_list[0]
        new_item = swap_list[1]
        if old_item in inventory:
            inventory.insert(inventory.index(old_item)+1, new_item)

    if action == "Renew" and item in inventory:
        inventory.remove(item)
        inventory.append(item)

    command = input()

print(", ".join(inventory))