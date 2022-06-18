judges = int(input())
student_grades_sum = 0
presentation_count = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break
    presentation_count += 1

    # Inside loop
    grades_sum = 0
    grades_count = 0
    for grades in range(judges):
        grade = float(input())
        grades_sum += grade
        grades_count += 1
    average_exam_grade = grades_sum / grades_count
    print(f"{presentation} - {average_exam_grade:.2f}.")

    student_grades_sum += average_exam_grade
    average_student_grade = student_grades_sum / presentation_count

print(f"Student's final assessment is {average_student_grade:.2f}.")




