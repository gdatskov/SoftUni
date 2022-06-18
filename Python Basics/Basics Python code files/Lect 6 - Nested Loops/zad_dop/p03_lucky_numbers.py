entry_number = int(input())

for digit1 in range(1, 9 + 1):
    for digit2 in range(1, 9 + 1):
        for digit3 in range(1, 9 + 1):
            for digit4 in range(1, 9 + 1):
                if digit1 + digit2 == digit3 + digit4:
                    if entry_number % (digit1 + digit2) == 0:
                        print(f"{digit1}{digit2}{digit3}{digit4}", end=" ")
