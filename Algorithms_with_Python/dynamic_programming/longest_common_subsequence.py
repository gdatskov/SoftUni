first_seq = input()
second_seq = input()

rows = len(first_seq) + 1
columns = len(second_seq) + 1

dp = []
[dp.append([0] * columns) for _ in range(rows)]

# algo
for row in range(1, rows):
    for col in range(1, columns):
        if first_seq[row - 1] == second_seq[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[rows - 1][columns - 1])

# print
row = rows - 1
col = columns - 1
result = []

while row > 0 and col > 0:
    if first_seq[row - 1] == second_seq[col - 1]:
        result.append(first_seq[row - 1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(list(reversed(result)))
