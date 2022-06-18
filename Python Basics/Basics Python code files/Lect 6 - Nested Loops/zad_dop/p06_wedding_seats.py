start_sector = "A"
end_sector = input() #B~Z
sector_A_rows = int(input())
#next sector rows += 1
odd_row_seats = int(input())        #a, b, c, d ....
even_row_seats = odd_row_seats + 2  #a, b, c, d ....

seats_start = ord("a")
seats_total = 0
odd_row_seats_range = odd_row_seats+seats_start
even_row_seats_range = even_row_seats+seats_start
start_sector_number = ord(start_sector)
end_sector_number = ord(end_sector)

row_range = sector_A_rows
for sector in range(start_sector_number, end_sector_number + 1):
    for row in range(1, row_range+1):
        if row % 2 == 0:
            for seat in range(seats_start, even_row_seats_range):
                print(f"{chr(sector)}{(row)}{chr(seat)}")
                seats_total += 1
        else:
            for seat in range(seats_start, odd_row_seats_range):
                print(f"{chr(sector)}{row}{chr(seat)}")
                seats_total += 1
    row_range += 1
print(seats_total)

# Изход
# Да се отпечата на конзолата всяко място на отделен ред по следния формат:
# {сектор}{ред}{място}
# Накрая трябва да отпечата броя на всички места.