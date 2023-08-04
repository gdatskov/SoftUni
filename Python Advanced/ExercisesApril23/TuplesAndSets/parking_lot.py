input_number = int(input())

lot = set()

for _ in range(input_number):
    direction, plate_num = input().split(", ")
    if direction == "IN":
        lot.add(plate_num)
    else:
        lot.discard(plate_num)

if len(lot) == 0:
    print("Parking Lot is Empty")
else:
    for car in lot:
        print(car)