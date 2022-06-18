lines = int(input())
liters = 0
capacity = 0
for i in range(lines):
    throughput = int(input())
    capacity += throughput
    if capacity > 255:
        print("Insufficient capacity!")
        capacity -= throughput
        continue
    else:
        liters += throughput
print(liters)
