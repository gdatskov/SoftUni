registered = {}
entry_lines = int(input())

for _ in range(entry_lines):
    entry = input()
    command_list = entry.split(" ")
    command = command_list[0]
    username = command_list[1]
    if command == "register":
        plate = command_list[2]
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


for parks in registered:
    print(f"{parks} => {registered[parks]}")
