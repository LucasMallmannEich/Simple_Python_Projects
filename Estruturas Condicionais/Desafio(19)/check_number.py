"""
19 - Make a program to check if a given integer number can be divided by 3 or 5, but not both.
"""

# Declaring a variable with the name "number".
number = 0.1

# Reading the number.
while type(number) is 'int':
    try:
        number = int(input('Please, type an integer number: '))
    except ValueError:
        print(' You should have inserted an integer number.')
    else:
        if number % 3 == 0 and number % 5 == 0:
            print(' The given number can be divided by 3 and 5.')
        elif number % 3 == 0:
            print(' The given number can be divided by 3, but not by 5.')
        elif number % 5 == 0:
            print(' The given number can be divided by 5, but not by 3.')
        else:
            print(' The given number can\'t be divided by 5 or by 3.')
