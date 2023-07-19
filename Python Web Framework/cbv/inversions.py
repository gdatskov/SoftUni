arr = [0, 2, 5, 9, 7, 1, 6, 3, 8, 4]
inversion_count = 0
len_arr = len(arr)
for i in range(len_arr):
    print(f"current: {arr[i]}")
    for j in range(i, len_arr):
        if arr[i] > arr[j]:
            print(f"added: {(arr[i], arr[j])}")
            inversion_count += 1

print(f"Total inversions: {inversion_count}")
