"""Phillip Cluff"""


def main():

    min_length = 5
    password = get_password(min_length)
    for i in range(0, len(password)):
        print("*", end='')


def get_password(min_length):
    password = input("Please enter password: ")
    while len(password) < min_length:
        password = input("Password not long enough: ")
    return password


main()
