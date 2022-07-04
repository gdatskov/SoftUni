array = [int(x) for x in input().split(" ")]


def calc(arr, idx):
    if idx < len(arr) - 1:
        return arr[idx] + calc(arr, idx+1)
    return arr[idx]


print(calc(array, 0))