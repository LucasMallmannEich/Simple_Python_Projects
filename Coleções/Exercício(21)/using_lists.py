"""
21 - Make a program that receives two lists from the user containing 10 integer numbers each, A and B.
Create a new list C calculating C = A - B. Display in the screen the data of list C.
"""
listA, listB, listC = [], [], []
while len(listA) < 10:
    try:
        number = int(input('Type an integer number for list A: '))
    except ValueError:
        print(' You need to type an integer number.')
    else:
        listA.append(number)
while len(listB) < 10:
    try:
        number = int(input('Type an integer number for list B: '))
    except ValueError:
        print(' You need to type an integer number.')
    else:
        listB.append(number)
for i in range(10):
    listC.append(listA[i]-listB[i])
for i in range(10):
    print(listC[i])
