entry = input()
food = entry.split(", ")
beggars = int(input())
# bounty = list("0"*beggars)
bounty = []
for i in range(beggars):
    bounty.append(0)

while len(food) > 0:
    for beg in range(beggars):
        if len(food) == 0:
            break
        bounty[beg] = int(bounty[beg]) + int(food[0])
        food.remove(food[0])

print(bounty)