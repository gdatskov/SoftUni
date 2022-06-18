import string

entry = input()
capitals = list(string.ascii_uppercase)
indexes = []
for i in range(len(entry)):
    if entry[i] in capitals:
        indexes.append(i)
print(indexes)
