orders = int(input())
total = 0

for order in range(orders):

    capsule_price = float(input())
    days = int(input())
    capsules_count = int(input())

    if not 0.01 <= capsule_price <= 100 or not 1 <= days <=31 or not 1 <= capsules_count <= 2000:
        continue

    total_month = capsules_count*capsule_price*days
    print(f"The price for the coffee is: ${total_month:.2f}")
    total += total_month

print(f"Total: ${total:.2f}")
