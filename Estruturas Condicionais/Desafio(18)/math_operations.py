"""
18 - Make a program that shows to the user a menu with 4 math operations (the basic ones). The user can choose an option
and the program will request two numeric values to execute the operation. After that, it will show the result.
"""
operations = ['-', '+', '/', '*']
operation, num1, num2 = '', '', ''
while operation not in operations:
    operation = str(input('Please, choose a math option (-, +, /, *): '))
    if operation not in operations:
        print(' You have to try again.\n')
    else:
        while type(num1) is not float:
            try:
                num1 = float(input('Please, insert the first numeric value: '))
            except ValueError:
                print('You need to insert a numeric value... Try again!\n')
            else:
                while type(num2) is not float:
                    try:
                        num2 = float(input('Please, insert the second numeric value: '))
                    except ValueError:
                        print('You need to insert a numeric value... Try again!\n')
                    else:
                        if operation == '-':
                            print(f'{num1} - {num2} = {num1-num2}')
                        elif operation == '+':
                            print(f'{num1} + {num2} = {num1+num2}')
                        elif operation == '*':
                            print(f'{num1} * {num2} = {num1*num2}')
                        else:
                            print(f'{num1} / {num2} = {num1/num2}')
