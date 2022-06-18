number_of_pairs = int(input())
previous_sum_of_pair = 0
previous_difference = 0
current_difference = 0
difference = False
max_diff = 0
sum_of_pair = 0

for pairs in range (number_of_pairs):
    number1 = int(input())
    number2 = int(input())
    sum_of_pair = number1 + number2
    if pairs == 0:
        previous_sum_of_pair = sum_of_pair
    if sum_of_pair != previous_sum_of_pair:
        current_difference = abs(sum_of_pair-previous_sum_of_pair)
    if pairs == 0:
        previous_difference = current_difference
    if current_difference != previous_difference:
        max_diff = abs(current_difference-previous_difference)
        difference = True
    previous_sum_of_pair = sum_of_pair


if difference:
    print(f"No, maxdiff={max_diff}")
else:
    print(f"Yes, value={sum_of_pair}" )

