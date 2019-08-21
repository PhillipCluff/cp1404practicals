"""Phillip Cluff"""


def main():

    min_length = 5
    password = input("Please enter password: ")
    while len(password) < min_length:
        password = input("Password not long enough: ")
    for i in range(0, len(password)):
        print("*", end='')


main()
