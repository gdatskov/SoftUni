array = [int(x) for x in input().strip().split(" ")]

while True:
    command = input().strip()
    if command == "end":
        break
    if command != "decrease":
        operation, index1, index2 = command.split(" ")
        index1, index2 = int(index1), int(index2)
    else:
        operation = command
    if operation == "swap":
        array[index1], array[index2] = array[index2], array[index1]
    if operation == "multiply":
        array[index1] = array[index1] * array[index2]
    if operation == "decrease":
        array = [x-1 for x in array]

print(", ".join(str(x) for x in array))
