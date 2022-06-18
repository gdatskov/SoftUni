price_baggage_over_20 = float(input())    #lv
weight = float(input())     #[kg]
days_left = int(input())
bag_number = int(input())
calc_price = price_baggage_over_20
if weight < 10:
    calc_price = calc_price*0.2
elif 10 <= weight <= 20:
    calc_price = calc_price*0.5
if days_left > 30:
    calc_price = calc_price*1.1
elif 7 <= days_left <= 30:
    calc_price = calc_price*1.15
else:
    calc_price = calc_price*1.4
total_price = calc_price * bag_number
print(f"The total price of bags is: {total_price:.2f} lv. ")
