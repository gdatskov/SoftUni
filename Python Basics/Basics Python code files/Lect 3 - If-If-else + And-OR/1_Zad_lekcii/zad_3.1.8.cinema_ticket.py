day_of_week = input()

cost = 0

if day_of_week == "Wednesday" or day_of_week == "Thursday":
    cost = 14
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    cost = 16
else:
    cost = 12

print(cost)