class Customer:
    __ID = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_id()

    @staticmethod
    def get_id():
        Customer.__ID += 1
        return Customer.__ID

    @staticmethod
    def get_next_id():
        return Customer.__ID + 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
