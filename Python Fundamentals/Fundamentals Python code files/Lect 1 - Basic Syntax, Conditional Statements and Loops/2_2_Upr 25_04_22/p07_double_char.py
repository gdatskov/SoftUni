# You will be given a string. You should print a string in which each character (case-sensitive) is repeated twice.
text = ""
while text != "End":
    text = input()
    if text == "SoftUni" or text == "End":
        continue
    for letter in range(len(text)):
        print(f"{text[letter]}{text[letter]}", end="")
    print()
