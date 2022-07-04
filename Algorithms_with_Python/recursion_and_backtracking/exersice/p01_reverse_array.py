from collections import deque

array = deque(int(x) for x in input().split(" "))


def rev(arr):
    if len(arr) > 0:
        x = arr.pop()
        rev(arr)
        arr.appendleft(x)
    return " ".join(str(x) for x in arr)


print(rev(array))