array = [int(x) for x in input().split(" ")]


def calc(arr):
    if arr:
        return arr.pop() + calc(arr)
    return 0


print(calc(array))