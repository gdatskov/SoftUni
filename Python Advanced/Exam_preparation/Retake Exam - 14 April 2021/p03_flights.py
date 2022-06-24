from collections import deque


def flights(*args):
    dic = dict()
    queue = deque(args)
    while True:
        key = queue.popleft()
        if key == "Finish":
            break
        value = queue.popleft()
        if key not in dic.keys():
            dic[key] = value
        else:
            dic[key] += value
    return dic


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print()
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print()
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))