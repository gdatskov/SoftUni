lilly = int(input())
laundry_machine = float(input())
toy_cost = int(input())
toys_number = 0
money = 0

for age in range(1, lilly+1):
    if age % 2 != 0:
        toys_number += 1
    else:
        money += 10*age/2 - 1

total_money = money + toys_number*toy_cost
if total_money >= laundry_machine:
    print(f"Yes! {total_money-laundry_machine:.2f}")
else:
    print(f"No! {laundry_machine-total_money:.2f}")