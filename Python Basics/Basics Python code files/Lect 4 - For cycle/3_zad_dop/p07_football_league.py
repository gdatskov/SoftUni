capacity = int(input())
total_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0
for fans in range(total_fans):
    sector = input()
    if sector == "A":
        fans_a += 1
    if sector == "B":
        fans_b += 1
    if sector == "V":
        fans_v += 1
    if sector == "G":
        fans_g += 1

print(f"{fans_a/total_fans*100:.2f}%")
print(f"{fans_b/total_fans*100:.2f}%")
print(f"{fans_v/total_fans*100:.2f}%")
print(f"{fans_g/total_fans*100:.2f}%")
print(f"{total_fans/capacity*100:.2f}%")