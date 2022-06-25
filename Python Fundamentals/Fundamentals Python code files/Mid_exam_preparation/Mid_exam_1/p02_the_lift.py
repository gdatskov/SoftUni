from collections import deque

people = int(input())
wagons = deque([int(x) for x in input().split(" ")])


for _ in range(len(wagons)):
    current_wagon = wagons.popleft()
    empty_seats = 4 - current_wagon
    if people >= empty_seats:
        current_wagon += empty_seats
        people -= empty_seats
    else:
        current_wagon += people
        people = 0
    wagons.append(current_wagon)

if any(x < 4 for x in wagons) and not people:
    print("The lift has empty spots!")
if people:
    print(f"There isn't enough space! {people} people in a queue!")
print(" ".join(str(x) for x in wagons))
