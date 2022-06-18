hour = int(input())
day_of_week = input()

open_or_closed = ""

if hour < 10 or hour > 18 or day_of_week == "Sunday":
    open_or_closed = "closed"
else:
    open_or_closed = "open"

print(open_or_closed)

# hour = int(input())
# day_of_week = input()
#
# # open_or_closed = ""
#
# if 10 <= hour <= 18:
#     if day_of_week == "Monday":
#         open_or_closed = "open"
#     elif day_of_week == "Tuesday":
#         open_or_closed = "open"
#     elif day_of_week == "Wednesday":
#         open_or_closed = "open"
#     elif day_of_week == "Thursday":
#         open_or_closed = "open"
#     elif day_of_week == "Friday":
#         open_or_closed = "open"
#     elif day_of_week == "Saturday":
#         open_or_closed = "open"
#     else:
#         open_or_closed = "closed"
# else:
#     open_or_closed = "closed"
#
# print(open_or_closed)
