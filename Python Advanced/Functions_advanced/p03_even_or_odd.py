def even_odd(*args):
    lis = list(args)
    command = lis.pop()
    even = [x for x in lis if x % 2 == 0]
    odd = [x for x in lis if x % 2 == 1]
    if command == "even":
        return even
    else:
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))