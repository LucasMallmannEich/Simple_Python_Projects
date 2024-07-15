"""
16 - Create a function named "draw_line". It must draw a straight line on the screen using multiple equal signs
(e.g., ======). The function receives a parameter that specifies how many equal signs to display.
"""


# Function DrawLine:
def draw_line(n_equal_signs):
    if type(n_equal_signs) is int and n_equal_signs >= 0:
        return print(n_equal_signs*'=')
    return print('The parameter should be a non-negative integer number.')


# Testing the functions.
draw_line(3)        #OUTPUT: ===
draw_line(-12)      #OUTPUT: The parameter should be a non-negative integer number.
