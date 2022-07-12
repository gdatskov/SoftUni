# list = [1, 2, 3, 4, 5, 6]
#
# print(sum(list[3:]))

def tribonacci_sequence(number):
    list = [1]
    list_copy = list.copy()

    while len(list) < number:
        list.append(sum(list_copy))
        list_copy.append(sum(list))
        list_copy.pop(0)
        while len(list) > 3:
            list.append(sum(list[len(list) - 3:]))
            if len(list) == number:
                break

    s = [str(integer) for integer in list]
    tribonacci_sequence_numbers = " ".join(s)
    return tribonacci_sequence_numbers


number = int(input())
print(tribonacci_sequence(number))