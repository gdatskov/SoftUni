import sys

entry_range = int(input())

total_sum = 0
max_number = -sys.maxsize

for number in range(entry_range):
    entry_number = int(input())
    total_sum += entry_number
    if entry_number > max_number:
        max_number = entry_number

if total_sum-max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number-(total_sum-max_number))}")