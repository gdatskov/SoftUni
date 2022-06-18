fire_entry = input()
water_entry = int(input())
fire_list = fire_entry.split("#")
water = water_entry
total_fire = 0
effort = 0
print("Cells:")
for fire in fire_list:
    spit_fire = fire.split(" ")
    firepower = int(spit_fire[2])
    strength = spit_fire[0]
    if strength == "High" and 81 <= firepower <= 125:
        if water >= firepower:
            total_fire += firepower
            effort += firepower*0.25
            water -= firepower
            print(f"- {firepower}")
    if strength == "Medium" and 51 <= firepower <= 80:
        if water >= firepower:
            total_fire += firepower
            effort += firepower*0.25
            water -= firepower
            print(f"- {firepower}")
    if strength == "Low" and 1 <= firepower <= 50:
        if water >= firepower:
            total_fire += firepower
            effort += firepower*0.25
            water -= firepower
            print(f"- {firepower}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


