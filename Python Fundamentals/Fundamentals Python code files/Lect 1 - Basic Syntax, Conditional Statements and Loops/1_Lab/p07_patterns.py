max_stars = int(input())
for row in range(max_stars):
    for stars in range(row+1):
        print("*", end="")
    print()
for row in range(max_stars-1, 0, -1):
    for stars in range(row):
        print("*", end="")
    print()