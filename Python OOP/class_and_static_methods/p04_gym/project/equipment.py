class Equipment:
    __ID = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_id()

    @staticmethod
    def get_id():
        Equipment.__ID += 1
        return Equipment.__ID

    @staticmethod
    def get_next_id():
        return Equipment.__ID + 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
