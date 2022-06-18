months = int(input())

sum_electricity = 0

for period in range(months):
    electricity = float(input())
    sum_electricity += electricity

sum_water = months * 20
sum_internet = months * 15
sum_other = (sum_internet+sum_water+sum_electricity) * 1.2
sum_total = sum_other+sum_water+sum_electricity+sum_internet
average = sum_total / months

print(f"Electricity: {sum_electricity:.2f} lv")
print(f"Water: {sum_water:.2f} lv")
print(f"Internet: {sum_internet:.2f} lv")
print(f"Other: {sum_other:.2f} lv")
print(f"Average: {average:.2f} lv")
