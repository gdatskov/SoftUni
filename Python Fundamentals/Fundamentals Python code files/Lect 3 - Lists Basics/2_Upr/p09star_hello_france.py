entry = input()
spending_money = float(input())
budget = spending_money
profit = 0
profit_list = []
shop_list = entry.split("|")

for item in shop_list:
    type_pricing = item.split("->")
    item_type = type_pricing[0]
    item_price = float(type_pricing[1])
    if item_type == "Clothes" and item_price <= 50:
        if budget >= item_price:
            budget -= item_price
            profit += item_price*0.4
            profit_list.append(f"{item_price*1.4:.2f}")
    if item_type == "Shoes" and item_price <= 35:
        if budget >= item_price:
            budget -= item_price
            profit += item_price*0.4
            profit_list.append(f"{item_price*1.4:.2f}")
    if item_type == "Accessories" and item_price <= 20.5:
        if budget >= item_price:
            budget -= item_price
            profit += item_price*0.4
            profit_list.append(f"{item_price*1.4:.2f}")

money = spending_money + profit
print(" ".join(profit_list))
print(f"Profit: {profit:.2f}")
if money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

