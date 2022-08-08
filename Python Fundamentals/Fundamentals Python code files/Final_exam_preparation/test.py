def fill_dict(number):
    hero_dict = {}
    for _ in range(number):
        instruction = input().split(' ')
        her_name = instruction[0]
        hero_hp = int(instruction[1])
        hero_mana = int(instruction[2])
        hero_dict[her_name] = {'HP': hero_hp, 'Mana': hero_mana}
    return hero_dict


def hero_operations(hero_dict: dict):
    while True:
        command = input()
        if command == 'End':
            break
        command = command.split(' - ')
        action = command[0]
        hero_name = command[1]
        if action == 'CastSpell':
            mp_needed = int(command[2])
            spell_name = command[3]
            if hero_dict[hero_name]['Mana'] > mp_needed:
                hero_dict[hero_name]['Mana'] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]['Mana']} MP!")
            else:
                print(f'{hero_name} does not have enough MP to cast {spell_name}!')
        elif action == 'TakeDamage':
            damage = int(command[2])
            attacker = command[3]
            hero_dict[hero_name]['HP'] -= damage
            if hero_dict[hero_name]['HP'] > 0:
                print(
                    f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dict[hero_name]['HP']} HP left!")
            else:
                del hero_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")
        elif action == 'Recharge':
            amount = int(command[2])
            if hero_dict[hero_name]['Mana'] + amount > 200:
                amount = 200 - hero_dict[hero_name]['Mana']
                hero_dict[hero_name]['Mana'] = 200
            else:
                hero_dict[hero_name]['Mana'] += amount
            print(f"{hero_name} recharged for {amount} MP!")
        elif action == 'Heal':
            amount = int(command[2])
            if hero_dict[hero_name]['HP'] + amount > 100:
                amount = 100 - hero_dict[hero_name]['HP']
                hero_dict[hero_name]['HP'] = 100
            else:
                hero_dict[hero_name]['HP'] += amount
            print(f"{hero_name} healed for {amount} HP!")
    return hero_dict


heroes = hero_operations(fill_dict(int(input())))
for hero in heroes.keys():
    print(f'{hero}')
    print(f'  HP: {heroes[hero]["HP"]}')
    print(f'  MP: {heroes[hero]["Mana"]}')
