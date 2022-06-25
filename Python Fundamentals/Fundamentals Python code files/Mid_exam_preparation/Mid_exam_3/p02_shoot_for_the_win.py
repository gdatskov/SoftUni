targets = [int(x) for x in input().strip().split(" ")]

while True:
    command = input()
    if command == "End":
        break
    idx = int(command)
    if not 0 <= idx < len(targets):
        continue
    current_target = targets[idx]
    if current_target == -1:
        continue
    targets[idx] = -1
    for t in range(len(targets)):
        if targets[t] > current_target and targets[t] != -1:
            targets[t] -= current_target
        elif targets[t] <= current_target and targets[t] != -1:
            targets[t] += current_target

print(f"Shot targets: {targets.count(-1)} -> {' '.join(str(x) for x in targets)}")