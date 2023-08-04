# 2.	Students' Grades
# Write a program that reads students' names and their grades and adds them to the student record.


# On the first line, you will receive the number of students – N.

# On the following N lines, you will be receiving a student's name and grade.

# For each student print all his/her grades and finally his/her average grade,
# formatted to the second decimal point in the format:
# "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".

# The order in which we print the result does not matter.

from collections import deque

students_dict = dict()
num_students = int(input())

for x in range(num_students):

    name, grade = input().split(" ")

    if name not in students_dict.keys():
        students_dict[name] = deque([float(grade)])
    else:
        students_dict[name].append(float(grade))

for student, grades in students_dict.items():
    student_grades = ""

    for x in grades:
        student_grades += f"{x:.2f} "

    student_grades.strip(" ")

    print(f"{student} -> {student_grades}(avg: {sum(grades)/len(grades):.2f})")









# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00	Mark -> 5.50 2.50 3.46 (avg: 3.82)
# Peter -> 5.20 3.20 (avg: 4.20)
# Alex -> 2.00 3.00 (avg: 2.50)

# 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66	Ted -> 3.00 3.66 (avg: 3.33)
# Scott -> 4.50 5.00 (avg: 4.75)

# 5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30	Peter -> 4.40 (avg: 4.40)
# Lee -> 6.00 5.50 6.00 (avg: 5.83)
# Kenny -> 3.30 (avg: 3.30)

