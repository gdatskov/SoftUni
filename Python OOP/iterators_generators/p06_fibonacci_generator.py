def fibonacci():
    fib = [0, 1]
    for i in range(2):
        yield fib[i]
    while True:
        fib.append(fib[-1]+fib[-2])
        yield fib[-1]

generator = fibonacci()
for i in range(11):
    print(next(generator))

# print(next(generator))

