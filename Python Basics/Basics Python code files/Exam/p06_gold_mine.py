destinations = int(input())

for location in range(destinations):
    expected_average = float(input())
    days = int(input())
    gold_mined_total = 0
    for day in range(days):
        gold_mined = float(input())
        gold_mined_total += gold_mined
    if gold_mined_total/days >= expected_average:
        print(f"Good job! Average gold per day: {gold_mined_total/days:.2f}.")
    else:
        print(f"You need {expected_average - gold_mined_total/days:.2f} gold.")
