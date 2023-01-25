"""
16 - Usando switch, escreva um programa que leia um inteiro entre 1 e 12.
Imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""


def switch(mes):
    if mes == 1:
        return 'janeiro'
    elif mes == 2:
        return 'fevereiro'
    elif mes == 3:
        return 'março'
    elif mes == 4:
        return 'abril'
    elif mes == 5:
        return 'maio'
    elif mes == 6:
        return 'junho'
    elif mes == 7:
        return 'julho'
    elif mes == 8:
        return 'agosto'
    elif mes == 9:
        return 'setembro'
    elif mes == 10:
        return 'outubro'
    elif mes == 11:
        return 'novembro'
    elif mes == 12:
        return 'dezembro'
    return 'este número não representa um mês do ano'


try:
    num_mes = int(input('Digite um mês do ano, em forma numérica: '))
except ValueError:
    print(' Você deveria ter digitado um número inteiro.')
else:
    print(f'O mês informado é escrito por extenso da seguinte forma: {switch(num_mes)}.')
