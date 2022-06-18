entry_string = input()
shuffle = int(input())

initial_deck = entry_string.split(" ")
half_deck_length = int(len(initial_deck) / 2)
new_deck = initial_deck

for j in range(shuffle):
    shuffled_deck = []
    for i in range(half_deck_length):
        shuffled_deck.append(new_deck[i])
        shuffled_deck.append(new_deck[i+half_deck_length])
    new_deck = shuffled_deck
print(new_deck)
