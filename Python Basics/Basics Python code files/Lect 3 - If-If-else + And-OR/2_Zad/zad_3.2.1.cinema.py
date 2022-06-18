projection = input()
rows = int(input())
columns = int(input())

if projection == "Premiere":
    income = rows*columns*12

if projection == "Normal":
    income = rows*columns*7.5

if projection == "Discount":
    income = rows*columns*5

print(f"{income:.2f}")
