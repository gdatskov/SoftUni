from collections import deque

textiles = deque(map(int, input().split()))  # get 1st
meds = deque(map(int, input().split()))  # get last

backpack = {
    "Bandage": 0,
    "MedKit": 0,
    "Patch": 0
}

while textiles and meds:
    textile = textiles.popleft()
    med = meds.pop()
    result = textile + med
    if result >= 100:
        backpack["MedKit"] += 1
        leftover = result - 100
        if leftover > 0:
            if meds:
                meds.append(meds.pop() + leftover)
            else:
                meds.append(leftover)
    elif result == 40:
        backpack["Bandage"] += 1
    elif result == 30:
        backpack["Patch"] += 1
    else:
        meds.append(med + 10)

if not textiles and not meds:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

sorted_backpack = sorted(backpack.items(), key=lambda x: (-x[1], x[0]))

for item, count in sorted_backpack:
    if count > 0:
        print(f"{item} - {count}")

if meds:
    print("Medicaments left: " + ", ".join(map(str, sorted(meds))))
if textiles:
    print("Textiles left: " + ", ".join(map(str, sorted(textiles, reverse=True))))
