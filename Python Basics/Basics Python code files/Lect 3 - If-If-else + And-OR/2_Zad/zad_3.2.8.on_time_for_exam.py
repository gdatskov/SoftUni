exam_hour = int(input())
exam_minute = int(input())
student_hour = int(input())
student_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
student_time = student_hour * 60 + student_minute
time_diff = abs(exam_time-student_time)

if time_diff > 30 and student_time < exam_time:
    print("Early")
    if time_diff >= 60:
        if time_diff % 60 < 10:
            print(f"{time_diff // 60}:0{time_diff % 60} hours before the start")
        else:
            print(f"{time_diff // 60}:{time_diff % 60} hours before the start")
    else:
        print(f"{time_diff % 60} minutes before the start")
elif exam_time < student_time:
    print("Late")
    if time_diff >= 60:
        if time_diff % 60 < 10:
            print(f"{time_diff // 60}:0{time_diff % 60} hours after the start")
        else:
            print(f"{time_diff // 60}:{time_diff % 60} hours after the start")
    else:
        print(f"{time_diff % 60} minutes after the start")
else:
    print("On time")
    if time_diff != 0:
        print(f"{time_diff % 60} minutes before the start")
