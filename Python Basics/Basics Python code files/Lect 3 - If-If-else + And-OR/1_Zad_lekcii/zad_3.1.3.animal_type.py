animal_entry = input()

animal_type = ""

if animal_entry == "dog":
    animal_type = "mammal"
elif animal_entry == "crocodile" or animal_entry == "tortoise" or animal_entry == "snake":
    animal_type = "reptile"
else:
    animal_type = "unknown"

print(animal_type)
