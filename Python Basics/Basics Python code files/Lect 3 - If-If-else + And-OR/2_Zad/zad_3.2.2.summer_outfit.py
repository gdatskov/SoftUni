degrees = int(input())
day_time = input()

Outfit = ""
Shoes = ""

if 10 <= degrees <= 18:
    if day_time == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    if day_time == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    if day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
if 18 < degrees <= 24:
    if day_time == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    if day_time == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    if day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
if degrees >= 25:
    if day_time == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    if day_time == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    if day_time == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")