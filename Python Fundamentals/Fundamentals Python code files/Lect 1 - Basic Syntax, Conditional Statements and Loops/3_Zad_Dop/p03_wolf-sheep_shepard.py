wolf_among_sheep = input()
sheep_list = wolf_among_sheep.split(", ")
for i in range(len(sheep_list)):
    if i == len(sheep_list)-1 and sheep_list[i] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if sheep_list[i] == "wolf":
        print(f"Oi! Sheep number {len(sheep_list)-i-1}! You are about to be eaten by a wolf!")
