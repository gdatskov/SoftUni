def aliquot_sum(aliquot_number):
    total = 0
    for number in range(1, aliquot_number):
        if aliquot_number % number == 0:
            total += number
    if total == aliquot_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


entry = int(input())
aliquot_sum(entry)
