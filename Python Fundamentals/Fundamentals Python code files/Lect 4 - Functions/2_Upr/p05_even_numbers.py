def even_numbers(number_in_sequence):
    if number_in_sequence % 2 == 0:
        return True
    return False


sequence_list = (input().split(" "))

number_list = []
for item in sequence_list:
    number_list.append(int(item))

filtered_list = list(filter(even_numbers, number_list))

print(filtered_list)

