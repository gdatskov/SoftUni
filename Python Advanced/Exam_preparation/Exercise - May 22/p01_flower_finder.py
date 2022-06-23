from collections import deque

vowels = deque(input().split(" "))
consonants = deque(input().split(" "))

flowers = {
    "rose": list("rose"),
    "tulip": list("tulip"),
    "lotus": list("lotus"),
    "daffodil": list("daffodil"),
}

word_found = False

while vowels and consonants:
    vo = vowels.popleft()
    co = consonants.pop()

    for name, letters in flowers.items():
        while vo in letters:
            letters.remove(vo)
        while co in letters:
            letters.remove(co)
        if not letters:
            word_found = True
            print(f"Word found: {name}")

    if word_found:
        break


if not word_found:
    print("Cannot find any word!")
if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
