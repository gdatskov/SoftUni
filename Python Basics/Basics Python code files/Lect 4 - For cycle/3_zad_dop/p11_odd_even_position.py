import sys
entry_number_count = int(input())
even_min = sys.maxsize
even_max = - sys.maxsize
odd_min = sys.maxsize
odd_max = - sys.maxsize
odd_sum = 0
even_sum = 0
for number_position in range(1, entry_number_count + 1):
    entry_number = float(input())
    if number_position % 2 == 0:
        even_sum += entry_number
        if entry_number < even_min:
            even_min = entry_number
        if entry_number > even_max:
            even_max = entry_number
    else:
        odd_sum += entry_number
        if entry_number < odd_min:
            odd_min = entry_number
        if entry_number > odd_max:
            odd_max = entry_number

print("OddSum=" + f"{odd_sum:.2f},")
if odd_min == sys.maxsize:
    print("OddMin=No,")
else:
    print("OddMin=" + f"{odd_min:.2f},")
if odd_max == - sys.maxsize:
    print("OddMax=No,")
else:
    print("OddMax=" + f"{odd_max:.2f},")
print("EvenSum=" + f"{even_sum:.2f},")
if even_min == sys.maxsize:
    print("EvenMin=No,")
else:
    print("EvenMin=" + f"{even_min:.2f},")
if even_max == - sys.maxsize:
    print("EvenMax=No")
else:
    print("EvenMax=" + f"{even_max:.2f}")
# Всяко число трябва да е форматирано до втория знак след десетичната запетая.
