from project.animals.animal import Bird
from project.food import Meat, Fruit, Vegetable, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.weight_increase = 0.25
        self.acceptable_foods = [Meat]

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.weight_increase = 0.35
        self.acceptable_foods = [Vegetable, Fruit, Meat, Seed]


    def make_sound(self):
        return "Cluck"
