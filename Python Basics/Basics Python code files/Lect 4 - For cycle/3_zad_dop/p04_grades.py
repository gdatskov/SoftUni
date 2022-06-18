students = int(input())
fail_sum = 0
good_sum = 0
very_good_sum = 0
excellent_sum = 0
fail = 0
good = 0
very_good = 0
excellent = 0
for attendees in range(students):
    grade = float(input())
    if grade < 3:
        fail_sum += grade
        fail += 1
    elif grade < 4:
        good_sum += grade
        good += 1
    elif grade < 5:
        very_good_sum += grade
        very_good += 1
    else:
        excellent_sum += grade
        excellent += 1

print(f"Top students: {excellent/students*100:.2f}%")
print(f"Between 4.00 and 4.99: {very_good/students*100:.2f}%")
print(f"Between 3.00 and 3.99: {good/students*100:.2f}%")
print(f"Fail: {fail/students*100:.2f}%")
print(f"Average: {(excellent_sum+very_good_sum+good_sum+fail_sum)/students:.2f}")
