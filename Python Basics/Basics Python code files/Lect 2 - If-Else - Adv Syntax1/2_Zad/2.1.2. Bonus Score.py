starting_points = int(input())
bonus_points = 0

if starting_points <= 1000:
    if starting_points <= 100:
        bonus_points += bonus_points + 5
    elif starting_points > 100:
        bonus_points += bonus_points + starting_points*0.2
else:
    bonus_points += bonus_points + starting_points*0.1

if (starting_points % 2) == 0:
    bonus_points = bonus_points + 1

if (starting_points % 10) == 5:
    bonus_points = bonus_points + 2

total_points = starting_points + bonus_points

print(bonus_points)
print(total_points)
