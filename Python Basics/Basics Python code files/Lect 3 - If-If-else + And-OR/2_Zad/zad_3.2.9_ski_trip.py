days = int(input())
room = input()
feedback = input()
single = 18
apartment = 25
president = 35
cost = 0

if room == "room for one person":
    cost = single*(days-1)
if room == "apartment":
    cost = apartment*(days-1)
    if days < 10:
        cost = cost * 0.70
    elif days <= 15:
        cost = cost * 0.65
    else:
        cost = cost * 0.50
if room == "president apartment":
    cost = president*(days-1)
    if days < 10:
        cost = cost * 0.90
    elif days <= 15:
        cost = cost * 0.85
    else:
        cost = cost * 0.80

if feedback == "positive":
    cost = cost * 1.25
else:
    cost = cost * 0.9

print(f"{cost:.2f}")