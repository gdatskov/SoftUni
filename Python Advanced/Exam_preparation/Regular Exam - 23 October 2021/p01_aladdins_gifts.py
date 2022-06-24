from collections import deque

materials = list(int(x) for x in input().split(" "))
genie_magic = deque(int(x) for x in input().split(" "))

gemstone = 0
porcelain = 0
gold = 0
diamond = 0

while materials and genie_magic:
    current_material = materials.pop()
    current_magic = genie_magic.popleft()
    product = current_material + current_magic
    success = False
    while not success:
        if 500 > product >= 400:
            diamond += 1
            success = True
        elif 400 > product >= 300:
            gold += 1
            success = True
        elif 300 > product >= 200:
            porcelain += 1
            success = True
        elif 200 > product >= 100:
            gemstone += 1
            success = True
        else:
            if product < 100:
                if product % 2 == 0:
                    product = 2 * current_material + 3 * current_magic
                else:
                    product = 2 * current_material + 2 * current_magic
            if product > 499:
                product /= 2
            if not 100 <= product <= 499:
                break


if (gemstone and porcelain) or (gold and diamond):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if genie_magic:
    print(f"Magic left: {', '.join(str(x) for x in genie_magic)}")
if diamond:
    print(f"Diamond Jewellery: {diamond}")
if gemstone:
    print(f"Gemstone: {gemstone}")
if gold:
    print(f"Gold: {gold}")
if porcelain:
    print(f"Porcelain Sculpture: {porcelain}")
