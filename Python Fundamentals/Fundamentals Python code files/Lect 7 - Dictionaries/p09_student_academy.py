students = {}
for _ in range(int(input())):
    student, grade = input(), float(input())
    if student not in students.keys():
        students[student] = [grade]
    else:
        students[student].append(grade)

for student, grades in students.items():
    average = sum(grades)/len(grades)
    if average >= 4.5:
        print(f"{student} -> {average:.2f}")
