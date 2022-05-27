matrix_rows, matrix_columns = [int(x) for x in input().split(" ")]
matrix = list()
a = 97

for row in range(matrix_rows):
    current_row = []
    for col in range(matrix_columns):
        current_row.append(chr(a + row) + chr(a + row + col) + chr(a + row))

    print(" ".join(map(str, current_row)))
