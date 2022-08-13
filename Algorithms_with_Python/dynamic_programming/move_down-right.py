from collections import deque

rows = int(input())
columns = int(input())

matrix = []
dp_matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp_matrix.append([0] * columns)

dp_matrix[0][0] = matrix[0][0]

for col in range(1, columns):
    dp_matrix[0][col] = dp_matrix[0][col - 1] + matrix[0][col]

for row in range(1, rows):
    dp_matrix[row][0] = dp_matrix[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, columns):
        dp_matrix[row][col] = max(dp_matrix[row - 1][col], dp_matrix[row][col - 1]) + matrix[row][col]

row = rows - 1
col = columns - 1

path = deque()
while row > 0 and col > 0:
    path.appendleft([row, col])
    if dp_matrix[row][col - 1] >= dp_matrix[row - 1][col]:
        col -= 1
    else:
        row -= 1

while row > 0:
    path.appendleft([row, col])
    row -= 1

while col > 0:
    path.appendleft([row, col])
    col -= 1

path.appendleft([0, 0])
print(*path)
