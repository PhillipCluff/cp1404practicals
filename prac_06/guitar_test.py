from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other_guitar = Guitar("Another Guitar", 2012)
    print(other_guitar)
    print(gibson)
    # :) the earth is in the wrong place
    print("{} get_age() - Expected 96. Got {} <- the earth is in the wrong place :)".format(gibson.name, gibson.get_age()))

    print("{} get_age() - Expected 7. Got {}".format(other_guitar.name, other_guitar.get_age()))

    print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))

    print("{} get_age() - Expected False. Got {}".format(other_guitar.name, gibson.is_vintage()))


main()
