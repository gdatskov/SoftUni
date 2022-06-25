won = 0
end = False
energy = int(input())

while True:
    command = input()
    if command == "End of battle":
        end = True
        break
    distance = int(command)
    if energy >= distance:
        won += 1
        energy -= distance
        if won % 3 == 0:
            energy += won
    else:
        print(f"Not enough energy! Game ends with {won} won battles and {energy} energy")
        break

if end:
    print(f"Won battles: {won}. Energy left: {energy}")