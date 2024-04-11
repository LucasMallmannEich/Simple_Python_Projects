"""
16 - Make a program that reads an array containing 5 elements (all of them being numbers) and, after that, a integer
code. If the code is zero, finish the program; if it's 1, show the arrau in the direct order. If it's 2, show the array
in the reverse order. If the code is different than 1 or 2, write a message notifing that it's an invalid code.
"""

# Inicializing the array and the ok variable.
array = []
ok = False
code = 0

# Filling the array with 5 numbers.
while len(array) < 5:
    try:
        number = float(input('Type a number: '))
    except ValueError:
        print(' Please, type a number.\n')
    else:
        array.append(number)

# Getting the code and printing the results.
while ok is False:
    try:
        code = int(input('Type the code: '))
    except ValueError:
        print(' Please, try again.\n')
    else:
        ok = True
    finally:
        if ok is True:
            if code == 1:
                print(array)
            elif code == 2:
                array.reverse()
                print(array)
            elif code != 0:
                print(' The code is invalid.\n')