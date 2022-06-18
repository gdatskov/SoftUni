N = int(input())
P = int(input())
count = 0
while N > 0:
    count += 1
    N -= P
print(count)
