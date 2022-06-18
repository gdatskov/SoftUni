number_limit_1 = int(input())
number_limit_2 = int(input())
number_limit_3 = int(input())

for number_1 in range(1, number_limit_1 + 1):
    if number_1 % 2 == 0 and number_1 < 10:
        for number_2 in (2, 3, 5, 7):
            if number_2 <= number_limit_2:
                for number_3 in range(1, number_limit_3 + 1):
                    if number_3 % 2 == 0 and number_3 < 10:
                        print(f"{number_1} {number_2} {number_3}")
