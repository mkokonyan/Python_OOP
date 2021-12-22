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
        self.number_of_not_completed_missions = 0
        self.number_of_successful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")
        if astronaut is not None:
            return f"{name} is already added."
        if astronaut_type == "Biologist":
            self.astronaut_repository.add(Biologist(name))
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.add(Geodesist(name))
        elif astronaut_type == "Meteorologist":
            self.astronaut_repository.add(Meteorologist(name))
        else:
            raise Exception("Astronaut type is not valid!")
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        searched_planet = self.planet_repository.find_by_name(name)
        if searched_planet is not None:
            return f"{name} is already added."
        planet = Planet(name)
        planet.items += items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut_to_retire = self.astronaut_repository.find_by_name(name)
        if astronaut_to_retire is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut_to_retire)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet_to_send = self.planet_repository.find_by_name(planet_name)
        if planet_to_send is None:
            raise Exception("Invalid planet name!")
        sorted_astronauts = list(sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen))
        suitable_astronauts = [astr for astr in sorted_astronauts if astr.oxygen > 30][:5]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        astros_went_to_open_space = []
        for astr in suitable_astronauts:
            while True:
                if planet_to_send.items:
                    astr.backpack.append(planet_to_send.items.pop())
                    astr.breathe()
                    if astr not in astros_went_to_open_space:
                        astros_went_to_open_space.append(astr)
                    if astr.oxygen <= 0:
                        break
                else:
                    break
        if planet_to_send.items:
            self.number_of_not_completed_missions += 1
            return "Mission is not completed."
        self.number_of_successful_missions += 1
        return f"Planet: {planet_name} was explored. {len(astros_went_to_open_space)} astronauts participated in collecting items."

    def report(self):
        result = f"{self.number_of_successful_missions} successful missions!\n" \
                 f"{self.number_of_not_completed_missions} missions were not completed!\n" \
                 f"Astronauts' info:\n"
        for astr in self.astronaut_repository.astronauts:
            backpack_data = ', '.join(astr.backpack) if astr.backpack else "none"
            result += f"Name: {astr.name}\n" \
                      f"Oxygen: {astr.oxygen}\n" \
                      f"Backpack items: {backpack_data}\n"

        return result.strip()


# space_station = SpaceStation()
# # print(space_station.add_astronaut("Biologist", "Gosho"))
# # print(space_station.add_astronaut("Geodesist", "Pesho"))
# # print(space_station.add_astronaut("Meteorologist", "Ivan"))
# # print(space_station.add_astronaut("Biologist", "Martin"))
# # print(space_station.add_astronaut("Geodesist", "Svetlin"))
# print(space_station.add_astronaut("Meteorologist", "Tanya"))
# print(space_station.add_astronaut("Geodesist", "Ivaylo"))
# print(space_station.add_planet("Saturn",
#                                "sad, adas, das, dasa, hfg, jgh, uyt, try, dsadsa"))
# print(space_station.add_planet("Uran",
#                                "sad, adas, das, dasa, hfg, as, asd, sda, dsa, dsa, sda, sad, sda"))
# print(space_station.add_astronaut("Biologist", "Jorj"))
# print(space_station.add_astronaut("Biologist", "Jorj"))
# print(space_station.add_planet("Saturn", "32, 52 , 543"))
# print([astro.name for astro in space_station.astronaut_repository.astronauts])
# # print(space_station.retire_astronaut("Ivaylo"))
# print([astro.name for astro in space_station.astronaut_repository.astronauts])
# print([planet.name for planet in space_station.planet_repository.planets])
# print([planet.items for planet in space_station.planet_repository.planets])
#
# print([astro.oxygen for astro in space_station.astronaut_repository.astronauts])
# space_station.recharge_oxygen()
# print([astro.oxygen for astro in space_station.astronaut_repository.astronauts])
# print(space_station.send_on_mission("Saturn"))
# print(space_station.send_on_mission("Uran"))
#
# print(space_station.report())
