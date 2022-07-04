def loop(array, idx):
    if idx == len(array):
        print(*matrix, sep=" ")
        return

    for x in range(len(array)):
        matrix[idx] = x + 1
        loop(array, idx + 1)


number = int(input())
matrix = [0] * number
loop(matrix, 0)