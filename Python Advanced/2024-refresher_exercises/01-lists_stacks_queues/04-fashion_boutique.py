box = [int(x) for x in input().split(' ')]
max_capacity = int(input())
curr_capacity = 0
racks = 1 if box else 0
while box:
    clothe = box.pop()
    if curr_capacity + clothe > max_capacity:
        racks += 1
        curr_capacity = 0
    curr_capacity += clothe
print(racks)

