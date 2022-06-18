lost = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0
shield_count = 0
for battle in range(1, lost+1):
    if battle % 2 == 0:
        expenses += helmet
    if battle % 3 == 0:
        expenses += sword
    if battle % 2 == 0 and battle % 3 ==0:
        expenses += shield
        shield_count += 1
    if shield_count % 2 == 0 and shield_count != 0:
        expenses += armor
        shield_count = 0
print(f"Gladiator expenses: {expenses:.2f} aureus")

