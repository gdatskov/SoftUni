from collections import deque

petrol_pumps = deque()
first_good_pump = 0

for number_of_pumps in range(int(input())):
    petrol_pumps.append(tuple(int(x) for x in input().split(" ")))

for pump in range(len(petrol_pumps)):
    tank = 0
    current_pump = petrol_pumps.popleft()
    fuel, distance = current_pump
    round_complete = False
    if fuel > distance:
        round_complete = True
        for _ in range(len(petrol_pumps)):
            tank += fuel - distance
            next_pump = petrol_pumps.popleft()
            fuel, distance = next_pump
            petrol_pumps.append(next_pump)
            if tank < 0:
                round_complete = False

    if round_complete:
        first_good_pump = pump
        break
    else:
        petrol_pumps.append(current_pump)

print(first_good_pump)