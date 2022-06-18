from collections import deque


def valid_parentheses(dd):
    valid_parentheses_types = ["(", ")", "[", "]", "{", "}"]
    for i in dd:
        if i not in valid_parentheses_types:
            return False
    return True


def closing_parentheses(s):
    if s == "(":
        return ")"
    if s == "[":
        return "]"
    if s == "{":
        return "}"
    return s


def even_list(dd):
    return True if len(dd) % 2 == 0 else False


def empty(dd):
    return True if len(dd) == 0 else False


def balanced(dd):
    open_parenthesis = ["(", "[", "{"]

    if not even_list(dd) or not valid_parentheses(dd) or empty(dd):
        return False

    if dd[0] not in open_parenthesis:
        return False

    counter = int(len(dd)/2)
    while counter and dd:
        current_sym = dd.popleft()
        next_sym = dd[0]
        if closing_parentheses(current_sym) == next_sym and current_sym in open_parenthesis:
            dd.popleft()
            counter = len(dd)
        else:
            dd.append(current_sym)
            counter -= 1

    return False if dd else True


lis = deque(input())

if balanced(lis):
    print("YES")
else:
    print("NO")
