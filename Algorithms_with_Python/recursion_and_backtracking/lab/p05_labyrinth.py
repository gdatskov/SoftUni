def read_lab():
    rows = int(input())
    columns = int(input())
    lab = []
    for _ in range(rows):
        lab.append(list(input()))
    return lab


def find_paths(row, col, direction, lab, path):

    if not 0 <= row < len(lab) or not 0 <= col < len(lab[0]):
        return

    if lab[row][col] == "*":
        return

    if lab[row][col] == "v":
        return

    path.append(direction)

    if lab[row][col] == "e":
        print(*path, sep="")
        path.pop()
        return

    lab[row][col] = "v"

    find_paths(row+1, col, "D", lab, path)
    find_paths(row-1, col, "U", lab, path)
    find_paths(row, col+1, "R", lab, path)
    find_paths(row, col-1, "L", lab, path)

    path.pop()
    lab[row][col] = "-"


lab = read_lab()
find_paths(0, 0, "", lab, [])