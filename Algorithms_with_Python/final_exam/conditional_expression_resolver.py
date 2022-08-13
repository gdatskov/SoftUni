entry = input()
entry_list = entry.split()

# print(entry_list)


# print("true", true_result)
# print("fal", false_result)
# print("con", condition)

middle_idx = len(entry_list) // 2
result = entry_list[middle_idx]

while len(entry_list) >= 5:
    middle_idx = len(entry_list) // 2
    true_result = result
    false_result = entry_list[middle_idx + 2]
    condition = entry_list[middle_idx - 2]

    if condition == "t":
        result = true_result
    else:
        result = false_result

    entry_list[middle_idx+2] = result
    entry_list = entry_list[:middle_idx-2] + entry_list[middle_idx+2:]
    # print(entry_list)

# print(entry_list[len(entry_list) // 2])
print(result)
