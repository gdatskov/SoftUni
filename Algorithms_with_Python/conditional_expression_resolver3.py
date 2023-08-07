# Test cases
from collections import deque


def extractor(expression):
    to_wait = ''
    to_solve = ''
    expr_len = len(expression)
    for idx in range(expr_len-1, -1, -1):
        if expression[idx] in ['t', 'f']:
            to_wait = expression[:idx]
            to_solve = expression[idx:]
            break
    return to_wait, to_solve


def solve_ternary(ternary_expression):
    operator, true_value = [x.strip() for x in ternary_expression[0].split('?')]
    false_value = ternary_expression[1].strip()
    return true_value if operator == 't' else false_value


def solver(expression):
    to_wait, to_solve = extractor(expression)
    to_queue = deque()
    to_solve = to_solve.split(':')
    while len(to_solve) > 2:
        to_queue.appendleft(' :' + to_solve.pop())
    result = solve_ternary(to_solve)
    queue = ''.join(to_queue)
    return to_wait + result + queue


def complex_resolver(expression):
    while '?' in expression:
        expression = solver(expression)
    return expression


# Test cases
# print(complex_resolver("t ? 4 : 2"))  # Output: 4
# print(complex_resolver("f ? 4 : 2"))  # Output: 2
# print(complex_resolver("f ? t ? 4 : 2 : 1"))  # Output: 1
# print(complex_resolver("t ? t ? t ? 4 : 1 : 2 : 3"))  # Output: 4
# print(complex_resolver("t ? t ? t ? 4 : 1 : f ? 4 : 2 : 3"))  # Output: 4


input_expression = input()
result = complex_resolver(input_expression)
print(result)