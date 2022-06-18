class Storage:

    def __init__(self, capacity):
        self.capacity = int(capacity)
        self.storage = []

    def add_product(self, x):
        if len(self.storage) < self.capacity:
            self.storage.append(x)

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())


# entry = input()
# while entry != "print(storage.get_products())":
#     entry = input()



# # basket = Storage(input())
# product = input()
# while product != "print":
#     if len(basket.storage) < basket.capacity:
#         basket.add_product(product)
#     product = input()
# print(basket.storage)
