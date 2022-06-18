fuel_type = input()
fuel = float(input())
club_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93

gasoline_reduced = 2.22-0.18
diesel_reduced = 2.33-0.12
gas_reduced = 0.93-0.08

if club_card == "Yes":
    gasoline=gasoline_reduced
    diesel=diesel_reduced
    gas=gas_reduced

if fuel_type == "Gasoline":
    total = fuel*gasoline

if fuel_type == "Diesel":
    total = fuel*diesel

if fuel_type == "Gas":
    total = fuel*gas

if fuel >= 20:
    if fuel <= 25:
        total = total*(1-0.08)
    elif fuel > 25:
        total = total*(1-0.1)

print(f"{total:.2f} lv.")
