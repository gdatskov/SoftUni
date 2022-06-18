entry_gifts = input()
gift_wishlist = entry_gifts.split(" ")
money = True
while money:
    command = input()
    operation = command.split(" ")
    if command == "No Money":
        money = False
        continue
    if "OutOfStock" in operation:
        for gift in gift_wishlist:
            if gift == operation[1]:
                gift_wishlist.insert(gift_wishlist.index(gift), "None")
                gift_wishlist.remove(gift)
    if "Required" in operation and 0 <= int(operation[2]) <= len(gift_wishlist)-1:
        gift_wishlist.pop(int(operation[2]))
        gift_wishlist.insert(int(operation[2]), operation[1])
    if "JustInCase" in operation:
        gift_wishlist.pop()
        gift_wishlist.append(operation[1])
# for gift in gift_wishlist:    #second None is missed when removing and shifting to next element
    # if gift == "None":
    #     gift_wishlist.remove(gift)
while "None" in gift_wishlist:
    gift_wishlist.remove("None")
print(" ".join(gift_wishlist))
