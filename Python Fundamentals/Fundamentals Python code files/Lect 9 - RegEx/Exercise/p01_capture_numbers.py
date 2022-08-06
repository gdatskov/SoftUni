import re

text = input()
while text:
    numbers = re.findall(r"\d+", text)
    for num in numbers:
        print(num, end=" ")
    text = input()

