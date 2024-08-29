from collections import deque

number_pumps = int(input())
pumps_list = deque()

for pump in range(number_pumps):
    pumps_list.append([int(x) for x in input().split(' ')])

for index in range(number_pumps):
    total_fuel = 0
    round_complete = True
    for pump in pumps_list:
        fuel, distance = pump
        total_fuel += fuel
        if total_fuel < distance:
            pumps_list.append(pumps_list.popleft())
            round_complete = False
            break
        else:
            total_fuel -= distance
    if round_complete:
        print(index)
        break




