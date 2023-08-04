guests_num = int(input())

guests = set()

for _ in range(guests_num):
    guests.add(input())

while True:
    visitor = input()
    if visitor == "END":
        break
    guests.discard(visitor)

print(len(guests))

for guest in sorted(guests):
    print(guest)