veggies = float(input())
fruits = float(input())
veggies_kg = int(input())
fruits_kg = int(input())
EUR=float(1.94)

gain = (veggies_kg*veggies+fruits*fruits_kg)/EUR

print("{:.2f}".format(gain))
