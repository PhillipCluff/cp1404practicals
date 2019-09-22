from prac_06.guitar import Guitar


def main():
    guitars = []
    fender = Guitar("Fender Stratocaster", 2014, 765.40)
    guitars.append(fender)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for guitar in guitars:
        print(guitar)


main()
