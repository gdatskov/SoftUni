elements_n = set()
elements_m = set()

n, m = map(int, input().split(" "))

for _ in range(n):
    elements_n.add(int(input()))
for _ in range(m):
    elements_m.add(int(input()))

[print(el) for el in elements_n.intersection(elements_m)]