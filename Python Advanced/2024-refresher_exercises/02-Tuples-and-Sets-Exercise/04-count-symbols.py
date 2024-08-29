entry = input()
entry_dict = dict()
for i in range(len(entry)):
    letter = entry[i]
    if letter not in entry_dict.keys():
        entry_dict[letter] = 1
    else:
        entry_dict[letter] += 1

for key in sorted(entry_dict.keys()):
    value = entry_dict[key]
    print(f"{key}: {value} time/s")