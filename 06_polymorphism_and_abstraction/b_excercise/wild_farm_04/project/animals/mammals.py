from project.animals.animal import Mammal
from project.animals.birds import Owl, Hen
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.weight_increase = 0.10
        self.acceptable_foods = [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.weight_increase = 0.40
        self.acceptable_foods = [Meat]

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.weight_increase = 0.30
        self.acceptable_foods = [Vegetable, Meat]

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.weight_increase = 1.00
        self.acceptable_foods = [Meat]

    def make_sound(self):
        return "ROAR!!!"
