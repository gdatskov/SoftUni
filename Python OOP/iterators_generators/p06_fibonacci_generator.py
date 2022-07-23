def fibonacci():
    fib1 = 0
    fib2 = 1
    yield fib1
    yield fib2

    while True:
        fib3 = fib1 + fib2
        yield fib3
        fib1, fib2 = fib2, fib3

generator = fibonacci()
for i in range(5):
    print(next(generator))

# print(next(generator))

