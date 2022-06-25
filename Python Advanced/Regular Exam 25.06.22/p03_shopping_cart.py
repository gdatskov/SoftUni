def shopping_cart(*args):
    cart = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }

    max_products ={
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2,
    }

    result = []

    for x in args:
        if x == "Stop":
            break

        key, value = x

        if len(cart[key]) < max_products[key] and value not in cart[key]:
            cart[key].append(value)

    for key, value in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{key}:")
        for item in sorted(value):
            result.append(f" - {item}")

    if any(cart.values()):
        return "\n".join(result)
    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
