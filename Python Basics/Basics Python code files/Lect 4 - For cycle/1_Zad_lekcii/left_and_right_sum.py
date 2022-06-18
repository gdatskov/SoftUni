entry = int(input())

left_side_sum = 0
right_side_sum = 0

for number in range(entry):
        left_side_sum += int(input())

for number in range(entry, entry*2):
        right_side_sum += int(input())

if left_side_sum == right_side_sum:
    print(f"Yes, sum = {right_side_sum}")
else:
    print(f"No, diff = {abs(right_side_sum-left_side_sum)}")