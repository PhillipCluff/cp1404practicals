from prac_06.guitar import Guitar


def main():
    guitars = []
    fender = Guitar("Fender Stratocaster", 2014, 765.40)
    guitars.append(fender)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i,
                                                                  guitar.name,
                                                                  guitar.year,
                                                                  guitar.cost,
                                                                  vintage_string))


main()
