initial_food = int(input())*1000
adopted = False
total_rations = 0
while not adopted:
    daily_rations = input()
    if daily_rations == "Adopted":
        adopted = True
        if total_rations <= initial_food:
            print(f"Food is enough! Leftovers: {initial_food-total_rations} grams.")
        else:
            print(f"Food is not enough. You need {total_rations-initial_food} grams more." )
        continue
    total_rations += int(daily_rations)

