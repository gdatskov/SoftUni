from math import floor
balls_picked = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0
for balls in range(balls_picked):
    color = input()
    if color == "red":
        red_balls += 1
        points += 5
    elif color == "orange":
        orange_balls += 1
        points += 10
    elif color == "yellow":
        yellow_balls += 1
        points += 15
    elif color == "white":
        white_balls += 1
        points += 20
    elif color == "black":
        black_balls += 1
        points /= 2
    elif color == "":
        other_balls += 0
    else:
        other_balls += 1

print(f"Total points: {floor(points)}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
