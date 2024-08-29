num_entries = int(input())
longest_intersection = set()
for _ in range(num_entries):
    first_range, second_range = input().split('-')

    first_start, first_end = map(int, first_range.split(','))
    second_start, second_end = map(int, second_range.split(','))

    first_set = set(range(first_start, first_end+1))
    second_set = set(range(second_start, second_end+1))

    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

intersection_string = ', '.join(map(str, longest_intersection))
print(f'Longest intersection is [{intersection_string}] with length {len(longest_intersection)}')
