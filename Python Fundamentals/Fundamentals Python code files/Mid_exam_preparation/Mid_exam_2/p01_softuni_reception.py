employees = [int(input().strip()) for x in range(3)]
students = int(input().strip())

hours = 0
counter = 0

# if students > 0:           # Pointless otherwise
while students > 0:
    counter += 1
    hours += 1
    for emp in employees:
        students -= emp
    if counter % 3 == 0 and students > 0:
        hours += 1           # count it as robot-employee breaks for recharging

print(f"Time needed: {hours}h.")
