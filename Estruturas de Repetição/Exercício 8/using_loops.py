"""
8 - Write a program that reads 10 numbers and write the smallest and the biggest value read.
"""

# Initializing the variables.
numbers = []

# Reading the values.
while len(numbers) < 10:
    try:
        number = int(input('Type a number: '))
    except ValueError:
        print(' You need to type a number.\nPlease, try again.\n')
    else:
        numbers.append(number)

# Showing the smallest and biggest values.
print(f' The smallest value is {min(numbers)} and the biggest value is {max(numbers)}.')
