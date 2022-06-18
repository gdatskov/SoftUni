# #ИЗПЪЛНЕНИЕ СПОРЕД SOFTUNI
start_number = int(input())
end_number = int(input())
number_is_odd = False

for number1 in range(int(str(start_number)[0]), int(str(end_number)[0])+1):
    if number1 % 2 != 0:
        for number2 in range(int(str(start_number)[1]), int(str(end_number)[1])+1):
            if number2 % 2 != 0:
                for number3 in range(int(str(start_number)[2]), int(str(end_number)[2])+1):
                    if number3 % 2 != 0:
                        for number4 in range(int(str(start_number)[3]), int(str(end_number)[3])+1):
                            if number4 % 2 != 0:
                                print(f"{number1}{number2}{number3}{number4}", end=" ")



# ИЗПЪЛНЕНИЕ СПОРЕД ЗАДАНИЕТО !!!

# start_number = int(input())
# end_number = int(input())
# number_is_odd = False
# for number in range(start_number, end_number + 1):
#     number_is_odd = True
#     for check in (str(number)):
#         if int(check) % 2 == 0:
#             number_is_odd = False
#     if number_is_odd:
#         print(f"{number} ")
