wanted_book = input()
book_input = input()
book_count = 0

while book_input != wanted_book:
    book_count += 1
    book_input = input()
    if book_input == "No More Books":
        break

if book_input == wanted_book:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
