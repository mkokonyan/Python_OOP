from project.product import Product


class Food(Product):
    quantity = 15
    def __init__(self, name):
        self.name = name
