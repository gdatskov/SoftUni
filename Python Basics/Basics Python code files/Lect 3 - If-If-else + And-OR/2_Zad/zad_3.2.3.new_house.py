flowers = input()
number = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcis_price = 3
gladiola_price = 2.5

price = 0

if flowers == "Roses":
    price = rose_price
    if number > 80:
        price = price*0.9
if flowers == "Dahlias":
    price = dahlia_price
    if number > 90:
        price = price*0.85
if flowers == "Tulips":
    price = tulip_price
    if number > 80:
        price = price*0.85
if flowers == "Narcissus":
    price = narcis_price
    if number < 120:
        price = price*1.15
if flowers == "Gladiolus":
    price = gladiola_price
    if number < 80:
        price = price*1.20

total_price = price*number

if total_price <= budget:
    print(f"Hey, you have a great garden with {number} {flowers} and {budget-total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price-budget:.2f} leva more.")