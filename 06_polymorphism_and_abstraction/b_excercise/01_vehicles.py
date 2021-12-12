from abc import ABC, abstractmethod


class Vehicle(ABC):
    fuel_consumption_increase = 0

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    def can_drive(self, distance, fuel_consumption_increase):
        return self.fuel_quantity > (self.fuel_consumption + fuel_consumption_increase) * distance


class Car(Vehicle):
    fuel_consumption_increase = 0.9

    def drive(self, distance):
        if not self.can_drive(distance, self.fuel_consumption_increase):
            return
        self.fuel_quantity -= (self.fuel_consumption + self.fuel_consumption_increase) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    fuel_consumption_increase = 1.6

    def drive(self, distance):
        if not self.can_drive(distance, self.fuel_consumption_increase):
            return
        self.fuel_quantity -= (self.fuel_consumption + self.fuel_consumption_increase) * distance

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
