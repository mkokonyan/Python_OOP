class Flower:
    def __init__(self, name, water_requirments):
        self.name = name
        self.water_requirments = water_requirments
        self.current_water = 0
    def water(self, quantity):
        self.current_water += quantity

    def is_happy(self):
        return self.water_requirments <= self.current_water
    def status(self):
        if self.is_happy():
            return f"{self.name} is happy"
        return f"{self.name} is not happy"

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())