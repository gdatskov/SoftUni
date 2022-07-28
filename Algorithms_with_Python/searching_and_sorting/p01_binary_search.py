def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle = int((right - left)/2) + left
        if numbers[middle] == target:
            return middle
        if target > numbers[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


nums = [int(x) for x in input().split(" ")]
tgt = int(input())
result = binary_search(nums, tgt)
print(result)

#
# res = binary_search([1, 2, 3, 4, 5], 1)
# # res = binary_search([-1, 0, 1, 2, 4], 4)
# print(res)