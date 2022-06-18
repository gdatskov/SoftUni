class Catalogue:

    # products = []

    def __init__(self, catalog_name):
        self.catalog_name = catalog_name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)
        # Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        start_letter_list = []
        for items in self.products:
        # for items in Catalogue.products:
            if items[0] == first_letter:
                start_letter_list.append(items)
        return start_letter_list

    def __repr__(self):
        self.products.sort()
        # print(f"Items in the {self.catalog_name} catalogue:")
        to_be_returned_list = f"Items in the {self.catalog_name} catalogue:\n" + '\n'.join(self.products)
        return to_be_returned_list


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
