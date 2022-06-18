from os.path import exists
from os import remove

while True:
    command = input()

    if command == "End":
        break

    command_parts = command.split("-")
    command_type, file_name = command_parts[0], command_parts[1]

    if command_type == "Create":
        with open(f"./{file_name}", "w") as file:
            pass

    elif command_type == "Add":
        content = command[2]
        with open(f"./{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command_type == "Replace":
        if not exists(f"./{file_name}"):
            print("An error occurred.")
            continue

        old_string, new_string = command_parts[2], command_parts[3]
        with open(f"./{file_name}", "r+") as file:
            file_content = file.read().replace(old_string, new_string)

            file.seek(0)
            file.truncate()
            file.write(file_content)

    elif command_type == "Delete":
        if not exists(f"./{file_name}"):
            print("An error occurred.")
            continue

        remove(f"./{file_name}")
