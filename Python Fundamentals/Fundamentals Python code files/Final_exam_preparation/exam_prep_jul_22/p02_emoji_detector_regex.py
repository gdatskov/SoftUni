

test_str = "In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, " \
           "12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**"

test_str2 = "5, 4, 3, 2, 1, go! The 1-th consecutive banana-eating contest has begun!" \
            " ::Joy:: **Banana** ::Wink:: **Vali** ::valid_emoji::"

test_str3 = "It is a long established fact that 1 a reader will be distracted by 9 the readable " \
            "content of a page when looking at its layout. The point of using ::LoremIpsum:: " \
            "is that it has a more-or-less normal 3 distribution of 8 letters, as opposed to " \
            "using 'Content here, content 99 here', making it look like readable **English**."

import re

entry = input()
regex = r"\*{2}[A-Z]{1}[a-z]{2,}\*{2}|\:{2}[A-Z][a-z]{2,}\:{2}"
matches = re.findall(regex, entry)
# matches = re.findall(regex, test_str)
# matches = re.findall(regex, test_str2)
# matches = re.findall(regex, test_str3)
# matches = [word[2:-2] for word in matches]
# print(matches)

total_candidates = len(matches)
numbers = re.findall(r"\d", entry)
# numbers = re.findall(r"\d", test_str)
# numbers = re.findall(r"\d", test_str2)
# numbers = re.findall(r"\d", test_str3)
# print(numbers)

if numbers:
    treshold = 1
    for x in numbers:
        treshold *= int(x)
else:
    treshold = 0

print(f"Cool threshold: {treshold}")
print(f"{total_candidates} emojis found in the text. The cool ones are:")
for smiley in matches:
    ascii_sum = 0
    for y in smiley[2:-2]:
        ascii_sum += ord(y)
    if ascii_sum > treshold:
        print(smiley)
