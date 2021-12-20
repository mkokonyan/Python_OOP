from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut_names = [astr.name for astr in self.astronaut_repository]
        if name in astronaut_names:
            return f"{name} is already added."
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")
        if astronaut_type == "Biologist":
            self.astronaut_repository.append(Biologist(name))
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.append(Geodesist(name))
        elif astronaut_type == "Meteorologist":
            self.astronaut_repository.append(Meteorologist(name))
        else:
            raise Exception("Astronaut type is not valid!")
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet_names = [planet.name for planet in self.planet_repository]
        if name in planet_names:
            return f"{name} is already added."
        planet = Planet(name)
        planet.items += items.split(", ")
        self.planet_repository.append(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut_to_retire = [astr for astr in self.astronaut_repository if name == astr.name]
        if not astronaut_to_retire:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove([astronaut_to_retire][0])
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet_to_send = [planet for planet in self.planet_repository if planet_name == planet.name]
        if not planet_to_send:
            raise Exception("Invalid planet name!")
        sorted_astronauts = list(sorted(self.astronaut_repository, key=lambda x: -x.oxygen))
        suitable_astronauts = [astr for astr in sorted_astronauts if astr.oxygen > 30]
        if len(suitable_astronauts) > 5:
            suitable_astronauts = suitable_astronauts[:5]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        planet_to_send = planet_to_send[0]
        planet_items = [item for item in planet_to_send.items][::-1]




    def report(self):
        pass
