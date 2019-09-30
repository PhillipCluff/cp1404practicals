from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: "))
    #     guitar_to_add = Guitar(name, year, cost)
    #     guitars.append(guitar_to_add)
    #     print(guitar_to_add, "added.")
    #     name = input("Name: ")

    fender = Guitar("Fender Stratocaster", 2014, 765.40)
    guitars.append(fender)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        guitars.sort()
        print_spacing = max(len(guitar.name) for guitar in guitars)

        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            else:
                vintage_string = ""
            print("Guitar {0}: {1.name:>{3}} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i,
                                                                                           guitar,
                                                                                           vintage_string,
                                                                                           print_spacing))


main()
