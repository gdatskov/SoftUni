from project.animal import Animal
from project.lion import Lion
from project.cheetah import Cheetah
from project.tiger import Tiger
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        return "Not enough budget"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_payment = 0
        for worker in self.workers:
            salary_payment += worker.salary
        if salary_payment <= self.__budget:
            self.__budget -= salary_payment
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend_payment = 0
        for animal in self.animals:
            tend_payment += animal.money_for_care
        if tend_payment <= self.__budget:
            self.__budget -= tend_payment
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals = {}
        for animal in self.animals:
            class_name = animal.__class__.__name__
            if class_name not in animals.keys():
                animals[class_name] = [animal]
            else:
                animals[class_name].append(animal)

        to_return = [f"You have {len(self.animals)} animals"]
        for animal_type in animals.keys():
            to_return.append(f"----- {len(animals[animal_type])} {animal_type}s:")
            [to_return.append(str(animal)) for animal in animals[animal_type]]

        return "\n".join(to_return)

    def workers_status(self):
        workers = {}
        for worker in self.workers:
            class_name = worker.__class__.__name__
            if class_name not in workers.keys():
                workers[class_name] = [worker]
            else:
                workers[class_name].append(worker)

        to_return = [f"You have {len(self.workers)} workers"]
        for worker_type in workers.keys():
            to_return.append(f"----- {len(workers[worker_type])} {worker_type}s:")
            [to_return.append(str(animal)) for animal in workers[worker_type]]

        return "\n".join(to_return)

