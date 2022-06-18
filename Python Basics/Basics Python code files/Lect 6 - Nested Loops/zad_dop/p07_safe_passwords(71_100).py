number1 = int(input())
number2 = int(input())
max_generations = int(input())

# generate max_generations consecutive times a string of type ABxyBA, where
# if A > 55, reset A = 35(ASCII)
# if B > 96, reset B = 64(ASCII)
# x := (1, number1)
# y := (1, number2)

start_A = 35
start_B = 64
changed_A = start_A
changed_B = start_B
counter = 0

for x in range(1, number1 + 1):
    for y in range(1, number2 + 1):
        counter += 1
        if counter > max_generations:
            break
        print(f"{chr(changed_A)}{chr(changed_B)}{x}{y}{chr(changed_B)}{chr(changed_A)}", end="|")
        changed_A += 1
        changed_B += 1
        if changed_A > 55:
            changed_A = start_A
        if changed_B > 96:
            changed_B = start_A
