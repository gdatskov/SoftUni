entry_num = input()
elements = set()
for _ in range(int(entry_num)):
    entry = input().split()
    elements.update(entry)
[print(x) for x in elements]