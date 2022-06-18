period = int(input())
physicians = 7
treated_patients = 0
untreated_patients = 0
for day in range(1, period+1):
    if day % 3 == 0 and untreated_patients > treated_patients:
        physicians += 1
    patients = int(input())
    treated_patients_today = 0
    if patients < physicians:
        treated_patients_today += patients
    else:
        treated_patients_today += physicians
    treated_patients += treated_patients_today
    untreated_patients += (patients - treated_patients_today)
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")




# Да се отпечатат на конзолата 2 реда :
# •	На първия ред: "Treated patients: {брой прегледани пациенти}."
# •	На втория ред: "Untreated patients: {брой непрегледани пациенти}."
