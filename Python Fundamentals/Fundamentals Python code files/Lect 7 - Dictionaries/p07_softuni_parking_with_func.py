def parking_status(entry_lines):
    registered = {}
    for _ in range(entry_lines):
        entry = input()
        entry = entry.split(" ")
        command = entry[0]
        username = entry[1]
        if command == "register":
            plate = entry[2]
            if username not in registered:
                registered[username] = plate
                print(f"{username} registered {plate} successfully")
            else:
                print(f"ERROR: already registered with plate number {plate}")
        if command == "unregister":
            if username in registered:
                registered.pop(username)
                print(f"{username} unregistered successfully")
            else:
                print(f"ERROR: user {username} not found")
    return registered


entry_number = int(input())
registered_parks = parking_status(entry_number)

for parks in registered_parks:
    print(f"{parks} => {registered_parks[parks]}")
