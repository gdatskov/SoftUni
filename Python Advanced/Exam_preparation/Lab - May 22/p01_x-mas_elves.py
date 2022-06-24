"""
Each elf make toy from given materials
Given - list of elves energy
Given - list of materials
TODO: elves energy used, toys successfuly made
First Elf picks last box of materials and tries to make a toy:

while elves and materials:
    if materials  >= elf energy:
        toy += 1 -> go to santa bag
        elf energy -= materials
        energy spent += materials
        elf + cookie = elf energy + 1
        append(elf) = popleft(elf)
    else:
        dont pick materials
        elf + hot choco = 2 * elf energy
        append(elf) = popleft(elf)

    if count elf % 3 == 0:
        if 2 x materials >= elf energy
            toy += 2
            elf energy -= 2 x mats
            energy spent += materials
            elf + cookie = elf energy + 1
            append(elf) = popleft(elf)
        else:
            dont pick materials
            elf + hot choco = 2 * elf energy
            append(elf) = popleft(elf)

    if count elf % 5 == 0 and % 3 == 0:
        if materials >= elf energy
            toy += 0
            elf energy -= mats
            energy spent += materials
            elf + no cookie = elf energy + 0
            append(elf) = popleft(elf)
        else:
            dont pick materials
            elf + hot choco = 2 * elf energy
            append(elf) = popleft(elf)

    if elf energy < 5:
        elf is retired
"""
from collections import deque

elves = deque(int(x) for x in input().split(" "))
materials = list(int(x) for x in input().split(" "))
toys = 0
energy_spent = 0
count = 0

while elves and materials:
    elf_energy = elves.popleft()

    if elf_energy < 5:
        continue

    current_box = materials.pop()
    required_energy = current_box
    count += 1

    production = 1  # 0 = Fail, 1 = Normal, 2 = Double

    if count % 3 == 0:
        required_energy *= 2
        production = 2

    if count % 5 == 0:
        production = 0

    if elf_energy >= required_energy:
        toys += production
        energy_spent += required_energy
        elf_energy -= required_energy
        if production:
            elf_energy += 1     # Cookie reward
    else:
        elf_energy *= 2     # Elf drinks hot chocolate
        materials.append(current_box)

    elves.append(elf_energy)

print(f"Toys: {toys}")
print(f"Energy: {energy_spent}")

if elves:
    print(f"Elves left: {', '.join(map(str, elves))}")

if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")

