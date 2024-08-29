from collections import deque


def append_to_stack(num, the_stack):
    return the_stack.append(int(num))


def pop_from_stack(the_stack):
    if the_stack:
        the_stack.pop()


def print_max(the_stack):
    sorted_stack = sorted(the_stack)
    print(sorted_stack[-1])


def print_min(the_stack):
    sorted_stack = sorted(the_stack)
    print(sorted_stack[0])


stack = []  # init empty list

number = int  # placeholder

operations = {
    '1': append_to_stack,
    '2': pop_from_stack,
    '3': print_max,
    '4': print_min,
}

number_of_lines = int(input())

for _ in range(number_of_lines):
    entry_list = deque(input().split(' '))
    operation = entry_list.popleft()

    if operation == '1':
        number = entry_list.pop()
        operations[operation](number, stack)
    else:
        if stack:
            operations[operation](stack)

reversed_stack = []

while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))


# 4
# 2
# 4
# 3
# 4
