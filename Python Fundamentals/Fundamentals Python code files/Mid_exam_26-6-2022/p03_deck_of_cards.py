"""
Inputs
•	The possible commands are:
o	"Add, {CardName}"
o	"Remove, {CardName}"
o	"Remove At, {index}"
o	"Insert, {index}, {CardName}"
Output
•	The possible outputs are:
o	"Card is already in the deck"
o	"Card successfully added"
o	"Card successfully removed"
o	"Card not found"
o	"Index out of range"
o	"Card is already added"
"""

deck = input().strip().split(", ")

for n in range(int(input())):

    input_line = input().strip().split(", ")

    command = input_line[0]

    if command == "Add":
        card_name = input_line[1]
        if card_name not in deck:
            deck.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    if command == "Remove":
        card_name = input_line[1]
        if card_name in deck:
            deck.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")

    if command == "Remove At":
        idx = int(input_line[1])
        if 0 <= idx < len(deck):
            card_name = deck[idx]
            deck.remove(card_name)
            print("Card successfully removed")
        else:
            print("Index out of range")

    if command == "Insert":
        idx = int(input_line[1])
        card_name = input_line[2]
        if 0 <= idx < len(deck):
            if card_name in deck:
                print("Card is already added")
            else:
                deck.insert(idx, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(deck))
