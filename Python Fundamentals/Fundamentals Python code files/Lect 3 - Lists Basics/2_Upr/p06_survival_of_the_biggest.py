import sys

numbers = input()
n = int(input())
numbers_list = numbers.split(" ")

for i in range(n):
    min_number = sys.maxsize
    for j in numbers_list:
        if int(j) < min_number:
            min_number = int(j)
    numbers_list.remove(str(min_number))

print(", ".join(numbers_list))
