from project.car.car import Car


class MuscleCar(Car):
    min_speed_limit = 250
    max_speed_limit = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        if not MuscleCar.min_speed_limit <= speed_limit <= MuscleCar.max_speed_limit:
            raise ValueError(f"Invalid speed limit! Must be between {self.min_speed_limit} and {self.max_speed_limit}!")
        self.__speed_limit = speed_limit


