company_name = input()
adult_tickets = int(input())
kid_tickets = int(input())
net_price_adult = float(input())
services_price = float(input())

agency_profit = ((net_price_adult*0.3 + services_price)*kid_tickets + (net_price_adult + services_price)*adult_tickets)*0.2

print(f"The profit of your agency from {company_name} tickets is {agency_profit:.2f} lv.")
