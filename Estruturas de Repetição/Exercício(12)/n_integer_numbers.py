"""
12 - Write a program that reads an integer positive number N and displays all the natural numbers from 0 to N in
descending order.
"""
N = ''
# Reading the number.
while type(N) is not int:
    try:
        N = int(input('Write an integer positive number: '))
    except ValueError:
        print(' You must insert an integer positive number.\n')
    else:
        while N <= 0:
            print(' Please, insert an integer positive number.\n')
            N = int(input('Write an integer positive number: '))
# Displaying all the natural numbers from 0 to N in descending order.
for num in range(N, -1, -1):
    print(num)
