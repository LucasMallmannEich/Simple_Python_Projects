"""
12 - Make a program that opens a text file, calculates and writes the number of characters, the number of lines and the
number of words in the file. Besides that, it has to write the number of times each letter appears in the file (ignoring
letter with accent mark). Words are separated by one or more characters, space, tabs or new lines.
"""
from unicodedata import normalize

# User inserting information.
filename = input('Please, type a text filename (without the extension ".txt"): ')
filename += '.txt'

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()
    num_word = 0
    num_character = 0
    num_lines = 1
    for word in text:
        for character in word:
            if character == ' ':
                num_word += 1
            elif character == '\n':
                num_lines += 1
            else:
                num_character += 1
    print(f'Number of characters: {num_character}')
    print(f'Number of lines: {num_lines}')
    print(f'Number of words: {num_word}\n')
    file.close()

letters = list('abcdefghijklmnopqrstuvwxyz')
occurance = list('00000000000000000000000000')

for i in range(26):
    for letter in text:
        if normalize('NFD', letter.lower()) == letters[i]:
            occurance[i] = str(int(occurance[i]) + 1)

for i in range(26):
    print(f'The letter {letters[i]} appeared {occurance[i]} times in the text.\n')
