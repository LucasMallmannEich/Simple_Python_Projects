"""
19 -  Make a list containing 50 elements and having its values following the rule: (i + 5 * i) % (i + 1).
Being "i" the element position in the list. After that, display the list on screen.
"""
list1 = []
for i in range(50):
    list1.append((i + 5 * i) % (i + 1))
print(list1)
