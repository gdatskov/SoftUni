lis = [str(x) for x in input().strip().split(" ")]

end = False
count = 0
while lis:
    command = input()
    if command == "end":
        end = True
        break
    first_index, second_index = [int(x) for x in command.strip().split(" ")]
    count += 1
    if not all(0 <= x < len(lis) for x in [first_index, second_index]) or first_index == second_index:
        print("Invalid input! Adding additional elements to the board")
        lis.insert(int(len(lis)/2), f"-{count}a")
        lis.insert(int(len(lis)/2), f"-{count}a")
        continue
    first_char = lis[first_index]
    second_char = lis[second_index]
    if first_char == second_char:
        lis.remove(first_char)
        lis.remove(second_char)
        print(f"Congrats! You have found matching elements - {first_char}!")
    else:
        print("Try again!")

if not end:
    print(f"You have won in {count} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(lis))
