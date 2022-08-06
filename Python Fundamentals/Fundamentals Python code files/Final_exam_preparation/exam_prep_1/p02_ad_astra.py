import re


search_pattern = r"([#|])([A-Za-z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
entry = input()
info = re.findall(search_pattern, entry)

needed_kcal_per_day = 2000
total_kcal = 0

for item in info:
    item_name, exp_date, kcal = item[1:]
    total_kcal += int(kcal)

days_to_last = total_kcal // needed_kcal_per_day

print(f"You have food to last you for: {days_to_last} days!")

for item in info:
    item_name, exp_date, kcal = item[1:]
    print(f"Item: {item_name}, Best before: {exp_date}, Nutrition: {kcal}")