# Problem definition:
"""
Create a program that will receive commands until the command "End". The commands can be:
•	"Create-{file_name}" - Creates the given file with an empty content. If the file already exists,
    remove the existing text in it (as if the file is created again)
•	"Add-{file_name}-{content}" - Append the content and a new line after it.
    If the file does not exist, create it, and add the content
•	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string
    with the new string. If the file does not exist, print: "An error occurred"
•	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
"""

# Input example:
"""
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End
"""

# Expected output:
"""
The first command creates the empty file
After the first and second Add command, the content is:
First Line
Second Line
On the first Replace command, an error must occur
After the next two Replace commands, the content is:
1st Line
2nd Line
After the first Delete command, an error occurs
Finally, the 'file.txt' file is deleted
"""

# Imports:
from collections import deque
from os import remove

# Function definition:
def create(file_name):
    with open(f"./{file_name}", "w") as ff:
        print(f"""
A new blank file named "{file_name}" has been created in current program folder.
If it already existed, it has been overwritten and any existing data has been lost.
""")


def add(file_name, tt):
    with open(f"./{file_name}", "a") as ff:
        for t in tt:
            ff.write(t + "\n")
        print(f"""
The text string(s) [{', '.join(tt)}] have been added each on a new line 
to the file "{file_name}" in the current program folder.
""")


def replace(file_name, *args):
    old, new = args

    # Try if the file exists:
    try:
        # Open and read file, replace what is needed and put it in a temporary file. Line by line.
        with open(f"./{file_name}", "r") as ff:
            with open(f"./{file_name}_temp.txt", "a") as temp:
                while True:
                    line = ff.readline()
                    if line == "":
                        break
                    line = line.replace(old, new)
                    temp.write(line)

        # Open temporary file, rewrite original file and delete temporary file. Line by line.
        with open(f"./{file_name}", "w") as ff:
            with open(f"./{file_name}_temp.txt", "r") as temp:
                while True:
                    line = temp.readline()
                    if line == "":
                        break
                    ff.write(line)
            remove(f"./{file_name}_temp.txt")

        print(f"""
The text "{old}" have been replaced with "{new}" on all occurrences 
in the file "{file_name}" in the current program folder.
""")

    except FileNotFoundError:   # If the file doesn't exist:
        print(f'An error occurred: The file "{file_name}" does not exist.' + "\n")


def delete(file_name):
    try:
        remove(f"./{file_name}")
        print(f"""
The file named "{file_name}" has been deleted.
""")
    except FileNotFoundError:
        print(f'An error occurred: The file "{file_name}" does not exist.' + "\n")


# Execution code:
while True:
    command_list = deque(input("Please enter a command: ").split("-"))

    if command_list[0] == "End":
        break

    # It could be done with list indexes, but I love popping left :D
    command, file, text = command_list.popleft(), command_list.popleft(), command_list

    if command == "Create":
        create(file)

    if command == "Add":
        add(file, text)

    if command == "Replace":
        replace(file, *text)

    if command == "Delete":
        delete(file)

    continue
