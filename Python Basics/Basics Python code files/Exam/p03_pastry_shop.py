pastry = input()
order_count = int(input())
day = int(input())

pastry_cost = 0

if day <= 15:
    if pastry == "Cake":
        pastry_cost = 24
    elif pastry == "Souffle":
        pastry_cost = 6.66
    elif pastry == "Baklava":
        pastry_cost = 12.6

if day > 15:
    if pastry == "Cake":
        pastry_cost = 28.7
    elif pastry == "Souffle":
        pastry_cost = 9.8
    elif pastry == "Baklava":
        pastry_cost = 16.98

total_cost = pastry_cost * order_count
# Additional discounts:

if day <= 22:
    if 100 <= total_cost <= 200:
        total_cost = total_cost*0.85
    elif total_cost > 200:
        total_cost = total_cost * 0.75

if day <= 15:
    total_cost = total_cost * 0.9

print(f"{total_cost:.2f}")
