text = input()
while True:
    instructions = input()
    if instructions == "Decode":
        break
    instructions = instructions.split("|")
    if instructions[0] == "Move":
        letters_to_move = int(instructions[1])
        wtf = text
        text = wtf[letters_to_move:]+wtf[:letters_to_move]
    if instructions[0] == "Insert":
        idx, value = int(instructions[1]), instructions[2]
        text = list(text)
        text.insert(idx, value)
        text = "".join(text)
    if instructions[0] == "ChangeAll":
        substring, replacement = instructions[1], instructions[2]
        text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")


