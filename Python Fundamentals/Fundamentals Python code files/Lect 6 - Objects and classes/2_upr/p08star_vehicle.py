class Vehicle:
    def __init__(self, veh_type, veh_model, veh_price):
        self.veh_type = veh_type
        self.veh_model = veh_model
        self.veh_price = veh_price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner != None:
            return "Car already sold"
        if money >= self.veh_price and self.owner == None:
            self.owner = owner
            return f"Successfully bought a {self.veh_type}. Change: {money - self.veh_price:.2f}"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            return f"{self.veh_model} {self.veh_type} is owned by: {self.owner}"
        return f"{self.veh_model} {self.veh_type} is on sale: {self.veh_price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)

