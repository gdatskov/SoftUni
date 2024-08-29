from collections import deque

# entry = '{[()[]{}]({})}'
# entry = '{[(])[]]}'
# entry = '[{[()[]]}'
entry = input()
# print(entry)

parenteses_list = deque(entry)

closing_brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
}

full_lenght = len(entry)
half_lenght = int(full_lenght/2)

for _ in range(half_lenght):
    open_bracket = parenteses_list.popleft()
    working_list = deque()
    opened = 1
    index_to_del = None
    for next_bracket_index in range(len(parenteses_list)):
        next_bracket = parenteses_list[next_bracket_index]
        if next_bracket == open_bracket:
            opened += 1
        if next_bracket == closing_brackets[open_bracket]:
            if opened == 1:
                # Match found
                index_to_del = next_bracket_index
                break
            else:
                # Match not found
                opened -= 1
    if index_to_del is not None:
        del parenteses_list[index_to_del]
    else:
        break
if parenteses_list:
    print('NO')
else:
    print('YES')











