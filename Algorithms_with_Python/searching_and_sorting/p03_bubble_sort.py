def bubble_sort(numbers):
    for itr in range(len(numbers) - 1):
        is_sorted = True
        for idx in range(len(numbers) - 1 - itr):
            if numbers[idx] > numbers[idx + 1]:
                numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
                is_sorted = False
        if is_sorted:
            break
    return numbers


numbers = [int(x) for x in input().split(" ")]
print(*bubble_sort(numbers), sep=" ", end="")
