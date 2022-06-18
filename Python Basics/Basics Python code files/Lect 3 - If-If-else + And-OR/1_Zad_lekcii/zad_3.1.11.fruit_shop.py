fruit = input()
day_of_week = input()
quantity = float(input())

print_price = 0

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        print_price = 2.5
    if fruit == "apple":
        print_price = 1.2
    if fruit == "orange":
        print_price = 0.85
    if fruit == "grapefruit":
        print_price = 1.45
    if fruit == "kiwi":
        print_price = 2.7
    if fruit == "pineapple":
        print_price = 5.50
    if fruit == "grapes":
        print_price = 3.85
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        print_price = 2.70
    if fruit == "apple":
        print_price = 1.25
    if fruit == "orange":
        print_price = 0.90
    if fruit == "grapefruit":
        print_price = 1.60
    if fruit == "kiwi":
        print_price = 3.00
    if fruit == "pineapple":
        print_price = 5.60
    if fruit == "grapes":
        print_price = 4.2

if print_price == 0 or quantity <= 0:
    print("error")
else:
    print(f"{print_price*quantity:.2f}")
