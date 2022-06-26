days = int(input())
players = int(input())
energy = float(input())
water_per_player_per_day = float(input())
food_per_player_per_day = float(input())
water = water_per_player_per_day * players * days
food = food_per_player_per_day * players * days

for day in range(1, days+1):
    energy -= float(input())
    if energy <= 0:
        break
    if day % 2 == 0:
        energy *= 1.05
        water *= 0.7
    if day % 3 == 0:
        food = food - food/players
        energy *= 1.1

if energy > 0:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")



