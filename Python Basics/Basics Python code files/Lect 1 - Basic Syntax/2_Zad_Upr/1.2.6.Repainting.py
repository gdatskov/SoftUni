nylon = float(input(f'Nylon, m2:'))
paint = float(input(f'Paint, L: '))
thinner = float(input('Thinner, L: '))
hours = float(input('Hours: '))
materials = float((paint*14.5*1.1+(nylon+2)*1.5+thinner*5+0.4))
cost = materials+materials*0.3*hours
print(cost)
