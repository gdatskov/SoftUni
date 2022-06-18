def ascii_range(char1, char2):
    char_list = []
    start = ord(char1)
    end = ord(char2)
    for ascii_number in range(start+1, end):
        character = chr(ascii_number)
        char_list.append(character)
    return " ".join(char_list)


input1 = input()
input2 = input()

print(ascii_range(input1, input2))
