from collections import deque

quantity = int(input())
orders = input().split(' ')
orders = [int(x) for x in orders]

biggest_order = sorted(orders)[-1]
print(biggest_order)

orders = deque(orders)

while orders:
    curr_order = orders[0]
    if quantity >= curr_order:
        orders.popleft()
        quantity -= int(curr_order)
    else:
        result_string = 'Orders left: '
        result_string += ' '.join([str(x) for x in orders])
        print(result_string)
        break
if not orders:
    print("Orders complete")



