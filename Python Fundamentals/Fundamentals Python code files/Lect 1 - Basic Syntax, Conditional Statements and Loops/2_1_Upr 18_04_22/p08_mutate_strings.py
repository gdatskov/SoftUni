text1 = input()
text2 = input()
transform_list = list(text1)

for letter in range(len(text1)):
    if transform_list[letter] != text2[letter]:
        transform_list[letter] = text2[letter]
        print("".join(transform_list))
