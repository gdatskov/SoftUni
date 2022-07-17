class Trainer:
    __ID = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_id()

    @staticmethod
    def get_id():
        Trainer.__ID += 1
        return Trainer.__ID

    @staticmethod
    def get_next_id():
        return Trainer.__ID + 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
