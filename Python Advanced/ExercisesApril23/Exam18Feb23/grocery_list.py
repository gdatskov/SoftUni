def shop_from_grocery_list(budget, grocery_list: list, *products):
    for product, price in products:
        if product in grocery_list:
            if budget >= price:
                grocery_list.remove(product)
                budget -= price
            else:
                break
    if grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    return f"Shopping is successful. Remaining budget: {budget:.2f}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print()

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print()

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))


print(shop_from_grocery_list(
            100,
            ["tomato", "cola", "chips", "meat"],
            ("cola", 5.8),
            ("tomato", 10.0),
            ("meat", 22)))
