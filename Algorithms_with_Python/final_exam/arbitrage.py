# class CurrencyConvert:
#     def __init__(self, from_curr, to_curr, rate):
#         self.from_curr = from_curr
#         self.to_curr = to_curr
#         self.rate = rate
from collections import deque

graph = {}

pairs_number = int(input())
for _ in range(pairs_number):
    from_curr, to_curr, rate = input().split()
    if from_curr not in graph.keys():
        graph[from_curr] = {to_curr: int(rate)}

target = input()
queue = deque([target])
value = 1
while queue:
    node = queue.popleft()
    for child in graph[node]:
        queue.append(child)
