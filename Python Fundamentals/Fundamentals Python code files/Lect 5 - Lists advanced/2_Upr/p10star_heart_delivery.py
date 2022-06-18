
neighborhood = list(map(int, input().split("@")))
jump_entry = input()
house = 0

while jump_entry != "Love!":

    jump = jump_entry.split(" ")
    length = int(jump[1])
    house += length

    if house > len(neighborhood)-1:
        house = 0

    if neighborhood[house] > 0:
        neighborhood[house] -= 2
        if neighborhood[house] == 0:
            print(f"Place {house} has Valentine's day.")
    else:
        print(f"Place {house} already had Valentine's day.")

    jump_entry = input()

failed = len([x for x in neighborhood if x != 0])

print(f"Cupid's last position was {house}.")

if failed == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")