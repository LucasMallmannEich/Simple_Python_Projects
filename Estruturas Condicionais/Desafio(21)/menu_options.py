"""
21 - Write the options menu bellow. Read the user option and execute the chosen operation.
Write an error message if the option is invalid.
Choose an option:
1 - Sum of 2 numbers.
2 - Difference between 2 numbers (biggest by smallest).
3 - Product of 2 numbers.
4 - Division between 2 numbers (denominator cannot be zero).
"""

# Declaring option variable value, number1 and number2.
option, number1, number2 = 0, '', ''

# Displaying the options menu and reading the user option.
while option > 4 or option < 1:
    try:
        option = int(input('1 - Sum of 2 numbers.\n2 - Difference between 2 numbers '
                           '(biggest by smallest).\n3 - Product of 2 numbers.\n4 - Division between 2 numbers '
                           '(denominator cannot be zero).\nPlease, choose an option: '))
    except ValueError:
        print(' You have to type an integer number.\n')
    else:
        if option > 4 or option < 1:
            print(' Please, try again. You chose an invalid option.\n')
        else:
            while type(number1) is not float:
                try:
                    number1 = float(input('Please, insert a number: '))
                except ValueError:
                    print(' You have to insert a numeric value!\n')
                else:
                    while type(number2) is not float:
                        try:
                            number2 = float(input('Please, insert a number: '))
                        except ValueError:
                            print(' You have to insert a numeric value!\n')
                        else:
                            if option == 1:
                                print(f' The sum of {number1} and {number2} is {number1+number2}.\n')
                            elif option == 2:
                                if number1 > number2:
                                    print(f' The difference between {number1} and {number2} is {number1-number2}.\n')
                                else:
                                    print(f' The difference between {number2} and {number1} is {number2-number1}.\n')
                            elif option == 3:
                                print(f' The product of {number1} and {number2} is {number1*number2}.\n')
                            else:
                                if number1 > number2:
                                    print(f' The division of {number1} by {number2} is {number1/number2}.\n')
                                else:
                                    print(f' The division of {number2} by {number1} is {number2/number1}.\n')