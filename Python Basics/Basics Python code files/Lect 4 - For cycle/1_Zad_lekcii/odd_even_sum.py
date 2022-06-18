count_of_numbers = int(input())

left_side_sum = 0
right_side_sum = 0

for number in range(count_of_numbers):
    if number%2 == 0:
        left_side_sum += int(input())
    else:
        right_side_sum += int(input())

if left_side_sum == right_side_sum:
    print("Yes")
    print(f"Sum = {right_side_sum}")
else:
    print("No")
    print(f"Diff = {abs(right_side_sum-left_side_sum)}")