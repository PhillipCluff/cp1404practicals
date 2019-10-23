from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0

    # display menu
    # get choice
    print("Let's drive!")
    choice = input("q)uit, c)hoose taxi, d)rive \n>>> ".lower())
    # while choice != <quit option>

    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: {:.2f}".format(total_bill))
        #     else if choice == <second option>
        #         <do second task>
        elif choice == "d":
            if current_taxi is not None:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                             trip_cost))
                total_bill += trip_cost

        else:
            # display invalid input error message
            print("invalid input")

        #     display menu
        #     get choice
        print("Bill to date: ${:.2f}".format(total_bill))
        choice = input("q)uit, c)hoose taxi, d)rive \n>>> ".lower())
    # <do final thing, if needed>
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
