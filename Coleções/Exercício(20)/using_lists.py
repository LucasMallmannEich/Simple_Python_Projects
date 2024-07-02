"""
20 - Write a program to read integer numbers in the interval [0,50] and store them in a list with 10 elements.
After that, fill a list with only the odd numbers from the first list. Display both lists, 2 elements by line.
"""
list1, odd_list1 = [], []
aux = 0
while len(list1) != 10:
    try:
        number = int(input('Type an integer number in the interval [0,50]: '))
    except ValueError:
        print(' You need to type an integer number.')
    else:
        if 0 <= number <= 50:
            list1.append(number)
            if number % 2 != 0:
                odd_list1.append(number)
        else:
            print(' You need to type an integer number in the interval [0,50].')
for i in range(10):
    if list1[i] == odd_list1[aux]:
        print(f'{list1[i]:>12} {odd_list1[aux]}')
        aux += 1
    else:
        print(f'{list1[i]:>12} []')
