def solution():
    def integers():
        result = 0
        # lis = []
        while True:
            result += 1
            # print(result)
            yield result

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)

# Sample input

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

# Expected output
# [0.5, aug_22.0, aug_22.5, 2.0, 2.5]