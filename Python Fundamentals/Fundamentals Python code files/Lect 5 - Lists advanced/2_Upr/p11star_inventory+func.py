

def collect_func(item, item_list):
    if item not in item_list:
        item_list.append(item)
    # return item_list


def drop_func(item, item_list):
    if item in item_list:
        item_list.remove(item)
    # return item_list


def combine_func(item, item_list):
    swap_list = item.split(":")
    old_item = swap_list[0]
    new_item = swap_list[1]
    if old_item in item_list:
        item_list.insert(item_list.index(old_item) + 1, new_item)
    # return item_list


def renew_func(item, item_list):
    if item in item_list:
        item_list.remove(item)
        item_list.append(item)
    # return item_list


def action_func(new_command, new_inventory):

    new_inventory = new_inventory.split(", ")

    while new_command != "Craft!":

        command_list = new_command.split(" - ")
        action = command_list[0]
        new_item = command_list[1]

        if action == "Collect":
            collect_func(new_item, new_inventory)

        if action == "Drop":
            drop_func(new_item, new_inventory)

        if action == "Combine Items":
            combine_func(new_item, new_inventory)

        if action == "Renew":
            renew_func(new_item, new_inventory)

        new_command = input()

    # print(", ".join(new_inventory))
    # return new_inventory
    return ", ".join(new_inventory)


inventory = input()
command = input()

# action_func(command, inventory)
# print(", ".join(inventory))
print(action_func(command, inventory))
