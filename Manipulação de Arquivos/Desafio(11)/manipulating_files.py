"""
11 - Make a program in which the user inserts a text filename and a word. The program returns how many times that word
appears in the file.
"""

# User inserting information.
filename = input('Please, type a text filename (without the extension ".txt"): ')
filename += '.txt'
word = input('Please, type a word to be searched in the file you inserted: ')


# Opening the file and searching for the word:
try:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.readlines()
except FileNotFoundError:
    print(' The file was not found.')
else:
    count = 0
    for text_paragraph in text:
        print(text_paragraph)
        if word in text_paragraph:
            count = count + 1
    print(f' The word "{word}" appears {count} time in the text file.')
    file.close()
