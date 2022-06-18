class Storage:

    # storage = []

    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.storage = []

    def add_product(self, x):
        self.storage.append(x)

    def get_products(self):
        return self.storage


basket = Storage(input())
product = input()
while product != "print":
    if len(basket.storage) < basket.capacity:
        basket.add_product(product)
    product = input()
print(basket.storage)
