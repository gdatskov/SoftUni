matrix_rows, matrix_columns = [int(x) for x in input().split(" ")]
matrix = list()
max_sum = -20*3*3
best_submatrix_start_index = tuple
submatrix = []

for rows in range(matrix_rows):
    row_entry = input().split()
    matrix.append(list(map(int, row_entry)))

for row in range(matrix_rows-2):
    for col in range(matrix_columns-2):
        current_sum = 0
        for row_num in range(row, row+3):
            for col_num in range(col, col+3):
                current_sum += matrix[row_num][col_num]
        if current_sum > max_sum:
            max_sum = current_sum
            best_submatrix_start_index = (row, col)
print(f"Sum = {max_sum}")

if best_submatrix_start_index:
    best_row, best_col = best_submatrix_start_index
    for row in range(best_row, best_row+3):
        submatrix_row = []
        for col in range(best_col, best_col+3):
            submatrix_row.append(str(matrix[row][col]))
        print(" ".join(submatrix_row))
