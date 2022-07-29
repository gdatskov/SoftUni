def insertion_sort(numbers):
    for idx in range(1, len(numbers)):
        is_sorted = True
        curr_num = numbers[idx]
        for curr_idx in range(idx, 0, -1):
            prev_num = numbers[curr_idx - 1]
            if curr_num < prev_num:
                is_sorted = False
                numbers[curr_idx - 1], numbers[curr_idx] = numbers[curr_idx], numbers[curr_idx - 1]
            if is_sorted:
                break
    return numbers


numbers = [int(x) for x in input().split(" ")]
print(*insertion_sort(numbers), sep=" ", end="")