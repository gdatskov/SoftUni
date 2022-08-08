heroes_number = int(input())
hero_hp = {}
hero_mp = {}
for hero in range(heroes_number):
    hero_name, hp, mp = input().split(" ")
    hero_hp[hero_name] = int(hp)
    hero_mp[hero_name] = int(mp)

while True:
    command_line = input().split(" - ")
    command = command_line[0]
    if command == "End":
        break
    if command == "CastSpell":
        _, hero_name, mp_needed, spell_name = command_line
        mp_needed = int(mp_needed)
        if hero_mp[hero_name] >= mp_needed:
            hero_mp[hero_name] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_mp[hero_name]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    if command == "TakeDamage":
        _, hero_name, damage, attacker = command_line
        damage = int(damage)
        hero_hp[hero_name] -= damage
        if hero_hp[hero_name] <= 0:
            hero_hp[hero_name] = 0
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_hp[hero_name]} HP left!")
    if command == "Recharge":
        _, hero_name, amount = command_line
        amount = int(amount)
        current_mp = hero_mp[hero_name]
        hero_mp[hero_name] += amount
        if hero_mp[hero_name] > 200:
            hero_mp[hero_name] = 200
        print(f"{hero_name} recharged for {hero_mp[hero_name] - current_mp} MP!")
    if command == "Heal":
        _, hero_name, amount = command_line
        amount = int(amount)
        current_hp = hero_hp[hero_name]
        hero_hp[hero_name] += amount
        if hero_hp[hero_name] > 100:
            hero_hp[hero_name] = 100
        print(f"{hero_name} healed for {hero_hp[hero_name] - current_hp} HP!")

for hero in hero_hp.keys():
    if int(hero_hp[hero]) > 0:
        print(hero)
        print(f"  HP: {hero_hp[hero]}")
        print(f"  MP: {hero_mp[hero]}")
