"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
"""


def main():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']
    name_to_be_checked = input("Please enter username: ")
    if name_to_be_checked in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
