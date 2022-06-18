
days = int(input())
start_food = float(input())
food_dog = 0
food_cat = 0
food_day3 = 0

for day in range(1, days+1):
    daily_dog = int(input())
    food_dog += daily_dog
    daily_cat = int(input())
    food_cat += daily_cat
    if day % 3 == 0:
        food_day3 += daily_cat+daily_dog

print(f"Total eaten biscuits: {round(food_day3*0.1)}gr.")
print(f"{(food_cat+food_dog)/start_food*100:.2f}% of the food has been eaten.")
print(f"{food_dog/(food_cat+food_dog)*100:.2f}% eaten from the dog.")
print(f"{food_cat/(food_cat+food_dog)*100:.2f}% eaten from the cat.")
