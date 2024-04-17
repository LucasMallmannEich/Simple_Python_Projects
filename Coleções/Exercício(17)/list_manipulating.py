"""
17 - Read a list containing 10 elements and assign the value 0 to all elements containing negative values.
"""

# Initializing the variables.
test_list = []
number = 0

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

# Testing.
print(test_list)
