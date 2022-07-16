command = input()
all = {}
while command != "exam finished":
    command = command.split("-")
    name = command[0]
    subject = command[1]
    if len(command) > 2:
        points = int(command[2])
    if subject == "banned":
        for i in all:
            if name in all[i]:
                all[i][name] = "banned"
        pass
    elif subject not in all:
        all[subject] = {}
        all[subject][name] = [points]
    else:
        if name in all[subject]:
            if all[subject][name] > [points]:
                all[subject][name * 2] = "pass"
            else:
                all[subject][name] = [points]
                all[subject][name * 2] = "pass"
        else:
            all[subject][name] = [points]
    command = input()
print("Results:")
for subject in all:
    for name in all[subject]:
        if all[subject][name] != "banned":
            if all[subject][name] != "pass":
                final = sum(all[subject][name])
                print(f"{name} | {final}")
        else:
            continue
print("Submissions:")
for subject in all:
    print(f"{subject} - {len(all[subject])}")
