"""
22 - Make a program that reads two lists containing 10 elements. Calculate another list containing, in the even
positions, the values of the first list and, in the odd positions, the values of the second list.
"""
# Declaring the lists.
list1, list2, result_list = [], [], []

# Initializing the lists.
while len(list1) < 10:
    number = input('Please, type anything to be inserted in list1: ')
    list1.append(number)
while len(list2) < 10:
    number = input('Please, type anything to be inserted in list2: ')
    list2.append(number)

# Filling result list.
for i in range(10):
    if i % 2 == 0:
        result_list.append(list2[i])
    else:
        result_list.append(list1[i])


# Testing.
print(list1, list2, result_list)
