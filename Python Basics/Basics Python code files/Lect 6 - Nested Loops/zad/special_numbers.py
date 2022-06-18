entry_number = int(input())
for r1 in range(1, 9+1):
    if entry_number % r1 == 0:
        for r2 in range(1, 9+1):
            if entry_number % r2 == 0:
                for r3 in range(1, 9+1):
                    if entry_number % r3 == 0:
                        for r4 in range(1, 9+1):
                            if entry_number % r4 == 0:
                                print(f"{r1}{r2}{r3}{r4}",end=" ")

