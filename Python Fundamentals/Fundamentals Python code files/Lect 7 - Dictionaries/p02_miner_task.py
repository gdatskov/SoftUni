some_dic = dict()
while True:
    entry1 = input()
    if entry1 == "stop":
        break
    entry2 = input()
    if entry1 not in some_dic.keys():
        some_dic[entry1] = int(entry2)
    else:
        some_dic[entry1] += int(entry2)
for elem in some_dic:
    print(f"{elem} -> {some_dic[elem]}")
