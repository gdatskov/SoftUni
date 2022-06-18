
entry = ""
step_counter = 0

while entry != "Going home" and step_counter <= 10000:
    entry = input()
    if entry == "Going home":
        step_counter += int(input())
        continue
    step_counter += int(entry)

if step_counter >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{step_counter-10000} steps over the goal!")
else:
    print(f"{10000-step_counter} more steps to reach goal.")
