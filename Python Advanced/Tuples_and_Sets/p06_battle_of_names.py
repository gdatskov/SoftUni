odd_set = set()
even_set = set()

for n in range(1, int(input()) + 1):
    current_sum = 0

    for x in input():
            current_sum += ord(x)

    current_result = current_sum // n

    if current_result % 2 == 0:
        even_set.add(current_result)
    else:
        odd_set.add(current_result)

if sum(odd_set) == sum(even_set):
    final_set = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    final_set = odd_set.difference(even_set)
else:
    final_set = odd_set.symmetric_difference(even_set)

final_set = list(final_set)
print(", ".join(str(x) for x in final_set))