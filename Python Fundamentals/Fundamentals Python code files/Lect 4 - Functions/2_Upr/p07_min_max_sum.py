sequence_list = (input().split(" "))

number_list = []
for item in sequence_list:
    number_list.append(int(item))

minimum_num = min(number_list)
maximum_num = max(number_list)
sum_num = sum(number_list)
print(f"The minimum number is {minimum_num}")
print(f"The maximum number is {maximum_num}")
print(f"The sum number is: {sum_num}")
