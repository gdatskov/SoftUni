import math
area = int(input())
production_coef = float(input())
needed_wine = int(input())
workers = int(input())

grapes_for_wine = area*production_coef*0.4
wine = grapes_for_wine/2.5

if wine < needed_wine:
    print(f"It will be a tough winter! More {math.floor(needed_wine-wine)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(wine-needed_wine)} liters left -> "
          f"{math.ceil((wine-needed_wine)/workers)} liters per person.")
