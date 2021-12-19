from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False
        self.min_speed_limit = None
        self.max_speed_limit = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if len(model) < 4:
            raise ValueError(f"Model {model} is less than 4 symbols!")
        self.__model = model

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        if not self.min_speed_limit <= speed_limit <= self.max_speed_limit:
            raise ValueError(f"Invalid speed limit! Must be between {self.min_speed_limit} and {self.max_speed_limit}!")
        self.__speed_limit = speed_limit
