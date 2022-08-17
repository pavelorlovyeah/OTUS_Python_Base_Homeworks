"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle

class Plane(Vehicle):

    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption,
                 max_cargo
                 ):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, extra_cargo):
        final_cargo = self.cargo + extra_cargo
        if final_cargo <= self.max_cargo:
            self.cargo = final_cargo
            return self.cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo_init = self.cargo
        self.cargo = 0
        return cargo_init