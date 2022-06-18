end_number = int(input())
start_number = int(input())
stop_number = int(input())

for number in range(start_number, end_number - 1, -1):
    if number % 2 == 0 and number % 3 == 0:
        if number == stop_number:
            break
        else:
            print(f"{number}", end=" ")
