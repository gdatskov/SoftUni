from collections import deque

ramen_bowls = [int(x) for x in input().split(", ")]
customer_list = deque([int(x) for x in input().split(", ")])

while ramen_bowls and customer_list:
    ramen = ramen_bowls.pop()
    customer = customer_list.popleft()

    if ramen > customer:
        ramen -= customer
        ramen_bowls.append(ramen)
    elif customer > ramen:
        customer -= ramen
        customer_list.appendleft(customer)

if not customer_list:
    print("Great job! You served all the customers.")
    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen_bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customer_list)}")
