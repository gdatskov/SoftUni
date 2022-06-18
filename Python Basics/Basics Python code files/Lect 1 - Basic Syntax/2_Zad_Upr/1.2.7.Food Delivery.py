chicken_menu = 10.35
fish_menu = 12.4
veggie_menu = 8.15
delivery = 2.5
chickens = float(input("Chicken menus: "))
fishes = float(input("Fish menus: "))
veggies = float(input("Veggie menus: "))
delivery_total_cost = (chickens*chicken_menu+fishes*fish_menu+veggies*veggie_menu)*1.2+delivery
print(delivery_total_cost)
