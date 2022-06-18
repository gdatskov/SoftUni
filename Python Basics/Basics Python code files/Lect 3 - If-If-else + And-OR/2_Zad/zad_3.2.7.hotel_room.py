month = input()
nights = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    if 7 < nights < 14:
        studio = studio * 0.95
    if nights >= 14:
        studio = studio * 0.7
    apartment = 65
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
else:
    studio = 76
    apartment = 77

if (month == "June" or month == "September") and nights > 14:
    studio = studio * 0.8

if nights > 14:
    apartment = apartment*0.9

print(f"Apartment: {apartment*nights:.2f} lv.")
print(f"Studio: {studio*nights:.2f} lv.")