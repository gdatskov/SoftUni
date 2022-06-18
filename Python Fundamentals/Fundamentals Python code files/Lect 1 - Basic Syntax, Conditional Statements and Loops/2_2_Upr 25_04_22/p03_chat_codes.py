# •	If the number is 88 - "Hello"
# •	If the number is 86 - "How are you?"
# •	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
# •	If the number is over 88 - "Bye."


entries = int(input())
for inputs in range(entries):
    entry = int(input())
    if entry == 88:
        print("Hello")
    elif entry == 86:
        print("How are you?")
    elif entry < 88:
        print("GREAT!")
    else:
        print("Bye.")

