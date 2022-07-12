def tribonacci(number):
    lis = [1, 1, 2]
    for i in range(2, number-1):
        lis.append(sum(lis[len(lis)-3:]))
    return " ".join(map(str, lis[:number]))


print(tribonacci(int(input())))