password = input()
while True:
    entry = input()
    if entry == "Done":
        print(f"Your password is: {password}")
        break

    command_list = entry.split(" ")

    if entry == "TakeOdd":
        new_password = ""
        for idx in range(len(password)):
            if idx % 2 == 1:
                new_password += password[idx]
        password = new_password
        if password:
            print(new_password)

    if command_list[0] == "Cut":
        idx, length = int(command_list[1]), int(command_list[2])
        cut = password[idx:(idx+length)]
        password = password.replace(cut, "")
        if password:
            print(password)

    if command_list[0] == "Substitute":
        _, substring, substitute = command_list
        if substring in password:
            while substring in password:
                password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
