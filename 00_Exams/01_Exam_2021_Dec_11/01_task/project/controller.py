from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):

        if model in [car.model for car in self.cars]:
            raise Exception(f"Car {model} is already created!")
        if car_type == "MuscleCar":
            self.cars.append(MuscleCar(model, speed_limit))
            return f"{car_type} {model} is created."
        if car_type == "SportsCar":
            self.cars.append(SportsCar(model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [driver.name for driver in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [race.name for race in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):

        if not [driver for driver in self.drivers if driver_name == driver.name]:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver_obj = [driver for driver in self.drivers if driver_name == driver.name][0]
        available_cars = [car for car in self.cars if car_type == car.__class__.__name__]

        if not available_cars:
            raise Exception(f"Car {car_type} could not be found!")
        if not [car for car in available_cars if car.is_taken == False]:
            raise Exception(f"Car {car_type} could not be found!")
        car_to_be_added = [car for car in available_cars if car.is_taken == False][-1]
        car_to_be_added.is_taken = True
        if driver_obj.car is not None:
            old_model = driver_obj.car.model
            driver_obj.car.is_taken = False
            new_model = car_to_be_added.model
            driver_obj.car = car_to_be_added

            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

        driver_obj.car = car_to_be_added
        return f"Driver {driver_name} chose the car {car_to_be_added.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not [race for race in self.races if race_name == race.name]:
            raise Exception(f"Race {race_name} could not be found!")
        if not [driver for driver in self.drivers if driver_name == driver.name]:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver_obj = [driver for driver in self.drivers if driver_name == driver.name][0]
        race_obj = [race for race in self.races if race_name == race.name][0]
        if driver_obj.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver_obj in race_obj.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race_obj.drivers.append(driver_obj)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not [race for race in self.races if race_name == race.name]:
            raise Exception(f"Race {race_name} could not be found!")
        race_obj = [race for race in self.races if race_name == race.name][0]
        if len(race_obj.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        top_three_cars = sorted([driver for driver in race_obj.drivers], key=lambda x: -x.car.speed_limit)[:3]
        result = []
        for driver in top_three_cars:
            driver.number_of_wins += 1
            result.append(
                f"Driver {driver.name} wins the {race_obj.name} race with a speed of {driver.car.speed_limit}.")
        return '\n'.join(result)


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]
