money_for_vacation = float(input())
starting_money = float(input())
current_money = starting_money
count_total = 0
count_bad = 0

while current_money < money_for_vacation:
    if count_bad == 5:
        break
    action = input()
    amount = float(input())
    count_total += 1
    if action == "save":
        current_money += amount
        count_bad = 0
    elif action == "spend":
        count_bad += 1
        current_money = current_money - amount
        if amount >= current_money:
            current_money = 0

if current_money >= money_for_vacation:
    print(f"You saved the money for {count_total} days.")
if count_bad >= 5:
    print(f"You can't save the money.")
    print(f"{count_total}")
