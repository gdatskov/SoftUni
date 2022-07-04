courses_dict = {}

while True:
    entry = input()
    if entry == "end":
        break
    course, name = entry.split(" : ")
    if course not in courses_dict.keys():
        courses_dict[course] = [name]
    else:
        courses_dict[course].append(name)

for course, students in courses_dict.items():
    print(f"{course}: {len(students)}")
    for name in students:
        print(f"-- {name}")
