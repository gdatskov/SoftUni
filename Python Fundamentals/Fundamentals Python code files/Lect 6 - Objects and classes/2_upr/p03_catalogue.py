class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [
            item for item in self.products
            if item.startswith(first_letter.upper()) or item.startswith(first_letter.lower())
        ]

    def __repr__(self):
        to_be_returned_list = [f"Items in the {self.name} catalogue:"]
        to_be_returned_list.extend(sorted(self.products, key=lambda x: x.lower()))
        return "\n".join(to_be_returned_list)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
