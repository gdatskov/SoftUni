from collections import deque
# 3 2 5 2 6 8 4
def merge_arrays(arr1, arr2):
    result_arr = [None] * (len(arr1) + len(arr2))
    arr1_idx = 0
    arr2_idx = 0
    res_idx = 0

    while arr1_idx < len(arr1) and arr2_idx < len(arr2):
        if arr1[arr1_idx] < arr2[arr2_idx]:
            result_arr[res_idx] = arr1[arr1_idx]
            arr1_idx += 1
        else:
            result_arr[res_idx] = arr2[arr2_idx]
            arr2_idx += 1
        res_idx += 1

    while arr1_idx < len(arr1):
        result_arr[res_idx] = arr1[arr1_idx]
        arr1_idx += 1
        res_idx += 1

    while arr2_idx < len(arr2):
        result_arr[res_idx] = arr2[arr2_idx]
        arr2_idx += 1
        res_idx += 1

    return result_arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr) // 2
    first_arr = arr[:mid_idx]
    second_arr = arr[mid_idx:]
    one = merge_sort(first_arr)
    two = merge_sort(second_arr)
    return merge_arrays(one, two)


numbers = [int(x) for x in input().split(" ")]
print(*merge_sort(numbers), sep=" ", end="")
