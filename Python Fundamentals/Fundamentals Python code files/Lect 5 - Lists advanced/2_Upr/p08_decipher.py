entry = input()
words_list = entry.split(" ")
digit_str_list = [str(x) for x in range(10)]
deciphered_list = []

for word in words_list:

    char_list = list(word)
    ascii_code = []
    non_ascii = []

    for ch in char_list:
        if ch in digit_str_list:
            ascii_code.append(ch)
        else:
            non_ascii.append(ch)

    new_list = [chr(int("".join(ascii_code)))]
    new_list.extend(non_ascii)
    new_list[1], new_list[-1] = new_list[-1], new_list[1]
    deciphered_list.append("".join(new_list))

print(" ".join(deciphered_list))
