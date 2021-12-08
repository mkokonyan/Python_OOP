class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def product_validation(self, product_name):
        if product_name not in [x.name for x in self.products]:
            return False
        return True

    def find(self, product_name):
        if not self.product_validation(product_name):
            return
        return [x.name for x in self.products if product_name == x.name][0]

    def remove(self, product_name):
        if not self.product_validation(product_name):
            return
        self.products = [x for x in self.products if not product_name == x.name]

    def __repr__(self):
        return "\n".join([f"{x.name}: {x.quantity}" for x in self.products])

