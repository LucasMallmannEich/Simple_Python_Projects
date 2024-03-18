"""
15 - First, read an array containing 20 integer numbers. Then, write a new  array eliminating its repetitive elements.
"""
# Inicializing the arrays.
original_array = []
new_array = []

# Loop while runing until array's length is equal to 20.
while len(original_array) < 20:
    # User input validation.
    try:
        number = int(input('Type an integer number: '))
    except ValueError:
        print('Please, try again. This time, using integer numbers.')
    else:
        original_array.append(number)
        if number not in new_array:
            new_array.append(number)

# Showing the results.
print(f'Original Array: {[element for element in original_array]}')
print(f'New Array: {[element for element in new_array]}')
