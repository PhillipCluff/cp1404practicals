from prac_08.car import Car
from random import uniform


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel and randomly doesn't drive
        or drive until fuel runs out return the distance actually driven.
        """
        distance_driven = 0
        if self.reliability > uniform(0, 100):
            distance_driven = super().drive(distance)
        return distance_driven
