"""The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total
before the amount is displayed on the screen."""


def main():
    number_of_items = int(input("Please enter number of items: "))
    while number_of_items < 1:
        print("Invalid number of items!")
        number_of_items = int(input("Please enter number of items: "))

    total = 0
    for i in range(number_of_items):
        total += float(input("Price of item: "))

    if total > 100:
        # getting discount.
        total = total * 0.9

    print("Total price for {} items is ${:.2f}".format(number_of_items, total))


main()
