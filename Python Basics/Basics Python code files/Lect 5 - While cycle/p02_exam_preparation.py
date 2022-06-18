max_bad_grades = int(input())
task_name = ""
end_exam = False
total_score = 0
exam_tasks = 0
bad_grades_count = 0

while end_exam is False:
    task_name = input()
    if task_name == "Enough":
        end_exam = True
        average_score = total_score/exam_tasks
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {exam_tasks}")
        print(f"Last problem: {last_problem}")
        continue
    grade = int(input())
    exam_tasks += 1
    total_score += grade
    last_problem = task_name
    if grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == max_bad_grades:
            end_exam = True
            print(f"You need a break, {bad_grades_count} poor grades.")


