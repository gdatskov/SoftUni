from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.trainer import Trainer
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, sub: Subscription):
        if sub not in self.subscriptions:
            self.subscriptions.append(sub)

    def subscription_info(self, sub_id):
        result = []
        for lis in [self.subscriptions, self.customers, self.trainers, self.equipment, self.plans]:
            for item in lis:
                if item.id == sub_id:
                    result.append(str(item))
        return "\n".join(result)


