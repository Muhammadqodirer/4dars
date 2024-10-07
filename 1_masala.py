from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}, Mileage: {self.mileage} km"

    @abstractmethod
    def start(self):
        pass




class Car(Vehicle):
    def __init__(self, brand, model, year, mileage, num_doors):
        super().__init__(brand, model, year, mileage)
        self.num_doors = num_doors

    def start(self):
        return f"The car {self.brand} {self.model} is starting with a roar!"

    def stop(self):
        return f"The car {self.brand} {self.model} has come to a stop."

    def open_trunk(self):
        return f"The trunk of the {self.brand} {self.model} is now open."


class Bicycle(Vehicle):
    def __init__(self, brand, model, year, mileage, gear_count):
        super().__init__(brand, model, year, mileage)
        self.gear_count = gear_count

    def start(self):
        return f"The bicycle {self.brand} {self.model} is ready to ride!"

    def stop(self):
        return f"The bicycle {self.brand} {self.model} has stopped."

    def ring_bell(self):
        return "pip pip! The bell."


car = Car("bmw", "m5", 2020, 100000, 1.2)
bicycle = Bicycle("chevrolet", "gentra", 2022, 15000, 2.3)

print(car.get_info())
print(car.start())
print(car.open_trunk())
print(car.stop())

print(bicycle.get_info())
print(bicycle.start())
print(bicycle.ring_bell())
print(bicycle.stop())