"""
22 - Read the age and years of service of a worker and write whether they can retire or not.
The retirement conditions are:
Must be at least 65 years old;
Or have worked for at least 30 years;
Or be at least 60 years old and have worked for at least 25 years.
"""

# Defining and initializing the variables.
age, serviceYears = -1, -1

# Loop while that checks if the user's inputs make sense and output retirement condition result.
while age <= 0:
    try:
        age = int(input('Please, type your age: '))
    except ValueError:
        print(' You must type an integer number. Please, try again.\n')
    else:
        if age > 0:
            while serviceYears < 0 or serviceYears > age:
                try:
                    serviceYears = int(input('Please, type your years of service: '))
                except ValueError:
                    print(' You must type an integer number.\n')
                else:
                    if serviceYears < 0:
                        print(' You can\'t type a negative number for years of service. Please, try again.\n')
                    elif serviceYears > age:
                        print(' You can\'t have more service years than your age!!!\n')
                    else:
                        if age >= 65 or serviceYears >= 30 or (age >= 60 and serviceYears >= 25):
                            print(' You can retire!')
                        else:
                            print(' You can\'t retire...')
        else:
            print(' You must type a positive number for age. Please, try again.\n')
