matrix_rows, matrix_columns = [int(x) for x in input().split(" ")]
matrix = list()
matrix_2x2_found = 0
# if matrix_rows == matrix_columns:
for rows in range(matrix_rows):
    row_entry = input().split()
    # if len(row_entry) == matrix_columns:
    matrix.append(row_entry)

for row in range(matrix_rows-1):
    for col in range(matrix_columns-1):
        col_ch = matrix[row][col]
        if col_ch == matrix[row+1][col]:
            if col_ch == matrix[row][col+1]:
                if col_ch == matrix[row+1][col+1]:
                    matrix_2x2_found += 1

print(matrix_2x2_found)
