eleset = set()
for el in range(int(input())):
    [eleset.add(x) for x in input().split(" ")]
print("\n".join(eleset))
