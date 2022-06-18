def collect_info(entry_data):

    products = dict()

    while entry_data != "buy":

        product_info = entry_data.split(" ")

        name = product_info[0]
        price = float(product_info[1])
        quantity = int(product_info[2])

        if name not in products:
            products[name] = [price, quantity]
        else:
            products[name][0] = price
            products[name][1] += quantity

        entry_data = input()

    return products


def print_info(info_dict):
    for prod in info_dict:
        price = info_dict[prod][0]
        quantity = info_dict[prod][1]
        total_price = quantity * price

        print(f"{prod} -> {total_price:.2f}")


entry = input()

info = collect_info(entry)

print_info(info)


