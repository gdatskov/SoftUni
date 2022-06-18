from string import ascii_lowercase
ijk = int(input())
for i in range(ijk):
    for j in range(ijk):
        for k in range(ijk):
            print(f"{ascii_lowercase[i]}{ascii_lowercase[j]}{ascii_lowercase[k]}")
