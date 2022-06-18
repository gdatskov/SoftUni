entry = input()
number_list = []
for i in range(len(entry)):
    number_list.append(int(entry[i]))

for i in range(len(number_list)):
    print(f"{max(number_list)}", end="")
    number_list.remove(max(number_list))
