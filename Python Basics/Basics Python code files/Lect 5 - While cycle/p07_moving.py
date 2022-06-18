width = int(input())
length = int(input())
height = int(input())
room = width*length*height

while room >= 0:
    boxes = input()
    if boxes == "Done":
        print(f"{room} Cubic meters left.")
        break
    room -= int(boxes)
    if room <= 0:
        print(f"No more free space! You need {-room} Cubic meters more.")

