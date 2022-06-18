width = int(input())
height = int(input())
cake = width*height

while cake >= 0:
    cut = input()
    if cut == "STOP":
        print(f"{cake} pieces are left.")
        cake = 0
        break
    cake -= int(cut)
if cake < 0:
    print(f"No more cake left! You need {-cake} pieces more.")
