decorations_per_shopping = int(input())
days_left = int(input())
money = 0
spirit = 0
ornament = 2
skirt = 5
garland = 3
lights = 15

current_day = 1
cat_factor = 1
# days_left -= 1
while days_left > 0:
    if current_day % 11 == 0:
        decorations_per_shopping += 2
    if current_day % 2 == 0:
        money += ornament*decorations_per_shopping
        spirit += 5
    if current_day % 3 == 0:
        money += (skirt+garland)*decorations_per_shopping
        spirit += (3+10)
    if current_day % 5 == 0:
        money += lights*decorations_per_shopping
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20         #CAT ATTACK!
        money += skirt+garland+lights
        # spirit += 3+10+17
        if days_left == 1:
            spirit -= 30
    current_day += 1
    days_left -= 1

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
