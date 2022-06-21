usernames = []

for user in range(int(input())):
    usernames.append(input())

print("\n".join(set(usernames)))