products = dict()

entry = input()

while entry != "buy":

    product_info = entry.split(" ")

    name = product_info[0]
    price = float(product_info[1])
    quantity = int(product_info[2])

    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity

    entry = input()


for prod in products:
    price = products[prod][0]
    quantity = products[prod][1]
    total_price = quantity * price

    print(f"{prod} -> {total_price:.2f}")
