class Subscription:
    __ID = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_id()

    @staticmethod
    def get_id():
        Subscription.__ID += 1
        return Subscription.__ID

    @staticmethod
    def get_next_id():
        return Subscription.__ID + 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"