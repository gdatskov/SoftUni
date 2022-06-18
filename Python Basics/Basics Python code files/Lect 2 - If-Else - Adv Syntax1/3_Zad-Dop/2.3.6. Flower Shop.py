import math

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.5
cacti_price = 8

taxes = 0.05

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

income = (magnolias*magnolias_price + hyacinths*hyacinths_price + roses_price*roses +
          cacti*cacti_price)*(1-taxes)

if income >= gift_price:
    print(f"She is left with {math.floor(income-gift_price):.0f} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price-income):.0f} leva.")