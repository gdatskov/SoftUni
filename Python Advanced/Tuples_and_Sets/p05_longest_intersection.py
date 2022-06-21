longest_set = set()
for ss in range(int(input())):
    a, b = input().split("-")
    start_a, end_a = map(int, a.split(","))
    start_b, end_b = map(int, b.split(","))
    set_a = set(range(start_a, end_a+1))
    set_b = set(range(start_b, end_b+1))
    current_intersection = set_b.intersection(set_a)
    if len(current_intersection) > len(longest_set):
        longest_set = current_intersection

print(f"Longest intersection is {list(longest_set)} with length {len(longest_set)}")