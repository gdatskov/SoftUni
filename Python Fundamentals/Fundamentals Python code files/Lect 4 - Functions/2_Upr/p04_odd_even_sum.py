# print(list("123412"))
def sort_and_sum(number):
    main_list = list(str(number))
    even_list = []
    odd_list = []
    for digit in main_list:
        digit = int(digit)
        if digit % 2 == 0:
            even_list.append(digit)
        else:
            odd_list.append(digit)
    print(f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}")


sort_and_sum(int(input()))

