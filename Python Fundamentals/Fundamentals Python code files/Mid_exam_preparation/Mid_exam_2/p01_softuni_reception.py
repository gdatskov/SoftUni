employees = [int(input().strip()) for x in range(3)]
students = int(input().strip())

hours = 0
counter = 0
while students > 0:
    counter += 1
    hours += 1
    for emp in employees:
        students -= emp
    if counter % 4 == 0 and students > 0:
        hours += 1

print(f"Time needed: {hours}h.")
