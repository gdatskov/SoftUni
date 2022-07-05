force = {}
while True:
    cheater = False
    user_does_not_exist = True
    entry = input()
    if entry == "Lumpawaroo":
        break

    if "|" in entry:
        force_side, force_user = entry.split(" | ")

        for users in force.values():
            if force_user in users:
                cheater = True
                break
        if cheater:
            continue

        if force_side not in force.keys():
            force[force_side] = [force_user]
        else:
            force[force_side].append(force_user)

    else:
        force_user, force_side = entry.split(" -> ")

        for side, users in force.items():
            if force_user in users:
                user_does_not_exist = False
                force[side].remove(force_user)
                break

        if force_side not in force.keys():
            force[force_side] = [force_user]
        else:
            force[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for side, users in force.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
