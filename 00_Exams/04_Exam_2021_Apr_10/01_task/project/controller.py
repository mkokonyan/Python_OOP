from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        aquarium_obj = [aquarium for aquarium in self.aquariums if aquarium_name == aquarium.name]
        decoration_obj = [decoration for decoration in self.decorations_repository.decorations if
                          decoration_type == decoration.__class__.__name__]
        if not decoration_obj:
            return f"There isn't a decoration of type {decoration_type}."
        if aquarium_obj:
            decoration_obj = decoration_obj[0]
            aquarium_obj[0].add_decoration(decoration_obj)
            self.decorations_repository.remove(decoration_obj)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        fish_obj = None
        if fish_type == "FreshwaterFish":
            fish_obj = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            fish_obj = SaltwaterFish(fish_name, fish_species, price)
        aquarium_obj = [aquarium for aquarium in self.aquariums if aquarium_name == aquarium.name]
        if aquarium_obj:
            aquarium_obj = aquarium_obj[0]
            if (fish_type == "FreshwaterFish" and aquarium_obj.__class__.__name__.startswith("Freshwater")) or \
                    (fish_type == "SaltwaterFish" and aquarium_obj.__class__.__name__.startswith("Saltwater")):
                return aquarium_obj.add_fish(fish_obj)
            else:
                return "Water not suitable."

    def feed_fish(self, aquarium_name):
        aquarium_obj = [aquarium for aquarium in self.aquariums if aquarium_name == aquarium.name]
        if aquarium_obj:
            aquarium_obj = aquarium_obj[0]
            aquarium_obj.feed()
        return f"Fish fed: {len(aquarium_obj.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium_obj = [aquarium for aquarium in self.aquariums if aquarium_name == aquarium.name]
        if aquarium_obj:
            aquarium_obj = aquarium_obj[0]
            value = sum([fish.price for fish in aquarium_obj.fish]) + sum(
                [decoration.price for decoration in aquarium_obj.decorations])
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return '\n'.join([str(aquarium) for aquarium in self.aquariums])


# controller = Controller()
# print(controller.add_aquarium("FreshwaterAquarium", "aquarium1"))
# print(controller.add_aquarium("SaltwaterAquarium", "aquarium2"))
# print(controller.add_aquarium("SaltwaterAquarium1", "aquarium2"))
# print(controller.add_decoration("Ornament"))
# print(controller.add_decoration("Plant"))
# print(controller.add_decoration("Plant1"))
# print(controller.insert_decoration("aquarium1", "Ornament"))
# print(controller.insert_decoration("aquarium1", "Plant"))
# print(controller.insert_decoration("aquarium1", "Plant"))
# print(controller.add_fish("aquarium1", "FreshwaterFish", "fish1", "specie1", 5))
#
#
# print(controller.__dict__)