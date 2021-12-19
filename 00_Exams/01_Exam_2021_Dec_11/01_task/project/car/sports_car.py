from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model, speed_limit):
        self.min_speed_limit = 400
        self.max_speed_limit = 600
        super().__init__(model, speed_limit)

