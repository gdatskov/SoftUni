def book():
    all = dict()
    command = input()
    while command != "Lumpawaroo":
        if "|" in command:
            command = command.split(" | ")
            user = command[1]
            side = command[0]
            cond = True
            for i in all.values():
                if user in i:
                    cond = False
                    break
            if cond:
                if side not in all:
                    all[side] = []
                all[side].append(user)
        else:
            command = command.split(" -> ")
            user = command[0]
            side = command[1]
            condition = False
            cond = False
            if side not in all:
                all[side] = []
            for k in all:
                if user in all[k]:
                    all[k].remove(user)
                    all[side].append(user)
                    cond = True
                    print(f"{user} joins the {side} side!")
                    break
            if not cond:
                all[side].append(user)
                print(f"{user} joins the {side} side!")
        command = input()
    for i in all:
        if len(all[i]) > 0:
            print(f"Side: {i}, Members: {len(all[i])}")
            for k in all[i]:
                print(f"! {k}")
book()