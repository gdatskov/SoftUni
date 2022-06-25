targets = [int(x) for x in input().strip().split(" ")]

while True:

    line = input()

    if line == "End":
        break

    command, idx, power = line.strip().split(" ")
    idx = int(idx)
    power = int(power)

    valid = True if 0 <= idx < len(targets) else False

    if command == "Shoot" and valid:

        targets[idx] -= power

        if targets[idx] <= 0:
            targets.remove(targets[idx])

    if command == "Add":

        if valid:
            targets.insert(idx, power)
        else:
            print("Invalid placement!")

    if command == "Strike":

        start_index, end_index = idx - power, idx + power

        if all(0 <= x < len(targets) for x in range(start_index, end_index+1)):

            for _ in range(start_index, end_index+1):
                targets.remove(targets[start_index])

        else:

            print("Strike missed!")

print("|".join(str(x) for x in targets))


