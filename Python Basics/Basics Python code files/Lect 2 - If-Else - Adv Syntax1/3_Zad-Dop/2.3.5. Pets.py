import math

days = int(input())
food_start = float(input())
dogfood_per_day = float(input())
catfood_per_day = float(input())
turtlefood_per_day = float(input())/1000

total_food_needed = days*(dogfood_per_day+catfood_per_day+turtlefood_per_day)

if total_food_needed <= food_start:
    print(f"{math.floor(food_start-total_food_needed)} kilos of food left.")
else:
    print(f"{math.ceil(total_food_needed-food_start)} more kilos of food are needed.")
