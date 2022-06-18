budget = float(input())
season = input()

destination = ""
spent_money = 0
accommodation = "Home"

if budget <= 100:
    destination = "Bulgaria"
elif budget <= 1000:
    destination = "Balkans"
elif budget > 1000:
    destination = "Europe"
else:
    destination = "Home"

if season == "summer":
    if destination == "Bulgaria":
        spent_money = budget * 0.3
        accommodation = "Camp"
    if destination == "Balkans":
        spent_money = budget * 0.4
        accommodation = "Camp"
    if destination == "Europe":
        spent_money = budget * 0.9
        accommodation = "Hotel"

if season == "winter":
    if destination == "Bulgaria":
        spent_money = budget * 0.7
    if destination == "Balkans":
        spent_money = budget * 0.8
    if destination == "Europe":
        spent_money = budget * 0.9
    accommodation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation} - {spent_money:.2f}")