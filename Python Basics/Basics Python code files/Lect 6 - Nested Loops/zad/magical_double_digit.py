start = int(input())
end = int(input())
magical_number = int(input())
count = 0
found = False

for number1 in range(start, end+1):
    for number2 in range(start, end+1):
        count += 1
        if number1+number2 == magical_number:
            print(f"Combination N:{count} ({number1} + {number2} = {magical_number})")
            found = True
            break       # без break изписва всички комбинации на нов ред
    if found:
        break           # без break изписва всички комбинации на нов ред
if not found:
    print(f"{count} combinations - neither equals {magical_number}")