from math import ceil

entry = input()
entry_list = [int(num) for num in entry.split(", ")]

max_number_in_entry = max(entry_list)

for group in range(ceil(max_number_in_entry/10)):
    current_10s_list = list(filter(lambda x: group*10 < x <= (group+1)*10, entry_list))
    print(f"Group of {(group+1)*10}'s: {current_10s_list}")
