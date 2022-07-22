class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration
        to_return = self.step * self.iterations
        self.iterations += 1
        return to_return





numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print()
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
print()
numbers = take_skip(1, 1)
for number in numbers:
    print(number)
