entry = input()
entry = entry.split("|")
new_list = []
for x in range(len(entry)-1, -1, -1):
    new_list.extend(entry[x].strip().split())
print(" ".join(new_list))
