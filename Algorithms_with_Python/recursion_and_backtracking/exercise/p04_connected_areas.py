def find_area(row, col, end_row, end_col, matrix, lib, current_area, recursion):

    if recursion == 0 and matrix[row][col] == "*":
        bad_start = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "-":
                    row, col = i, j
                    bad_start = False
                    break
            if not bad_start:
                break

    recursion += 1

    if not 0 <= row <= end_row or not 0 <= col <= end_col:
        return

    if matrix[row][col] == "*" or matrix[row][col] == "x":
        return

    matrix[row][col] = "x"
    lib[current_area].append((row, col))

    find_area(row+1, col, end_row, end_col, matrix, lib, current_area, recursion)
    find_area(row-1, col, end_row, end_col, matrix, lib, current_area, recursion)
    find_area(row, col+1, end_row, end_col, matrix, lib, current_area, recursion)
    find_area(row, col-1, end_row, end_col, matrix, lib, current_area, recursion)

    recursion -= 1

    if recursion <= 0:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row, col = i, j
                if matrix[i][j] == "-":
                    current_area += 1
                    lib.append([])
                    find_area(row, col, end_row, end_col, matrix, lib, current_area, recursion+1)

        if row == end_row and col == end_col:
            lib = sorted(lib, key=lambda x: ( -len(x), x[0][0], x[0][1] ) )
            print(f"Total areas found: {len(lib)}")
            for ll in range(len(lib)):
                print(f"Area #{ll+1} at {lib[ll][0]}, size: {len(lib[ll])} ")
            return


area = []
rows = int(input())
columns = int(input())

for _ in range(rows):
    area.append(list(input()))

find_area(0, 0, rows - 1, columns - 1, area, [[]], 0, 0)
