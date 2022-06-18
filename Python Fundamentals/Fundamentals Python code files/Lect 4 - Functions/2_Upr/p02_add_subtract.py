def add_and_subtract(a, b, c):

    # def sum_numbers():
    #     return a + b
    #
    # def subtract():
    #     return sum_numbers() - c

    sum_numbers = lambda: a+b
    subtract = lambda: sum_numbers() - c

    print(subtract())


sh = int(input())
t = int(input())
b = int(input())

add_and_subtract(sh, t, b)

# v = int(input())
# g = int(input())
# z = int(input())
#
# add_and_subtract(v, g, z)
