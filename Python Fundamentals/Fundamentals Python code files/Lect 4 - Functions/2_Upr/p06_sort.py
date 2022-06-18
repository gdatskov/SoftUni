# new_list = [1, 231, 32, 2341]
# sorted_list = sorted(new_list, reverse=True)
# print(sorted_list)

sequence_list = (input().split(" "))

number_list = []
for item in sequence_list:
    number_list.append(int(item))

sorted_list = sorted(number_list)
print(sorted_list)
