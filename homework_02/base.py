from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC

class Vehicle(ABC):

    # Attributes for class Vehicle:
    # weight [kg], started [Y/N], fuel [liters], fuel_consumption [liters/km]

    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, dist):
        range = self.fuel / self.fuel_consumption
        if dist <= range:
            self.fuel = self.fuel - dist * self.fuel_consumption
        else:
            raise NotEnoughFuel