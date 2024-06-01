"""
18 - Make a program that reads a list containing 10 numbers. Read a number x. Count the multiple values of an integer
number x in a list and show them in the screem.
"""

# Initializing the variables.
test_list, multiples = [], []
number = 0
number_x = 0.1

# Filling the array with 10 numbers.
while len(test_list) < 10:
    try:
        number = float(input('Type a number, please: '))
        if number < 0:
            number = 0
    except ValueError:
        print(' The value has to be a number.')
    else:
        test_list.append(number)

# Reading the number x.
while type(number_x) is not int:
    try:
        number_x = int(input('Type the number x (integer), please: '))
    except ValueError:
        print(' The value has to be an integer number.')

# Checking if the number x has multiple values inside the list.
for i in range(10):
    if test_list[i] % number_x == 0:
        multiples.append(test_list[i])

# Testing.
print(f' List of Numbers: {test_list}')
print(f' Number X: {number_x}')
print(f' List of Multiples: {multiples}')
