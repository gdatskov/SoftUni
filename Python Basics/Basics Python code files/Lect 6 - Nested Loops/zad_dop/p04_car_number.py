start_number = int(input())
end_number = int(input())

for n1 in range(start_number, end_number + 1):
    for n2 in range(start_number, end_number + 1):
        for n3 in range(start_number, end_number + 1):
            for n4 in range(start_number, end_number + 1):
                sum_second_third = n2 + n3
                if sum_second_third % 2 == 0:
                    if n1 > n4:
                        if (n1 % 2 == 0 and n4 % 2 != 0) or (n1 % 2 != 0 and n4 % 2 == 0):
                            print(f"{n1}{n2}{n3}{n4}", end=" ")


# Решение при въвеждане на четирицифрени номера от начален номер - до краен номер
# for plate in range(start_number, end_number + 1):
#     string_of_plate = str(plate)
#     n1 = int(string_of_plate[0])
#     n2 = int(string_of_plate[1])
#     n3 = int(string_of_plate[2])
#     n4 = int(string_of_plate[3])
#     sum_second_third = n2 + n3
#     if sum_second_third % 2 == 0:
#         if n1 > n4:
#             if (n1 % 2 == 0 and n4 % 2 != 0) or (n1 % 2 != 0 and n4 % 2 == 0):
#                 print(plate)

