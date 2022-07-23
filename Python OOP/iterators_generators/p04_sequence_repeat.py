from collections import deque


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = deque(sequence)
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        current_item = self.sequence.popleft()
        self.sequence.append(current_item)
        self.number -= 1
        return current_item


result = sequence_repeat('abc', 5)
# print(next(result))
for item in result:
    print(item, end ='')
