#import sys

numbers = int(input())

# min_num = sys.maxsize
# max_num = -sys.maxsize

start_number = int(input())

min_num = start_number
max_num = start_number

for n in range(0, numbers-1):
    minmax_entry = int(input())
    if minmax_entry < min_num:
        min_num = minmax_entry
    if minmax_entry > max_num:
        max_num = minmax_entry

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
