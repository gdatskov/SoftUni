entry = input().split(" ")
string = "".join(entry)
char_dict = {}

for char in string:
    if char not in char_dict.keys():
        char_dict[char] = 1
    else:
        char_dict[char] += 1

for key in char_dict.keys():
    print(f"{key} -> {char_dict[key]}")

