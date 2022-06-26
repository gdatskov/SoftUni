"""
The possible commands are:
"Add {value}"
"Remove {value}"
"Replace {value} {replacement}"
"Collapse {value}"
"Finish"

Example input 1:
1 4 5 19
Add 1
Remove 4
Finish

Expected output 1:
1 5 19 1


Example input 2:
1 20 -1 10
Collapse 8
Finish

Expected output 2:
20 10


Example input 3:
5 9 70 -56 9 9
Replace 9 10
Remove 9
Finish

Expected output 3:
5 10 70 -56 9
"""

numbers = input().strip().split(" ")

while True:

    input_line = input().strip().split(" ")
    command = input_line[0]

    if command == "Finish":
        break

    if command == "Add":
        command, value = input_line
        numbers.append(value)

    if command == "Remove":
        command, value = input_line
        numbers.remove(value)

    if command == "Replace":
        command, value, replacement = input_line
        for element in range(len(numbers)):
            if numbers[element] == value:
                numbers[element] = replacement
                break

    if command == "Collapse":
        command, value = input_line
        numbers = [x for x in numbers if int(x) >= int(value)]

print(" ".join(str(x) for x in numbers))
