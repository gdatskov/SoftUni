game_on = True
free_chairs = 0
rooms = int(input())

for room in range(rooms):

    entry = input()
    chairs = entry.count("X")

    if "-" in entry:
        game_on = False
        continue

    entry_list = entry.split(" ")
    visitors = int(entry_list[1])

    if chairs >= visitors:
        free_chairs += chairs - visitors
    else:
        game_on = False
        needed_chairs = visitors - chairs
        print(f"{needed_chairs} more chairs needed in room {room+1}")

if game_on and rooms > 0:
    print(f"Game On, {free_chairs} free chairs left")
