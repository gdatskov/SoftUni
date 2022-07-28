def selection_sort(numbers: list):
    for start_idx in range(len(numbers)):
        min_idx = start_idx
        for idx in range(start_idx + 1, len(numbers)):
            next_idx = idx
            if numbers[min_idx] > numbers[next_idx]:
                min_idx = next_idx
        numbers[start_idx], numbers[min_idx] = numbers[min_idx], numbers[start_idx]
    return numbers


numbers = [int(x) for x in input().split(" ")]
print(" ".join(str(x) for x in selection_sort(numbers)))
