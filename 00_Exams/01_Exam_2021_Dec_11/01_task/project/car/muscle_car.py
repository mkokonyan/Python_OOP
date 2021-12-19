from project.car.car import Car


class MuscleCar(Car):
    def __init__(self, model, speed_limit):
        self.min_speed_limit = 250
        self.max_speed_limit = 450
        super().__init__(model, speed_limit)

