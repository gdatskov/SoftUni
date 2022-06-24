board = []
size = 6
balls = 3
bucket_list = []
points = 0

for i in range(size):
    row = input().split(" ")
    board.append(row)
    for j in range(size):
        if row[j] == "B":
            bucket_list.append((i, j))

while balls:
    throw_coordinates = eval(input())
    balls -= 1
    if throw_coordinates in bucket_list:
        throw_row, throw_col = throw_coordinates
        bucket_list.remove(throw_coordinates)
        for rr in range(size):
            value = board[rr][throw_col]
            if value.isdigit():
                points += int(value)


if points >= 300:
    prize = "Lego Construction Set"
elif points >= 200:
    prize = "Teddy Bear"
elif points >= 100:
    prize = "Football"
else:
    prize = ""

if prize:
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
