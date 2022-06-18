def ascii_range_check(start, end, symbol):
    start = ord(str(start))
    end = ord(str(end))
    symbol = ord(str(symbol))
    if start <= symbol <= end:
        return True
    else:
        return False



password = list(input())
count = 0
special_character = False
invalid = False

for char in password:

    if ascii_range_check(0, 9, char):
        count += 1
        continue

    elif ascii_range_check("a", "z", char):
        continue

    elif ascii_range_check("A", "Z", char):
        continue

    else:
        special_character = True


if not 6 <= len(password) <= 10:
    print("Password must be between 6 and 10 characters")
    invalid = True
if special_character:
    print("Password must consist only of letters and digits")
    invalid = True
if count < 2:
    print("Password must have at least 2 digits")
    invalid = True
if not invalid:
    print("Password is valid")
