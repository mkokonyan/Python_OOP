from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        pass

    def add_decoration(self, decoration_type):
        pass

    def insert_decoration(self, aquarium_name, decoration_type):
        pass

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        pass

    def feed_fish(self):
        pass

    def calculate_value(self, aquarium_name):
        pass

    def report(self):
        pass
