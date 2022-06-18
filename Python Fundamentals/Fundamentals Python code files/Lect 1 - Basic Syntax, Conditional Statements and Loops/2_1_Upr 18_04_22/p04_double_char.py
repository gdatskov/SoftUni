# You will be given a string. You should print a string in which each character (case-sensitive) is repeated twice.
text = input()
for letter in range(len(text)):
    print(f"{text[letter]}{text[letter]}", end="")
