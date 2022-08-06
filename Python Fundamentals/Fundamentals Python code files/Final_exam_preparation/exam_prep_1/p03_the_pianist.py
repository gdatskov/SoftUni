pieces_number = int(input())

pieces_keys = {}
pieces_composers = {}

for pieces in range(pieces_number):
    piece, composer, key = input().split("|")
    pieces_keys[piece] = key
    pieces_composers[piece] = composer

while True:
    command = input()
    if command == "Stop":
        break
    command, instructions = command.split("|", 1)
    if command == "Add":
        piece, composer, key = instructions.split("|")
        if piece not in pieces_composers.keys():
            pieces_keys[piece] = key
            pieces_composers[piece] = composer
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    if command == "Remove":
        piece = instructions
        if piece in pieces_composers.keys():
            del pieces_keys[piece]
            del pieces_composers[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    if command == "ChangeKey":
        piece, new_key = instructions.split("|")
        if piece in pieces_keys.keys():
            pieces_keys[piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece in pieces_composers:
    print(f"{piece} -> Composer: {pieces_composers[piece]}, Key: {pieces_keys[piece]}")
