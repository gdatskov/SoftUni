price = 0
discount = False

while True:
    command = input()
    if command == "regular":
        break
    if command == "special":
        discount = True
        break
    if float(command) > 0:
        price += float(command)
    else:
        print("Invalid price!")
        continue

if discount:
    discount = 0.9
else:
    discount = 1

if price == 0:
    print("Invalid order!")
else:
    print(
        f"""Congratulations you've just bought a new computer!
        Price without taxes: {price:.2f}$
        Taxes: {price*0.2:.2f}$
        -----------
        Total price: {price*discount*1.2:.2f}$
        """)