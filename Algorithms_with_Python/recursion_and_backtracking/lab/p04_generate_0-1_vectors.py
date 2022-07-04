def vec(vector, idx):
    if idx == len(vector):
        print(*vector, sep="")
        return

    for num in range(2):
        vector[idx] = num
        vec(vector, idx + 1)


number = int(input())
vector = [0] * number
vec(vector, 0)