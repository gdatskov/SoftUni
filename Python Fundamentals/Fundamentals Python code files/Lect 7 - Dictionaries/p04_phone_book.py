add_entry = input()
phonebook = dict()
while True:
    if "-" in add_entry:
        contact = add_entry.split("-")
        phonebook[contact[0]] = contact[1]
        add_entry = input()
    else:
        break

search_entry = int(add_entry)

for contacts in range(search_entry):
    contact_search = input()
    if contact_search in phonebook.keys():
        print(f"{contact_search} -> {phonebook[contact_search]}")
    else:
        print(f"Contact {contact_search} does not exist.")