entry = input()
entry_list = list(map(int, entry.split(" ")))
target_list = entry_list
command = input()
while command != "End":

    command_list = command.split(" ")
    action = command_list[0]
    target = int(command_list[1])
    effect = int(command_list[2])

    if 0 <= target < len(target_list):
        # and len(target_list) > 0:
        valid = True
    else:
        valid = False

    if action == "Shoot" and valid:
        target_list[target] -= effect
        if target_list[target] <= 0:
            target_list.pop(target)

    if action == "Add":
        if valid:
            target_list.insert(target, effect)
        else:
            print("Invalid placement!")

    if action == "Strike" and valid:
        if 0 <= target-effect <= target+effect < len(target_list):
            for x in range(target-effect, target+effect+1):
                target_list.pop(target-effect)

        #     target_list = target_list[:target-effect] + target_list[target+effect+1:]

        else:
            print("Strike missed!")

    command = input()

final_list = "|".join(list(map(str, target_list)))
print(final_list)
