fruit = input()
set_size = input()
sets_order = int(input())
booster_price = 0
set_price = 0
if set_size == "small":
    if fruit == "Watermelon":
        booster_price = 56
    if fruit == "Mango":
        booster_price = 36.66
    if fruit == "Pineapple":
        booster_price = 42.10
    if fruit == "Raspberry":
        booster_price = 20
    set_price = booster_price*2
if set_size == "big":
    if fruit == "Watermelon":
        booster_price = 28.70
    if fruit == "Mango":
        booster_price = 19.6
    if fruit == "Pineapple":
        booster_price = 24.8
    if fruit == "Raspberry":
        booster_price = 15.2
    set_price = booster_price*5
total_price = set_price*sets_order
if 400 <= total_price <= 1000:
    total_price = total_price*0.85
elif total_price > 1000:
   total_price = total_price*0.5

print(f"{total_price:.2f} lv.")
