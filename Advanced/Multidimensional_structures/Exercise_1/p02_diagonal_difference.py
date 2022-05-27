matrix = list()
primary_diag = list()
secondary_diag = list()
matrix_size = int(input())
for rows in range(matrix_size):
    matrix.append(list(map(int, input().split(" "))))
    primary_diag.append(matrix[rows][rows])
    secondary_diag.append(matrix[rows][matrix_size-rows-1])

print(abs(sum(primary_diag) - sum(secondary_diag)))
