def right_down(row, col, end_row, end_col, recursion, count):
    if row > end_row or col > end_col:
        return
    if row == end_row and col == end_col:
        count.append(1)

    right_down(row+1, col, end_row, end_col, recursion, count)
    right_down(row, col+1, end_row, end_col, recursion, count)

    return len(count)


rows = int(input())
columns = int(input())

print(right_down(0, 0, rows-1, columns-1, 0, []))
