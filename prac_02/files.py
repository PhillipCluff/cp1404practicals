
name_file = open('name.txt', 'w')
name = input("Please enter your name: ")
name_file.write(name)
name_file.close()
name_file = open('name.txt', 'r')
print("Your name is", name_file.read())
name_file.close()

# numbers_file = open('numbers.txt', 'w')
# how_many_number = int(input('Please enter how many numbers you would like to enter: '))
# for i in range(0, how_many_number):
#      number_to_file = input('Please enter a number to file: ')
#      numbers_file.write(number_to_file + '\n')
# numbers_file.close()
# wasn't asked to do this

# need to use .redlines

numbers_file = open('numbers.txt', 'r')
total = 0
for line in numbers_file:
    total += int(line)
print(total)
numbers_file.close()
