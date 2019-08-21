"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user enters something that is not a number.
2. When will a ZeroDivisionError occur?
When the user enters a zero into the denominator input.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could ask the user not to do it.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator(Please do not enter zero): "))
    while denominator == 0:
        denominator = int(input("Please don't do that!, Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
