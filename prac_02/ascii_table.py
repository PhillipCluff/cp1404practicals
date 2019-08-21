LOWER = 33
UPPER = 127

# letter = input('Enter a character ')
# print('The ASCII code for', letter, 'is', ord(letter))
# ascii_number = int(input('Enter a number between {} and {}: '.format(LOWER, UPPER)))
# while ascii_number < LOWER or ascii_number > UPPER:
#     ascii_number = int(input("Number must be between {} and {}: ".format(LOWER, UPPER)))
#
# print('The character for {} is {}'.format(ascii_number, chr(ascii_number)))

starting_number = LOWER
for i in range(0, UPPER - LOWER + 1):
    print('{:>3} {:>2}'.format((starting_number + i), chr(starting_number + i)))
