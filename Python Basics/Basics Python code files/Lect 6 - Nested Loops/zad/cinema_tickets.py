total_student_count = 0
total_standard_count = 0
total_kid_count = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    max_seats = int(input())

    student_count = 0
    standard_count = 0
    kid_count = 0

    for free_seats in range(max_seats):
        ticket_type = input()
        if ticket_type == "student":
            student_count += 1
        elif ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "kid":
            kid_count += 1
        else:
            break
    total_movie_tickets = student_count + standard_count + kid_count
    print(f"{movie_name} - {total_movie_tickets / max_seats * 100:.2f}% full.")

    total_student_count += student_count
    total_standard_count += standard_count
    total_kid_count += kid_count

total_tickets = total_standard_count + total_kid_count + total_student_count
print(f"Total tickets: {total_tickets}")
print(f"{total_student_count/total_tickets*100:.2f}% student tickets.")
print(f"{total_standard_count/total_tickets*100:.2f}% standard tickets.")
print(f"{total_kid_count/total_tickets*100:.2f}% kids tickets.")
