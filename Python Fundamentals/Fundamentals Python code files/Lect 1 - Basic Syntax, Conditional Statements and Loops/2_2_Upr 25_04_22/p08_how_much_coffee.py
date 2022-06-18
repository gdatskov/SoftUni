command = ""
uppercase_list = ["CODING", "DOG", "CAT", "MOVIE"]
lowercase_list = ["coding", "dog", "cat", "movie"]
coffees = 0
while command != "END":
    command = input()
    if command == "END":
        continue
    if command in uppercase_list:
        coffees += 2
    if command in lowercase_list:
        coffees += 1
    # if coffees > 5:
    #     break
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
