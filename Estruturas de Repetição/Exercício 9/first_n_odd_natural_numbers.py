"""
9 - Write a code that reads an integer number N and shows the first N odd natural numbers.
"""
N = -1
while N < 1:
    try:
        N = int(input('Type a natural number: '))
    except ValueError:
        print(' Please, type a natural number. Try again!\n')
    else:
        for num in range(1, N*2, 2):
            print(num)
