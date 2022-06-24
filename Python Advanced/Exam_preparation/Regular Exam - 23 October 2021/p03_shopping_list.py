def shopping_list(kinti, **kwargs):
    products_bought = {}
    if kinti < 100:
        return "You do not have enough budget."
    for product in kwargs.keys():
        price, quantity = [float(x) for x in kwargs[product]]
        if kinti >= price * quantity >= 0:
            products_bought[product] = price * quantity
            kinti -= price * quantity
        if len(products_bought) == 5 or not kinti:
            break
    text = [
        f"You bought {product_name} for {total_price:.2f} leva."
        for product_name, total_price in products_bought.items()
    ]
    return "\n".join(text)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print()
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


