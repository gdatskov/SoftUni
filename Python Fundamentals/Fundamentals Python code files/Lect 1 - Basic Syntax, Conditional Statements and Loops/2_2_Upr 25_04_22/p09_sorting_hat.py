while True:
    entry = input()
    if entry == "Welcome!":
        break
    if entry == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(entry) < 5:
        print(f"{entry} goes to Gryffindor.")
    if len(entry) == 5:
        print(f"{entry} goes to Slytherin.")
    if len(entry) == 6:
        print(f"{entry} goes to Ravenclaw.")
    if len(entry) > 6:
        print(f"{entry} goes to Hufflepuff.")
if entry != "Voldemort":
    print("Welcome to Hogwarts.")
