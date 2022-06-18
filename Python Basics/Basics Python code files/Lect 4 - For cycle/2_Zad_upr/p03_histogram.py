entry_range = int(input())
p1 = p2 = p3 = p4 = p5 = 0

for number in range(entry_range):
    entry_number = int(input())
    if entry_number < 200:
        p1 += 1
    if 200 <= entry_number < 400:
        p2 += 1
    if 400 <= entry_number < 600:
        p3 += 1
    if 600 <= entry_number < 800:
        p4 += 1
    if 800 <= entry_number:
        p5 += 1

print(f"{p1/entry_range*100:.2f}%")
print(f"{p2/entry_range*100:.2f}%")
print(f"{p3/entry_range*100:.2f}%")
print(f"{p4/entry_range*100:.2f}%")
print(f"{p5/entry_range*100:.2f}%")