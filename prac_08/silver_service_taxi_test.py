from prac_08.silver_service_taxi import SilverServiceTaxi


town_car = SilverServiceTaxi("Town Car", 150, 2)
town_car.drive(18)
town_car.get_fare()
print(town_car)
print(town_car.get_fare())
print("The fare is $ {:.2f}".format(town_car.get_fare()))
