"""
15 - Make a program that will receive 3 values (they have to be bigger than zero).
The three values represent the measurements of the three sides of a triangle. Make functions for:
(a) Determinate if these sides can make a triangle, knowing that:
The length of each side of a triangle is less than the sum of the other two sides.
(b) Determine and show the type of triangle, if the measurements form a triangle. Specifically:
A triangle with three equal sides is called equilateral;
A triangle with two equal sides is called isosceles;
A triangle with three different sides is called scalene.
"""


# Function a:
def can_sides_make_triangle(first_side, second_side, third_side):
    if first_side < (second_side+third_side) and second_side < (first_side+third_side) and third_side < (second_side+first_side):
        return 'They can make a triangle.'
    return 'They can\'t make a triangle.'


# Function b:
def type_of_triangle(first_side, second_side, third_side):
    if can_sides_make_triangle(first_side, second_side, third_side) == 'They can make a triangle.':
        if first_side == second_side == third_side:
            return 'Equilateral triangle.'
        if first_side != second_side != third_side:
            return 'Scalene triangle.'
        return 'Isosceles triangle.'
    else:
        return can_sides_make_triangle(first_side, second_side, third_side)


# Initializing the variables.
side1, side2, side3 = 0, 0, 0
# Receiving 3 values from the user.
while side1 <= 0:
    try:
        side1 = float(input('Please, type the size, in meters, of the first side: '))
    except ValueError:
        print(' Please, try again.')
    else:
        if side1 > 0:
            while side2 <= 0:
                try:
                    side2 = float(input('Please, type the size, in meters, of the second side: '))
                except ValueError:
                    print(' Please, try again.')
                else:
                    if side2 > 0:
                        while side3 <= 0:
                            try:
                                side3 = float(input('Please, type the size, in meters, of the third side: '))
                            except ValueError:
                                print(' Please, try again.')
                            else:
                                if side3 <= 0:
                                    print(' The value has to be bigger than zero.')
                    else:
                        print(' The value has to be bigger than zero.')
        else:
            print(' The value has to be bigger than zero.')


# Testing the functions.
print(can_sides_make_triangle(side1, side2, side3))
print(type_of_triangle(side1, side2, side3))
