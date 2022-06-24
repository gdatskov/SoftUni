from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
pizza_makers = list(int(x) for x in input().split(", "))
total_pizzas_made = 0

while pizza_orders and pizza_makers:
    order = pizza_orders.popleft()
    if not 0 < order <= 10:
        continue
    employee = pizza_makers.pop()
    if order <= employee:
        total_pizzas_made += order
        continue
    if order > employee:
        order_count = order
        order -= employee
        while order > 0 and pizza_makers:
            employee = pizza_makers.pop()
            order -= employee
        if order <= 0:
            total_pizzas_made += order_count
        else:
            pizza_orders.appendleft(order)

if not pizza_orders:
    print(f"""
All orders are successfully completed!
Total pizzas made: {total_pizzas_made}
Employees: {", ".join(str(x) for x in pizza_makers)}
    """)
else:
    print(f"""
Not all orders are completed.
Orders left: {", ".join(str(x) for x in pizza_orders)}
        """)
