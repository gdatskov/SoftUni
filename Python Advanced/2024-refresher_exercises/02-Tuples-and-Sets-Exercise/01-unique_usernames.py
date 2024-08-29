uniques = set()
name_entries = int(input())

for i in range(name_entries):
    entry = input()
    uniques.add(entry)

[print(x) for x in uniques]

