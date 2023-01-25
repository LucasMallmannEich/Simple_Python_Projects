# 15 - Utilizando switch, escreva um programa que leia um inteiro entre 1 e 7.
# Ele deve imprimir o dia da semana correspondente a este número.
# Isto é, se domingo é 1, segunda-feira se 2, e assim por diante.

def switch(dia):
    if dia == 1:
        return 'domingo'
    elif dia == 2:
        return 'segunda-feira'
    elif dia == 3:
        return 'terça-feira'
    elif dia == 4:
        return 'quarta-feira'
    elif dia == 5:
        return 'quinta-feira'
    elif dia == 6:
        return 'sexta-feira'
    elif dia == 7:
        return 'sábado'
    return 'este dia não é um dia da semana'


try:
    dia_semana = int(input('Digite um dia da semana, em forma numérica: '))
except ValueError:
    print(' Você deveria ter digitado um número inteiro.')
else:
    print(f'O dia informado é escrito por extenso da seguinte forma: {switch(dia_semana)}.')
