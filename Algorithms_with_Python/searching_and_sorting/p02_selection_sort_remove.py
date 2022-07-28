def selection_sort(numbers: list):
    sorted_numbers = []
    while numbers:
        min_number = numbers[0]
        for num in numbers:
            if num < min_number:
                min_number = num
        numbers.remove(min_number)
        sorted_numbers.append(min_number)
    return sorted_numbers


numbers = [int(x) for x in input().split(" ")]
print(" ".join(str(x) for x in selection_sort(numbers)))
