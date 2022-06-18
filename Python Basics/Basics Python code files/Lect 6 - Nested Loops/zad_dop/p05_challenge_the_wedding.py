men = int(input())
women = int(input())
tables = int(input())
count = 0

if tables > 0:
    for m in range(1, men +1):
        for w in range(1, women +1):
            count += 1
            if count > tables:
                break
            print(f"({m} <-> {w})", end=" ")

