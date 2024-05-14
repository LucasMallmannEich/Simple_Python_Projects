"""
17 - Make a program that calculates and shows the area of a trapeze.
It is known that: A = ((bigbase + smallbase) * height)/2.
Remember that: the big base and the small base must be numbers bigger than zero.
"""


# Writing the function to calculate the trapeze's area.
def trapeze_area(bigbase, smallbase, height):
    if bigbase > 0 and smallbase > 0 and height > 0:
        return ((bigbase+smallbase)*height)/2
    else:
        return 0


# Testing.
print(trapeze_area(12, 5, 10))  # OUTPUT: 85
