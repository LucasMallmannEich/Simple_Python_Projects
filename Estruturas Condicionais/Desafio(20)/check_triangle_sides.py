"""
20 - Given three values, A, B, C, check if they can be the sides of a triangle.
And, if they are, determine if the triangle is scalene, equilateral, or isosceles, considering the following concepts:
The length of each side of a triangle is less than the sum of the other two sides.
A triangle is called equilateral if it has three equal sides.
A triangle is called isosceles if it has two sides of equal length.
A triangle is called scalene if all three sides are different lengths.
"""

# Declaring the values A, B and C and a list to store them after user insert.
sideA, sideB, sideC, listValues = '', '', '', []

# Reading the number.
while type(sideA) is not 'float':
    try:
        sideA = float(input('Please, type the first numeric value: '))
    except ValueError:
        print('Please, try again (this time, use a numeric value).\n')
    else:
        while type(sideB) is not 'float':
            try:
                sideB = float(input('Please, type the second numeric value: '))
            except ValueError:
                print('Please, try again (this time, use a numeric value).\n')
            else:
                while type(sideC) is not 'float':
                    try:
                        sideC = float(input('Please, type the third numeric value: '))
                    except ValueError:
                        print('Please, try again (this time, use a numeric value).\n')
                    else:
                        listValues = [sideA, sideB, sideC]

# Checking if the values can be the sides of a triangle (and if they can, checking what is the triangle type).
if max(listValues) < (sum(listValues) - max(listValues)):
    print(' These values can be the sides of a triangle.\n')
    if sideA == sideB == sideC:
        print(' These values can make a equilateral triangle.')
    elif sideA != sideB != sideC:
        print(' These value can make a scalene triangle.')
    else:
        print(' These values can make a isosceles triangle.')
else:
    print(' These values cannot be the sides of a triangle.\n')
