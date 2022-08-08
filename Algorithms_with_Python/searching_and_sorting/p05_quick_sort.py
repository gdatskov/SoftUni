def quick_sort(start, end, nums):
    if start >= end:
        return

    pivot = start
    lower = start + 1
    higher = end

    while lower <= higher:
        if nums[higher] < nums[pivot] < nums[lower]:
            nums[higher], nums[lower] = nums[lower], nums[higher]
        if nums[lower] <= nums[pivot]:
            lower += 1
        if nums[higher] >= nums[pivot]:
            higher -= 1

    nums[pivot], nums[higher] = nums[higher], nums[pivot]

    quick_sort(0, higher-1, nums)
    quick_sort(lower, end, nums)


numbers = [int(x) for x in input().split(" ")]
quick_sort(0, len(numbers)-1, numbers)
print(numbers)