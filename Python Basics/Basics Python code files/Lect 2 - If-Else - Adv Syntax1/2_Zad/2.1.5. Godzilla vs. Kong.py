budget = float(input())
extras = int(input())
extra_price = float(input())

decor = budget*0.1

if extras>150:
    extra_price = extra_price*0.9

if extras*extra_price+decor > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget-(extras*extra_price)-decor):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget-(extras*extra_price)-decor:.2f} leva left.")
