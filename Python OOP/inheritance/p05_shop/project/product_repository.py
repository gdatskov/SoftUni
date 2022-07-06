from project.product import Product


class ProductRepository:

    products = list()

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for x in self.products:
            if x.name == product_name:
                return x

    def remove(self, product_name):
        [self.products.remove(x) for x in self.products if x.name == product_name]
        # for x in self.products:
        #     if x.name == product_name:
        #         self.products.remove(x)

    def __repr__(self):
        data = [f"{product.name}: {product.quantity}" for product in self.products]
        return "\n".join(data)
