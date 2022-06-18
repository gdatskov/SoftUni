number_of_joinery = int(input())
joinery_dimension_type = input()
delivery_type = input()
quantity_discount = 0
extra_discount = 0
price_per_unit = 0
delivery = 0

if number_of_joinery >= 10:
    if joinery_dimension_type == "90X130":
        price_per_unit = 110
        if number_of_joinery > 60:
            quantity_discount = 8
        elif number_of_joinery > 30:
            quantity_discount = 5
    if joinery_dimension_type == "100X150":
        price_per_unit = 140
        if number_of_joinery > 80:
            quantity_discount = 10
        elif number_of_joinery > 40:
            quantity_discount = 6
    if joinery_dimension_type == "130X180":
        price_per_unit = 190
        if number_of_joinery > 50:
            quantity_discount = 12
        elif number_of_joinery > 20:
            quantity_discount = 7
    if joinery_dimension_type == "200X300":
        price_per_unit = 250
        if number_of_joinery > 50:
            quantity_discount = 14
        elif number_of_joinery > 25:
            quantity_discount = 9

    if number_of_joinery > 99:
        extra_discount = 4

    if delivery_type == "With delivery":
        delivery = 60

    price = number_of_joinery * price_per_unit
    price_with_discount = price * (1 - quantity_discount / 100)
    price_with_delivery = price_with_discount + delivery
    price_with_extra_discount = price_with_delivery * (1 - extra_discount / 100)

    print(f"{price_with_extra_discount:.2f} BGN")

else:
    print("Invalid order")

