entry = input()
task_list = entry.split("|")
energy = 100
coins = 100
gained_energy = int
success = True
for event in task_list:
    event_list = event.split("-")
    action = event_list[0]
    benefit = int(event_list[1])
    if action == "rest":
        current_energy = energy
        energy += benefit
        if energy > 100:
            energy = 100
            gained_energy = energy - current_energy
        else:
            gained_energy = benefit
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif action == "order":
        if energy >= 30:
            coins += benefit
            energy -= 30
            print(f"You earned {benefit} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= benefit:
            coins -= benefit
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            success = False
            break
if success:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
