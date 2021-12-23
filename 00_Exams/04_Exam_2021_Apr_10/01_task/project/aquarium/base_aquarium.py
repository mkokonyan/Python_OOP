from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = name

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        fish_data = "none" if not self.fish else ' '.join([fish.name for fish in self.fish])
        return f"{self.name}:\nFish: {fish_data}\n" \
               f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}"
