"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("my_car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    # next can be a put im a loop that runs though the list
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print("odo limo =", limo.odometer)
    print(limo)


main()
