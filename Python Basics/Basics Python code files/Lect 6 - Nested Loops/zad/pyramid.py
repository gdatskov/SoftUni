entry = int(input())
current = 1
col = 1

while current <= entry:
    col += 1
    row = 1
    while col-row != 0 : #and current <= entry
        print(current, end=" ")
        row += 1
        current += 1
    print()