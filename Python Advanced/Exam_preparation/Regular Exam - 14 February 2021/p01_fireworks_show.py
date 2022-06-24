from collections import deque

fireworks = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0,
}

effects_list = deque(int(x) for x in input().split(", "))
power_list = list(int(x) for x in input().split(", "))

while any(x < 3 for x in fireworks.values()) and effects_list and power_list:
    if effects_list[0] <= 0:
        effects_list.popleft()
        continue
    if power_list[-1] <= 0:
        power_list.pop()
        continue
    current_effect = effects_list.popleft()
    current_power = power_list.pop()
    current_sum = current_power + current_effect
    if current_sum % 3 == 0 and current_sum % 5 != 0:
        fireworks["Palm"] += 1
    elif current_sum % 3 != 0 and current_sum % 5 == 0:
        fireworks["Willow"] += 1
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks["Crossette"] += 1
    else:
        effects_list.append(current_effect - 1)
        power_list.append(current_power)


if all(x >= 3 for x in fireworks.values()):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if effects_list:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects_list)}")
if power_list:
    print(f"Explosive Power left: {', '.join(str(x) for x in power_list)}")
for key, value in fireworks.items():
    print(f"{key} Fireworks: {value}")
