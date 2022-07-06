from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
# repo.remove("apple")
repo.remove("apple")
print(repo)
