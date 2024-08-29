first_set_len, second_set_len = input().split(' ')
first_set = {int(input()) for _ in range(int(first_set_len))}
second_set = {int(input()) for _ in range(int(second_set_len))}
[print(x) for x in first_set.intersection(second_set)]



