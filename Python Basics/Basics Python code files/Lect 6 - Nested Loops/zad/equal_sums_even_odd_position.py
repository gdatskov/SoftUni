number1 = int(input())
number2 = int(input())


for x in range(number1, number2 + 1):
    text_of_x = str(x)
    length_of_text_of_x = len(text_of_x)
    sum_odd = 0
    sum_even = 0

    for y in range(length_of_text_of_x):
        digit_y = int(text_of_x[y])
        if y % 2 == 0:
            sum_even += digit_y
        else:
            sum_odd += digit_y

    if sum_odd == sum_even:
        print(x, end= " ")