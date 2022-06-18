budget = int(input())
season = input()
fishermen = int(input())

boat = 0

if season == "Spring":
    boat = 3000
elif season == "Winter":
    boat = 2600
else:
    boat = 4200

discount = 1

if fishermen <= 6:
    discount = 0.9
elif 7 <= fishermen <= 11:
    discount = 0.85
elif 12 <= fishermen:
    discount = 0.75

cost_with_discount = boat*discount

if fishermen % 2 == 0 and season != "Autumn":
    cost_with_discount = cost_with_discount*0.95

if budget >= cost_with_discount:
    print(f"Yes! You have {budget-cost_with_discount:.2f} leva left.")
elif budget <= cost_with_discount:
    print(f"Not enough money! You need {cost_with_discount-budget:.2f} leva.")

