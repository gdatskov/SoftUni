from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.lion import Lion
from project.vet import Vet
from project.zoo_better_solution import Zoo

zoo = Zoo("Zootopia", 3000, 5, 8)
cheeto = Cheetah("Cheeto", "Male", 2)
cheeto_price = 200
print(zoo.add_animal(cheeto,cheeto_price))
leo = Lion("Leo", "Male", 2)
cheeto_price = 200
print(zoo.add_animal(leo,cheeto_price))
leia = Lion("Leia", "Female", 1)
print(zoo.add_animal(leia,cheeto_price))

stacy = Caretaker("Stacy", 35, 140)
print(zoo.hire_worker(stacy))
casey = Vet("Casey", 37, 280)
print(zoo.hire_worker(casey))
print(zoo._Zoo__workers_capacity)

print(zoo.pay_workers())
print(zoo.tend_animals())

print(zoo.animals_status())
print(zoo.workers_status())

