entry = input()

while True:
    command_line = input()
    if command_line == "End":
        break
    command_line = command_line.split(" ")

    if command_line[0] == "Translate":
        command, char, replacement = command_line
        entry =entry.replace(char, replacement)
        print(entry)

    if command_line[0] == "Includes":
        command, substring = command_line
        print(substring in entry)

    if command_line[0] == "Start":
        command, substring = command_line
        print(entry.startswith(substring))

    if command_line[0] == "Lowercase":
        entry = entry.lower()
        print(entry)

    if command_line[0] == "FindIndex":
        command, char = command_line
        print(entry.rindex(char))

    if command_line[0] == "Remove":
        start_index, count = [int(x) for x in command_line[1:]]
        end_index = start_index + count
        entry = entry[:start_index] + entry[end_index:]
        print(entry)
