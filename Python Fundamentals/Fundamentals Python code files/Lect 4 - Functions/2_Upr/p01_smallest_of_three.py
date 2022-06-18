def smallest_of_three():
    number_list = []
    for number in range(3):
        number_list.append(int(input()))
    smallest = min(number_list)
    return smallest


print(smallest_of_three)
