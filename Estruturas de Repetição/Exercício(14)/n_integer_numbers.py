"""
14 - Write a program that reads an integer positive even number N and displays all the even numbers from 0 to N in
descending order.
"""
N = ''
# Reading the number.
while type(N) is not int:
    try:
        N = int(input('Write an integer positive even number: '))
    except ValueError:
        print(' You must insert an integer positive even number.\n')
    else:
        while N <= 0:
            print(' Please, insert an integer positive even number.\n')
            N = int(input('Write an integer positive even number: '))
# Displaying all the natural even numbers from 0 to N in descending order.
for num in range(N, -1, -2):
    print(num)
