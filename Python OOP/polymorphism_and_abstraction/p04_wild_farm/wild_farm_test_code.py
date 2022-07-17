from project.animals.birds import Owl, Hen
from project.animals.mammals import Tiger
from project.food import Vegetable, Meat, Fruit

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

tiger = Tiger("Maria", 1011, "Asia")
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(11)
print(tiger)
print(tiger.make_sound())
tiger.feed(veg)
print(tiger.feed(fruit))
tiger.feed(meat)
print(tiger)