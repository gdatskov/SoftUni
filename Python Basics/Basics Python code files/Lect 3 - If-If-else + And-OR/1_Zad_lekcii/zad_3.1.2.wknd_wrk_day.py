day_of_week = input()

day_type = ""

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
    day_type = "Working day"
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    day_type = "Weekend"
else:
    day_type = "Error"

print(day_type)
