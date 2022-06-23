def naughty_or_nice_list(lis, *args, **kwargs):
    return_dict = {
        "Nice": [],
        "Naughty": [],
        "Not found": [],
    }

    kids_dict = dict()

    for key, value in lis:
        if key not in kids_dict.keys():
            kids_dict[key] = [value]
        else:
            kids_dict[key].append(value)

    for command in args:
        number, attribute = command.split("-")
        number = int(number)
        if number in kids_dict.keys():
            if len(kids_dict[number]) == 1:
                kid = kids_dict[number].pop()
                # lis.remove((number, kid))
                # kids_dict[number][0].remove(kid)
                if attribute == "Naughty":
                    return_dict["Naughty"].append(kid)
                if attribute == "Nice":
                    return_dict["Nice"].append(kid)

    for name, quality in kwargs.items():
        count = 0
        for lists in kids_dict.values():
            for kid in lists:
                if kid == name:
                    count += 1
        if count == 1:
            if quality == "Naughty":
                return_dict["Naughty"].append(name)
            if quality == "Nice":
                return_dict["Nice"].append(name)
            for number in kids_dict.keys():
                if name in kids_dict[number]:
                    kids_dict[number].remove(name)

    for lists in kids_dict.values():
        for kid in lists:
            return_dict["Not found"].append(kid)

    text = [f'{key}: {", ".join(value)}' for key, value in return_dict.items() if value]
    return '\n'.join(text)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print()
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
